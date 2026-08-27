#!/usr/bin/env python3
"""Validate the portable FDE bundle without changing repository content."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "README.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    ".github/copilot-instructions.md",
    ".github/agents/business-modeler.agent.md",
    ".github/agents/diagram-author.agent.md",
    ".github/agents/diagram-reviewer.agent.md",
    "templates/icon-context.mmd",
    "templates/business-flow.mmd",
    "templates/github-actions-validate.yml",
    "examples/repair-intake/model.md",
    "examples/repair-intake/model-set-index.md",
    "examples/repair-intake/overview.mmd",
]
SKILLS = [
    "business-context-modeling",
    "mermaid-icon-context-diagram",
    "mermaid-business-flow-diagram",
]
RENDERED_ICON_SIZES = {
    "overview.svg": {(22, 22): 3},
    "context.svg": {(22, 22): 1, (38, 38): 4},
    "flow.svg": {(22, 22): 3, (38, 38): 1},
}


def run(command: list[str]) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


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


def validate_rendered_icons() -> None:
    """Keep committed renders portable and faithful to the source dimensions."""
    examples = ROOT / "examples/repair-intake"
    for filename, expected in RENDERED_ICON_SIZES.items():
        path = examples / filename
        root = ElementTree.parse(path).getroot()
        counts: dict[tuple[int, int], int] = {}
        for element in root.iter():
            if not element.tag.endswith("image"):
                continue
            size = (int(element.attrib["width"]), int(element.attrib["height"]))
            counts[size] = counts.get(size, 0) + 1
            href = next(
                (value for key, value in element.attrib.items() if key.endswith("href")),
                "",
            )
            if not href.startswith("data:image/svg+xml;base64,"):
                raise ValueError(f"external icon remains in {path.relative_to(ROOT)}")
        if counts != expected:
            raise ValueError(
                f"unexpected rendered icon sizes in {path.relative_to(ROOT)}: "
                f"expected {expected}, found {counts}"
            )


def main() -> int:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            raise FileNotFoundError(relative)
    for skill in SKILLS:
        validate_skill(skill)
    json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "config/puppeteer.json").read_text(encoding="utf-8"))
    scan_public_text()
    validate_rendered_icons()

    python_files = [path for path in ROOT.rglob("*.py") if "node_modules" not in path.parts]
    for path in python_files:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    context = ".agents/skills/mermaid-icon-context-diagram/scripts/check_context_diagram.py"
    business = ".agents/skills/business-context-modeling/scripts/check_business_context.py"
    flow = ".agents/skills/mermaid-business-flow-diagram/scripts/check_business_flow.py"
    run([sys.executable, context, "templates/icon-context.mmd", "--strict"])
    run([sys.executable, business, "examples/repair-intake/context.mmd"])
    run([sys.executable, flow, "templates/business-flow.mmd", "--strict"])
    run([sys.executable, flow, "examples/repair-intake/overview.mmd", "--strict"])
    run([sys.executable, flow, "examples/repair-intake/flow.mmd", "--strict"])
    print("OK: repository structure, skills, privacy, Python, Mermaid sources, and renders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
