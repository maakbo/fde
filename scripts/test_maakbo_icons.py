#!/usr/bin/env python3
"""Regression checks for local exports and optical-stroke compensation."""

import base64
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


validator = module("maakbo_validator", "scripts/validate_repository.py")
exporter = module("maakbo_exporter", ".agents/skills/mermaid-diagram-export/scripts/export_mermaid.py")


class MaakboIcons(unittest.TestCase):
    def test_every_icon_exports_local_approved_bytes_without_network(self):
        for name in validator.MAAKBO_ICONS:
            source = f'img: "{exporter.MAAKBO_ICON_RAW_PREFIX}{name}.svg"'
            result = exporter.inline_icon_assets(source, ROOT)
            encoded = result.split("base64,", 1)[1].rstrip('"')
            self.assertEqual(base64.b64decode(encoded), (ROOT / f"assets/icons/maakbo/{name}.svg").read_bytes())

    def test_missing_local_icon_fails_instead_of_fetching_remote(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(FileNotFoundError):
                exporter.inline_icon_assets(f'img: "{exporter.MAAKBO_ICON_RAW_PREFIX}user.svg"', Path(temp))

    def test_validator_rejects_uncompensated_optical_scale(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(ROOT / "assets/icons", root / "assets/icons")
            path = root / "assets/icons/maakbo/user.svg"
            text = path.read_text()
            # Replacing inverse compensation with the nominal stroke must fail.
            import re
            path.write_text(re.sub(r'stroke-width="[^"]+"', 'stroke-width="1.15"', text))
            with patch.object(validator, "ROOT", root):
                with self.assertRaisesRegex(ValueError, "effective maakbo stroke"):
                    validator.validate_maakbo_icons()


if __name__ == "__main__":
    unittest.main()
