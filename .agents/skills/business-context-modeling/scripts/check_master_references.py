#!/usr/bin/env python3
"""Check that context nodes match the canonical master node definitions."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True


NODE_RE = re.compile(
    r'^\s{2}(?P<id>[a-z][a-z0-9_]*)@\{\s*'
    r'img:\s*"(?P<img>[^"]+)",\s*'
    r'label:\s*"(?P<label>[^"]*)",\s*'
    r'pos:\s*"b",\s*'
    r'w:\s*(?P<w>\d+),\s*'
    r'h:\s*(?P<h>\d+),\s*'
    r'constraint:\s*"on"\s*\}\s*$'
)
CLASS_RE = re.compile(
    r"^\s{2}class\s+(?P<ids>[a-z0-9_,]+)\s+"
    r"(?P<class_name>[a-z][a-z0-9_]*)\s*;\s*$"
)

MASTER_ARGS = {
    "actor": ("--actor", "a_"),
    "system": ("--system", "x_"),
    "information": ("--information", "i_"),
}


def split_table_row(line: str) -> list[str]:
    """Split a simple Markdown table row without interpreting cell content."""

    stripped = line.strip()
    if not stripped.startswith("|") or "|" not in stripped[1:]:
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def is_table_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def parse_master_reference_table(section: str) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Parse the required Master references table inside one heading section."""

    lines = section.splitlines()
    header_index: int | None = None
    headers: list[str] = []
    for index, line in enumerate(lines):
        cells = split_table_row(line)
        normalized = [re.sub(r"\s+", " ", cell.lower()) for cell in cells]
        if {
            "master",
            "id",
            "canonical label",
        }.issubset(normalized) and any(
            value in normalized for value in {"use in this view", "reason", "use / reason"}
        ):
            header_index = index
            headers = normalized
            break

    if header_index is None:
        return {}, [
            "Master references must contain a table with Master, ID, Canonical label, and Use in this view (or Reason) columns"
        ]
    separator_index = header_index + 1
    if separator_index >= len(lines) or not is_table_separator(split_table_row(lines[separator_index])):
        return {}, ["Master references table must have a Markdown separator row"]

    column = {name: headers.index(name) for name in headers}
    reason_column = next(
        name for name in ("use in this view", "reason", "use / reason") if name in column
    )
    references: dict[str, dict[str, str]] = {}
    errors: list[str] = []
    for line in lines[separator_index + 1 :]:
        cells = split_table_row(line)
        if not cells or is_table_separator(cells):
            continue
        if len(cells) != len(headers):
            errors.append("each Master references row must match the table header width")
            continue
        id_matches = re.findall(r"`([axi]_[a-z0-9_]+)`", cells[column["id"]])
        if len(id_matches) != 1:
            errors.append("each Master references row must contain exactly one backticked a_, x_, or i_ ID")
            continue
        node_id = id_matches[0]
        if node_id in references:
            errors.append(f"Master references contains duplicate ID {node_id}")
            continue
        master_cell = cells[column["master"]]
        canonical_label = cells[column["canonical label"]].strip().strip("`")
        reason = cells[column[reason_column]].strip()
        if not master_cell:
            errors.append(f"{node_id}: Master references master path is empty")
        if not canonical_label:
            errors.append(f"{node_id}: Master references canonical label is empty")
        if not reason or reason == "-":
            errors.append(f"{node_id}: Master references use/reason is empty")
        references[node_id] = {
            "master": master_cell,
            "label": canonical_label,
            "reason": reason,
        }
    if not references:
        errors.append("Master references table must contain at least one data row")
    return references, errors


def master_cell_matches_path(master_cell: str, supplied_path: Path, context_path: Path) -> bool:
    """Accept only a path that resolves to the supplied master file."""

    expected = supplied_path.resolve()
    destinations = re.findall(r"\[[^\]]+\]\(([^)]+)\)", master_cell)
    destinations.extend(re.findall(r"`([^`]+\.md(?:#[^`]*)?)`", master_cell))
    for destination in destinations:
        destination = destination.split("#", 1)[0]
        if not destination:
            continue
        if (context_path.parent / destination).resolve() == expected:
            return True
    return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("context", type=Path)
    parser.add_argument("--actor", type=Path)
    parser.add_argument("--system", type=Path)
    parser.add_argument("--information", type=Path)
    parser.add_argument("--allow-complexity", action="store_true")
    parser.add_argument(
        "--allow-sparse",
        action="store_true",
        help="allow a supplied master to contain multiple candidates without observed same-type edges",
    )
    return parser.parse_args()


