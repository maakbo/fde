#!/usr/bin/env python3
"""Command-selection simulation for the two Portable FDE launchers."""

from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]


def windows_choice(has_py: bool, has_python3: bool) -> Optional[str]:
    if has_py:
        return "py -3"
    if has_python3:
        return "python"
    return None


def main() -> int:
    assert windows_choice(True, True) == "py -3"
    assert windows_choice(False, True) == "python"
    assert windows_choice(False, False) is None
    unix = (ROOT / "scripts/fde").read_text()
    windows = (ROOT / "scripts/fde.ps1").read_text()
    assert "command -v python3" in unix and "command -v python" in unix
    assert "& py -3" in windows and "& python" in windows
    print("OK: launcher selection simulation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
