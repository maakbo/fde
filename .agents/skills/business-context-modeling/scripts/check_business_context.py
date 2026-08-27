#!/usr/bin/env python3
"""Validate business-centered semantics on a fixed-icon context diagram."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


NODE_RE = re.compile(r'^\s{2}(?P<id>[a-z][a-z0-9_]*)@\{')
EDGE_RE = re.compile(
    r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+---\s+"
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
    context_linter = root / ".agents/skills/mermaid-icon-context-diagram/scripts/check_context_diagram.py"
    command = [sys.executable, str(context_linter), str(args.input), "--strict"]
    if args.allow_complexity:
        command.append("--allow-complexity")
    if subprocess.run(command, check=False).returncode != 0:
        return 1

    nodes: set[str] = set()
    edges: list[tuple[str, str]] = []
    for line in args.input.read_text(encoding="utf-8").splitlines():
        if match := NODE_RE.match(line):
            nodes.add(match.group("id"))
        elif match := EDGE_RE.match(line):
            edges.append((match.group("left"), match.group("right")))

    errors: list[str] = []
    unsupported = sorted({node.split("_", 1)[0] for node in nodes} - {"a", "b", "i", "x"})
    if unsupported:
        errors.append("foundation business context uses only a_, b_, i_, and x_")
    if not any(node.startswith("b_") for node in nodes):
        errors.append("include at least one b_ business activity")
    for left, right in edges:
        if left.startswith("b_") == right.startswith("b_"):
            errors.append(f"{left} --- {right}: join exactly one activity and one non-business element")

    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        return 1
    print(f"OK: {args.input} — business-centered semantics")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
