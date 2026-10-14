#!/usr/bin/env python3
"""Regression checks for explicit immutable selection from multi-diagram Markdown."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / '.agents/skills/mermaid-diagram-authoring/scripts'))
from source_loader import SourceError, load_mermaid_source


class DiagramSelection(unittest.TestCase):
    def test_multiple_blocks_require_selection_and_keep_source_location(self):
        text = '# First\n\n```mermaid\nflowchart LR\n  a --- b\n```\n\n# Second\n\n```mermaid\nflowchart TB\n  c --> d\n```\n'
        with tempfile.TemporaryDirectory() as temporary:
            page = Path(temporary) / 'README.md'
            page.write_text(text)
            with self.assertRaises(SourceError):
                load_mermaid_source(page)
            selected = load_mermaid_source(page, diagram_index=2)
            self.assertEqual(selected.text, 'flowchart TB\n  c --> d\n')
            self.assertEqual(selected.start_line, 11)
            self.assertEqual(page.read_text(), text)
            for index in (0, -1, 3):
                with self.assertRaises(SourceError):
                    load_mermaid_source(page, diagram_index=index)

    def test_single_block_default_is_unchanged_and_mmd_selection_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            page = Path(temporary) / 'single.md'
            page.write_text('# Business\n\n```mermaid\nflowchart LR\n```\n')
            self.assertEqual(load_mermaid_source(page), load_mermaid_source(page, diagram_index=1))
            standalone = page.with_suffix('.mmd')
            standalone.write_text('flowchart LR\n')
            self.assertEqual(load_mermaid_source(standalone).text, 'flowchart LR\n')
            with self.assertRaises(SourceError):
                load_mermaid_source(standalone, diagram_index=1)


if __name__ == '__main__':
    unittest.main()
