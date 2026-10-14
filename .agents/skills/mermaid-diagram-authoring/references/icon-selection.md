# Project icon selection

Use one shared icon family for newly authored Business Contexts, master maps,
Flows, and Architecture Contexts. The project's `.fde/config.json` is
consumer-owned and is never part of the managed profile.

```json
{
  "icon_set": "mdi"
}
```

Allowed values are `mdi` and `maakbo`. Unconfigured consumer projects default
to `mdi`; this fde repository selects `maakbo` in its own config. The consumer profile includes
maakbo SVGs and the registry, plus MDI license information without MDI image
data. MDI directly references Iconify's API; maakbo keeps its approved effective
1.15 viewBox stroke. Do not try to make
MDI thin by adding a stroke-width style.

## New diagrams

Resolve meaning to a URL and size through `icon-sets.json`, not a copied
hard-coded choice inside a Skill. Read the selected mappings with:

```bash
python3 .agents/skills/mermaid-diagram-authoring/scripts/icon_registry.py show --project .
```

Instantiate a template using the destination project's preference:

```bash
python3 .agents/skills/mermaid-diagram-authoring/scripts/icon_registry.py create \
  templates/icon-context.md --output models/context.md
```

The same command works with `business-flow.md`, `architecture-context.md`,
and the three master templates. It refuses to overwrite an existing file.
For hand-authored diagrams, use the URLs and dimensions returned by `show`.

## Change the preference

```bash
python3 .agents/skills/mermaid-diagram-authoring/scripts/icon_registry.py configure \
  --project . --icon-set maakbo
```

This preserves other config keys and does not rewrite diagrams. Initial
installation accepts `--icon-set mdi` or `--icon-set maakbo`; an existing
project config always wins. Profile updates preserve the preference.

## Existing diagrams

Explicit image URLs in a diagram are its durable choice. Checkers and exports
infer `mdi` or `maakbo` from those URLs, independent of the current preference.
They reject mixed families within one diagram. `--icon-set` can require a
particular family for a check or export but never converts the source.

An intentional source migration is a separate action:

```bash
python3 .agents/skills/mermaid-diagram-authoring/scripts/icon_registry.py migrate \
  models/context.md --icon-set mdi --write
```

Or use `--output models/context-mdi.md` to create a separate copy. Migration
changes registered image URLs only; labels, identities, dimensions and
relationships stay intact. When a context copies master nodes, migrate the
master and its dependent context together and recheck master references.

## Distribution and export

Maakbo uses raw URLs under `assets/icons/maakbo/`. MDI uses
`https://api.iconify.design/mdi/{icon-name}.svg` directly, so its diagrams do not
depend on icons stored in this fde repository. The registry provides all twelve
MDI names; no MDI SVGs or icon package data are shipped in the consumer profile.

For export, maakbo is embedded from local files. MDI is fetched from Iconify
and embedded, with duplicate URLs cached within that export. This requires
network access for MDI export; afterward, the output does not need remote icons.
API URLs do not pin a particular package version. No fde-hosted fallback is used.

Earlier fde-hosted MDI URLs remain recognizable for migration. Run
`icon_registry.py migrate model.md --icon-set mdi --write` to replace them with
Iconify URLs explicitly. The host change does not alter labels or relationships.

Keep MIT metadata with maakbo and the [MDI license information](mdi-license/README.md)
with redistributed MDI exports. Lucide runtime assets and old compatibility URLs
are retired. Historical comparisons retain notices in their archive folder.