def load_nodes(path: Path) -> tuple[dict[str, dict[str, object]], dict[str, list[str]]]:
    root = Path(__file__).resolve().parents[4]
    loader_dir = root / ".agents/skills/mermaid-diagram-authoring/scripts"
    sys.path.insert(0, str(loader_dir))
    from source_loader import SourceError, load_mermaid_source

    try:
        source = load_mermaid_source(path).text
    except SourceError as error:
        raise ValueError(f"{path}: {error}") from error

    nodes: dict[str, dict[str, object]] = {}
    classes: dict[str, list[str]] = {}
    for line in source.splitlines():
        if match := NODE_RE.match(line):
            nodes[match.group("id")] = {
                "img": match.group("img"),
                "label": match.group("label"),
                "pos": "b",
                "w": int(match.group("w")),
                "h": int(match.group("h")),
                "constraint": "on",
            }
        elif match := CLASS_RE.match(line):
            for node_id in match.group("ids").split(","):
                classes.setdefault(node_id, []).append(match.group("class_name"))
    return nodes, classes


def main() -> int:
    args = parse_args()
    if not args.context.is_file():
        print(f"ERROR: file not found: {args.context}", file=sys.stderr)
        return 2

    try:
        context_nodes, context_classes = load_nodes(args.context)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[4]
    context_linter = root / ".agents/skills/mermaid-diagram-authoring/scripts/check_context_diagram.py"
    context_command = [sys.executable, str(context_linter), str(args.context), "--strict"]
    if args.allow_complexity:
        context_command.append("--allow-complexity")
    if subprocess.run(context_command, check=False).returncode != 0:
        return 1

    errors: list[str] = []
    context_text = args.context.read_text(encoding="utf-8")
    references_match = re.search(r"^##\s+Master references\s*$", context_text, re.I | re.M)
    if not references_match:
        errors.append("context must include a `## Master references` section")
    if references_match:
        tail = context_text[references_match.end() :]
        next_heading = re.search(r"^#{1,6}\s+", tail, re.M)
        section_end = references_match.end() + next_heading.start() if next_heading else len(context_text)
        reference_text = context_text[references_match.start() : section_end]
    else:
        reference_text = ""
    references, reference_errors = parse_master_reference_table(reference_text) if references_match else ({}, [])
    errors.extend(reference_errors)

    master_nodes: dict[str, dict[str, object]] = {}
    master_classes: dict[str, list[str]] = {}
    checker = Path(__file__).resolve()
    for kind, (option, prefix) in MASTER_ARGS.items():
        path = getattr(args, option[2:])
        selected = [node_id for node_id in context_nodes if node_id.startswith(prefix)]
        if selected and path is None:
            errors.append(f"provide {option} for context {prefix} nodes")
            continue
        if path is None:
            continue
        if not path.is_file():
            errors.append(f"{option}: file not found: {path}")
            continue
        command = [sys.executable, str(checker.parent / "check_master_map.py"), str(path), "--kind", kind, "--strict"]
        if args.allow_complexity:
            command.append("--allow-complexity")
        if args.allow_sparse:
            command.append("--allow-sparse")
        if subprocess.run(command, check=False, capture_output=True, text=True).returncode != 0:
            errors.append(f"{option}: master map did not pass check_master_map.py")
            continue
        try:
            nodes, classes = load_nodes(path)
        except ValueError as error:
            errors.append(str(error))
            continue
        for node_id in nodes:
            if node_id.startswith(prefix):
                master_nodes[node_id] = nodes[node_id]
                master_classes[node_id] = classes.get(node_id, [])
        unexpected = sorted(node_id for node_id in nodes if not node_id.startswith(prefix))
        if unexpected:
            errors.append(f"{path}: {kind} master contains unexpected IDs: {', '.join(unexpected)}")

    for node_id, context_node in context_nodes.items():
        prefix = f"{node_id.split('_', 1)[0]}_" if "_" in node_id else ""
        if prefix not in {"a_", "x_", "i_"}:
            continue
        master_node = master_nodes.get(node_id)
        if master_node is None:
            errors.append(f"{node_id}: not found in the supplied master map")
            continue
        for field in ("img", "label", "pos", "w", "h", "constraint"):
            if context_node[field] != master_node[field]:
                errors.append(
                    f"{node_id}: {field} differs from master "
                    f"({context_node[field]!r} != {master_node[field]!r})"
                )
        if context_classes.get(node_id) != master_classes.get(node_id):
            errors.append(f"{node_id}: class assignment differs from master")
        reference = references.get(node_id)
        if reference is None:
            errors.append(f"{node_id}: add a row for this ID to the Master references table")
            continue
        expected_path = next(
            (
                getattr(args, option[2:])
                for kind, (option, prefix) in MASTER_ARGS.items()
                if node_id.startswith(prefix)
            ),
            None,
        )
        if expected_path and not master_cell_matches_path(reference["master"], expected_path, args.context):
            errors.append(f"{node_id}: Master references points to the wrong master path")
        if reference["label"] != master_node["label"]:
            errors.append(
                f"{node_id}: Master references canonical label differs from master "
                f"({reference['label']!r} != {master_node['label']!r})"
            )

    selected_ids = {
        node_id for node_id in context_nodes if node_id.startswith(("a_", "x_", "i_"))
    }
    for node_id in sorted(set(references) - selected_ids):
        errors.append(f"Master references includes unselected ID {node_id}")

    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        print(f"FAILED: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(f"OK: {args.context} — master references match ({len(context_nodes)} nodes checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
