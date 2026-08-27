#!/usr/bin/env python3
"""Fetch the selected Lucide icons and normalize their stroke width.

The working Mermaid sources reference the generated SVGs rather than relying on
an Iconify query parameter. Iconify serves Lucide's inner SVG with an explicit
``stroke-width=2`` and does not expose a thin variant, so this small, repeatable
step keeps the Lucide geometry while making the visual weight part of the repo.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "assets/icons/lucide-thin"
ICON_NAMES = (
    "user",
    "ellipse",
    "file",
    "server",
    "diamond",
    "tablet",
    "smartphone",
    "laptop",
)
ICONIFY_URL = "https://api.iconify.design/lucide/{name}.svg"
SOURCE_COMMENT = "<!-- Derived from Lucide via Iconify; stroke width normalized for fde. -->"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stroke-width", type=float, default=1.35)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def fetch_icon(name: str) -> str:
    request = urllib.request.Request(
        ICONIFY_URL.format(name=name),
        headers={"User-Agent": "maakbo-fde-icon-sync/0.2"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8")


def thin_svg(source: str, stroke_width: float) -> str:
    value = f"{stroke_width:g}"
    if source.count('stroke-width="2"') != 1:
        raise ValueError("expected exactly one Lucide stroke-width=2 attribute")
    transformed = source.replace('width="1em"', 'width="24"')
    transformed = transformed.replace('height="1em"', 'height="24"')
    transformed = transformed.replace('stroke-width="2"', f'stroke-width="{value}"')
    if not re.match(r"^<svg\b", transformed):
        raise ValueError("Iconify response is not an SVG document")
    return f"{SOURCE_COMMENT}\n{transformed}\n"


def main() -> int:
    args = parse_args()
    if args.stroke_width <= 0:
        print("ERROR: stroke width must be positive", file=sys.stderr)
        return 2
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    for name in ICON_NAMES:
        destination = output_dir / f"{name}.svg"
        destination.write_text(thin_svg(fetch_icon(name), args.stroke_width), encoding="utf-8")
        print(f"Wrote {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
