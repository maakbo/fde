# Business model set

## Purpose

State the shared discussion or decision this set supports.

## View map

| View | Role | Level | Parent / expanded node | Child views | Focus | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `overview` | overview context or flow | capability | — | `detail-a`, `observation` | Whole business shape | working hypothesis |
| `observation` | complexity observation | activity | `overview.md / b_area_a` | — | Preserve full same-level backbone | working hypothesis |
| `detail-a` | focused context | activity | `overview.md / b_area_a` | `detail-a-flow` | One business area | working hypothesis |
| `detail-a-flow` | focused flow | task | `detail-a.md / b_activity` | — | Order and decisions | working hypothesis |

Replace placeholders with relative links and stable Mermaid node IDs.

## Master layer

When reusable element inventories are in scope, list their three canonical
sources before the context views:

| Master | Role | Prefix | Source | Context views that select it |
| --- | --- | --- | --- | --- |
| Actor map | participants, hierarchy, and peer relations | `a_` | `master-actor-map.md` | `context.md` |
| External-system map | integrations and dependencies | `x_` | `master-system-map.md` | `context.md` |
| Information model | conceptual information relationships | `i_` | `master-information-model.md` | `context.md` |

The index is navigation and trace only. Canonical labels, icons, sizes, and
stable identities live in the master Mermaid nodes. Each context source should
also include a `Master references` table with the exact IDs it selects.

## Complexity observation

Record what density, hubs, clusters, or crossings made visible before refinement.

## Concrete to abstract

Record which details were grouped into each overview concept and why.

## Abstract to concrete

For each overview node, link the focused diagrams that expand it.

## Open modeling questions

Keep only questions that may change boundary, level, type, or relationship.
