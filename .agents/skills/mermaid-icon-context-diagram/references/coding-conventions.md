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
| `b_` | business activity | `https://api.iconify.design/lucide/ellipse.svg` | `22 x 22` |
| `i_` | information | `https://api.iconify.design/ph/file-thin.svg` | `38 x 38` |
| `x_` | external system | `https://api.iconify.design/ph/hard-drives-thin.svg` | `38 x 38` |
| `v_` | device or contact surface | Phosphor Thin device icon | `38 x 38` |

Device URLs:

- iPad: `https://api.iconify.design/ph/device-tablet-thin.svg`
- iPhone: `https://api.iconify.design/ph/device-mobile-thin.svg`
- laptop: `https://api.iconify.design/ph/laptop-thin.svg`

Keep node properties in this exact order: `img`, `label`, `pos`, `w`, `h`, `constraint`. Keep one node per line.

The source canvas is square because Mermaid v11 sizes image nodes from the height property. The Lucide path inside that canvas remains a horizontal ellipse; do not enlarge the canvas merely to make the source numbers look use-case-shaped.

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

## Compatibility

Keep Iconify URLs in `.mmd` for portability. The renderer retrieves and embeds SVG data into output files. Rendering therefore requires network access, while committed `.svg` and `.png` remain self-contained.
