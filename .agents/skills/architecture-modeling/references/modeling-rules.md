# Architecture Modeling Rules

Use these rules after writing the architecture story and before editing Mermaid.

## Element types and names

| Type | Prefix | Meaning | Default icon | Size | Naming |
| --- | --- | --- | --- | --- | --- |
| Human | `h_` | Person or accountable human role | `user.svg` | 38 x 38 | Short role or public name |
| AI agent | `g_` | AI collaborator acting within an assigned responsibility | `bot.svg` | 38 x 38 | Role or agent name |
| Application / system | `s_` | In-boundary runtime or technical system | `server.svg` | 32 x 32 | Short system noun |
| Repository | `r_` | Versioned repository whose storage or ownership matters | `folder-git-2.svg` | 32 x 32 | Repository role or public name |
| Knowledge / artifact | `k_` | Durable object people or systems read, change, or return | `file.svg` | 32 x 32 | Concrete artifact noun |
| External service | `x_` | Technical service outside the selected responsibility boundary | `cloud.svg` | 32 x 32 | Service role or public name |
| Communication channel | `c_` | Channel whose communication mode or access matters | `message-square.svg` | 32 x 32 | Channel noun |
| Boundary | `bd_` | Repository, product, runtime, ownership, or trust boundary | subgraph | — | Enclosed responsibility |

Use stable `prefix_lower_snake_case` IDs. Keep labels to 1–4 words or no more than 12 Japanese
characters. Reuse one identity across sibling Views. Do not create a new type merely because an
icon would look distinctive.

Classify from the selected boundary. A hosted service may be internal in a product View and
external in an ownership View. A repository is not an artifact when its version history,
publication surface, or access boundary is part of the question.

## Story and relationship evidence

Write two or three ordinary sentences first. A usable story answers:

- who initiates, operates, or decides;
- what workspace, system, or capability is in focus;
- what repositories, systems, or artifacts hold durable responsibility;
- what external service participates;
- who receives or reviews the result.

Create a relationship table before Mermaid:

| Left | Right | Plain meaning | Evidence | Direction essential? |
| --- | --- | --- | --- | --- |
| `h_operator` | `r_workspace` | operator makes final decisions through the workspace | source phrase | no |

Reject a relation that is only a layout wish. Reject a channel or artifact that exists only to make
a chain. Keep uncertainty beside the Model rather than encoding it as a solid line.

## Semantic placement

For an `LR` context:

- left = initiator, provider, upstream dependency, or operator;
- center = in-focus system, workspace, repository, or capability;
- right = consumer, downstream dependency, publication surface, or outcome receiver.

This is a reading aid, not a universal data-flow convention. A left node may receive information,
and a right node may provide feedback. Add the actual relationships it participates in instead of
duplicating the node on both sides.

## Relations

Use `---` for an ordinary relevant architecture relationship. Placement and prose carry common
read, store, request, sync, publish, and receive meanings when distinguishing them is not the View's
question.

Use one or a few unlabelled `-->` relations only when direction itself changes the architecture
answer, such as a one-way publication or trust dependency that placement cannot express. Record
the reason and validate with `--allow-directed`. Do not use arrows to narrate a multi-step process.

When request, review, commit, publish, or response order matters, make a separate Interaction Flow.
Do not overload the context with edge labels, line weights, bidirectional arrows, or protocol
notation.

## Boundaries

Use a `subgraph bd_name["Boundary name"]` only when containment expresses responsibility:

- repository boundary: versioned content under one repository;
- product boundary: capability owned as one product;
- runtime boundary: components executing together;
- ownership or trust boundary: where accountability or access changes.

Use at most three boundaries in a focused View. Keep them shallow unless nesting itself changes the
answer. Give every boundary a visible neutral style. Do not move a node inside a boundary only to
reduce crossings, and do not draw a relation to a boundary label as though it were a system.

## View hierarchy

Use the smallest rung that answers the current question:

```text
Architecture Overview / System Context
  -> Architecture Context around one selected node
     -> Detailed Architecture Context for one internal responsibility
        -> Interaction Flow when order, branching, or review matters
```

This hierarchy is recursive and optional. A Flow may hang directly from an Overview if no separate
Context is needed. Record the parent View, expanded node ID, child View role, and status in the
authoring workspace. Reader-facing pages need only natural parent and child links.

Return upward when detail changes a parent node's name, responsibility, boundary, or relationship.
Do not preserve a clean parent diagram whose meaning the detail has disproved.

## Review checklist

- The architecture story exists before the inventory.
- The View has one purpose, boundary, state, and reading sentence.
- Each node and relation has evidence or is kept unresolved outside the diagram.
- Left, center, and right have semantic roles.
- Repository, artifact, system, and external service are not collapsed by convenience.
- Boundaries express containment or responsibility, not decoration.
- Arrows are absent unless direction changes the answer.
- Sequence is in an Interaction Flow.
- The public sample contains no private operational history.
- Parent and detail remain traceable in both directions.
