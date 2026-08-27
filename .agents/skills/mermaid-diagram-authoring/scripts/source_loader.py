#!/usr/bin/env python3
"""Load one Mermaid source from Markdown or a standalone .mmd file."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


MERMAID_FENCE_RE = re.compile(
    r"^```mermaid[ \t]*\r?\n(?P<body>.*?)^```[ \t]*$",
    re.MULTILINE | re.DOTALL,
)


class SourceError(ValueError):
    """Raised when a working file does not contain one unambiguous diagram."""


@dataclass(frozen=True)
class MermaidSource:
    text: str
    start_line: int


def load_mermaid_source(path: Path) -> MermaidSource:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".mmd":
        return MermaidSource(text=text, start_line=1)
    if path.suffix != ".md":
        raise SourceError("use a Markdown file or a standalone .mmd file")

    matches = list(MERMAID_FENCE_RE.finditer(text))
    if len(matches) != 1:
        raise SourceError(
            f"Markdown working source must contain exactly one mermaid block; found {len(matches)}"
        )
    match = matches[0]
    start_line = text[: match.start("body")].count("\n") + 1
    return MermaidSource(text=match.group("body"), start_line=start_line)
