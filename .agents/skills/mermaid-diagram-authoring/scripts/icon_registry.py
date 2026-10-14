#!/usr/bin/env python3
"""Shared semantic icons, consumer-owned preference, and explicit source migration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


REGISTRY_PATH = Path(__file__).resolve().parents[1] / "references/icon-sets.json"
RAW_BASE = "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/"
CONFIG_PATH = Path(".fde/config.json")
IMAGE_RE = re.compile(r'(?P<prefix>img:\s*")(?P<url>[^"]+)(?P<suffix>")')


def registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def checked_set(value: str) -> str:
    if not isinstance(value, str) or value not in registry()["sets"]:
        raise ValueError(f"unknown icon_set {value!r}; choose maakbo or mdi")
    return value


def configured_set(path: Path | None = None) -> str:
    """Use the nearest project preference; never inherit past a project boundary."""
    current = (path or Path.cwd()).resolve()
    if not current.is_dir():
        current = current.parent
    for parent in (current, *current.parents):
        config = parent / CONFIG_PATH
        if config.is_file():
            try:
                value = json.loads(config.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeError) as error:
                raise ValueError(f"invalid {config}: {error}") from error
            if not isinstance(value, dict):
                raise ValueError(f"{config} must contain a JSON object")
            return checked_set(value.get("icon_set", registry()["default"]))
        if (parent / ".git").exists() or (parent / ".fde/fde-consumer.json").exists():
            break
    return registry()["default"]


def asset(icon_set: str, role: str) -> dict:
    data = registry()
    family = data["sets"][checked_set(icon_set)]
    if role not in family["icons"]:
        raise ValueError(f"unknown semantic icon role: {role}")
    return {"filename": family["icons"][role], "size": tuple(family["sizes"][role]),
            "url": RAW_BASE + icon_set + "/" + family["icons"][role]}


def asset_for_url(url: str) -> tuple[str, str] | None:
    for family, spec in registry()["sets"].items():
        for role, filename in spec["icons"].items():
            if url == RAW_BASE + family + "/" + filename:
                return family, role
            # Known Iconify MDI names can also be exported from the pinned local copy.
            if family == "mdi" and url == "https://api.iconify.design/mdi/" + filename:
                return family, role
    return None


def icon_set_for_source(source: str, path: Path, override: str | None = None) -> str:
    """Explicit URLs are the durable source; preference affects only new diagrams."""
    families = {match[0] for url in IMAGE_RE.findall(source)
                if (match := asset_for_url(url[1]))}
    if len(families) > 1:
        raise ValueError("mixed maakbo/mdi icons in one diagram; migrate explicitly")
    if override is not None:
        selected = checked_set(override)
        if families and selected not in families:
            raise ValueError(f"diagram uses {next(iter(families))}; --icon-set {selected} requires explicit migration")
        return selected
    return next(iter(families)) if families else configured_set(path)


def canonical_url(url: str) -> str:
    found = asset_for_url(url)
    return asset(*found)["url"] if found else url


def icon_rules(icon_set: str, meanings: dict) -> dict:
    """Resolve a notation's prefix -> (semantic role, visual class)."""
    return {prefix: (asset(icon_set, role)["url"], asset(icon_set, role)["size"], visual_class)
            for prefix, (role, visual_class) in meanings.items()}


def rewrite_icons(source: str, icon_set: str) -> str:
    checked_set(icon_set)

    def replace(match: re.Match) -> str:
        existing = asset_for_url(match["url"])
        if existing is None:
            raise ValueError(f"unregistered icon URL: {match['url']}")
        return match["prefix"] + asset(icon_set, existing[1])["url"] + match["suffix"]

    return IMAGE_RE.sub(replace, source)


def configure(project: Path, icon_set: str) -> Path:
    path = project.resolve() / CONFIG_PATH
    value = json.loads(path.read_text()) if path.exists() else {}
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    value["icon_set"] = checked_set(icon_set)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    show = commands.add_parser("show", help="show selected URLs and node sizes")
    show.add_argument("--project", type=Path, default=Path.cwd())
    show.add_argument("--icon-set", choices=("maakbo", "mdi"))
    config = commands.add_parser("configure", help="set the preference without changing diagrams")
    config.add_argument("--project", type=Path, default=Path.cwd())
    config.add_argument("--icon-set", choices=("maakbo", "mdi"), required=True)
    create = commands.add_parser("create", help="instantiate a template using the destination project's preference")
    create.add_argument("template", type=Path)
    create.add_argument("--output", type=Path, required=True)
    create.add_argument("--icon-set", choices=("maakbo", "mdi"))
    migrate = commands.add_parser("migrate", help="explicitly migrate one diagram; labels and relations stay intact")
    migrate.add_argument("input", type=Path)
    migrate.add_argument("--icon-set", choices=("maakbo", "mdi"), required=True)
    destination = migrate.add_mutually_exclusive_group(required=True)
    destination.add_argument("--output", type=Path)
    destination.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "configure":
            print(f"OK: {configure(args.project, args.icon_set)}; existing diagrams unchanged")
        elif args.command == "show":
            selected = args.icon_set or configured_set(args.project)
            print(json.dumps({"icon_set": selected, "icons": {role: asset(selected, role)
                  for role in registry()["sets"][selected]["icons"]}}, indent=2, ensure_ascii=False))
        else:
            source_path = args.template if args.command == "create" else args.input
            output = args.output or args.input
            if output.exists() and not (args.command == "migrate" and args.write):
                raise ValueError(f"refusing to overwrite {output}; use migrate --write explicitly")
            selected = args.icon_set or configured_set(output)
            text = rewrite_icons(source_path.read_text(), selected)
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(text)
            print(f"OK: {output} uses {selected}; labels, relationships and dimensions unchanged")
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
