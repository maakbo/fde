#!/usr/bin/env python3
"""Validate business-centered semantics on a fixed-icon context diagram."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True


NODE_RE = re.compile(
    r'^\s{2}(?P<id>[a-z][a-z0-9_]*)@\{\s*label:\s*"(?P<label>[^"]*)",'
)
UNDIRECTED_EDGE_RE = re.compile(
    r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+---\s+"
    r"(?P<right>[a-z][a-z0-9_]*)\s*$"
)
DIRECTED_EDGE_RE = re.compile(
    r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+-->\s+"
    r"(?P<right>[a-z][a-z0-9_]*)\s*$"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--allow-complexity", action="store_true")
    parser.add_argument("--allow-arrow-exception", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[4]
    authoring_scripts = root / ".agents/skills/mermaid-diagram-authoring/scripts"
    sys.path.insert(0, str(authoring_scripts))
    from source_loader import SourceError, load_mermaid_source

    context_linter = authoring_scripts / "check_context_diagram.py"
    command = [sys.executable, str(context_linter), str(args.input), "--strict"]
    if args.allow_complexity:
        command.append("--allow-complexity")
    if args.allow_arrow_exception:
        command.append("--allow-arrow-exception")
    if subprocess.run(command, check=False).returncode != 0:
        return 1

    try:
        source = load_mermaid_source(args.input).text
    except SourceError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    nodes: list[str] = []
    labels: dict[str, str] = {}
    edges: list[tuple[str, str, bool]] = []
    flow_lines: list[str] = []
    for line in source.splitlines():
        if match := NODE_RE.match(line):
            nodes.append(match.group("id"))
            labels[match.group("id")] = match.group("label")
        elif match := DIRECTED_EDGE_RE.match(line):
            edges.append((match.group("left"), match.group("right"), True))
        elif match := UNDIRECTED_EDGE_RE.match(line):
            edges.append((match.group("left"), match.group("right"), False))
        elif line.strip().startswith("flowchart "):
            flow_lines.append(line.strip())

    errors: list[str] = []
    if flow_lines != ["flowchart LR"]:
        errors.append("Business Context uses exactly one flowchart LR declaration")
    unsupported = sorted({node.split("_", 1)[0] for node in nodes} - {"a", "b", "i", "x"})
    if unsupported:
        errors.append("foundation business context uses only a_, b_, i_, and x_")
    businesses = [node for node in nodes if node.startswith("b_")]
    if len(businesses) != 1:
        errors.append(f"include exactly one central b_ business activity; found {len(businesses)}")
    if not edges:
        errors.append("context requires at least one relationship")
    else:
        for left, right, directed in edges:
            if left.startswith("b_") == right.startswith("b_"):
                connector = "-->" if directed else "---"
                errors.append(
                    f"{left} {connector} {right}: join exactly one activity and one non-business element"
                )

    if len(businesses) == 1:
        business = businesses[0]
        business_index = nodes.index(business)
        left_nodes: set[str] = set()
        right_nodes: set[str] = set()
        for left, right, _directed in edges:
            if right == business and left != business:
                left_nodes.add(left)
            elif left == business and right != business:
                right_nodes.add(right)
        if not left_nodes:
            errors.append("place at least one executor/provider/input on the left of the Business")
        if not right_nodes:
            errors.append("place at least one recipient/output on the right of the Business")
        misplaced_left = sorted(node for node in left_nodes if nodes.index(node) > business_index)
        misplaced_right = sorted(node for node in right_nodes if nodes.index(node) < business_index)
        if misplaced_left:
            errors.append(
                "define left-side executor/provider/input nodes before the Business: "
                + ", ".join(misplaced_left)
            )
        if misplaced_right:
            errors.append(
                "define right-side recipient/output nodes after the Business: "
                + ", ".join(misplaced_right)
            )

    seen_labels: dict[tuple[str, str], str] = {}
    for node_id, label in labels.items():
        key = (node_id.split("_", 1)[0], label)
        if key in seen_labels:
            errors.append(
                f"{node_id}: duplicate {key[0]}_ identity label `{label}`; "
                "do not duplicate one identity as a layout workaround"
            )
        seen_labels[key] = node_id

    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        return 1
    print(f"OK: {args.input} — left/center/right business-context semantics")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
