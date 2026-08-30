#!/usr/bin/env python3
"""Validate the portable FDE bundle without changing repository content."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "README.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    ".github/copilot-instructions.md",
    ".github/agents/business-modeler.agent.md",
    ".github/agents/diagram-author.agent.md",
    ".github/agents/diagram-exporter.agent.md",
    ".github/agents/diagram-reviewer.agent.md",
    "templates/icon-context.md",
    "templates/business-flow.md",
    "templates/master-actor-map.md",
    "templates/master-system-map.md",
    "templates/master-information-model.md",
    "templates/master-model-index.md",
    "templates/github-actions-validate.yml",
    ".agents/skills/mermaid-diagram-authoring/scripts/source_loader.py",
    ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py",
    ".agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py",
    ".agents/skills/business-context-modeling/scripts/check_master_map.py",
    ".agents/skills/business-context-modeling/scripts/check_master_references.py",
    ".agents/skills/business-context-modeling/references/master-elements.md",
    ".agents/skills/mermaid-diagram-export/scripts/export_mermaid.py",
    "examples/repair-intake/model.md",
    "examples/repair-intake/model-set-index.md",
    "examples/repair-intake/master-model-index.md",
    "examples/repair-intake/master-actor-map.md",
    "examples/repair-intake/master-system-map.md",
    "examples/repair-intake/master-information-model.md",
    "examples/repair-intake/overview.md",
    "examples/repair-intake/context.md",
    "examples/repair-intake/flow.md",
    "examples/repair-intake/previews/README.md",
]
SKILLS = [
    "business-context-modeling",
    "mermaid-diagram-authoring",
    "mermaid-diagram-export",
]
THIN_LUCIDE_ICONS = (
    "user",
    "ellipse",
    "file",
    "server",
    "diamond",
    "tablet",
    "smartphone",
    "laptop",
)
OBSOLETE_SKILL_DIRS = [
    ".agents/skills/mermaid-icon-context-diagram",
    ".agents/skills/mermaid-business-flow-diagram",
]


def run(command: list[str]) -> None:
    print("+", " ".join(command))
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run(command, cwd=ROOT, check=True, env=environment)


def validate_skill(skill: str) -> None:
    path = ROOT / ".agents/skills" / skill / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or f"name: {skill}\n" not in text:
        raise ValueError(f"invalid frontmatter in {path}")
    if "description:" not in text.split("---", 2)[1]:
        raise ValueError(f"missing description in {path}")
    if "TODO" in text:
        raise ValueError(f"unfinished TODO in {path}")
    metadata = ROOT / ".agents/skills" / skill / "agents/openai.yaml"
    if not metadata.is_file() or f"${skill}" not in metadata.read_text(encoding="utf-8"):
        raise ValueError(f"stale or missing {metadata}")


def scan_public_text() -> None:
    forbidden = (
        "/" + "Users" + "/",
        "i" + "Cloud~",
        "Mobile" + " Documents/",
        "career-history" + "-full",
    )
    suffixes = {".md", ".mmd", ".py", ".json", ".yaml", ".yml"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "node_modules" in path.parts:
            continue
        if path.suffix not in suffixes and path.name not in {"LICENSE"}:
            continue
        text = path.read_text(encoding="utf-8")
        for token in forbidden:
            if token in text:
                raise ValueError(f"private-path token `{token}` found in {path.relative_to(ROOT)}")


def validate_thin_icons() -> None:
    icon_dir = ROOT / "assets/icons/lucide-thin"
    for name in THIN_LUCIDE_ICONS:
        path = icon_dir / f"{name}.svg"
        if not path.is_file():
            raise FileNotFoundError(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        if 'stroke-width="1.35"' not in text:
            raise ValueError(f"thin Lucide icon has the wrong stroke width: {path.relative_to(ROOT)}")
        if 'stroke-width="2"' in text:
            raise ValueError(f"standard Lucide stroke width remains: {path.relative_to(ROOT)}")


def main() -> int:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            raise FileNotFoundError(relative)
    for relative in OBSOLETE_SKILL_DIRS:
        if (ROOT / relative / "SKILL.md").exists():
            raise ValueError(f"obsolete overlapping Skill remains: {relative}")
    for skill in SKILLS:
        validate_skill(skill)
    json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "config/puppeteer.json").read_text(encoding="utf-8"))
    scan_public_text()
    validate_thin_icons()

    python_files = [path for path in ROOT.rglob("*.py") if "node_modules" not in path.parts]
    for path in python_files:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    context = ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py"
    business = ".agents/skills/business-context-modeling/scripts/check_business_context.py"
    flow = ".agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py"
    run([sys.executable, context, "templates/icon-context.md", "--strict"])
    master = ".agents/skills/business-context-modeling/scripts/check_master_map.py"
    run([sys.executable, master, "templates/master-actor-map.md", "--kind", "actor", "--strict"])
    run([sys.executable, master, "templates/master-system-map.md", "--kind", "system", "--strict"])
    run([sys.executable, master, "templates/master-information-model.md", "--kind", "information", "--strict"])
    run([
        sys.executable,
        master,
        "examples/repair-intake/master-actor-map.md",
        "--kind",
        "actor",
        "--strict",
        "--allow-sparse",
    ])
    run([sys.executable, master, "examples/repair-intake/master-system-map.md", "--kind", "system", "--strict"])
    run([sys.executable, master, "examples/repair-intake/master-information-model.md", "--kind", "information", "--strict"])
    references = ".agents/skills/business-context-modeling/scripts/check_master_references.py"
    run([
        sys.executable,
        references,
        "examples/repair-intake/context.md",
        "--actor",
        "examples/repair-intake/master-actor-map.md",
        "--system",
        "examples/repair-intake/master-system-map.md",
        "--information",
        "examples/repair-intake/master-information-model.md",
        "--allow-sparse",
    ])
    run([sys.executable, business, "examples/repair-intake/context.md"])
    run([sys.executable, flow, "templates/business-flow.md", "--strict"])
    run([sys.executable, flow, "examples/repair-intake/overview.md", "--strict"])
    run([sys.executable, flow, "examples/repair-intake/flow.md", "--strict"])
    print("OK: repository structure, skills, privacy, Python, and Markdown Mermaid sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
