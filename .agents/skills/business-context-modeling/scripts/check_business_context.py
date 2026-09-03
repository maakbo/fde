#!/usr/bin/env python3
"""Validate business-centered semantics on a fixed-icon context diagram."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict, deque
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
    if not businesses:
        errors.append("include at least one b_ Business activity")
    if not edges:
        errors.append("context requires at least one relationship")
    else:
        for left, right, directed in edges:
            if not left.startswith("b_") and not right.startswith("b_"):
                connector = "-->" if directed else "---"
                errors.append(
                    f"{left} {connector} {right}: Business Context relations require at least one Business endpoint"
                )

    node_index = {node: index for index, node in enumerate(nodes)}
    reverse_edges = [
        (left, right, directed)
        for left, right, directed in edges
        if left in node_index and right in node_index and node_index[left] >= node_index[right]
    ]
    for left, right, directed in reverse_edges:
        connector = "-->" if directed else "---"
        errors.append(
            f"{left} {connector} {right}: write relationships in approximate left-to-right source order"
        )

    if businesses:
        first_business = min(node_index[node] for node in businesses)
        last_business = max(node_index[node] for node in businesses)
        outer_relations = [
            (left, right)
            for left, right, _directed in edges
            if left in node_index and right in node_index
            and (left.startswith("b_") != right.startswith("b_"))
        ]
        left_nodes = {
            left for left, right in outer_relations
            if node_index[left] < first_business and right.startswith("b_")
        }
        right_nodes = {
            right for left, right in outer_relations
            if left.startswith("b_") and node_index[right] > last_business
        }
        if not left_nodes:
            errors.append("place at least one executor/provider/input before the Business backbone")
        if not right_nodes:
            errors.append("place at least one recipient/output after the Business backbone")

    if len(businesses) > 1:
        backbone: dict[str, set[str]] = defaultdict(set)
        information_neighbors: dict[str, set[str]] = defaultdict(set)
        for left, right, _directed in edges:
            if left.startswith("b_") and right.startswith("b_"):
                backbone[left].add(right)
                backbone[right].add(left)
            elif left.startswith("b_") and right.startswith("i_"):
                information_neighbors[right].add(left)
            elif left.startswith("i_") and right.startswith("b_"):
                information_neighbors[left].add(right)
        for neighbors in information_neighbors.values():
            for business in neighbors:
                backbone[business].update(neighbors - {business})
        seen = {businesses[0]}
        queue = deque(seen)
        while queue:
            for neighbor in backbone[queue.popleft()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        if seen != set(businesses):
            missing = ", ".join(sorted(set(businesses) - seen))
            errors.append(
                "connect the Business backbone with observed Information bridges or direct "
                f"Business relationships; disconnected: {missing}"
            )

    if businesses and not any(
        left.startswith("b_") != right.startswith("b_")
        for left, right, _directed in edges
    ):
        errors.append(
            "relate the Business backbone to at least one Actor, Information item, or External System"
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
    print(f"OK: {args.input} — {len(businesses)} Business node(s) in one use-case context")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
