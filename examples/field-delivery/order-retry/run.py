#!/usr/bin/env python3
"""Compile and run the synthetic Java case without leaving build files in Git."""
from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix="fde-order-retry-") as build:
    subprocess.run(["javac", "--release", "16", "-d", build,
                    *map(str, sorted(root.glob("*.java")))], check=True)
    for name in ("OrderServiceTest", "AcceptanceTest"):
        subprocess.run(["java", "-cp", build, name], check=True)
