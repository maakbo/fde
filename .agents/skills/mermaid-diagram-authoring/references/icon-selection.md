# Project icon selection

Use one shared icon family for newly authored Business Contexts, master maps,
Flows, and Architecture Contexts. The project's `.fde/config.json` is
consumer-owned and is never part of the managed profile.

```json
{
  "icon_set": "mdi",
  "mdi_source": "upstream"
}
```

Allowed values are `mdi` and `maakbo`. Unconfigured consumer projects default
to `mdi`; this fde repository selects `maakbo` in its own config. The consumer profile includes
maakbo SVGs and the registry, plus MDI license information without MDI image
data. MDI defaults to the official MDI GitHub source; `mdi_source: "iconify"`
selects Iconify's API instead. Neither source depends on fde-hosted icons.
Maakbo keeps its approved effective
1.15 viewBox stroke. Do not try to make
MDI thin by adding a stroke-width style.

All twelve roles in both families use `28 x 28` Mermaid image nodes.
Keep labels at `14px` and preserve the SVGs’ internal optical adjustments.

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

For MDI, select the external source independently:

```bash
python3 .agents/skills/mermaid-diagram-authoring/scripts/icon_registry.py configure \
  --project . --icon-set mdi --mdi-source iconify
```

`upstream` (default) uses official MDI GitHub SVGs pinned to v7.4.47 and works
in GitHub Mermaid. `iconify` uses the Iconify API in environments that allow it.
GitHub Mermaid's image policy blocks the Iconify API; use `upstream` there or
publish a self-contained export. `show`, `create`, and `migrate` also accept
`--mdi-source` for an explicit override.

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

Maakbo uses raw URLs under `assets/icons/maakbo/`. MDI defaults to
`https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/{icon-name}.svg`.
The optional Iconify source is `https://api.iconify.design/mdi/{icon-name}.svg`.
Neither depends on this fde repository's icon storage. The registry provides
all twelve MDI names; no MDI SVGs or package data are shipped in the profile.

For export, maakbo is embedded from local files. MDI is fetched from the
explicit source URL and embedded, with duplicate URLs cached within that
export. MDI export requires network access; afterward, output is self-contained.
The upstream tag pins the SVG version; Iconify API URLs do not. No fde-hosted
fallback is used. Existing Iconify diagrams retain their explicit URLs even
when the project defaults to upstream.

Earlier fde-hosted MDI URLs remain recognizable for migration. Run
`icon_registry.py migrate model.md --icon-set mdi --mdi-source upstream --write`
to replace them explicitly. Use `--mdi-source iconify` for the API instead.
The host change does not alter labels or relationships.

Keep MIT metadata with maakbo and the [MDI license information](mdi-license/README.md)
with redistributed MDI exports. Lucide runtime assets and old compatibility URLs
are retired. Historical comparisons retain notices in their archive folder.
