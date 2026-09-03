# Mermaid icon context conventions

## Visual invariant

The icon is the visual object. Its size does not depend on its label.

```mermaid
a_customer@{ label: "依頼者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

## Scope and direction

- Keep one subject and one relationship meaning.
- Begin focused review around 5–12 nodes and up to 16 relationships. These are
  review signals, not semantic limits.
- Use `--allow-complexity` only after rendering a larger coherent scene and
  deciding that it remains readable.
- Use `flowchart TB` or `flowchart LR` for layout, independently of line direction.
- In a Business Context, place executors, providers, and inputs left; the
  scene's Business backbone at center; and recipients and outputs right.
- Use `---` for ordinary Business Context relationships. Input, output,
  provider, and recipient direction comes from placement, not arrowheads.
- Use `-->` only when direction itself is essential and placement cannot
  express it. Record the reason and validate with `--allow-arrow-exception`.

## Context profiles

Use the profile that matches the question; do not make one figure carry every
level at once.

| Profile | Center | Include |
| --- | --- | --- |
| Overall context | A title-level business area or outcome as a `b_` anchor | Major actor subjects; keep detailed information and systems for child views |
| Use-case / scene context | Multiple sibling `b_` activities forming one Business Use Case backbone | The `a_`, `x_`, and `i_` elements whose responsibility, boundary, handoff, or value matters in that scene |
| Complexity observation | The current same-level backbone | All useful candidates when the density itself needs to be seen; acknowledge it with `--allow-complexity` |

Each Business node is a detail expansion point. Expand it as a Business Flow
when order matters, or as a recursive Detailed Business Context when its
sub-Businesses and boundaries matter. Keep the parent View and expanded
Business ID in the authoring trace.

## Node IDs and icons

Use stable `prefix_lower_snake_case` IDs.

| Prefix | Meaning | Thin Lucide asset | Size |
| --- | --- | --- | --- |
| `a_` | actor | `lucide-thin/user.svg` | `38 x 38` |
| `b_` | business activity | `lucide-thin/ellipse.svg` | `30 x 30` |
| `i_` | information | `lucide-thin/file.svg` | `32 x 32` |
| `x_` | external system | `lucide-thin/server.svg` | `32 x 32` |
| `v_` | device or contact surface | Thin Lucide device asset | `38 x 38` |

Use this raw asset base in Mermaid nodes:
`https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/`

The assets preserve Lucide geometry and normalize the shared stroke width to
`1.35`. Do not switch back to standard Iconify Lucide URLs: their embedded
`stroke-width` is `2`, so a Mermaid stylesheet cannot make the external SVG
thinner consistently.

Device URLs:

- iPad: `lucide-thin/tablet.svg`
- iPhone: `lucide-thin/smartphone.svg`
- laptop: `lucide-thin/laptop.svg`

Keep node properties in this exact order: `label`, `img`, `pos`, `w`, `h`,
`constraint`. Keeping the English ID immediately next to the Japanese label
makes renaming and consistency checks easier. Keep one node per line.

The source canvas is square because Mermaid v11 sizes image nodes from the height property. The business ellipse stays at `30 x 30`; information and external-system icons use `32 x 32` so their visible geometry stays close to the actor and business marks without overpowering them. Actors and devices remain `38 x 38` because their Lucide geometry needs the taller canvas. Use `nodeSpacing: 64` and `rankSpacing: 80` so relationship paths have roughly one-character breathing room around the icon field.

Lift only the business label by `6px` with `margin-top` to compensate for the ellipse icon's transparent lower canvas. Avoid CSS transforms on the HTML label inside Mermaid's SVG `foreignObject`: some GitHub/browser combinations can move that label outside its node. The canonical CSS selects Mermaid image-node IDs containing the stable `-flowchart-b_` prefix because Mermaid does not preserve `class` statement names on image-node DOM elements. Do not shift labels for actors, information, systems, or devices.

The canonical CSS gives only Mermaid's first, icon-sized transparent
image-boundary path a `6px` white stroke. This masks the last few pixels of a
relation path and creates a stable visual gap without covering an arrow marker.
The earlier `10px` halo visibly clipped arrowhead triangles. The
`g:first-child` selector follows Mermaid v11.16's image-node structure and
survives Mermaid's themeCSS sanitizer; re-render and inspect all previews
whenever Mermaid is upgraded. Keep this rule paired with the white background
token; if the background changes, change both together.

## Labels

- Use short nouns for actors, information, and systems.
- Use one outcome-oriented verb phrase for activities.
- Prefer 1–4 words or no more than 8 Japanese characters.
- Do not use sentences, line breaks, parentheses, or step numbers.

## Relationships and style

For a Business Context, use a semantic left-to-right source pattern with a
multi-Business backbone and undirected relationships:

```mermaid
flowchart LR
  a_requester
  i_request
  b_understand
  i_record
  b_fulfill
  a_recipient

  a_requester --- b_understand
  i_request --- b_understand
  b_understand --- i_record
  i_record --- b_fulfill
  b_fulfill --- a_recipient
```

Node declarations use the full canonical image-node properties; they are
abbreviated above only to show order. Define left nodes first, then place
Business nodes and genuine shared Information according to their semantic
roles, then define right nodes. Do not alternate Business and Information
mechanically. The relation endpoint order carries the same authoring intent.

Do not use arrows, edge labels, multiple weights, visible node boxes, or color
hierarchy between equivalent nodes. Replace one `---` with `-->` only when the
direction itself changes the View's answer and position cannot express it.
Do not write both `node_a --- node_b` and `node_b --- node_a`; an undirected
line already represents both directions.

Keep the connected Business backbone at the center. An observed Information
concept may bridge two Businesses. A direct `Business --- Business` relation is
allowed when continuity matters and no mediator is observed; it never asserts
exact sequence. Other Context relations require at least one Business
endpoint. Do not invent nodes or relations to shape the layout, or duplicate
one identity on both sides. If provider and recipient roles are equally
important, revisit the View question, boundary, or grain.

## Master map exception

An actor, external-system, or information master map intentionally connects
same-type nodes. In that profile, `---` means an undirected structural relation
and `-->` means a deliberate hierarchy, integration, derivation, or dependency
direction as defined by the map's reading sentence. These arrows are not a
business-process sequence. Read
`../business-context-modeling/references/master-elements.md` and use the
matching master template and checker; do not apply this exception to a
business-centered context view.

Use the template colors, 14px font, `diagramPadding: 40`, and a `0.75px` relation line or arrow. The outer padding prevents labels on edge nodes from being clipped without enlarging the icons. Keep source order: frontmatter, flowchart declaration, nodes, relationships, classes, class definitions, link style.

Before completion, inspect the preview: the Business backbone should be central
and traceable;
executors/providers should read left; recipients should read right; Information
should sit on the side matching its meaning; all nodes should not collapse to
one side; arrows should be absent unless justified; and line gaps, arrowhead
triangles, and labels should remain intact. Use
`fixtures/context-arrow-visual-regression.md` after CSS or Mermaid changes.

## Working-source compatibility

Keep the repository's thin Lucide raw URLs in the Mermaid block. The geometry remains Lucide and the shared stroke width is `1.35`. Default to a Markdown working file so GitHub or VS Code can preview the same source being discussed. A preview engine must support Mermaid v11 image nodes and remote SVG URLs; if it does not, keep editing the source and use `mermaid-diagram-export` only when the user explicitly needs stable media assets.
