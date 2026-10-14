#!/usr/bin/env python3
"""Explicitly validate and export one Mermaid source to SVG, PNG, or both."""

from __future__ import annotations

import argparse
import base64
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / ".agents/skills/mermaid-diagram-authoring/scripts"))
from icon_registry import RAW_BASE, ICONIFY_MDI_BASE, UPSTREAM_MDI_BASE, asset, asset_for_url, icon_set_for_source


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--icon-set", choices=("maakbo", "mdi"))
    parser.add_argument("--diagram", type=int, help="one-based Mermaid block in a multi-diagram Markdown page")
    parser.add_argument("--type", choices=("context", "architecture", "flow", "mermaid"), required=True)
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--allow-complexity", action="store_true")
    parser.add_argument("--allow-arrow-exception", action="store_true")
    parser.add_argument("--allow-directed", action="store_true")
    parser.add_argument("--config", type=Path)
    return parser.parse_args()


def browser_environment() -> dict[str, str]:
    env = os.environ.copy()
    if env.get("PUPPETEER_EXECUTABLE_PATH"):
        return env
    candidates = [
        Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
        Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
        Path("/usr/bin/google-chrome"),
        Path("/usr/bin/chromium"),
        Path("/usr/bin/chromium-browser"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            env["PUPPETEER_EXECUTABLE_PATH"] = str(candidate)
            break
    return env


INLINE_ICON_URL_PREFIXES = (
    RAW_BASE + "maakbo/",
    RAW_BASE + "mdi/",
    ICONIFY_MDI_BASE,
    UPSTREAM_MDI_BASE,
)
MAAKBO_ICON_RAW_PREFIX = INLINE_ICON_URL_PREFIXES[0]


def inline_icon_assets(source: str, root: Path) -> str:
    cache: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        url = match.group("url")
        if not any(url.startswith(prefix) for prefix in INLINE_ICON_URL_PREFIXES):
            return match.group(0)
        if url not in cache:
            found = asset_for_url(url)
            if found is None:
                raise ValueError(f"unregistered icon URL: {url}")
            family, role = found
            if family == "mdi":
                external_url = url if url.startswith((ICONIFY_MDI_BASE, UPSTREAM_MDI_BASE)) else asset(family, role)["url"]
                request = urllib.request.Request(external_url, headers={"User-Agent": "maakbo-fde-exporter/0.2"})
                with urllib.request.urlopen(request, timeout=20) as response:
                    data = response.read()
                svg = ET.fromstring(data)
                if svg.tag != "{http://www.w3.org/2000/svg}svg" or svg.get("viewBox") != "0 0 24 24":
                    raise ValueError("Iconify returned an unexpected MDI SVG")
            else:
                local_path = root / "assets/icons/maakbo" / asset(family, role)["filename"]
                data = local_path.read_bytes()
            cache[url] = base64.b64encode(data).decode("ascii")
        return f'{match.group("prefix")}data:image/svg+xml;base64,{cache[url]}{match.group("suffix")}'

    return re.sub(r'(?P<prefix>img:\s*")(?P<url>[^"]+)(?P<suffix>")', replace, source)


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    root = Path(__file__).resolve().parents[4]
    authoring_scripts = root / ".agents/skills/mermaid-diagram-authoring/scripts"
    sys.path.insert(0, str(authoring_scripts))
    from source_loader import SourceError, load_mermaid_source

    if not input_path.is_file():
        print(f"ERROR: file not found: {input_path}", file=sys.stderr)
        return 2
    try:
        source = load_mermaid_source(input_path, diagram_index=args.diagram).text
        icon_set_for_source(source, input_path, args.icon_set)
    except (SourceError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    if args.type == "mermaid":
        print("Native Mermaid render: syntax is checked by Mermaid; no governed modeling profile is claimed")
    else:
        if args.type == "architecture":
            checker = root / ".agents/skills/architecture-modeling/scripts/check_architecture_context.py"
        elif args.type == "context":
            checker = authoring_scripts / "check_context_diagram.py"
        else:
            checker = authoring_scripts / "check_business_flow.py"
        lint = [sys.executable, str(checker), str(input_path), "--strict"]
        if args.icon_set:
            lint.extend(["--icon-set", args.icon_set])
        if args.type in {"context", "architecture"} and args.allow_complexity:
            lint.append("--allow-complexity")
        if args.type == "context" and args.allow_arrow_exception:
            lint.append("--allow-arrow-exception")
        if args.type == "architecture" and args.allow_directed:
            lint.append("--allow-directed")
        if args.diagram is None:
            lint_result = subprocess.run(lint, cwd=root, check=False)
        else:
            # The checker consumes one block. Validate an unchanged temporary snapshot,
            # keeping the multi-diagram page as the only editable working source.
            with tempfile.TemporaryDirectory(prefix="fde-diagram-check-") as temporary:
                selected = Path(temporary) / "selected.md"
                selected.write_text(f"```mermaid\n{source}\n```\n", encoding="utf-8")
                lint[2] = str(selected)
                lint_result = subprocess.run(lint, cwd=root, check=False)
        if lint_result.returncode != 0:
            return 1

    node = shutil.which("node")
    renderer = Path(__file__).with_name("render_mermaid.mjs")
    config = args.config.resolve() if args.config else root / "config/puppeteer.json"
    if not node or not (root / "node_modules/mermaid").is_dir():
        print("ERROR: Node/rendering dependencies missing; run npm ci before requested rendering", file=sys.stderr)
        return 2
    if not config.is_file():
        print(f"ERROR: Puppeteer config not found: {config}", file=sys.stderr)
        return 2

    output_dir = args.output_dir.resolve() if args.output_dir else input_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    formats = ("svg", "png") if args.format == "both" else (args.format,)
    output_stem = input_path.stem if args.diagram is None else f"{input_path.stem}-diagram-{args.diagram}"
    try:
        rendered = inline_icon_assets(source, root)
    except (OSError, ValueError, ET.ParseError) as error:
        print(f"ERROR: unable to embed selected icons: {error}", file=sys.stderr)
        return 2
    outputs: list[Path] = []
    for suffix in formats:
        output = output_dir / f"{output_stem}.{suffix}"
        command = [node, str(renderer), "--puppeteer-config", str(config),
                   "--output", str(output), "--format", suffix]
        print("+", " ".join(command))
        subprocess.run(command, input=rendered, text=True, check=True, env=browser_environment())
        outputs.append(output)

    print("Exported:", ", ".join(str(path) for path in outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
