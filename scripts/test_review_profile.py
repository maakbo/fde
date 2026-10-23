#!/usr/bin/env python3
"""Verify reader review is distributed and runs in a source-only consumer."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
REVIEW = '.agents/skills/reader-facing-artifact-review'


class ReviewProfile(unittest.TestCase):
    def test_delivery_profile_skill_handoffs_resolve_without_upstream_checkout(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            archive = base / 'delivery.zip'
            subprocess.run([sys.executable, str(ROOT / 'scripts/build_consumer_profile.py'),
                            '--profile', str(ROOT / 'consumer/profiles/field-delivery-v0.1.paths.json'),
                            '--output', str(archive), '--version', 'delivery-test', '--allow-dirty'],
                           check=True, capture_output=True, text=True)
            with zipfile.ZipFile(archive) as package:
                package.extractall(base / 'stage')
            stage = base / 'stage'
            for skill in ('discovery-facilitation', 'definition-facilitation',
                          'architecture-modeling', 'knowledge-stewardship', 'ai-pilot-evaluation',
                          'workflow-design-facilitation'):
                self.assertTrue((stage / '.agents/skills' / skill / 'SKILL.md').is_file())
            for document in (stage / '.agents/skills').rglob('*.md'):
                # Example code is not a live dependency (e.g. hypothetical parent.md).
                prose = re.sub(r'(?ms)^```.*?^```[^\n]*', '', document.read_text())
                for target in re.findall(r'\]\(([^)]+)\)', prose):
                    if '://' in target or target.startswith('#'):
                        continue
                    dependency = document.parent / target.split('#', 1)[0]
                    self.assertTrue(dependency.exists(),
                                    f'{document.relative_to(stage)} -> {target}')

    def test_profile_build_install_and_source_only_review(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            archive = base / 'profile.zip'
            subprocess.run([sys.executable, str(ROOT / 'scripts/build_consumer_profile.py'),
                            '--profile', str(ROOT / 'consumer/profiles/business-context-v0.1.paths.json'),
                            '--output', str(archive), '--version', 'review-test', '--allow-dirty'],
                           check=True, capture_output=True, text=True)
            stage = base / 'stage'
            with zipfile.ZipFile(archive) as package:
                package.extractall(stage)
                names = set(package.namelist())
            required = {
                f'{REVIEW}/SKILL.md', f'{REVIEW}/agents/openai.yaml',
                f'{REVIEW}/scripts/check_reader_artifact.py',
                '.agents/skills/mermaid-diagram-authoring/references/layout-and-curves.md',
                '.agents/skills/business-context-modeling/references/reader-facing-artifacts.md',
            }
            self.assertTrue(required <= names, required - names)
            self.assertFalse(any('__pycache__' in name or name.endswith('.pyc') for name in names))
            target = base / 'consumer'
            target.mkdir()
            owned = target / 'AGENTS.md'
            owned.write_text('# Consumer-owned instructions\n')
            subprocess.run([sys.executable, str(stage / '.fde/fde-manage.py'), 'install',
                            '--source', str(stage), '--target', str(target)],
                           check=True, capture_output=True, text=True)
            self.assertEqual(owned.read_text(), '# Consumer-owned instructions\n')
            manifest = json.loads((target / '.fde/fde-consumer.json').read_text())
            managed = {item['path']: item['sha256'] for item in manifest['managed']}
            for name in required:
                self.assertEqual(hashlib.sha256((target / name).read_bytes()).hexdigest(), managed[name])
            self.assertFalse((target / 'node_modules').exists())
            for command in (
                [sys.executable, str(target / REVIEW / 'scripts/check_reader_artifact.py'), str(target / 'templates/icon-context.md')],
                [sys.executable, str(target / '.agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py'),
                 str(target / 'templates/icon-context.md'), '--strict'],
            ):
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_directory_packaging_excludes_python_cache(self):
        spec = importlib.util.spec_from_file_location('review_builder', ROOT / 'scripts/build_consumer_profile.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            (base / 'skill/__pycache__').mkdir(parents=True)
            (base / 'skill/SKILL.md').write_text('source')
            (base / 'skill/__pycache__/module.pyc').write_bytes(b'cache')
            (base / 'skill/stray.pyc').write_bytes(b'cache')
            profile = base / 'profile.json'
            profile.write_text(json.dumps({'paths': ['skill']}))
            builder.ROOT = base
            self.assertEqual(builder.files_for(profile), [base / 'skill/SKILL.md'])


if __name__ == '__main__':
    unittest.main()
