#!/usr/bin/env python3
"""Build a verbatim Portable FDE consumer-profile artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_value(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def files_for(profile_path: Path) -> list[Path]:
    definition = json.loads(profile_path.read_text())
    files: list[Path] = []
    for relative in definition["paths"]:
        source = ROOT / relative
        if source.is_dir():
            files.extend(sorted(path for path in source.rglob("*") if path.is_file()))
        elif source.is_file():
            files.append(source)
        else:
            raise ValueError(f"profile path is missing: {relative}")
    return files


def artifact_path(source: Path) -> str:
    relative = source.relative_to(ROOT).as_posix()
    if relative == "consumer/fde-instructions.md":
        return ".fde/fde-instructions.md"
    if relative == "scripts/fde_consumer.py":
        return ".fde/fde-manage.py"
    if relative == "scripts/fde":
        return ".fde/fde"
    if relative == "scripts/fde.ps1":
        return ".fde/fde.ps1"
    return relative


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--version", required=True)
    parser.add_argument("--artifact-url", default="")
    parser.add_argument("--allow-dirty", action="store_true")
    args = parser.parse_args()

    dirty = bool(git_value("status", "--porcelain"))
    if dirty and not args.allow_dirty:
        raise ValueError("refusing to build a release artifact from a dirty tree; commit first")
    definition = json.loads(args.profile.read_text())
    managed = []
    source_files = files_for(args.profile)
    targets: set[str] = set()
    for source in source_files:
        target = artifact_path(source)
        if target in targets:
            raise ValueError(f"duplicate artifact path: {target}")
        targets.add(target)
        managed.append({"path": target, "sha256": sha256(source)})

    manifest = {
        "schema": "fde-consumer/v1",
        "profile": definition["profile"],
        "upstream": {
            "repository": git_value("config", "--get", "remote.origin.url"),
            "revision": git_value("rev-parse", "HEAD") + ("-dirty" if dirty else ""),
            "version": args.version,
            "artifact_url": args.artifact_url,
        },
        "managed": managed,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source in source_files:
            archive.write(source, artifact_path(source))
        archive.writestr(".fde/fde-consumer.json", json.dumps(manifest, indent=2) + "\n")
    print(f"OK: {definition['profile']} -> {args.output} ({len(managed)} managed files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
