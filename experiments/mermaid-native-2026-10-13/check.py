#!/usr/bin/env python3
"""Check semantic projections and flow preservation against the current baseline."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import re
from render import BASELINES, HERE, ROOT


def block(path):
    blocks = re.findall(r'^```mermaid\s*\n(.*?)^```', path.read_text(), re.M | re.S)
    assert len(blocks) == 1, path.name
    return blocks[0]


def nodes(source):
    return dict(re.findall(r'^\s*([a-z_]+)@\{ label: "([^"]+)"', source, re.M))


def main():
    cases = [('fde-participants-usecase', 'baseline-fde-participants'),
             ('fde-change-usecase', 'baseline-fde-change'),
             ('requirements-usecase', 'baseline-requirements')]
    for name, baseline in cases:
        original = block(ROOT / BASELINES[baseline])
        path = HERE / (name + '.md')
        trial = block(path)
        expected = {k: v for k, v in nodes(original).items() if k.startswith(('a_', 'b_'))}
        actual = dict(re.findall(r'^(?:actor )?([a-z_]+)\("([^"]+)"\)$', trial, re.M))
        assert actual == expected, (name, 'node mismatch')
        assert set(re.findall(r'^actor ([a-z_]+)', trial, re.M)) == {k for k in expected if k.startswith('a_')}, name
        all_edges = set(re.findall(r'^\s*([a-z_]+) --- ([a-z_]+)$', original, re.M))
        kept = {(a, b) for a, b in all_edges if a in expected and b in expected}
        assert set(re.findall(r'^([a-z_]+) -- ([a-z_]+)$', trial, re.M)) == kept, (name, 'association mismatch')
        labels = nodes(original)
        labels['p_ultimate_purpose'] = '個も仲間も、自然と自分たちらしく居られる'
        for a, b in all_edges - kept:
            assert f'| {labels[a]} | {labels[b]} |' in path.read_text(), (name, 'missing omission')
        assert 'systemBoundary' not in trial and 'include' not in trial and 'extend' not in trial, name
        print(f'PASS {name}: {len(expected)} nodes, {len(kept)} associations, {len(all_edges-kept)} documented omissions')
    neutral = block(HERE / 'fde-participants-usecase.md').split('usecase-beta', 1)[1]
    assert neutral == block(HERE / 'fde-participants-default.md').split('usecase-beta', 1)[1]
    for name, baseline in [('fde-change-swimlane', 'baseline-fde-change-flow'), ('requirements-swimlane', 'baseline-requirements-flow')]:
        original = block(ROOT / BASELINES[baseline]); trial = block(HERE / (name + '.md'))
        actual = dict(re.findall(r'^\s*([a-z_]+)[\[{]"([^"]+)"[\]}]$', trial, re.M))
        assert actual == nodes(original), (name, 'node mismatch')
        edges = lambda s: set(re.findall(r'^\s*([a-z_]+) -->(.*?) ([a-z_]+)$', s, re.M))
        assert edges(trial) == edges(original), (name, 'flow mismatch')
        assert 'layout:' not in trial and '仮置き' in trial, name
        assert ('d_requirements_agreed{"' in trial) == ('d_requirements_agreed' in nodes(original)), name
        print(f'PASS {name}: {len(actual)} nodes, {len(edges(trial))} edges')
    print('PASS default variant: identical graph')


if __name__ == '__main__':
    main()
