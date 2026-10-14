#!/usr/bin/env python3
"""Refresh legacy URLs from the canonical MIT-licensed maakbo SVGs."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    source = ROOT / "assets/icons/maakbo"
    legacy = ROOT / "assets/icons/lucide-thin"
    legacy.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.glob("*.svg")):
        shutil.copyfile(path, legacy / path.name)
    shutil.copyfile(source / "LICENSE", legacy / "LICENSE")
    print("OK: legacy icon URLs contain the canonical maakbo originals")


if __name__ == "__main__":
    main()
