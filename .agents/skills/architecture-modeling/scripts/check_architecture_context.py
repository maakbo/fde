#!/usr/bin/env python3
"""Lint FDE fixed-icon architecture context diagrams."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
AUTHORING_SCRIPTS = (
    Path(__file__).resolve().parents[2] / "mermaid-diagram-authoring" / "scripts"
)
sys.path.insert(0, str(AUTHORING_SCRIPTS))

from source_loader import SourceError, load_mermaid_source  # noqa: E402


NODE_RE = re.compile(
    r'^\s{2,}(?P<id>[a-z][a-z0-9_]*)@\{\s*'
    r'label:\s*"(?P<label>[^"]*)",\s*'
    r'img:\s*"(?P<img>[^"]+)",\s*'
    r'pos:\s*"b",\s*w:\s*(?P<w>\d+),\s*h:\s*(?P<h>\d+),\s*'
    r'constraint:\s*"on"\s*\}\s*$'
)
UNDIRECTED_RE = re.compile(
    r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+---\s+"
    r"(?P<right>[a-z][a-z0-9_]*)\s*$"
)
DIRECTED_RE = re.compile(
    r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+-->\s+"
    r"(?P<right>[a-z][a-z0-9_]*)\s*$"
)
CLASS_RE = re.compile(
    r"^\s{2}class\s+(?P<ids>[a-z0-9_,]+)\s+"
    r"(?P<class_name>[a-z][a-z0-9_]*)\s*;\s*$"
)
CLASS_DEF_RE = re.compile(
    r"^\s{2}classDef\s+(?P<class_name>[a-z][a-z0-9_]*)\s+(?P<style>.+);\s*$"
)
SUBGRAPH_RE = re.compile(
    r'^\s{2,}subgraph\s+(?P<id>bd_[a-z0-9_]+)\["(?P<label>[^"]+)"\]\s*$'
)
STYLE_RE = re.compile(
    r"^\s{2}style\s+(?P<id>bd_[a-z0-9_]+)\s+(?P<style>.+);\s*$"
)

RAW = "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/"
NODE_RULES = {
    "h": ("user.svg", (38, 38), "human"),
    "g": ("bot.svg", (38, 38), "agent"),
    "s": ("server.svg", (32, 32), "system"),
    "r": ("folder-git-2.svg", (32, 32), "repository"),
    "k": ("file.svg", (32, 32), "artifact"),
    "x": ("cloud.svg", (32, 32), "external"),
    "c": ("message-square.svg", (32, 32), "channel"),
}
CLASS_STYLES = {
    "human": "fill:none,stroke:none,color:#25231F",
    "agent": "fill:none,stroke:none,color:#25231F",
    "system": "fill:none,stroke:none,color:#5F5A52",
    "repository": "fill:none,stroke:none,color:#5F5A52",
    "artifact": "fill:none,stroke:none,color:#5F5A52",
    "external": "fill:none,stroke:none,color:#5F5A52",
    "channel": "fill:none,stroke:none,color:#5F5A52",
}
BOUNDARY_STYLE = (
    "fill:#FAF8F2,stroke:#C8C1B6,stroke-width:0.75px,color:#5F5A52"
)
THEME_CSS = (
    'themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } '
    '.image-shape foreignObject { overflow: visible; } '
    '.image-shape .labelBkg { background-color:#FFFFFF !important; } '
    '.image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } '
    '.image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"'
)
LINK_STYLE = "linkStyle default stroke:#9E988E,stroke-width:0.75px;"
FOCUSED_NODES = 12
FOCUSED_RELATIONS = 16


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-complexity", action="store_true")
    parser.add_argument("--allow-directed", action="store_true")
    parser.add_argument("--allow-sparse", action="store_true")
    return parser.parse_args()


def label_too_long(label: str) -> bool:
    words = label.split()
    return len(words) > 4 if len(words) > 1 else len(label) > 12


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        print(f"ERROR: file not found: {args.input}", file=sys.stderr)
        return 2
    try:
        source = load_mermaid_source(args.input)
    except SourceError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    observations: list[str] = []
    nodes: dict[str, dict[str, object]] = {}
    edges: list[tuple[str, str, bool]] = []
    classes: dict[str, list[str]] = defaultdict(list)
    class_defs: dict[str, str] = {}
    boundaries: dict[str, str] = {}
    boundary_styles: dict[str, str] = {}
    boundary_stack: list[str] = []
    boundary_members: dict[str, set[str]] = defaultdict(set)
    node_lines: list[int] = []
    edge_lines: list[int] = []
    link_styles: list[str] = []
    undirected: set[tuple[str, str]] = set()

    lines = source.text.splitlines()
    for number, line in enumerate(lines, source.start_line):
        if match := SUBGRAPH_RE.match(line):
            boundary_id = match.group("id")
            if boundary_id in boundaries:
                errors.append(f"line {number}: duplicate boundary {boundary_id}")
            boundaries[boundary_id] = match.group("label")
            boundary_stack.append(boundary_id)
        elif line.strip() == "end":
            if boundary_stack:
                boundary_stack.pop()
        elif match := NODE_RE.match(line):
            node_id = match.group("id")
            if node_id in nodes:
                errors.append(f"line {number}: duplicate node {node_id}")
            nodes[node_id] = {
                "label": match.group("label"),
                "img": match.group("img"),
                "size": (int(match.group("w")), int(match.group("h"))),
            }
            node_lines.append(number)
            for boundary_id in boundary_stack:
                boundary_members[boundary_id].add(node_id)
        elif match := DIRECTED_RE.match(line):
            edges.append((match.group("left"), match.group("right"), True))
            edge_lines.append(number)
        elif match := UNDIRECTED_RE.match(line):
            left, right = match.group("left"), match.group("right")
            key = tuple(sorted((left, right)))
            if key in undirected:
                errors.append(f"line {number}: duplicate undirected relationship {left} --- {right}")
            undirected.add(key)
            edges.append((left, right, False))
            edge_lines.append(number)
        elif match := CLASS_RE.match(line):
            for node_id in match.group("ids").split(","):
                classes[node_id].append(match.group("class_name"))
        elif match := CLASS_DEF_RE.match(line):
            class_defs[match.group("class_name")] = match.group("style")
        elif match := STYLE_RE.match(line):
            boundary_styles[match.group("id")] = match.group("style")
        elif line.strip().startswith("linkStyle"):
            link_styles.append(line.strip())
        elif line.strip().startswith("%%") or line.strip().startswith("direction "):
            continue
        elif "@{" in line:
            errors.append(
                f"line {number}: use one-line properties in order label, img, pos, w, h, constraint"
            )
        elif any(token in line for token in ("-.->", "<--", "==>")):
            errors.append(f"line {number}: use only --- or --> architecture relations")
        elif "-->" in line or ("---" in line and line.strip() != "---"):
            errors.append(f"line {number}: malformed or labelled architecture relation")

    if boundary_stack:
        errors.append("unclosed architecture boundary")
    flow_lines = [line.strip() for line in lines if line.strip().startswith("flowchart ")]
    if flow_lines != ["flowchart LR"]:
        errors.append("use exactly one flowchart LR declaration for architecture context")
    if not any(line.startswith("title:") for line in lines):
        warnings.append("frontmatter title is missing")
    if not any(line.strip() == "diagramPadding: 40" for line in lines):
        warnings.append("use diagramPadding: 40")
    if not any(line.strip() == "nodeSpacing: 64" for line in lines):
        warnings.append("use nodeSpacing: 64")
    if not any(line.strip() == "rankSpacing: 80" for line in lines):
        warnings.append("use rankSpacing: 80")
    if not any(line.strip() == THEME_CSS for line in lines):
        warnings.append("use the canonical architecture themeCSS")
    if link_styles != [LINK_STYLE]:
        errors.append(f"use `{LINK_STYLE}` exactly once")
    if len(nodes) < 3 and not args.allow_sparse:
        errors.append(f"use at least 3 semantic nodes; found {len(nodes)}")
    if node_lines and edge_lines and max(node_lines) > min(edge_lines):
        errors.append("place all node definitions before relationships")

    for count, limit, noun in (
        (len(nodes), FOCUSED_NODES, "nodes"),
        (len(edges), FOCUSED_RELATIONS, "relationships"),
    ):
        if count > limit:
            message = f"complexity signal: {count} {noun} exceed the {limit}-{noun} guideline"
            (observations if args.allow_complexity else warnings).append(message)
    if len(boundaries) > 3:
        message = f"complexity signal: {len(boundaries)} boundaries exceed the 3-boundary guideline"
        (observations if args.allow_complexity else warnings).append(message)

    directed_count = sum(directed for _left, _right, directed in edges)
    if directed_count and not args.allow_directed:
        errors.append("directed architecture relations require --allow-directed and a recorded reason")
    elif directed_count:
        observations.append(f"direction enabled for {directed_count} relationship(s)")

    for node_id, data in nodes.items():
        if "_" not in node_id:
            errors.append(f"{node_id}: use prefix_lower_snake_case")
            continue
        prefix = node_id.split("_", 1)[0]
        if prefix not in NODE_RULES:
            errors.append(f"{node_id}: unsupported architecture prefix {prefix}_")
            continue
        icon, size, expected_class = NODE_RULES[prefix]
        if data["img"] != RAW + icon:
            errors.append(f"{node_id}: use {RAW + icon}")
        if data["size"] != size:
            errors.append(f"{node_id}: use size {size[0]}x{size[1]}")
        if classes.get(node_id, []) != [expected_class]:
            errors.append(f"{node_id}: use exactly class {expected_class}")
        label = str(data["label"])
        if not label:
            errors.append(f"{node_id}: label must not be empty")
        elif label_too_long(label):
            warnings.append(f"{node_id}: shorten label `{label}`")
        if "<br" in label.lower():
            errors.append(f"{node_id}: keep labels on one plain-text line")

    for class_name, style in class_defs.items():
        expected = CLASS_STYLES.get(class_name)
        if expected is None:
            errors.append(f"classDef {class_name}: unsupported architecture class")
        elif style.replace(" ", "") != expected:
            errors.append(f"classDef {class_name}: use `{expected}` exactly")
    for values in classes.values():
        for class_name in values:
            if class_name not in class_defs:
                errors.append(f"missing classDef for {class_name}")

    for boundary_id, label in boundaries.items():
        if label_too_long(label):
            warnings.append(f"{boundary_id}: shorten boundary label `{label}`")
        if not boundary_members[boundary_id]:
            errors.append(f"{boundary_id}: boundary must contain at least one node")
        if boundary_styles.get(boundary_id, "").replace(" ", "") != BOUNDARY_STYLE:
            errors.append(f"{boundary_id}: use the canonical neutral boundary style")
    for boundary_id in boundary_styles:
        if boundary_id not in boundaries:
            errors.append(f"style references undefined boundary {boundary_id}")

    degree = Counter()
    for left, right, _directed in edges:
        for endpoint in (left, right):
            if endpoint not in nodes:
                errors.append(f"undefined relationship endpoint: {endpoint}")
            degree[endpoint] += 1
    if not args.allow_sparse:
        for node_id in nodes:
            if degree[node_id] == 0:
                errors.append(f"{node_id}: isolated node")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    for message in observations:
        print(f"OBSERVE: {message}")
    if errors or (args.strict and warnings):
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"OK: {args.input} — {len(nodes)} nodes, {len(edges)} relationships, {len(boundaries)} boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
