#!/usr/bin/env python3
"""Exercise both diagram families and consumer-owned config across installation/update."""

import base64
from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / ".agents/skills/mermaid-diagram-authoring/scripts"
sys.path.insert(0, str(AUTHORING))
import icon_registry as icons


def load_module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


exporter = load_module("family_exporter", ".agents/skills/mermaid-diagram-export/scripts/export_mermaid.py")
consumer = load_module("family_consumer", "scripts/fde_consumer.py")


class IconSets(unittest.TestCase):
    def run_check(self, script, path, *args):
        result = subprocess.run([sys.executable, str(ROOT / script), str(path), *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_project_config_and_existing_source_are_independent(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertEqual(icons.configured_set(root), "mdi")
            config = root / ".fde/config.json"
            config.parent.mkdir()
            config.write_text('{"icon_set":"maakbo","custom":"keep"}')
            icons.configure(root, "mdi")
            self.assertEqual(json.loads(config.read_text())["custom"], "keep")
            source = (ROOT / "templates/icon-context.md").read_text()
            self.assertEqual(icons.icon_set_for_source(source, root / "old.md"), "maakbo")
            with self.assertRaisesRegex(ValueError, "explicit migration"):
                icons.icon_set_for_source(source, root / "old.md", "mdi")
            config.write_text('{"icon_set":"typo"}')
            with self.assertRaisesRegex(ValueError, "unknown icon_set"):
                icons.configured_set(root)
            config.write_text('{"icon_set":[]}')
            with self.assertRaisesRegex(ValueError, "unknown icon_set"):
                icons.configured_set(root)

    def test_project_boundary_does_not_inherit_upstream_preference(self):
        with tempfile.TemporaryDirectory() as temp:
            parent = Path(temp)
            icons.configure(parent, "maakbo")
            child = parent / "child"
            (child / ".git").mkdir(parents=True)
            self.assertEqual(icons.configured_set(child), "mdi")

    def test_both_families_pass_context_flow_master_and_architecture(self):
        jobs = [
            ("templates/icon-context.md", ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py", ["--strict"]),
            ("templates/business-flow.md", ".agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py", ["--strict"]),
            ("templates/architecture-context.md", ".agents/skills/architecture-modeling/scripts/check_architecture_context.py", ["--strict"]),
            ("examples/human-agent-workspace/README.md", ".agents/skills/architecture-modeling/scripts/check_architecture_context.py", ["--strict"]),
            ("templates/master-actor-map.md", ".agents/skills/business-context-modeling/scripts/check_master_map.py", ["--kind", "actor", "--strict"]),
            ("templates/master-system-map.md", ".agents/skills/business-context-modeling/scripts/check_master_map.py", ["--kind", "system", "--strict"]),
            ("templates/master-information-model.md", ".agents/skills/business-context-modeling/scripts/check_master_map.py", ["--kind", "information", "--strict"]),
        ]
        with tempfile.TemporaryDirectory() as temp:
            for family in ("mdi", "maakbo"):
                for index, (source, checker, options) in enumerate(jobs):
                    path = Path(temp) / f"{family}-{index}.md"
                    path.write_text(icons.rewrite_icons((ROOT / source).read_text(), family))
                    self.run_check(checker, path, *options, "--icon-set", family)

    def test_mixed_families_are_rejected(self):
        source = (ROOT / "templates/icon-context.md").read_text()
        mixed = source.replace(icons.asset("maakbo", "actor")["url"], icons.asset("mdi", "actor")["url"], 1)
        with self.assertRaisesRegex(ValueError, "mixed"):
            icons.icon_set_for_source(mixed, ROOT / "templates/icon-context.md")

    def test_mdi_business_context_keeps_master_reference_identity(self):
        fixture = ROOT / ".agents/skills/business-context-modeling/fixtures/repair-intake"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("context.md", "master-actor-map.md", "master-system-map.md", "master-information-model.md"):
                (root / name).write_text(icons.rewrite_icons((fixture / name).read_text(), "mdi"))
            self.run_check(".agents/skills/business-context-modeling/scripts/check_business_context.py", root / "context.md", "--icon-set", "mdi")
            self.run_check(".agents/skills/business-context-modeling/scripts/check_master_references.py", root / "context.md",
                           "--actor", str(root / "master-actor-map.md"), "--system", str(root / "master-system-map.md"),
                           "--information", str(root / "master-information-model.md"), "--allow-sparse", "--icon-set", "mdi")

    def test_all_registered_assets_export_pinned_local_bytes(self):
        for family, spec in icons.registry()["sets"].items():
            for role in spec["icons"]:
                icon = icons.asset(family, role)
                urls = [icon["url"]]
                if family == "mdi":
                    urls.append("https://api.iconify.design/mdi/" + icon["filename"])
                for url in urls:
                    result = exporter.inline_icon_assets(f'img: "{url}"', ROOT)
                    data = base64.b64decode(result.split("base64,", 1)[1].rstrip('"'))
                    self.assertEqual(data, (ROOT / "assets/icons" / family / icon["filename"]).read_bytes())

    def test_installer_seeds_choice_but_update_preserves_owned_config_and_models(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source"
            (source / ".fde").mkdir(parents=True)
            managed = source / "managed.txt"
            managed.write_text("version one")
            manifest = {"schema":"fde-consumer/v1", "profile":"test", "upstream":{"repository":"test","revision":"one","version":"one"},
                        "managed":[{"path":"managed.txt","sha256":hashlib.sha256(managed.read_bytes()).hexdigest()}]}
            (source / consumer.MANIFEST_PATH).write_text(json.dumps(manifest))
            target = root / "target"
            with redirect_stdout(io.StringIO()):
                self.assertEqual(consumer.install(source, target, manifest), 0)
            config = target / ".fde/config.json"
            self.assertEqual(json.loads(config.read_text())["icon_set"], "mdi")
            config.write_text('{"icon_set":"maakbo","custom":"keep"}')
            model = target / "model.md"
            model.write_text("consumer-owned diagram")
            before = config.read_bytes()
            managed.write_text("version two")
            candidate = json.loads(json.dumps(manifest))
            candidate["upstream"].update(revision="two",version="two")
            candidate["managed"][0]["sha256"] = hashlib.sha256(managed.read_bytes()).hexdigest()
            (source / consumer.MANIFEST_PATH).write_text(json.dumps(candidate))
            with redirect_stdout(io.StringIO()):
                self.assertEqual(consumer.update(source, target, candidate), 0)
            self.assertEqual(config.read_bytes(), before)
            self.assertEqual(model.read_text(), "consumer-owned diagram")
            # An existing preference wins even if installation has a different flag.
            other = root / "other"
            icons.configure(other, "maakbo")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(consumer.install(source, other, candidate, "mdi"), 0)
            self.assertEqual(icons.configured_set(other), "maakbo")
            unset = root / "unset"
            (unset / ".fde").mkdir(parents=True)
            (unset / ".fde/config.json").write_text('{"custom":"keep"}')
            with redirect_stdout(io.StringIO()):
                self.assertEqual(consumer.install(source, unset, candidate, "maakbo"), 0)
            self.assertEqual(json.loads((unset / ".fde/config.json").read_text()), {"custom":"keep", "icon_set":"maakbo"})

    def test_profile_cannot_manage_owned_config(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = icons.configure(root, "maakbo")
            manifest = {"managed":[{"path":".fde/config.json", "sha256":hashlib.sha256(config.read_bytes()).hexdigest()}]}
            self.assertIn("must not be a managed file", consumer.verify_source(root, manifest)[0])

    def test_create_uses_destination_config_and_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output = root / "model.md"
            script = AUTHORING / "icon_registry.py"
            command = [sys.executable, str(script), "create", str(ROOT / "templates/icon-context.md"), "--output", str(output)]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stdout)
            self.assertEqual(icons.icon_set_for_source(output.read_text(), output), "mdi")
            before = output.read_bytes()
            second = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(output.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
