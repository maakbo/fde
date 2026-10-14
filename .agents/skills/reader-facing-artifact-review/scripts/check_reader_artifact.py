#!/usr/bin/env python3
"""Check reader-page structure, not prose quality, meaning, or rendered output."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


AUTHOR_HEADINGS = re.compile(
    r"^(?:この(?:モデル|図|ページ)(?:が表していること|の構成|について|の見方|の読み方)?|"
    r"モデル|図の読み方|ページの構成|読み方|作成意図|検証結果|保守メモ)$"
)
HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def visible_line(line: str, in_comment: bool) -> tuple[str, bool]:
    """Remove HTML comments while retaining visible text on either side."""
    parts = []
    position = 0
    while position < len(line):
        if in_comment:
            end = line.find("-->", position)
            if end == -1:
                break
            position = end + 3
            in_comment = False
        else:
            start = line.find("<!--", position)
            if start == -1:
                parts.append(line[position:])
                break
            parts.append(line[position:start])
            position = start + 4
            in_comment = True
    return "".join(parts), in_comment


def inspect(text: str, allow_diagram_title: bool = False) -> tuple[list[str], list[str]]:
    """Return errors and observations with one-based source locations."""
    lines = text.splitlines()
    headings: list[tuple[int, str]] = []
    blocks: list[tuple[int, int, str]] = []
    errors: list[str] = []
    observations: list[str] = []
    visible = [""] * len(lines)
    in_comment = False
    index = 0
    while index < len(lines):
        line, in_comment = visible_line(lines[index], in_comment)
        opening = FENCE.match(line)
        if opening:
            start = index
            marker, language = opening.groups()
            index += 1
            while index < len(lines):
                if re.fullmatch(r" {0,3}" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*", lines[index]):
                    break
                index += 1
            if index == len(lines):
                errors.append(f"line {start + 1}: unclosed code fence")
            if language.strip() == "mermaid":
                blocks.append((start, index, "\n".join(lines[start + 1:index])))
        else:
            visible[index] = line
            heading = HEADING.match(line)
            if heading:
                title = heading.group(1)
                headings.append((index, title))
                if AUTHOR_HEADINGS.fullmatch(title):
                    errors.append(f"line {index + 1}: use a business/theme heading instead of '{title}'")
        index += 1

    configurations: set[tuple[str, str]] = set()
    for number, (start, end, body) in enumerate(blocks, 1):
        preceding = [position for position, _ in headings if position < start]
        if not preceding:
            errors.append(f"line {start + 1}: Mermaid diagram needs a preceding subject heading")
        elif any(line.strip() and not line.lstrip().startswith("%%") for line in visible[preceding[-1] + 1:start]):
            errors.append(f"line {start + 1}: place the diagram directly after its subject heading; move introductory prose below it")
        # Do not count a later section's prose, another diagram, or code as reading.
        boundary = min(
            [position for position, _ in headings if position > end]
            + [position for position, _, _ in blocks if position > end]
            + [len(lines)]
        )
        reading = [
            line.strip() for line in visible[end + 1:boundary]
            if line.strip() and not line.lstrip().startswith("%%")
        ]
        if not reading:
            errors.append(f"line {start + 1}: add business explanation after this diagram, before the next heading/diagram")
        source = "\n".join(line for line in body.splitlines() if not line.lstrip().startswith("%%"))
        frontmatter = re.match(r"\s*---\s*\n(.*?)\n---(?:\s|$)", source, re.DOTALL)
        if frontmatter and re.search(r"^\s*title\s*:", frontmatter.group(1), re.MULTILINE) and not allow_diagram_title:
            errors.append(f"line {start + 1}: remove Mermaid frontmatter title; the Markdown heading owns the title")
        settings = []
        for key in ("layout", "curve"):
            match = re.search(r'[\"\']?\b' + key + r'\b[\"\']?\s*:\s*[\"\']?([A-Za-z][\w-]*)', source)
            settings.append(match.group(1) if match else "renderer-default")
        configuration = (settings[0], settings[1])
        configurations.add(configuration)
        observations.append(f"line {start + 1}: diagram {number}: layout={settings[0]}, curve={settings[1]} (inspect rendered behavior)")
    if len(configurations) > 1:
        observations.append("mixed layout/curve settings: compare rendered lines; differences may be intentional")
    observations.append("Structure checks do not verify natural language, business meaning, or an actual visual preview.")
    return errors, observations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--allow-diagram-title", action="store_true")
    args = parser.parse_args()
    failed = False
    for path in args.paths:
        errors, observations = inspect(path.read_text(encoding="utf-8"), args.allow_diagram_title)
        for message in errors:
            print(f"ERROR: {path}: {message}")
        for message in observations:
            print(f"OBSERVE: {path}: {message}")
        failed |= bool(errors)
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
