#!/usr/bin/env python3
"""Validate the portable FDE bundle without changing repository content."""

from __future__ import annotations

import json
import os
import re
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
    "examples/maakbo-expression-loop/README.md",
    "examples/maakbo-expression-loop/model.md",
    "examples/maakbo-expression-loop/model-set-index.md",
    "examples/maakbo-expression-loop/master-model-index.md",
    "examples/maakbo-expression-loop/master-actor-map.md",
    "examples/maakbo-expression-loop/master-system-map.md",
    "examples/maakbo-expression-loop/master-information-model.md",
    "examples/maakbo-expression-loop/overview.md",
    "examples/maakbo-expression-loop/context.md",
    "examples/maakbo-expression-loop/flow.md",
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


MODEL_SET_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MODEL_SET_PARENT_RE = re.compile(
    r"^(?P<diagram>[^\s]+\.md)\s*/\s*(?P<node>[a-z][a-z0-9_]*)$"
)
MERMAID_NODE_RE = re.compile(r"^\s{2}(?P<node>[a-z][a-z0-9_]*)@\{")


def _table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _linked_views(cell: str) -> list[str]:
    return MODEL_SET_LINK_RE.findall(cell)


def _load_mermaid_node_ids(path: Path) -> set[str]:
    return {
        match.group("node")
        for line in path.read_text(encoding="utf-8").splitlines()
        if (match := MERMAID_NODE_RE.match(line))
    }


def validate_model_set_index(relative: str) -> None:
    """Validate parent/child links and expansion IDs in one model-set index."""

    index_path = ROOT / relative
    lines = index_path.read_text(encoding="utf-8").splitlines()
    try:
        view_header = next(
            number for number, line in enumerate(lines) if line.strip() == "## View map"
        )
    except StopIteration as error:
        raise ValueError(f"{relative}: missing `## View map` section") from error

    rows: list[list[str]] = []
    for line in lines[view_header + 1 :]:
        if not line.strip().startswith("|"):
            if rows:
                break
            continue
        cells = _table_cells(line)
        if len(cells) < 5 or all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        if cells[0].lower() == "view":
            continue
        rows.append(cells)
    if not rows:
        raise ValueError(f"{relative}: view map has no rows")

    views: dict[str, dict[str, object]] = {}
    for number, cells in enumerate(rows, start=1):
        view_links = _linked_views(cells[0])
        if len(view_links) != 1:
            raise ValueError(
                f"{relative}: view row {number} must contain exactly one Markdown link"
            )
        view_target = Path(view_links[0]).as_posix()
        if view_target in views:
            raise ValueError(f"{relative}: duplicate view link: {view_target}")
        view_path = (index_path.parent / view_target).resolve()
        if not view_path.is_file():
            raise ValueError(f"{relative}: view link does not exist: {view_target}")

        parent_cell = cells[3].strip().strip("`")
        parent_target: str | None = None
        expanded_node: str | None = None
        if parent_cell not in {"", "—", "-", "none", "None"}:
            parent_match = MODEL_SET_PARENT_RE.fullmatch(parent_cell)
            if not parent_match:
                raise ValueError(
                    f"{relative}: invalid parent/expanded node in {view_target}: "
                    f"{cells[3]}"
                )
            parent_target = Path(parent_match.group("diagram")).as_posix()
            expanded_node = parent_match.group("node")
            parent_path = (index_path.parent / parent_target).resolve()
            if not parent_path.is_file():
                raise ValueError(
                    f"{relative}: parent diagram does not exist for {view_target}: "
                    f"{parent_target}"
                )
            if expanded_node not in _load_mermaid_node_ids(parent_path):
                raise ValueError(
                    f"{relative}: expansion node `{expanded_node}` is absent from "
                    f"{parent_target}"
                )

        child_targets = [Path(target).as_posix() for target in _linked_views(cells[4])]
        views[view_target] = {
            "path": view_path,
            "parent": parent_target,
            "expanded": expanded_node,
            "children": child_targets,
        }

    view_targets = set(views)
    for view_target, details in views.items():
        parent_target = details["parent"]
        if parent_target is not None:
            if parent_target not in view_targets:
                raise ValueError(
                    f"{relative}: {view_target} points to a parent not listed in the view map: "
                    f"{parent_target}"
                )
            parent_children = views[parent_target]["children"]
            if view_target not in parent_children:
                raise ValueError(
                    f"{relative}: parent/child trace is not reciprocal: {view_target} "
                    f"is missing from {parent_target}'s child links"
                )

        for child_target in details["children"]:
            if child_target not in view_targets:
                raise ValueError(
                    f"{relative}: {view_target} links to a child not listed in the view map: "
                    f"{child_target}"
                )
            child_parent = views[child_target]["parent"]
            if child_parent != view_target:
                raise ValueError(
                    f"{relative}: parent/child trace is not reciprocal: {child_target} "
                    f"declares parent {child_parent or '—'}, not {view_target}"
                )


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
    validate_model_set_index("examples/repair-intake/model-set-index.md")
    validate_model_set_index("examples/maakbo-expression-loop/model-set-index.md")

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
    run([
        sys.executable,
        master,
        "examples/maakbo-expression-loop/master-actor-map.md",
        "--kind",
        "actor",
        "--strict",
        "--allow-sparse",
    ])
    run([
        sys.executable,
        master,
        "examples/maakbo-expression-loop/master-system-map.md",
        "--kind",
        "system",
        "--strict",
    ])
    run([
        sys.executable,
        master,
        "examples/maakbo-expression-loop/master-information-model.md",
        "--kind",
        "information",
        "--strict",
    ])
    run([
        sys.executable,
        references,
        "examples/maakbo-expression-loop/overview.md",
        "--actor",
        "examples/maakbo-expression-loop/master-actor-map.md",
        "--allow-sparse",
    ])
    run([
        sys.executable,
        references,
        "examples/maakbo-expression-loop/context.md",
        "--actor",
        "examples/maakbo-expression-loop/master-actor-map.md",
        "--system",
        "examples/maakbo-expression-loop/master-system-map.md",
        "--information",
        "examples/maakbo-expression-loop/master-information-model.md",
        "--allow-sparse",
    ])
    run([sys.executable, business, "examples/maakbo-expression-loop/overview.md"])
    run([sys.executable, business, "examples/maakbo-expression-loop/context.md"])
    run([sys.executable, flow, "examples/maakbo-expression-loop/flow.md", "--strict"])
    print("OK: repository structure, skills, privacy, Python, and Markdown Mermaid sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
