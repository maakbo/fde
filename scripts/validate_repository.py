#!/usr/bin/env python3
"""Validate the portable FDE bundle without changing repository content."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
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
    "templates/architecture-context.md",
    "templates/business-flow.md",
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
    "examples/maakbo-fde/README.md",
    "examples/maakbo-fde/purpose-outcome.md",
    "examples/maakbo-fde/business-map.md",
    "examples/maakbo-fde/system-context.md",
    "examples/maakbo-fde/actor-requirement.md",
    "examples/maakbo-fde/shape-change-context.md",
    "examples/maakbo-fde/build-collaboration-context.md",
    "examples/maakbo-fde/establish-work-context.md",
    "examples/maakbo-fde/change-design-flow.md",
    "examples/human-agent-workspace/README.md",
    "examples/human-agent-workspace/architecture-overview.md",
    "examples/human-agent-workspace/handoff-review-flow.md",
    "examples/pdf-report-system/README.md",
    "examples/pdf-report-system/domain-overview.md",
    "examples/pdf-report-system/report-creation-context.md",
    "examples/pdf-report-system/model-set-index.md",
    "examples/pdf-report-system/master-model-index.md",
    "examples/pdf-report-system/master-actor-map.md",
    "examples/pdf-report-system/master-system-map.md",
    "examples/pdf-report-system/master-information-model.md",
]
SKILLS = [
    "architecture-modeling",
    "business-context-modeling",
    "mermaid-diagram-authoring",
    "mermaid-diagram-export",
]
THIN_LUCIDE_ICONS = (
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


FDE_READER_MODEL_FILES = (
    "purpose-outcome.md",
    "system-context.md",
    "actor-requirement.md",
    "business-map.md",
    "shape-change-context.md",
    "build-collaboration-context.md",
    "establish-work-context.md",
    "change-design-flow.md",
)


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
    )

    for name in FDE_READER_MODEL_FILES:
        relative = Path(name)
        artifact = sample / relative
        text = artifact.read_text(encoding="utf-8")
        if text.count("```mermaid") != 1:
            raise ValueError(f"{artifact.relative_to(ROOT)}: expected one Mermaid model")
        if "## モデル" not in text or "## このモデルが表していること" not in text:
            raise ValueError(
                f"{artifact.relative_to(ROOT)}: missing reader-facing page structure"
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
    model_files = ("architecture-overview.md", "handoff-review-flow.md")
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
        if "## モデル" not in text or "## このモデルが表していること" not in text:
            raise ValueError(
                f"{artifact.relative_to(ROOT)}: missing reader-facing page structure"
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


def validate_pdf_report_reader_surface() -> None:
    """Keep the PDF sample readable without exposing its authoring method."""

    sample = ROOT / "examples/pdf-report-system"
    reader_files = ("README.md", "domain-overview.md", "report-creation-context.md")
    forbidden_tokens = (
        "RDRA",
        "BUC",
        "Activity",
        "UC",
        "## モデル",
        "## 図の業務",
        "## この図が表していること",
        "## Master references",
        "## Supporting model",
        "model-set-index",
        "master-model-index",
        "validation",
    )
    for name in reader_files:
        artifact = sample / name
        text = artifact.read_text(encoding="utf-8")
        for token in forbidden_tokens:
            if token in text:
                raise ValueError(
                    f"{artifact.relative_to(ROOT)}: authoring term leaked into reader surface: {token}"
                )

    root_page = (sample / "README.md").read_text(encoding="utf-8")
    required_headings = (
        "# PDF帳票システム",
        "## 実現したいこと",
        "## 業務",
        "### 帳票業務",
        "## 情報",
    )
    for heading in required_headings:
        if heading not in root_page:
            raise ValueError(f"PDF root page is missing reader section: {heading}")
    if root_page.count("```mermaid") != 4:
        raise ValueError("PDF root page must contain exactly four Mermaid views")

    overview = (sample / "domain-overview.md").read_text(encoding="utf-8")
    detail = (sample / "report-creation-context.md").read_text(encoding="utf-8")
    if overview.count("```mermaid") != 1 or detail.count("```mermaid") != 1:
        raise ValueError("PDF sample reader pages must contain one Mermaid diagram each")
    if "b_pdf_reporting --- b_report_ready" not in overview:
        raise ValueError("PDF overview must show the parent-to-child business relationship")
    for child in ("b_prepare_report", "b_generate_pdf", "b_retrieve_report", "b_retrieve_pdf"):
        if child not in overview:
            raise ValueError(f"PDF overview is missing major child business: {child}")
    if "[帳票業務の全体](domain-overview.md)" not in detail:
        raise ValueError("PDF detail page must link back to the parent business")

    blocks = re.findall(
        r"^```mermaid[ \t]*\r?\n(?P<body>.*?)^```[ \t]*$",
        root_page,
        flags=re.MULTILINE | re.DOTALL,
    )
    if len(blocks) != 4:
        raise ValueError("PDF root page Mermaid blocks could not be extracted")
    purpose_block = blocks[1]
    purpose_nodes = set(
        re.findall(r"^\s{2}(p_[a-z][a-z0-9_]*)\(\[\"", purpose_block, re.MULTILINE)
    )
    if len(purpose_nodes) < 3:
        raise ValueError("PDF purpose view must include at least three reader-facing notes")
    for actor_id in ("a_report_user", "a_report_owner"):
        if actor_id not in purpose_block:
            raise ValueError(f"PDF purpose view is missing actor intention for {actor_id}")
    if "p_report_shared_outcome" not in purpose_nodes:
        raise ValueError("PDF purpose view must show the shared desired outcome")
    if "p_report_purpose" not in blocks[0]:
        raise ValueError("PDF whole-system view must show an in-diagram purpose note")
    purpose_edge_re = re.compile(
        r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+---\s+"
        r"(?P<right>[a-z][a-z0-9_]*)\s*$"
    )
    purpose_edges = {
        tuple(sorted((match.group("left"), match.group("right"))))
        for line in purpose_block.splitlines()
        if (match := purpose_edge_re.match(line))
    }
    required_purpose_edges = {
        tuple(sorted(edge))
        for edge in (
            ("a_report_user", "p_report_user_goal"),
            ("a_report_owner", "p_report_owner_goal"),
            ("p_report_user_goal", "p_report_shared_outcome"),
            ("p_report_owner_goal", "p_report_shared_outcome"),
        )
    }
    if not required_purpose_edges <= purpose_edges:
        missing = sorted(required_purpose_edges - purpose_edges)
        raise ValueError(
            "PDF purpose view is missing intended actor/goal/outcome relationships: "
            + ", ".join(f"{left} --- {right}" for left, right in missing)
        )

    canonical_node_re = re.compile(
        r'^\s{2}(?P<id>[a-z][a-z0-9_]*)@\{\s*'
        r'label:\s*"(?P<label>[^"]*)",\s*'
        r'img:\s*"(?P<img>[^"]+)",\s*'
        r'pos:\s*"b",\s*'
        r'w:\s*(?P<w>\d+),\s*'
        r'h:\s*(?P<h>\d+),\s*'
        r'constraint:\s*"on"\s*\}\s*$'
    )

    def node_definitions(text: str) -> dict[str, str]:
        definitions: dict[str, str] = {}
        for line in text.splitlines():
            if match := canonical_node_re.match(line):
                node_id = match.group("id")
                normalized = line.strip()
                previous = definitions.get(node_id)
                if previous is not None and previous != normalized:
                    raise ValueError(
                        f"{sample / 'README.md'}: canonical node {node_id} changes definition across views"
                    )
                definitions[node_id] = normalized
        return definitions

    root_nodes = node_definitions(root_page)
    root_business_nodes = node_definitions(blocks[2])
    domain_nodes = node_definitions(overview)
    detail_nodes = node_definitions(detail)
    master_nodes: dict[str, str] = {}
    for name in ("master-actor-map.md", "master-system-map.md", "master-information-model.md"):
        master_nodes.update(node_definitions((sample / name).read_text(encoding="utf-8")))

    required_master_ids = {
        node_id for node_id in master_nodes if node_id.startswith(("a_", "x_", "i_"))
    }
    missing_root_ids = sorted(required_master_ids - set(root_nodes))
    if missing_root_ids:
        raise ValueError(
            "PDF root page is missing canonical Actor/System/Information IDs: "
            + ", ".join(missing_root_ids)
        )
    for page_name, definitions in (
        ("README.md", root_nodes),
        ("domain-overview.md", domain_nodes),
        ("report-creation-context.md", detail_nodes),
    ):
        for node_id, expected in master_nodes.items():
            if node_id in definitions and definitions[node_id] != expected:
                raise ValueError(
                    f"{page_name}: {node_id} diverges from its master-map definition"
                )

    root_business_ids = {node_id for node_id in root_business_nodes if node_id.startswith("b_")}
    overview_business_ids = {node_id for node_id in domain_nodes if node_id.startswith("b_")}
    detail_business_ids = {node_id for node_id in detail_nodes if node_id.startswith("b_")}
    if root_business_ids != overview_business_ids:
        raise ValueError("PDF root business view and domain-overview business IDs diverge")
    if not detail_business_ids <= overview_business_ids:
        raise ValueError("PDF detail introduces a Business ID absent from domain-overview")
    for node_id in sorted(detail_business_ids | overview_business_ids):
        expected = root_business_nodes.get(node_id) or domain_nodes.get(node_id)
        if expected is None:
            continue
        for page_name, definitions in (
            ("domain-overview.md", domain_nodes),
            ("report-creation-context.md", detail_nodes),
        ):
            if node_id in definitions and definitions[node_id] != expected:
                raise ValueError(
                    f"{page_name}: {node_id} diverges from the root business definition"
                )

    edge_re = re.compile(
        r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+(?P<connector>---|-->)\s+"
        r"(?P<right>[a-z][a-z0-9_]*)\s*$"
    )

    def edges(text: str) -> set[tuple[str, str, str]]:
        result: set[tuple[str, str, str]] = set()
        for line in text.splitlines():
            if match := edge_re.match(line):
                left, right, connector = match.group("left"), match.group("right"), match.group("connector")
                if connector == "---":
                    left, right = sorted((left, right))
                result.add((left, connector, right))
        return result

    root_business_edges = edges(blocks[2])
    overview_edges = edges(
        re.search(
            r"^```mermaid[ \t]*\r?\n(?P<body>.*?)^```[ \t]*$",
            overview,
            flags=re.MULTILINE | re.DOTALL,
        ).group("body")
    )
    if root_business_edges != overview_edges:
        raise ValueError("PDF root business view diverges from domain-overview relationships")
    root_information_edges = edges(blocks[3])
    information_master = (sample / "master-information-model.md").read_text(encoding="utf-8")
    information_master_block = re.search(
        r"^```mermaid[ \t]*\r?\n(?P<body>.*?)^```[ \t]*$",
        information_master,
        flags=re.MULTILINE | re.DOTALL,
    )
    if information_master_block is None or root_information_edges != edges(
        information_master_block.group("body")
    ):
        raise ValueError("PDF root information view diverges from the information master")

    context = ROOT / ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py"
    business = ROOT / ".agents/skills/business-context-modeling/scripts/check_business_context.py"
    with tempfile.TemporaryDirectory(prefix="fde-pdf-root-") as directory:
        temporary_files: list[Path] = []
        for number, body in enumerate(blocks, start=1):
            path = Path(directory) / f"view-{number}.md"
            path.write_text(f"```mermaid\n{body}\n```\n", encoding="utf-8")
            temporary_files.append(path)
            run([sys.executable, str(context), str(path), "--strict"])
        run([sys.executable, str(business), str(temporary_files[0])])
        run([sys.executable, str(business), str(temporary_files[2])])
    _validate_sample_links(sample)


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
    validate_fde_reader_surface()
    validate_architecture_reader_surface()
    validate_pdf_report_reader_surface()
    validate_model_set_index("examples/repair-intake/model-set-index.md")
    validate_model_set_index("examples/maakbo-expression-loop/model-set-index.md")
    validate_model_set_index("examples/pdf-report-system/model-set-index.md")

    python_files = [path for path in ROOT.rglob("*.py") if "node_modules" not in path.parts]
    for path in python_files:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    context = ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py"
    architecture = ".agents/skills/architecture-modeling/scripts/check_architecture_context.py"
    business = ".agents/skills/business-context-modeling/scripts/check_business_context.py"
    flow = ".agents/skills/mermaid-diagram-authoring/scripts/check_business_flow.py"
    run([sys.executable, business, "templates/icon-context.md"])
    run([sys.executable, architecture, "templates/architecture-context.md", "--strict"])
    run([
        sys.executable,
        architecture,
        "examples/human-agent-workspace/architecture-overview.md",
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
    run([
        sys.executable,
        master,
        "examples/pdf-report-system/master-actor-map.md",
        "--kind",
        "actor",
        "--strict",
        "--allow-sparse",
    ])
    run([
        sys.executable,
        master,
        "examples/pdf-report-system/master-system-map.md",
        "--kind",
        "system",
        "--strict",
        "--allow-sparse",
    ])
    run([
        sys.executable,
        master,
        "examples/pdf-report-system/master-information-model.md",
        "--kind",
        "information",
        "--strict",
    ])
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
    run([sys.executable, context, "examples/maakbo-expression-loop/overview.md", "--strict"])
    run([sys.executable, business, "examples/maakbo-expression-loop/context.md"])
    run([sys.executable, flow, "examples/maakbo-expression-loop/flow.md", "--strict"])
    run([
        sys.executable,
        context,
        "examples/maakbo-fde/business-map.md",
        "--strict",
        "--allow-complexity",
    ])
    for relative in (
        "examples/maakbo-fde/shape-change-context.md",
        "examples/maakbo-fde/build-collaboration-context.md",
        "examples/maakbo-fde/establish-work-context.md",
    ):
        command = [sys.executable, business, relative]
        if relative.endswith("shape-change-context.md"):
            command.append("--allow-complexity")
        run(command)
    run([sys.executable, flow, "examples/maakbo-fde/change-design-flow.md", "--strict"])
    run([
        sys.executable,
        flow,
        "examples/human-agent-workspace/handoff-review-flow.md",
        "--strict",
    ])
    run([sys.executable, business, "examples/pdf-report-system/domain-overview.md"])
    run([sys.executable, business, "examples/pdf-report-system/report-creation-context.md"])
    print("OK: repository structure, skills, privacy, Python, and Markdown Mermaid sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
