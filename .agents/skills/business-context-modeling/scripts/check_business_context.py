#!/usr/bin/env python3
"""Validate business-centered semantics on a fixed-icon context diagram."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True


NODE_RE = re.compile(r'^\s{2}(?P<id>[a-z][a-z0-9_]*)@\{')
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
    if subprocess.run(command, check=False).returncode != 0:
        return 1

    try:
        source = load_mermaid_source(args.input).text
    except SourceError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    nodes: set[str] = set()
    edges: list[tuple[str, str, bool]] = []
    flow_lines: list[str] = []
    for line in source.splitlines():
        if match := NODE_RE.match(line):
            nodes.add(match.group("id"))
        elif match := DIRECTED_EDGE_RE.match(line):
            edges.append((match.group("left"), match.group("right"), True))
        elif match := UNDIRECTED_EDGE_RE.match(line):
            edges.append((match.group("left"), match.group("right"), False))
        elif line.strip().startswith("flowchart "):
            flow_lines.append(line.strip())

    errors: list[str] = []
    value_flow = flow_lines == ["flowchart LR"]
    if len(flow_lines) != 1 or flow_lines[0] not in {"flowchart TB", "flowchart LR"}:
        errors.append("use exactly one flowchart TB or flowchart LR declaration")
    if value_flow and any(not directed for _left, _right, directed in edges):
        errors.append("flowchart LR value views use only --> edges")
    if not value_flow and any(directed for _left, _right, directed in edges):
        errors.append("flowchart TB relationship views use only --- edges")
    unsupported = sorted({node.split("_", 1)[0] for node in nodes} - {"a", "b", "i", "x"})
    if unsupported:
        errors.append("foundation business context uses only a_, b_, i_, and x_")
    if not any(node.startswith("b_") for node in nodes):
        errors.append("include at least one b_ business activity")
    if not value_flow:
        for left, right, _directed in edges:
            if left.startswith("b_") == right.startswith("b_"):
                errors.append(
                    f"{left} --- {right}: join exactly one activity and one non-business element"
                )
    elif not edges:
        errors.append("value-flow context requires at least one --> edge")
    else:
        for left, right, _directed in edges:
            if left.startswith("b_") == right.startswith("b_"):
                errors.append(
                    f"{left} --> {right}: value-flow context edges join exactly one activity and one non-business element"
                )

    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        return 1
    view_name = "value-flow semantics" if value_flow else "business-centered semantics"
    print(f"OK: {args.input} — {view_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
