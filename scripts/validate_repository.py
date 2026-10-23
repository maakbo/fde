#!/usr/bin/env python3
"""Validate the portable FDE bundle without changing repository content."""

from __future__ import annotations

import json
import math
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "examples/system-development/README.md",
    "examples/system-development/deliverables.md",
    "examples/system-development/design/README.md",
    "examples/system-development/environments.md",
    "examples/system-development/implementation/README.md",
    "examples/system-development/implementation/agent-assisted-flow.md",
    "examples/system-development/implementation/development-flow.md",
    "examples/system-development/people.md",
    "examples/system-development/release-and-operations/README.md",
    "examples/system-development/requirements/README.md",
    "examples/system-development/testing/README.md",

    "AGENTS.md",
    "README.md",
    "LICENSE",
    "assets/icons/maakbo/README.md",
    "assets/icons/maakbo/LICENSE",
    "assets/icons/maakbo/PROVENANCE.md",
    "scripts/test_maakbo_icons.py",
    "scripts/test_icon_sets.py",
    "scripts/test_review_profile.py",
    ".agents/skills/mermaid-diagram-authoring/scripts/icon_registry.py",
    ".agents/skills/mermaid-diagram-authoring/references/icon-sets.json",
    ".agents/skills/mermaid-diagram-authoring/references/mdi-license/README.md",
    ".agents/skills/mermaid-diagram-authoring/references/mdi-license/LICENSE",
    ".agents/skills/mermaid-diagram-authoring/references/mdi-license/UPSTREAM-LICENSE",
    ".github/copilot-instructions.md",
    ".github/agents/business-modeler.agent.md",
    ".github/agents/diagram-author.agent.md",
    ".github/agents/diagram-exporter.agent.md",
    ".github/agents/diagram-reviewer.agent.md",
    "templates/icon-context.md",
    "templates/architecture-context.md",
    "templates/business-flow.md",
    "templates/discovery-brief.md",
    "templates/definition-brief.md",
    "templates/workflow-brief.md",
    ".agents/skills/architecture-modeling/references/task-context.md",
    ".agents/skills/discovery-facilitation/references/field-delivery-loop.md",
    ".agents/skills/architecture-modeling/references/agent-work-design.md",
    "templates/knowledge-use-brief.md",
    "templates/ai-trial-brief.md",
    "templates/team-adoption-brief.md",
    ".agents/skills/team-adoption-facilitation/references/operating-and-measures.md",
    ".agents/skills/knowledge-stewardship/references/knowledge-and-retrieval.md",
    ".agents/skills/ai-pilot-evaluation/references/governance-and-use.md",
    ".agents/skills/business-context-modeling/references/field-interview-and-grain.md",
    "templates/agent-feasibility.md",
    ".agents/skills/architecture-modeling/references/ai-agent-foundations.md",
    ".agents/skills/business-context-modeling/references/work-understanding-and-redesign.md",
    ".agents/skills/discovery-facilitation/references/agent-feasibility.md",
    "examples/request-triage/README.md",
    "templates/master-actor-map.md",
    "templates/master-system-map.md",
    "templates/master-information-model.md",
    "templates/master-model-index.md",
    "templates/github-actions-validate.yml",
    ".agents/skills/mermaid-diagram-authoring/scripts/source_loader.py",
    ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py",
    ".agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py",
    ".agents/skills/mermaid-diagram-authoring/fixtures/context-arrow-visual-regression.md",
    ".agents/skills/architecture-modeling/scripts/check_architecture_context.py",
    ".agents/skills/architecture-modeling/references/modeling-rules.md",
    ".agents/skills/architecture-modeling/references/reader-facing-artifacts.md",
    ".agents/skills/business-context-modeling/scripts/check_master_map.py",
    ".agents/skills/business-context-modeling/scripts/check_master_references.py",
    ".agents/skills/business-context-modeling/references/business-story-and-5w2h.md",
    ".agents/skills/business-context-modeling/references/master-elements.md",
    ".agents/skills/business-context-modeling/references/reader-facing-artifacts.md",
    ".agents/skills/mermaid-diagram-export/scripts/export_mermaid.py",
    ".agents/skills/mermaid-diagram-export/scripts/test_diagram_selection.py",
    ".agents/skills/mermaid-diagram-export/scripts/render_mermaid.mjs",
    ".agents/skills/mermaid-diagram-authoring/references/layout-and-curves.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/model.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/model-set-index.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/master-model-index.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/master-actor-map.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/master-system-map.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/master-information-model.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/overview.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/context.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/flow.md",
    ".agents/skills/business-context-modeling/fixtures/repair-intake/previews/README.md",
    ".agents/skills/discovery-facilitation/fixtures/system-development-intake.md",
    ".agents/skills/discovery-facilitation/fixtures/system-development-brief.md",
    "examples/maakbo-fde/README.md",
    "examples/human-agent-workspace/README.md",
]
SKILLS = [
    "team-adoption-facilitation",
    "workflow-design-facilitation",
    "definition-facilitation",
    "knowledge-stewardship",
    "ai-pilot-evaluation",
    "business-flow-facilitation",
    "architecture-modeling",
    "business-context-modeling",
    "discovery-facilitation",
    "mermaid-diagram-authoring",
    "mermaid-diagram-export",
    "reader-facing-artifact-review",
]
MAAKBO_ICONS = (
    "user",
    "bot",
    "ellipse",
    "file",
    "folder-git-2",
    "server",
    "cloud",
    "message-square",
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


def run_expect_failure(command: list[str]) -> None:
    print("+ EXPECT FAILURE:", " ".join(command))
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        env=environment,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        raise ValueError(f"command unexpectedly passed: {' '.join(command)}")


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


def validate_maakbo_icons() -> None:
    icon_dir = ROOT / "assets/icons/maakbo"
    expected = {f"{name}.svg" for name in MAAKBO_ICONS}
    if {path.name for path in icon_dir.glob("*.svg")} != expected:
        raise ValueError("maakbo must contain exactly the twelve approved icons")
    if "MIT License" not in (icon_dir / "LICENSE").read_text():
        raise ValueError("maakbo icons must include their MIT license")
    if (ROOT / "assets/icons/lucide-thin").exists():
        raise ValueError("retired Lucide assets must not remain")
    for name in MAAKBO_ICONS:
        path = icon_dir / f"{name}.svg"
        svg = ET.parse(path).getroot()
        if svg.get("viewBox") != "0 0 24 24" or svg.get("style") != "color:#25231F":
            raise ValueError(f"wrong maakbo canvas or ink: {path.relative_to(ROOT)}")
        groups = svg.findall("{http://www.w3.org/2000/svg}g")
        if len(groups) != 1:
            raise ValueError(f"expected one maakbo geometry group: {path.name}")
        group = groups[0]
        transform = group.get("transform", "")
        scale = 1.0
        if transform:
            match = re.fullmatch(
                r"translate\((-?[\d.]+) (-?[\d.]+)\) scale\(([\d.]+)\)", transform
            )
            if not match:
                raise ValueError(f"unsupported maakbo optical transform: {path.name}")
            scale = float(match[3])
        if not math.isclose(float(group.get("stroke-width", "0")) * scale, 1.15, abs_tol=1e-7):
            raise ValueError(f"wrong effective maakbo stroke width: {path.name}")
        if group.get("fill") != "none" or group.get("stroke") != "currentColor":
            raise ValueError(f"wrong maakbo fill or stroke: {path.name}")
        if group.get("stroke-linecap") != "round" or group.get("stroke-linejoin") != "round":
            raise ValueError(f"wrong maakbo line endings: {path.name}")
        for child in group:
            if child.tag.rsplit("}", 1)[-1] not in {"path", "rect", "ellipse", "circle"}:
                raise ValueError(f"unsupported maakbo geometry: {path.name}")
    # Historical comparisons keep their source; active authoring must use the new URLs.
    for folder in (".agents", "templates", "examples", "consumer"):
        for path in (ROOT / folder).rglob("*.md"):
            if "assets/icons/lucide-thin/" in path.read_text():
                raise ValueError(f"legacy icon URL in active source: {path.relative_to(ROOT)}")


def validate_mdi_icons() -> None:
    if (ROOT / "assets/icons/mdi").exists():
        raise ValueError("MDI must refer directly to Iconify, not hosted repository assets")
    registry = json.loads((ROOT / ".agents/skills/mermaid-diagram-authoring/references/icon-sets.json").read_text())
    license_path = ROOT / ".agents/skills/mermaid-diagram-authoring/references/mdi-license/LICENSE"
    if "Apache License" not in license_path.read_text():
        raise ValueError("MDI Apache license is missing")
    mdi = registry["sets"]["mdi"]
    if registry["default"] != "mdi" or mdi["default_source"] != "upstream":
        raise ValueError("MDI must default to external upstream SVGs")
    if mdi["sources"] != {
        "upstream": "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/",
        "iconify": "https://api.iconify.design/mdi/",
    }:
        raise ValueError("MDI sources must not depend on hosted fde images")


def validate_icon_sizes() -> None:
    registry = json.loads((ROOT / ".agents/skills/mermaid-diagram-authoring/references/icon-sets.json").read_text())
    for name, family in registry["sets"].items():
        if any(size != [28, 28] for size in family["sizes"].values()):
            raise ValueError(f"{name}: all icon roles must use 28x28")
    # Historical experiments retain the dimensions used to make each decision.
    for folder in (".agents", "templates", "examples", "consumer", "assets"):
        for path in (ROOT / folder).rglob("*.md"):
            for line in path.read_text().splitlines():
                if "img:" not in line:
                    continue
                size = re.search(r"w:\s*(\d+),\s*h:\s*(\d+)", line)
                if size and size.groups() != ("28", "28"):
                    raise ValueError(f"{path.relative_to(ROOT)}: image nodes must use 28x28")


FDE_READER_MODEL_FILES = ("README.md",)
FDE_READER_SECTIONS = (
    "FDEを担う人とAI",
    "業務を理解し、変化を決める",
    "人とAIの協働をつくり、試す",
    "現場で使い、ともに育てる",
)

FDE_READER_BUSINESSES = {
    "FDEを担う人とAI": (),
    "業務を理解し、変化を決める": ("対象業務選定", "業務定義"),
    "人とAIの協働をつくり、試す": ("協働設計", "協働検証"),
    "現場で使い、ともに育てる": ("現場導入・改善",),
}


def fde_reader_sections() -> dict[str, str]:
    text = (ROOT / "examples/maakbo-fde/README.md").read_text(encoding="utf-8")
    sections = {}
    for section in re.split(r"^## ", text, flags=re.MULTILINE)[1:]:
        title, _, body = section.partition("\n")
        if title in FDE_READER_SECTIONS:
            if title in sections:
                raise ValueError(f"duplicate FDE section: {title}")
            sections[title] = body
    if tuple(sections) != FDE_READER_SECTIONS:
        raise ValueError("FDE reader sections are missing or out of order")
    return sections


def _validate_sample_links(sample: Path) -> None:
    for artifact in sample.glob("*.md"):
        text = artifact.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            linked = (artifact.parent / target.split("#", 1)[0]).resolve()
            if not linked.exists():
                raise ValueError(
                    f"{artifact.relative_to(ROOT)}: broken sample link: {target}"
                )


def validate_fde_reader_surface() -> None:
    """Keep the public FDE sample focused on business understanding."""

    sample = ROOT / "examples/maakbo-fde"
    forbidden_sections = (
        "## Modeling question",
        "## Candidate inventory",
        "## ASCII options",
        "## Boundary",
        "## Unresolved",
        "## Next review question",
        "## Status",
        "## Complexity note",
        "## モデル",
        "### モデル",
        "## このモデルが表していること",
        "### このモデルが表していること",
        "### この段階で残すもの",
        "## このページの構成",
    )

    for name in FDE_READER_MODEL_FILES:
        relative = Path(name)
        artifact = sample / relative
        text = artifact.read_text(encoding="utf-8")
        sections = fde_reader_sections()
        if text.count("```mermaid") != len(FDE_READER_SECTIONS):
            raise ValueError(f"{artifact.relative_to(ROOT)}: unexpected Mermaid count")
        for title, body in sections.items():
            if body.count("```mermaid") != 1:
                raise ValueError(f"{artifact.relative_to(ROOT)} / {title}: expected one Mermaid model")
            # Retain all five businesses under the three scenes after removing
            # the separate delivery flow. Headings alone do not validate meaning.
            businesses = tuple(re.findall(r"^### (.+)$", body, re.MULTILINE))
            if businesses != FDE_READER_BUSINESSES[title]:
                raise ValueError(
                    f"{artifact.relative_to(ROOT)} / {title}: missing or misplaced business"
                )
            # A subject heading leads directly to its diagram and business reading.
            reading = body.strip()
            match = re.match(r"```mermaid\n.*?\n```\n\n(.+)", reading, re.DOTALL)
            if not match:
                raise ValueError(
                    f"{artifact.relative_to(ROOT)} / {title}: expected diagram then business reading"
                )
        for heading in forbidden_sections:
            if heading in text:
                raise ValueError(
                    f"{artifact.relative_to(ROOT)}: authoring section leaked into reader surface: "
                    f"{heading}"
                )
    _validate_sample_links(sample)


def validate_architecture_reader_surface() -> None:
    """Keep the public architecture sample small and free of authoring history."""

    sample = ROOT / "examples/human-agent-workspace"
    model_files = ("README.md",)
    forbidden_sections = (
        "## Candidate inventory",
        "## Relationship model",
        "## Boundary reasoning",
        "## Naming candidates",
        "## Validation",
        "## Unresolved",
    )
    private_only_tokens = (
        "90_system/",
        "agent-handoff/",
        "matti-to-kubox.md",
        "kubox-to-matti.md",
        "kubox-role.md",
        "kubox-reviewer-role.md",
        "request_id:",
        "status:",
        "owner:",
        "updated:",
        "sprint-briefs/",
    )
    for name in model_files:
        artifact = sample / name
        text = artifact.read_text(encoding="utf-8")
        if text.count("```mermaid") != 1:
            raise ValueError(f"{artifact.relative_to(ROOT)}: expected one Mermaid model")
        if not text.startswith("# "):
            raise ValueError(
                f"{artifact.relative_to(ROOT)}: missing reader-facing page title"
            )
        for heading in forbidden_sections:
            if heading in text:
                raise ValueError(
                    f"{artifact.relative_to(ROOT)}: authoring section leaked into reader surface: "
                    f"{heading}"
                )
    for artifact in sample.glob("*.md"):
        text = artifact.read_text(encoding="utf-8")
        for token in private_only_tokens:
            if token in text:
                raise ValueError(
                    f"{artifact.relative_to(ROOT)}: private-only operational token leaked: "
                    f"{token}"
                )

    _validate_sample_links(sample)


def validate_system_development_reader_surface() -> None:
    """Validate linked reader pages, semantic profiles and shared identities."""
    sample = ROOT / "examples/system-development"
    context = ROOT / ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py"
    business = ROOT / ".agents/skills/business-context-modeling/scripts/check_business_context.py"
    flow = ROOT / ".agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py"
    master = ROOT / ".agents/skills/business-context-modeling/scripts/check_master_map.py"
    refs = ROOT / ".agents/skills/business-context-modeling/scripts/check_master_references.py"
    reader = ROOT / ".agents/skills/reader-facing-artifact-review/scripts/check_reader_artifact.py"
    masters = {"people.md": "actor", "deliverables.md": "information", "environments.md": "system"}
    root_text = (sample / "README.md").read_text()
    for child in ("requirements", "design", "implementation", "testing", "release-and-operations"):
        if f"({child}/)" not in root_text:
            raise ValueError(f"sample root missing business link: {child}")
    for artifact in sorted(sample.rglob("*.md")):
        text = artifact.read_text()
        run([sys.executable, str(reader), str(artifact)])
        if artifact.name in masters and artifact.parent == sample:
            run([sys.executable, str(master), str(artifact), "--kind", masters[artifact.name],
                 "--strict", "--allow-complexity", "--allow-sparse"])
        elif artifact.name.endswith("-flow.md"):
            run([sys.executable, str(flow), str(artifact), "--strict"])
        else:
            run([sys.executable, str(context), str(artifact), "--strict", "--allow-complexity"])
            run([sys.executable, str(business), str(artifact), "--allow-complexity"])
            run([sys.executable, str(refs), str(artifact),
                 "--actor", str(sample / "people.md"),
                 "--information", str(sample / "deliverables.md"),
                 "--system", str(sample / "environments.md"),
                 "--allow-complexity", "--allow-sparse"])
        parent = re.search(r"%% parent: ([^ ;]+) / (b_[a-z0-9_]+)", text)
        if artifact != sample / "README.md" and artifact.name not in masters and not parent:
            raise ValueError(f"{artifact}: missing parent Business trace")
        if parent:
            target = (artifact.parent / parent[1]).resolve()
            if not target.is_file() or not re.search(rf"^\s+{re.escape(parent[2])}@", target.read_text(), re.M):
                raise ValueError(f"{artifact}: missing parent Business {parent[1]} / {parent[2]}")
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in link or link.startswith("#"):
                continue
            if not (artifact.parent / link.split("#", 1)[0]).resolve().exists():
                raise ValueError(f"{artifact}: broken sample link: {link}")


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
    validate_maakbo_icons()
    validate_mdi_icons()
    validate_icon_sizes()
    run([sys.executable, "scripts/test_maakbo_icons.py"])
    run([sys.executable, "scripts/test_icon_sets.py"])
    run([sys.executable, "scripts/test_review_profile.py"])
    run([sys.executable, "-m", "unittest", "discover", "-s",
         "examples/field-delivery/order-search", "-p", "test_workflow.py"])
    reader_checker = ".agents/skills/reader-facing-artifact-review/scripts/check_reader_artifact.py"
    run([sys.executable, ".agents/skills/reader-facing-artifact-review/scripts/test_reader_artifact.py"])
    run([sys.executable, ".agents/skills/mermaid-diagram-export/scripts/test_diagram_selection.py"])
    run([sys.executable, reader_checker,
         "examples/maakbo-fde/README.md",
         "examples/request-triage/README.md",
         "templates/icon-context.md", "templates/business-flow.md", "templates/architecture-context.md"])
    validate_fde_reader_surface()
    validate_architecture_reader_surface()
    validate_system_development_reader_surface()
    validate_model_set_index(
        ".agents/skills/business-context-modeling/fixtures/repair-intake/model-set-index.md"
    )

    python_files = [path for path in ROOT.rglob("*.py") if "node_modules" not in path.parts]
    for path in python_files:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    context = ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py"
    architecture = ".agents/skills/architecture-modeling/scripts/check_architecture_context.py"
    business = ".agents/skills/business-context-modeling/scripts/check_business_context.py"
    flow = ".agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py"
    run([sys.executable, flow, "examples/request-triage/README.md", "--strict"])
    run([sys.executable, business, "templates/icon-context.md"])
    run([sys.executable, architecture, "templates/architecture-context.md", "--strict"])
    run([
        sys.executable,
        architecture,
        "examples/human-agent-workspace/README.md",
        "--strict",
    ])
    regression_fixture = (
        ".agents/skills/mermaid-diagram-authoring/fixtures/"
        "context-arrow-visual-regression.md"
    )
    run_expect_failure([sys.executable, context, regression_fixture, "--strict", "--allow-complexity"])
    run([
        sys.executable,
        context,
        regression_fixture,
        "--strict",
        "--allow-complexity",
        "--allow-arrow-exception",
    ])
    master = ".agents/skills/business-context-modeling/scripts/check_master_map.py"
    run([sys.executable, master, "templates/master-actor-map.md", "--kind", "actor", "--strict"])
    run([sys.executable, master, "templates/master-system-map.md", "--kind", "system", "--strict"])
    run([sys.executable, master, "templates/master-information-model.md", "--kind", "information", "--strict"])
    fixture = ".agents/skills/business-context-modeling/fixtures/repair-intake"
    run([
        sys.executable,
        master,
        f"{fixture}/master-actor-map.md",
        "--kind",
        "actor",
        "--strict",
        "--allow-sparse",
    ])
    run([sys.executable, master, f"{fixture}/master-system-map.md", "--kind", "system", "--strict"])
    run([sys.executable, master, f"{fixture}/master-information-model.md", "--kind", "information", "--strict"])
    references = ".agents/skills/business-context-modeling/scripts/check_master_references.py"
    run([
        sys.executable,
        references,
        f"{fixture}/context.md",
        "--actor",
        f"{fixture}/master-actor-map.md",
        "--system",
        f"{fixture}/master-system-map.md",
        "--information",
        f"{fixture}/master-information-model.md",
        "--allow-sparse",
    ])
    run([sys.executable, business, f"{fixture}/context.md"])
    run([sys.executable, flow, "templates/business-flow.md", "--strict"])
    run([sys.executable, flow, f"{fixture}/overview.md", "--strict"])
    run([sys.executable, flow, f"{fixture}/flow.md", "--strict"])
    # Existing checkers accept one model per input. Extract the consolidated
    # sections only into a temporary directory, keeping README as the sole source.
    sections = fde_reader_sections()
    checks = (
        ("FDEを担う人とAI", context, ["--strict"]),
        ("業務を理解し、変化を決める", business, []),
        ("人とAIの協働をつくり、試す", business, []),
        ("現場で使い、ともに育てる", business, []),
    )
    with tempfile.TemporaryDirectory(prefix="fde-reader-") as temporary:
        for index, (title, checker, options) in enumerate(checks):
            artifact = Path(temporary) / f"section-{index}.md"
            artifact.write_text(f"# {title}\n\n{sections[title]}", encoding="utf-8")
            print(f"FDE reader section: {title}")
            run([sys.executable, checker, str(artifact), *options])
    print("OK: repository structure, skills, privacy, Python, and Markdown Mermaid sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
