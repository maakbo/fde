#!/usr/bin/env python3
"""Render comparison Markdown and original baselines without changing source."""
import argparse
import base64
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINES = {
    'baseline-fde-participants': 'experiments/mermaid-native-2026-10-13/baselines/fde-participants.md',
    'baseline-fde-change': 'experiments/mermaid-native-2026-10-13/baselines/fde-change.md',
    'baseline-requirements': 'experiments/mermaid-native-2026-10-13/baselines/requirements-context.md',
    'baseline-fde-change-flow': 'experiments/mermaid-native-2026-10-13/baselines/fde-change-flow.md',
    'baseline-requirements-flow': 'experiments/mermaid-native-2026-10-13/baselines/requirements-flow.md',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mmdc', required=True, type=Path)
    parser.add_argument('--output-dir', type=Path, default=HERE / 'previews')
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    sources = {p.stem: p for p in HERE.glob('*.md') if p.name != 'README.md'}
    sources.update({k: ROOT / v for k, v in BASELINES.items()})
    env = os.environ.copy()
    chrome = Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    if chrome.is_file():
        env.setdefault('PUPPETEER_EXECUTABLE_PATH', str(chrome))
    prefix = 'https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/'
    with tempfile.TemporaryDirectory(prefix='fde-mermaid-') as temp:
        for name, path in sorted(sources.items()):
            blocks = re.findall(r'^```mermaid\s*\n(.*?)^```', path.read_text(), re.M | re.S)
            if len(blocks) != 1:
                raise ValueError(f'{path.name}: expected one Mermaid block')
            def embed(match):
                icon = ROOT / 'assets/icons/maakbo' / match[1]
                return 'img: "data:image/svg+xml;base64,' + base64.b64encode(icon.read_bytes()).decode() + '"'
            source = re.sub(r'img: "' + re.escape(prefix) + r'([^"/]+)"', embed, blocks[0])
            input_path = Path(temp) / (name + '.mmd')
            input_path.write_text(source)
            for fmt in ('svg', 'png'):
                subprocess.run([str(args.mmdc.resolve()), '-i', str(input_path), '-o',
                    str(args.output_dir / (name + '.' + fmt)), '-p', str(ROOT / 'config/puppeteer.json'),
                    '-b', 'white', '--size', '1600', '-s', '2'], env=env, check=True)
            print('PASS', name, flush=True)


if __name__ == '__main__':
    main()
