# Layout and curve review

`layout` chooses node placement and edge routing; `curve` smooths the route
supplied by the selected engine. Equal `curve` values do not guarantee equal
looking lines across engines.

| Configuration | Expected route in the checked Mermaid v11 implementation |
| --- | --- |
| `dagre` + `basis` | Smooth curves through Dagre control points |
| `elk` + `basis` | ELK orthogonal routes with rounded corners; the adapter assigns `rounded` |

Use `dagre` / `basis` by default for a new reader-facing model set. Keep an
existing engine until the user asks to change it or a reviewed need warrants
it. ELK remains useful for dense structural routing; do not declare it wrong
or promise that changing `curve` alone makes it look like Dagre. Recheck engine
behavior when Mermaid is upgraded.

For a requested routing change:

1. Inventory each diagram's layout, curve, direction, spacing, and grouping.
2. Preview the current sources. Identify crossings, long detours, label/line
   collisions, clipped labels, and whether readers can follow the main work.
3. Try semantic node/edge source order and native configuration first. Remove
   engine-specific options after switching engines. Revisit groups that were
   justified for the old engine; preserve real boundaries.
4. Compare candidates at a readable size. Crossing counts and canvas size are
   supporting observations, not a substitute for seeing the diagram.
5. Keep identities and relationships intact. Never invent invisible edges,
   duplicate an identity, or drop a relationship to improve a score. Ask only
   when an unresolved meaning change actually needs the user's decision.
6. Validate the final source, then inspect its final preview. Verify arrowheads,
   symbol gaps, and labels, not only global layout. An unchanged configuration
   does not justify claiming that a changed source was visually inspected.

Record why a layout was chosen and relevant source-order constraints in `%%`
comments. Keep temporary review images outside the published source tree
unless fixed assets were requested. State honestly when preview was unavailable.
