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
from pathlib import Path

sys.dont_write_bytecode = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--type", choices=("context", "flow"), required=True)
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--allow-complexity", action="store_true")
    parser.add_argument("--config", type=Path)
    return parser.parse_args()


def find_mmdc(root: Path) -> str | None:
    local = root / "node_modules/.bin/mmdc"
    return str(local) if local.is_file() else shutil.which("mmdc")


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
    "https://api.iconify.design/",
    "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/",
)
THIN_ICON_RAW_PREFIX = INLINE_ICON_URL_PREFIXES[1]


def inline_icon_assets(source: str, root: Path) -> str:
    cache: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        url = match.group("url")
        if not any(url.startswith(prefix) for prefix in INLINE_ICON_URL_PREFIXES):
            return match.group(0)
        if url not in cache:
            local_path: Path | None = None
            if url.startswith(THIN_ICON_RAW_PREFIX):
                local_path = root / "assets/icons/lucide-thin" / url[len(THIN_ICON_RAW_PREFIX) :]
            if local_path and local_path.is_file():
                cache[url] = base64.b64encode(local_path.read_bytes()).decode("ascii")
            else:
                request = urllib.request.Request(url, headers={"User-Agent": "maakbo-fde-exporter/0.2"})
                with urllib.request.urlopen(request, timeout=20) as response:
                    cache[url] = base64.b64encode(response.read()).decode("ascii")
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
        source = load_mermaid_source(input_path).text
    except SourceError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    checker = authoring_scripts / (
        "check_context_diagram.py" if args.type == "context" else "check_business_flow.py"
    )
    lint = [sys.executable, str(checker), str(input_path), "--strict"]
    if args.type == "context" and args.allow_complexity:
        lint.append("--allow-complexity")
    if subprocess.run(lint, cwd=root, check=False).returncode != 0:
        return 1

    mmdc = find_mmdc(root)
    config = args.config.resolve() if args.config else root / "config/puppeteer.json"
    if not mmdc:
        print("ERROR: mmdc not found; run npm ci before explicit export", file=sys.stderr)
        return 2
    if not config.is_file():
        print(f"ERROR: Puppeteer config not found: {config}", file=sys.stderr)
        return 2

    output_dir = args.output_dir.resolve() if args.output_dir else input_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    formats = ("svg", "png") if args.format == "both" else (args.format,)
    rendered = inline_icon_assets(source, root)
    with tempfile.NamedTemporaryFile("w", suffix=".mmd", encoding="utf-8", delete=False) as handle:
        handle.write(rendered)
        temporary = Path(handle.name)
    try:
        outputs: list[Path] = []
        for suffix in formats:
            output = output_dir / f"{input_path.stem}.{suffix}"
            command = [
                mmdc,
                "-p",
                str(config),
                "-i",
                str(temporary),
                "-o",
                str(output),
                "-b",
                "#FAF8F2",
            ]
            print("+", " ".join(command))
            subprocess.run(command, check=True, env=browser_environment())
            outputs.append(output)
    finally:
        temporary.unlink(missing_ok=True)

    print("Exported:", ", ".join(str(path) for path in outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
