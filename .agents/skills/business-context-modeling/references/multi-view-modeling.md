# Multi-view business modeling

Use a model set when one diagram cannot answer every useful question at one
abstraction level. Views are projections of maintained meaning, not isolated
pictures.

## Model and View

A **Model** maintains purpose, desired outcomes, Business activities,
participants, Information, systems, flows, implementation choices, and their
relationships. A **View** selects only what answers one reader question at one
boundary, state, and abstraction level.

Keep the Why-to-How trace in `business-story-and-5w2h.md`. Move downward to
make meaning concrete and upward when detail reveals a wrong name, split,
merge, responsibility, Information concept, or Context boundary.

## Recursive View hierarchy

Use this as the default shape, not a fixed number of levels:

```text
Overall / Business Map
  -> Business Context: one Business Use Case / scene
       -> Business activity: a detail expansion point
            -> Business Flow
            or Detailed Business Context
                 -> another Business activity
                      -> further detail when useful
```

An Overall Context or Business Map names the whole and its major capabilities.
A Business Context selects one coherent scene and shows its Business backbone,
Actors, Information, and External Systems. Each Business node can expand in one
of two ways:

- **Business Flow** when the question is sequence, decision, branch, loop, or
  rework inside that Business;
- **Detailed Business Context** when the question is which sub-Businesses,
  responsibilities, Information changes, or External System boundaries make
  that Business work.

A Detailed Business Context follows the same Business Use Case rule and may be
expanded recursively. Do not assume that every Context must have a child or
that the next child must be a Flow.

## Business Map, Context, and Flow

| View | Question | Relationship meaning |
| --- | --- | --- |
| Overall / Business Map | What whole or peer capabilities exist? | composition or business relation; no order |
| Business Context | What activities and participants make one scene work? | approximate value progression through a central backbone; no exact order |
| Detailed Business Context | What sub-Businesses and boundaries make one parent Business work? | the same Context rule, one level deeper |
| Business Flow | What happens next inside one selected Business? | arrows mean sequence, decisions, branches, loops, or rework |

Do not turn a Context backbone into a detailed route. Its left-to-right reading
helps people follow value across a scene, but exact order belongs to Flow.

Master element maps remain a parallel canonical layer. They maintain reusable
Actor, External System, and Information identities and relationships. A
Context selects those IDs; detail findings that change their meaning return to
the master.

## Choosing and splitting a scene

Begin with the Business Story and place all plausible sibling activities on one
observation surface. Split into sibling Business Contexts when participant or
stakeholder composition, provider/recipient, Information, External System, or
responsibility boundary changes enough that the scene no longer reads as one.
Also split when density, crossings, or backbone shape prevents a reader from
seeing what to discuss.

Business count and node thresholds are review signals, not mechanical split
rules. Do not shrink labels, invent bridge Information, or add fake relations
to keep a scene on one page.

## Parent / child trace

For every detail View, retain at least this table in the authoring workspace or
model-set index:

| Parent View | Expanded Business ID | Child View type | Child View | Status |
| --- | --- | --- | --- | --- |
| `scene-context.md` | `b_selected_business` | Business Flow or Detailed Business Context | `child-view.md` | draft / review / accepted |

The child must name the same parent View and Business ID. Reader-facing pages
need only natural links between the relevant Views.

## Bidirectional refinement loop

1. Inspect the Overall Context or Business Map.
2. Cut one Business Use Case as a Context.
3. Model its sibling Businesses, Actors, Information, and External Systems.
4. Expand one Business into a Flow or Detailed Business Context.
5. Use detail to test the parent meaning.
6. Return upward to rename, split, or merge Business nodes; revise Information,
   Actor responsibility, master identity, or Context boundary.
7. Re-enter detail from the corrected parent.

Concrete-to-abstract correction is as important as abstract-to-concrete
expansion. A child View is evidence about its parent, not a terminal artifact.
