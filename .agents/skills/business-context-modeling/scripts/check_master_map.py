#!/usr/bin/env python3
"""Validate one fixed-icon master map for actors, systems, or information."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True


NODE_RE = re.compile(
    r'^\s{2}(?P<id>[a-z][a-z0-9_]*)@\{\s*'
    r'label:\s*"(?P<label>[^"]*)",\s*'
    r'img:\s*"(?P<img>[^"]+)",\s*'
    r'pos:\s*"b",\s*'
    r'w:\s*(?P<w>\d+),\s*'
    r'h:\s*(?P<h>\d+),\s*'
    r'constraint:\s*"on"\s*\}\s*$'
)
EDGE_RE = re.compile(
    r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+(?P<connector>---|-->)\s+"
    r"(?P<right>[a-z][a-z0-9_]*)\s*$"
)
CLASS_RE = re.compile(
    r"^\s{2}class\s+(?P<ids>[a-z0-9_,]+)\s+"
    r"(?P<class_name>[a-z][a-z0-9_]*)\s*;\s*$"
)

KINDS = {
    "actor": {
        "prefix": "a",
        "icon": "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg",
        "size": (38, 38),
        "class": "actor",
    },
    "system": {
        "prefix": "x",
        "icon": "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg",
        "size": (32, 32),
        "class": "external",
    },
    "information": {
        "prefix": "i",
        "icon": "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg",
        "size": (32, 32),
        "class": "information",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--kind", choices=sorted(KINDS), required=True)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-complexity", action="store_true")
    parser.add_argument(
        "--allow-sparse",
        action="store_true",
        help="allow multiple candidate nodes whose same-type relationships are not observed yet",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        print(f"ERROR: file not found: {args.input}", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[4]
    authoring_scripts = root / ".agents/skills/mermaid-diagram-authoring/scripts"
    sys.path.insert(0, str(authoring_scripts))
    from source_loader import SourceError, load_mermaid_source

    context_linter = authoring_scripts / "check_context_diagram.py"
    command = [
        sys.executable,
        str(context_linter),
        str(args.input),
        "--strict",
        "--allow-sparse",
    ]
    if args.allow_complexity:
        command.append("--allow-complexity")
    if subprocess.run(command, check=False).returncode != 0:
        return 1

    try:
        source = load_mermaid_source(args.input).text
    except SourceError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    nodes: dict[str, dict[str, object]] = {}
    edges: list[tuple[str, str, str]] = []
    classes: dict[str, list[str]] = {}
    for line in source.splitlines():
        if line.strip().startswith("%%"):
            continue
        if match := NODE_RE.match(line):
            node_id = match.group("id")
            if node_id in nodes:
                print(f"ERROR: duplicate node {node_id}")
                return 1
            nodes[node_id] = {
                "img": match.group("img"),
                "size": (int(match.group("w")), int(match.group("h"))),
            }
        elif match := EDGE_RE.match(line):
            edges.append((match.group("left"), match.group("right"), match.group("connector")))
        elif match := CLASS_RE.match(line):
            for node_id in match.group("ids").split(","):
                classes.setdefault(node_id, []).append(match.group("class_name"))

    spec = KINDS[args.kind]
    errors: list[str] = []
    if not nodes:
        errors.append("master map requires at least one image node")

    expected_prefix = f"{spec['prefix']}_"
    for node_id, data in nodes.items():
        if not node_id.startswith(expected_prefix):
            errors.append(f"{node_id}: {args.kind} master uses only {expected_prefix} IDs")
        if data["img"] != spec["icon"]:
            errors.append(f"{node_id}: use {spec['icon']}")
        if data["size"] != spec["size"]:
            width, height = spec["size"]
            errors.append(f"{node_id}: use size {width}x{height}")
        assignments = classes.get(node_id, [])
        if assignments != [spec["class"]]:
            errors.append(f"{node_id}: require exactly one class {spec['class']}")

    for left, right, _connector in edges:
        if left not in nodes or right not in nodes:
            errors.append(f"undefined edge endpoint: {left} or {right}")
        if not left.startswith(expected_prefix) or not right.startswith(expected_prefix):
            errors.append(f"master relationships must stay within {expected_prefix} nodes")

    degree = {node_id: 0 for node_id in nodes}
    for left, right, _connector in edges:
        if left in degree:
            degree[left] += 1
        if right in degree:
            degree[right] += 1
    if len(nodes) > 1 and not edges:
        message = "a multi-node master map has no observed same-type relationship"
        if args.allow_sparse:
            print(f"OBSERVE: {message}; keep candidates without inventing an edge")
        else:
            errors.append(f"{message}; use --allow-sparse when the relation is unresolved")
    for node_id, count in degree.items():
        if count == 0 and len(nodes) > 1:
            message = f"{node_id}: isolated master candidate"
            if args.allow_sparse:
                print(f"OBSERVE: {message}; relationship not observed yet")
            else:
                errors.append(f"{message}; use --allow-sparse when the relation is unresolved")

    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        return 1
    print(f"OK: {args.input} — {args.kind} master, {len(nodes)} nodes, {len(edges)} relationships")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
