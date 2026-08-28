#!/usr/bin/env python3
"""Lint the portable fixed-icon Mermaid business-flow convention."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

sys.dont_write_bytecode = True

from source_loader import SourceError, load_mermaid_source


NODE_RE = re.compile(
    r'^\s{2}(?P<id>[a-z][a-z0-9_]*)@\{\s*img:\s*"(?P<img>[^"]+)",\s*'
    r'label:\s*"(?P<label>[^"]*)",\s*pos:\s*"b",\s*w:\s*(?P<w>\d+),\s*'
    r'h:\s*(?P<h>\d+),\s*constraint:\s*"on"\s*\}\s*$'
)
EDGE_RE = re.compile(
    r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+-->"
    r"(?:\|(?P<label>[^|]+)\|)?\s+(?P<right>[a-z][a-z0-9_]*)\s*$"
)
CLASS_RE = re.compile(r"^\s{2}class\s+(?P<ids>[a-z0-9_,]+)\s+(?P<class_name>[a-z]+);\s*$")
CLASS_DEF_RE = re.compile(
    r"^\s{2}classDef\s+(?P<class_name>[a-z]+)\s+(?P<style>.+);\s*$"
)

CANONICAL_THEME_CSS = (
    'themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } '
    '.image-shape foreignObject { overflow: visible; } '
    '.image-shape .labelBkg { background-color:#FFFFFF !important; } '
    '.image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } '
    ".image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } "
    '.image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:10px !important; }\"'
)
CANONICAL_LINK_STYLE = (
    "linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;"
)
CANONICAL_CLASS_STYLES = {
    "activity": "fill:none,stroke:none,color:#25231F",
    "decision": "fill:none,stroke:none,color:#25231F",
}

RULES = {
    "b": (
        "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg",
        (30, 30),
        "activity",
    ),
    "d": (
        "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg",
        (38, 38),
        "decision",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--strict", action="store_true")
    return parser.parse_args()


def reachable(start: str, graph: dict[str, list[str]]) -> set[str]:
    seen = {start}
    queue = deque([start])
    while queue:
        for target in graph.get(queue.popleft(), []):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def too_long(label: str) -> bool:
    words = label.split()
    return len(words) > 3 if len(words) > 1 else len(label) > 12


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    if not args.input.is_file():
        print(f"ERROR: file not found: {args.input}", file=sys.stderr)
        return 2

    try:
        source = load_mermaid_source(args.input)
    except SourceError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    lines = source.text.splitlines()
    nodes: dict[str, dict[str, object]] = {}
    edges: list[tuple[str, str, str | None]] = []
    classes: dict[str, list[str]] = defaultdict(list)
    class_defs: dict[str, str] = {}
    link_styles: list[tuple[int, str]] = []
    node_lines: list[int] = []
    edge_lines: list[int] = []

    for number, line in enumerate(lines, source.start_line):
        if match := NODE_RE.match(line):
            node_id = match.group("id")
            nodes[node_id] = {
                "img": match.group("img"),
                "label": match.group("label"),
                "size": (int(match.group("w")), int(match.group("h"))),
            }
            node_lines.append(number)
        elif match := EDGE_RE.match(line):
            edges.append((match.group("left"), match.group("right"), match.group("label")))
            edge_lines.append(number)
        elif match := CLASS_RE.match(line):
            for node_id in match.group("ids").split(","):
                classes[node_id].append(match.group("class_name"))
        elif match := CLASS_DEF_RE.match(line):
            class_defs[match.group("class_name")] = match.group("style")
        elif line.strip().startswith("linkStyle"):
            link_styles.append((number, line.strip()))
        elif "@{" in line:
            errors.append(f"line {number}: use canonical one-line image-node properties")
        elif "-->" in line:
            errors.append(f"line {number}: malformed flow edge")
        elif any(token in line for token in ("---", "-.->", "==>")) and line.strip() != "---":
            errors.append(f"line {number}: use only solid --> arrows")

    flow_lines = [line.strip() for line in lines if line.strip().startswith("flowchart ")]
    if len(flow_lines) != 1 or flow_lines[0] not in {"flowchart TB", "flowchart LR"}:
        errors.append("use exactly one flowchart TB or flowchart LR declaration")
    elif flow_lines[0] == "flowchart LR" and len(nodes) > 5:
        errors.append("use flowchart TB above five nodes")
    if not 2 <= len(nodes) <= 8:
        errors.append(f"use 2–8 nodes; found {len(nodes)}")
    if not any(line.strip() == "diagramPadding: 40" for line in lines):
        warnings.append("use diagramPadding: 40 to protect edge-node labels")
    if not any(line.strip() == CANONICAL_THEME_CSS for line in lines):
        warnings.append("use the canonical themeCSS label-clipping guard")
    if len(link_styles) != 1 or link_styles[0][1] != CANONICAL_LINK_STYLE:
        errors.append(f"use `{CANONICAL_LINK_STYLE}` exactly once")
    if len(edges) > 10:
        errors.append(f"use no more than 10 arrows; found {len(edges)}")
    if node_lines and edge_lines and max(node_lines) > min(edge_lines):
        errors.append("place all node definitions before flow edges")

    decisions: list[str] = []
    for node_id, data in nodes.items():
        if "_" not in node_id:
            errors.append(f"{node_id}: use prefix_lower_snake_case")
            continue
        prefix = node_id.split("_", 1)[0]
        if prefix not in RULES:
            errors.append(f"{node_id}: use only b_ activity or d_ decision")
            continue
        expected_icon, expected_size, expected_class = RULES[prefix]
        if data["img"] != expected_icon:
            errors.append(f"{node_id}: use {expected_icon}")
        if data["size"] != expected_size:
            errors.append(f"{node_id}: use size {expected_size[0]}x{expected_size[1]}")
        if classes.get(node_id, []) != [expected_class]:
            errors.append(f"{node_id}: use exactly class {expected_class}")
        label = str(data["label"])
        if not label:
            errors.append(f"{node_id}: label must not be empty")
        elif too_long(label):
            warnings.append(f"{node_id}: shorten label `{label}`")
        if prefix == "d":
            decisions.append(node_id)
    if len(decisions) > 1:
        errors.append("foundation flows use at most one decision")

    graph: dict[str, list[str]] = defaultdict(list)
    reverse: dict[str, list[str]] = defaultdict(list)
    indegree = Counter()
    outdegree = Counter()
    outgoing_labels: dict[str, list[str | None]] = defaultdict(list)
    for left, right, label in edges:
        if left not in nodes or right not in nodes:
            errors.append(f"undefined endpoint in {left} --> {right}")
            continue
        graph[left].append(right)
        reverse[right].append(left)
        indegree[right] += 1
        outdegree[left] += 1
        outgoing_labels[left].append(label)
        if label and not left.startswith("d_"):
            errors.append(f"{left} --> {right}: only decisions have branch labels")
        if label and len(label.split()) > 2:
            warnings.append(f"{left} --> {right}: shorten branch label `{label}`")

    for decision in decisions:
        labels = outgoing_labels.get(decision, [])
        if len(labels) != 2 or any(label is None for label in labels) or len(set(labels)) != 2:
            errors.append(f"{decision}: use exactly two distinctly labeled branches")

    if nodes:
        first = next(iter(nodes))
        if not first.startswith("b_"):
            errors.append("define the first activity first")
        sinks = [node for node in nodes if outdegree[node] == 0]
        if len(sinks) != 1 or not sinks[0].startswith("b_"):
            errors.append("require one final business activity")
        if len(reachable(first, graph)) != len(nodes):
            errors.append("every node must be reachable from the first activity")
        if len(sinks) == 1 and len(reachable(sinks[0], reverse)) != len(nodes):
            errors.append("every node must be able to reach the final activity")

    for class_name, style in class_defs.items():
        compact = style.replace(" ", "")
        expected = CANONICAL_CLASS_STYLES.get(class_name)
        if expected is None:
            errors.append(f"classDef {class_name}: unsupported visual class")
        elif compact != expected:
            errors.append(f"classDef {class_name}: use `{expected}` exactly")
    for used_class in {values[0] for values in classes.values() if values}:
        if used_class not in class_defs:
            errors.append(f"missing classDef for {used_class}")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if errors or (args.strict and warnings):
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"OK: {args.input} — {len(nodes)} nodes, {len(edges)} arrows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
