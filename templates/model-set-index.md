# Business model set

## Purpose

State the shared discussion or decision this set supports.

## View map

| View | Role | Level | Parent / expanded node | Child views | Focus | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `overview` | overall context | business area | — | `use-case-a`, `observation` | Title-level business area and major actor subjects | working hypothesis |
| `observation` | complexity observation | activity | `overview.md / b_area_a` | — | Preserve full same-level backbone | working hypothesis |
| `use-case-a` | Business Context | Business Use Case / scene | `overview.md / b_area_a` | `activity-a-detail`, `activity-b-flow` | Multiple sibling Businesses and their participants | working hypothesis |
| `activity-a-detail` | Detailed Business Context | sub-Business | `use-case-a.md / b_activity_a` | — | Sub-Businesses, responsibilities, and boundaries | working hypothesis |
| `activity-b-flow` | Business Flow | task | `use-case-a.md / b_activity_b` | — | Order, decisions, and essential rework | working hypothesis |

Replace placeholders with relative links and stable Mermaid node IDs.

The normal path is `Overall / Business Map` → `Business Context` → one selected
Business node → `Business Flow` or `Detailed Business Context`. A Detailed
Business Context may repeat this pattern recursively. Keep every child's parent
View and expanded Business ID reciprocal. Return detail discoveries upward
when they change a parent name, split, merge, responsibility, or boundary.

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
