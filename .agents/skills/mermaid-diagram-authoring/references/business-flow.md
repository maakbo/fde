# Mermaid business flow conventions

## Visual invariant

Activity and decision symbols keep fixed canvases independent of labels.

| Prefix | Meaning | Iconify URL | Size |
| --- | --- | --- | --- |
| `b_` | business activity | `https://api.iconify.design/lucide/ellipse.svg` | `22 x 22` |
| `d_` | decision | `https://api.iconify.design/ph/diamond-thin.svg` | `38 x 38` |

Keep property order `img`, `label`, `pos`, `w`, `h`, `constraint` and one node per line.

The square source canvas matches Mermaid v11's rendered image bounds. The Lucide path inside it remains a horizontal ellipse and keeps the label close.

## Scope and direction

- Omit start and end symbols by default.
- Start with 2–5 activities; allow no more than 8 nodes and 10 arrows.
- Use at most one decision and one return route in a foundation flow.
- Use `flowchart TB` by default; use `flowchart LR` only for a straight flow of five nodes or fewer.

## Labels

- Use short verbs or action phrases for activities.
- Prefer 1–3 words or no more than 8 Japanese characters.
- Phrase decisions as short questions.
- Keep branch labels to 1–2 words or 4 Japanese characters.
- Do not use sentences, line breaks, parentheses, role names, or step numbers.

## Flow

Use solid arrows:

```mermaid
b_receive --> d_complete
d_complete -->|Complete| b_book
d_complete -->|Missing| b_request_details
```

Only a decision may have labeled outgoing arrows. Give it exactly two distinct labels. Keep every node reachable from the first activity and able to reach the single last activity.

Use template colors, 14px font, `diagramPadding: 40`, and `0.75px` arrows. The outer padding prevents edge labels from being clipped without enlarging symbols. Keep source order: frontmatter, flowchart declaration, nodes, forward route, return route, classes, class definitions, link style.

## Working-source compatibility

Keep Iconify URLs in the Mermaid block. Default to a Markdown working file for immediate preview. If a preview engine cannot display Mermaid v11 image nodes, do not silently replace the visual language; use `mermaid-diagram-export` only after the user requests stable SVG or PNG assets.
