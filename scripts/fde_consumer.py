#!/usr/bin/env python3
"""Install, inspect and safely update a Portable FDE consumer profile."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
import urllib.request
import zipfile
from pathlib import Path


MANIFEST_PATH = Path(".fde/fde-consumer.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_manifest(root: Path) -> dict:
    path = root / MANIFEST_PATH
    if not path.is_file():
        raise ValueError(f"consumer manifest is missing: {path}")
    manifest = json.loads(path.read_text())
    if manifest.get("schema") != "fde-consumer/v1":
        raise ValueError("unsupported consumer manifest schema")
    if not isinstance(manifest.get("managed"), list):
        raise ValueError("consumer manifest has no managed file set")
    return manifest


def verify_source(root: Path, manifest: dict) -> list[str]:
    errors = []
    for item in manifest["managed"]:
        path = root / item["path"]
        if not path.is_file():
            errors.append(f"missing artifact file: {item['path']}")
        elif sha256(path) != item["sha256"]:
            errors.append(f"artifact hash mismatch: {item['path']}")
    return errors


def source_root(args: argparse.Namespace) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    if args.source:
        return Path(args.source).resolve(), None
    url = args.artifact_url
    if not url and args.command in ("check", "update"):
        installed = read_manifest(Path(args.target).resolve())
        url = installed["upstream"].get("artifact_url", "")
    if not url:
        raise ValueError("provide --source or --artifact-url")
    temporary = tempfile.TemporaryDirectory(prefix="fde-consumer-")
    archive_path = Path(temporary.name) / "profile.zip"
    urllib.request.urlretrieve(url, archive_path)
    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(temporary.name)
    return Path(temporary.name), temporary


def destination(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if root not in path.parents and path != root:
        raise ValueError(f"managed path escapes target: {relative}")
    return path


def current_problems(target: Path, manifest: dict) -> list[str]:
    problems = []
    for item in manifest["managed"]:
        path = destination(target, item["path"])
        if not path.is_file():
            problems.append(f"missing managed file: {item['path']}")
        elif sha256(path) != item["sha256"]:
            problems.append(f"locally modified managed file: {item['path']}")
    return problems


def profiles_match(installed: dict, candidate: dict) -> bool:
    return installed["profile"] == candidate["profile"] and installed["upstream"]["repository"] == candidate["upstream"]["repository"]


def install(source: Path, target: Path, manifest: dict) -> int:
    collisions = [item["path"] for item in manifest["managed"] if destination(target, item["path"]).exists()]
    if (target / MANIFEST_PATH).exists():
        collisions.append(MANIFEST_PATH.as_posix())
    if collisions:
        print("STOP: install would collide with existing files")
        print("\n".join(collisions))
        return 2
    for item in manifest["managed"]:
        source_file = source / item["path"]
        target_file = destination(target, item["path"])
        target_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, target_file)
        if item["path"] == ".fde/fde":
            target_file.chmod(target_file.stat().st_mode | 0o111)
    manifest_file = target / MANIFEST_PATH
    manifest_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source / MANIFEST_PATH, manifest_file)
    print(f"OK: installed {manifest['profile']} {manifest['upstream']['version']}")
    print("NEXT: add the optional integration snippet from .fde/fde-instructions.md to your own routing surface.")
    return 0


def check(source: Path, target: Path, candidate: dict) -> int:
    installed = read_manifest(target)
    if not profiles_match(installed, candidate):
        raise ValueError("candidate profile does not match the installed profile")
    problems = current_problems(target, installed)
    print(f"installed: {installed['upstream']['version']} ({installed['upstream']['revision']})")
    print(f"candidate: {candidate['upstream']['version']} ({candidate['upstream']['revision']})")
    if problems:
        print("local state: unsafe to update")
        print("\n".join(problems))
        return 2
    if (
        installed["upstream"]["revision"] == candidate["upstream"]["revision"]
        and installed["upstream"]["version"] == candidate["upstream"]["version"]
    ):
        print("update: none")
        return 0
    print("update: available")
    return 1


def update(source: Path, target: Path, candidate: dict) -> int:
    installed = read_manifest(target)
    if not profiles_match(installed, candidate):
        raise ValueError("candidate profile does not match the installed profile")
    problems = current_problems(target, installed)
    installed_paths = {item["path"] for item in installed["managed"]}
    for item in candidate["managed"]:
        path = destination(target, item["path"])
        if item["path"] not in installed_paths and path.exists():
            problems.append(f"new managed file would collide: {item['path']}")
    if problems:
        print("STOP: update would overwrite or collide")
        print("\n".join(problems))
        return 2
    for item in candidate["managed"]:
        target_file = destination(target, item["path"])
        target_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / item["path"], target_file)
        if item["path"] == ".fde/fde":
            target_file.chmod(target_file.stat().st_mode | 0o111)
    candidate_paths = {item["path"] for item in candidate["managed"]}
    for item in installed["managed"]:
        if item["path"] not in candidate_paths:
            destination(target, item["path"]).unlink()
    shutil.copy2(source / MANIFEST_PATH, target / MANIFEST_PATH)
    print(f"OK: updated to {candidate['upstream']['version']} ({candidate['upstream']['revision']})")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("install", "check", "update"))
    parser.add_argument("--source", help="extracted profile artifact directory")
    parser.add_argument("--artifact-url", help="profile zip URL")
    parser.add_argument("--target", default=".", help="consumer repository root")
    args = parser.parse_args()
    target = Path(args.target).resolve()
    try:
        source, temporary = source_root(args)
        manifest = read_manifest(source)
        errors = verify_source(source, manifest)
        if errors:
            print("STOP: invalid profile artifact")
            print("\n".join(errors))
            return 2
        if args.command == "install":
            return install(source, target, manifest)
        if args.command == "check":
            return check(source, target, manifest)
        return update(source, target, manifest)
    except ValueError as error:
        print(f"STOP: {error}")
        return 2
    finally:
        if 'temporary' in locals() and temporary:
            temporary.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
