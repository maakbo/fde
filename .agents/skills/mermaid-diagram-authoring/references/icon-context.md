# Mermaid icon context conventions

## Visual invariant

The icon is the visual object. Its size does not depend on its label.

```mermaid
a_customer@{ img: "https://api.iconify.design/ph/user-thin.svg", label: "Customer", pos: "b", w: 38, h: 38, constraint: "on" }
```

## Scope and direction

- Keep one subject and one relationship meaning.
- Start focused views with 3–7 nodes and up to 9 relationships.
- Use `--allow-complexity` only after recognizing a larger view as intentional observation.
- Use `flowchart TB` for narrow screens and `flowchart LR` only when the backbone benefits.
- Direction never implies process in a context diagram.

## Node IDs and icons

Use stable `prefix_lower_snake_case` IDs.

| Prefix | Meaning | Iconify URL | Size |
| --- | --- | --- | --- |
| `a_` | actor | `https://api.iconify.design/ph/user-thin.svg` | `38 x 38` |
| `b_` | business activity | `https://api.iconify.design/lucide/ellipse.svg` | `30 x 30` |
| `i_` | information | `https://api.iconify.design/ph/file-thin.svg` | `38 x 38` |
| `x_` | external system | `https://api.iconify.design/ph/hard-drives-thin.svg` | `38 x 38` |
| `v_` | device or contact surface | Phosphor Thin device icon | `38 x 38` |

Device URLs:

- iPad: `https://api.iconify.design/ph/device-tablet-thin.svg`
- iPhone: `https://api.iconify.design/ph/device-mobile-thin.svg`
- laptop: `https://api.iconify.design/ph/laptop-thin.svg`

Keep node properties in this exact order: `img`, `label`, `pos`, `w`, `h`, `constraint`. Keep one node per line.

The source canvas is square because Mermaid v11 sizes image nodes from the height property. At `30 x 30`, the Lucide path remains a horizontal ellipse with enough visual presence to carry the business subject while staying quieter than the `38 x 38` supporting icons.

Lift only the business label by `6px` to compensate for the ellipse icon's transparent lower canvas. The canonical CSS selects Mermaid image-node IDs containing the stable `-flowchart-b_` prefix because Mermaid does not preserve `class` statement names on image-node DOM elements. Do not shift labels for actors, information, systems, or devices.

## Labels

- Use short nouns for actors, information, and systems.
- Use one outcome-oriented verb phrase for activities.
- Prefer 1–4 words or no more than 8 Japanese characters.
- Do not use sentences, line breaks, parentheses, or step numbers.

## Relationships and style

Use only undecorated undirected relationships:

```mermaid
a_customer --- b_receive
```

Do not use arrows, edge labels, multiple weights, visible node boxes, or color hierarchy between equivalent nodes.

Use the template colors, 14px font, `diagramPadding: 40`, and a `0.75px` relation line. The outer padding prevents labels on edge nodes from being clipped without enlarging the icons. Keep source order: frontmatter, flowchart declaration, nodes, relationships, classes, class definitions, link style.

## Working-source compatibility

Keep Iconify URLs in the Mermaid block. Default to a Markdown working file so GitHub or VS Code can preview the same source being discussed. A preview engine must support Mermaid v11 image nodes and remote Iconify URLs; if it does not, keep editing the source and use `mermaid-diagram-export` only when the user explicitly needs stable media assets.
