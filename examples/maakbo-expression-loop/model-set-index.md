# maakbo表現制作 — モデルセット

## Purpose

自分が置いたアイデアの種を、対話を通じて言葉・図解・プレゼンなどの
表現へ育てる仕事の全体と具体を、同じ意味のまま往復して検討する。

## View map

| View | Role | Level | Parent / expanded node | Child views | Focus | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [overview](overview.md) | overall context | business area | — | [context](context.md) | 表現制作という題名と主要主体 | working hypothesis |
| [context](context.md) | Business Context | Business Use Case / scene | `overview.md / b_expression_practice` | [flow](flow.md) | アイデアの種を初稿へ形にする場 | working hypothesis |
| [flow](flow.md) | Business Flow | task | `context.md / b_shape_expression` | — | 芯を見つけ、初稿を磨く順序と戻り道 | working hypothesis |

The parent trace is intentional: overall context → Business Context → selected
Business node → Business Flow. A different Business node could instead expand
into a recursive Detailed Business Context.

## Master layer

| Master | Role | Prefix | Source | Context views that select it |
| --- | --- | --- | --- | --- |
| Actor map | participants and collaboration relation | `a_` | [master-actor-map.md](master-actor-map.md) | [overview](overview.md), [context](context.md) |
| External-system map | outside system boundary | `x_` | [master-system-map.md](master-system-map.md) | [context](context.md) |
| Information model | conceptual seed-to-draft relation | `i_` | [master-information-model.md](master-information-model.md) | [context](context.md) |

## Concrete to abstract

The overall `b_expression_practice` groups the shared work of taking an idea,
talking it through, and giving it a form that a reader can receive. Device and
preview details are intentionally not promoted to this first overview.

## Abstract to concrete

`b_expression_practice` expands into the `b_shape_expression` scene. The scene
expands into the flow's receiving, finding, drafting, and dialogue-refinement
activities.

## Open modeling question

読み手を全体の主要主体として確定するか、それとも発信・共有という別の
ユースケースで扱うか？
