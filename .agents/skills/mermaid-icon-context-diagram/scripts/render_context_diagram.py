#!/usr/bin/env python3
"""Validate a context diagram and render self-contained SVG and PNG siblings."""

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--allow-complexity", action="store_true")
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


def inline_iconify(source: str) -> str:
    cache: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        url = match.group("url")
        if not url.startswith("https://api.iconify.design/"):
            return match.group(0)
        if url not in cache:
            request = urllib.request.Request(url, headers={"User-Agent": "maakbo-fde-renderer/0.1"})
            with urllib.request.urlopen(request, timeout=20) as response:
                payload = response.read()
            cache[url] = base64.b64encode(payload).decode("ascii")
        return f'{match.group("prefix")}data:image/svg+xml;base64,{cache[url]}{match.group("suffix")}'

    return re.sub(r'(?P<prefix>img:\s*")(?P<url>[^"]+)(?P<suffix>")', replace, source)


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    root = Path(__file__).resolve().parents[4]
    linter = Path(__file__).resolve().parent / "check_context_diagram.py"
    config = args.config.resolve() if args.config else root / "config/puppeteer.json"
    mmdc = find_mmdc(root)
    if not mmdc:
        print("ERROR: mmdc not found; run npm ci", file=sys.stderr)
        return 2
    if not input_path.is_file() or not config.is_file():
        print("ERROR: input or Puppeteer config not found", file=sys.stderr)
        return 2

    lint = [sys.executable, str(linter), str(input_path), "--strict"]
    if args.allow_complexity:
        lint.append("--allow-complexity")
    if subprocess.run(lint, check=False).returncode != 0:
        return 1

    rendered = inline_iconify(input_path.read_text(encoding="utf-8"))
    with tempfile.NamedTemporaryFile("w", suffix=".mmd", encoding="utf-8", delete=False) as handle:
        handle.write(rendered)
        temporary = Path(handle.name)
    try:
        for suffix in (".svg", ".png"):
            output = input_path.with_suffix(suffix)
            command = [mmdc, "-p", str(config), "-i", str(temporary), "-o", str(output), "-b", "#FAF8F2"]
            print("+", " ".join(command))
            subprocess.run(command, check=True, env=browser_environment())
    finally:
        temporary.unlink(missing_ok=True)
    print(f"Rendered: {input_path.with_suffix('.svg')} and {input_path.with_suffix('.png')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
