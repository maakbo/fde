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
to `mdi`; this fde repository selects `maakbo` in its own config. Both families
and their licenses are included in the consumer profile. MDI is pinned to
Iconify's `@iconify-json/mdi@1.2.3`, with unmodified filled-outline geometry;
maakbo keeps its approved effective 1.15 viewBox stroke. Do not try to make
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

Use canonical raw URLs under `assets/icons/maakbo/` or `assets/icons/mdi/`
for GitHub preview. The export tool embeds matching local SVG bytes, so neither
family requires network access during export. Known `api.iconify.design/mdi/`
URLs also resolve to the pinned local copy; author with canonical raw URLs to
keep live previews and exports on the same data.

Keep MIT metadata with maakbo and Apache-2.0/upstream notices with MDI. Lucide
runtime assets and the old compatibility URLs are retired. Historical
third-party comparison images keep notices inside their own archive folder.
