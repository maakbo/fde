# Mermaid business flow conventions

## Visual invariant

Activity and decision symbols keep fixed canvases independent of labels.

| Prefix | Meaning | Thin Lucide asset | Size |
| --- | --- | --- | --- |
| `b_` | business activity | `lucide-thin/ellipse.svg` | `30 x 30` |
| `d_` | decision | `lucide-thin/diamond.svg` | `38 x 38` |

Use the raw asset base
`https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/`.
These are Lucide geometries with the shared `stroke-width` normalized to
`1.35`; keep the same thin assets in context diagrams and flows.

Keep property order `img`, `label`, `pos`, `w`, `h`, `constraint` and one node per line.

The square source canvas matches Mermaid v11's rendered image bounds. At `30 x 30`, the Lucide path remains a horizontal ellipse, keeps the label close, and no longer reads as a minor marker beside the `38 x 38` decision symbol.

Lift only the activity label by `6px` with `margin-top` to compensate for the ellipse icon's transparent lower canvas. Avoid CSS transforms on the HTML label inside Mermaid's SVG `foreignObject`: some GitHub/browser combinations can move that label outside its node. The canonical CSS selects Mermaid image-node IDs containing the stable `-flowchart-b_` prefix because Mermaid does not preserve `class` statement names on image-node DOM elements. Do not shift decision labels.

The canonical CSS also gives Mermaid's transparent image-boundary path a `10px` white stroke. This masks the last few pixels of an arrow path and creates a stable visual gap between the line and the icon without shrinking the icon. Keep this rule paired with the white background token; if the background changes, change both together.

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
d_complete -->|揃っている| b_book
d_complete -->|不足あり| b_request_details
```

Only a decision may have labeled outgoing arrows. Give it exactly two distinct labels. Keep every node reachable from the first activity and able to reach the single last activity.

Use template colors, 14px font, `diagramPadding: 40`, and `0.75px` arrows. The outer padding prevents edge labels from being clipped without enlarging symbols. Keep source order: frontmatter, flowchart declaration, nodes, forward route, return route, classes, class definitions, link style.

## Working-source compatibility

Keep the repository's thin Lucide raw URLs in the Mermaid block. Default to a Markdown working file for immediate preview. If a preview engine cannot display Mermaid v11 image nodes, do not silently replace the visual language; use `mermaid-diagram-export` only after the user requests stable SVG or PNG assets.
