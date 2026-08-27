#!/usr/bin/env python3
"""Lint the portable fixed-icon Mermaid context-diagram convention."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True

from source_loader import SourceError, load_mermaid_source


NODE_RE = re.compile(
    r'^\s{2}(?P<id>[a-z][a-z0-9_]*)@\{\s*'
    r'img:\s*"(?P<img>[^"]+)",\s*'
    r'label:\s*"(?P<label>[^"]*)",\s*'
    r'pos:\s*"b",\s*'
    r'w:\s*(?P<w>\d+),\s*'
    r'h:\s*(?P<h>\d+),\s*'
    r'constraint:\s*"on"\s*\}\s*$'
)
EDGE_RE = re.compile(
    r"^\s{2}(?P<left>[a-z][a-z0-9_]*)\s+---\s+"
    r"(?P<right>[a-z][a-z0-9_]*)\s*$"
)
CLASS_RE = re.compile(
    r"^\s{2}class\s+(?P<ids>[a-z0-9_,]+)\s+"
    r"(?P<class_name>[a-z][a-z0-9_]*)\s*;\s*$"
)
CLASS_DEF_RE = re.compile(
    r"^\s{2}classDef\s+(?P<class_name>[a-z][a-z0-9_]*)\s+(?P<style>.+);\s*$"
)

CANONICAL_THEME_CSS = (
    'themeCSS: ".image-shape p { padding: 0 !important; } '
    '.image-shape foreignObject { overflow: visible; }"'
)
CANONICAL_LINK_STYLE = (
    "linkStyle default stroke:#9E988E,stroke-width:0.75px;"
)
CANONICAL_CLASS_STYLES = {
    "actor": "fill:none,stroke:none,color:#25231F",
    "business": "fill:none,stroke:none,color:#25231F",
    "information": "fill:none,stroke:none,color:#5F5A52",
    "external": "fill:none,stroke:none,color:#5F5A52",
}

ICON_RULES = {
    "a": ("https://api.iconify.design/ph/user-thin.svg", (38, 38), "actor"),
    "b": ("https://api.iconify.design/lucide/ellipse.svg", (30, 30), "business"),
    "i": ("https://api.iconify.design/ph/file-thin.svg", (38, 38), "information"),
    "x": ("https://api.iconify.design/ph/hard-drives-thin.svg", (38, 38), "external"),
}
DEVICE_ICONS = {
    "https://api.iconify.design/ph/device-tablet-thin.svg",
    "https://api.iconify.design/ph/device-mobile-thin.svg",
    "https://api.iconify.design/ph/laptop-thin.svg",
}


def label_too_long(label: str) -> bool:
    words = label.split()
    return len(words) > 4 if len(words) > 1 else len(label) > 12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-complexity", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    observations: list[str] = []

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
    edges: list[tuple[str, str]] = []
    classes: dict[str, list[str]] = defaultdict(list)
    class_defs: dict[str, str] = {}
    link_styles: list[tuple[int, str]] = []
    node_lines: list[int] = []
    edge_lines: list[int] = []

    for number, line in enumerate(lines, source.start_line):
        if match := NODE_RE.match(line):
            node_id = match.group("id")
            if node_id in nodes:
                errors.append(f"line {number}: duplicate node {node_id}")
            nodes[node_id] = {
                "img": match.group("img"),
                "label": match.group("label"),
                "size": (int(match.group("w")), int(match.group("h"))),
            }
            node_lines.append(number)
        elif match := EDGE_RE.match(line):
            edges.append((match.group("left"), match.group("right")))
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
        elif any(token in line for token in ("-->", "-.->", "<--", "==>")):
            errors.append(f"line {number}: context diagrams use only ---")
        elif "---" in line and line.strip() != "---":
            errors.append(f"line {number}: malformed or labeled context edge")

    flow_lines = [line.strip() for line in lines if line.strip().startswith("flowchart ")]
    if len(flow_lines) != 1 or flow_lines[0] not in {"flowchart TB", "flowchart LR"}:
        errors.append("use exactly one flowchart TB or flowchart LR declaration")
    if not any(line.startswith("title:") for line in lines):
        warnings.append("frontmatter title is missing")
    if not any(line.strip() == "diagramPadding: 40" for line in lines):
        warnings.append("use diagramPadding: 40 to protect edge-node labels")
    if not any(line.strip() == CANONICAL_THEME_CSS for line in lines):
        warnings.append("use the canonical themeCSS label-clipping guard")
    if len(link_styles) != 1 or link_styles[0][1] != CANONICAL_LINK_STYLE:
        errors.append(f"use `{CANONICAL_LINK_STYLE}` exactly once")
    if len(nodes) < 3:
        errors.append(f"use at least 3 semantic nodes; found {len(nodes)}")
    if len(nodes) > 7:
        message = f"complexity signal: {len(nodes)} nodes exceed the focused-view guideline"
        (observations if args.allow_complexity else warnings).append(message)
    if len(edges) > 9:
        message = f"complexity signal: {len(edges)} relationships exceed the focused-view guideline"
        (observations if args.allow_complexity else warnings).append(message)
    if node_lines and edge_lines and max(node_lines) > min(edge_lines):
        errors.append("place all node definitions before relationships")

    for node_id, data in nodes.items():
        if "_" not in node_id:
            errors.append(f"{node_id}: use prefix_lower_snake_case")
            continue
        prefix = node_id.split("_", 1)[0]
        image = str(data["img"])
        size = data["size"]
        expected_class: str | None = None
        if prefix in ICON_RULES:
            expected_icon, expected_size, expected_class = ICON_RULES[prefix]
            if image != expected_icon:
                errors.append(f"{node_id}: use {expected_icon}")
            if size != expected_size:
                errors.append(f"{node_id}: use size {expected_size[0]}x{expected_size[1]}")
        elif prefix == "v":
            if image not in DEVICE_ICONS:
                errors.append(f"{node_id}: use a supported Phosphor Thin device icon")
            if size != (38, 38):
                errors.append(f"{node_id}: devices use size 38x38")
        else:
            errors.append(f"{node_id}: unsupported node prefix {prefix}_")

        label = str(data["label"])
        if not label:
            errors.append(f"{node_id}: label must not be empty")
        elif label_too_long(label):
            warnings.append(f"{node_id}: shorten label `{label}`")
        if "<br" in label.lower():
            errors.append(f"{node_id}: keep labels on one plain-text line")

        assignments = classes.get(node_id, [])
        if len(assignments) != 1:
            errors.append(f"{node_id}: require exactly one class assignment")
        elif expected_class and assignments[0] != expected_class:
            errors.append(f"{node_id}: use class {expected_class}")

    degree = Counter()
    for left, right in edges:
        for endpoint in (left, right):
            if endpoint not in nodes:
                errors.append(f"undefined edge endpoint: {endpoint}")
            degree[endpoint] += 1
    for node_id in nodes:
        if degree[node_id] == 0:
            errors.append(f"{node_id}: isolated node")

    for class_name, style in class_defs.items():
        compact = style.replace(" ", "")
        expected = CANONICAL_CLASS_STYLES.get(class_name)
        if expected is None:
            errors.append(f"classDef {class_name}: unsupported visual class")
        elif compact != expected:
            errors.append(f"classDef {class_name}: use `{expected}` exactly")
    if not class_defs:
        errors.append("add classDef declarations")
    for used_class in {values[0] for values in classes.values() if values}:
        if used_class not in class_defs:
            errors.append(f"missing classDef for {used_class}")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    for message in observations:
        print(f"OBSERVE: {message}")

    if errors or (args.strict and warnings):
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"OK: {args.input} — {len(nodes)} nodes, {len(edges)} relationships")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
