---
name: reader-facing-artifact-review
description: Review and finish reader-facing business Markdown and Mermaid together, including natural Japanese, connected sections and pages, duplicate titles, visual evidence, and an independent sub-agent review when authorized and available. Use for proofreading, consolidating, or reviewing business model pages and retaining recurring lessons in existing Skills.
---

# Reader-facing Artifact Review

Help the people doing the work recognize its purpose, participants, information,
and outcomes together. Review the actual page, not the author's account of it.

## Read and scope

Read `../business-context-modeling/references/reader-facing-artifacts.md` and
`../mermaid-diagram-authoring/references/layout-and-curves.md`. Use the governing
modeling Skill when changing business meaning, and Mermaid authoring when
changing diagrams. Read the current pages and relevant linked pages before
editing. Record the requested audience, scope, relationships to preserve, and
session-specific publication authorization in the working context.

## Finish the page

1. Follow the business from its purpose through its work and outcomes. When
   consolidating pages, join their context and remove repeated explanation;
   preserve distinct business questions and meaningful links. Do not force
   every model set into one page or discard meaning to shorten it.
2. Use a subject heading, a diagram, and the short explanation needed beside
   it. Headings name the business or theme. Remove headings about the author's
   model, page structure, writing process, or reading instructions. Let the
   Markdown heading own the title; omit Mermaid frontmatter `title` in embedded
   diagrams. A real subgraph boundary is not a duplicate diagram title.
3. Read the prose as a business participant. Prefer concrete actions and
   natural Japanese; remove repetitions, inflated abstractions, and sentences
   announcing what the writer is showing. Explain what the work does and what
   reaches the next activity. Keep uncertainty visible when participants need
   it to make a decision.
4. Put concise, useful maintenance intent in Mermaid `%%` comments near the
   relevant source. Record why a relationship or layout choice matters, not a
   transcript of the editing session. Keep validation logs, review findings,
   and private evidence out of the published business explanation.
5. Run `scripts/check_reader_artifact.py` on the changed Markdown. Run the
   appropriate modeling/source checkers too. Automated checks detect structural
   regressions; they cannot establish natural Japanese, semantic preservation,
   or a successful visual preview.
6. For an explicit preview or visual-review request, inspect actual rendered
   diagrams. Delegate temporary rendering to Mermaid authoring/export and keep
   generated assets temporary unless publication was requested. Compare layout,
   curve, crossings, endpoints, clipping, and page consistency; revise the
   Markdown source and inspect changed diagrams again. Source settings alone
   are not visual evidence. Without a renderer or preview, state the limitation
   and do not claim visual verification. Ordinary prose review does not require
   installing renderer dependencies.

The source checkers accept one diagram per input. For a page with several
diagrams, extract each original Mermaid block unchanged into a Markdown file in
a temporary directory, then validate it using its matching context/flow profile.
The upstream exporter can select a block directly with `--diagram N` (one-based)
without maintaining a duplicate source. Put exported previews in a temporary
directory too. The source-only consumer profile does not require or package the
renderer; use an available native preview or report that visual verification
could not be completed. Inspect the page sequence as well as individual diagrams.

## Independent review

When the user or applicable instructions authorize sub-agents and the facility
is available, use a separate reviewer before completion. Give the reviewer only
the requirements, current files and relevant neighbors, diff, and validation or
preview evidence. Do not pass the author's self-evaluation as evidence. Ask for
read-only findings on business meaning, audience, Japanese, section continuity,
duplicate headings, and actual visual evidence. The reviewer must not edit,
commit, or push. Classify findings by consequence and include file/location,
evidence, and the change needed.

Resolve material findings, validate the revision, and ask the reviewer to check
the affected findings again when needed. Stop once material findings are
resolved; do not generate cosmetic work merely to prolong review. If delegation
is unavailable or unauthorized, perform a separate review pass and report it as
self-review, not independent review.

## Keep recurring lessons

After review, distinguish a local preference from a recurring failure. Update
the existing Skill or reference that owns a recurring rule; this Skill owns the
review loop, business modeling owns reader-facing prose, and Mermaid authoring
owns source/layout behavior. Add a small regression check only when it can
reliably detect the failure. When adding Skill files or dependencies, check the
repository routing, Skill metadata/validation registry, and consumer profile's
explicit distribution paths. Build and inspect a temporary consumer artifact
when distribution changes. Do not assume a Skill directory is automatically
packaged or installed in another environment.

## Completion

Report what changed, the actual source/visual checks and independent review
performed, remaining limitations, and any reusable Skill updates. Commit or
publish only within the authorization already present in the session; this
Skill grants no standing permission to push.

```bash
python3 .agents/skills/reader-facing-artifact-review/scripts/check_reader_artifact.py path/to/README.md path/to/detail.md
PYTHONDONTWRITEBYTECODE=1 python3 .agents/skills/reader-facing-artifact-review/scripts/test_reader_artifact.py
```

`--allow-diagram-title` is an explicit exception for reviewing a standalone
diagram inside a Markdown wrapper that needs its own exported title. Embedded
reader-facing diagrams use the default check. Layout/curve differences are
observations to inspect, not automatic failures or permission to change meaning.

For native diagrams outside the Context/Flow profiles (for example purpose or
actor-requirement diagrams), the upstream exporter accepts `--type mermaid`.
This checks syntax through rendering, not the governed modeling semantics.
Use the correct governed type for Contexts and Flows; never alter meaning to fit
a checker or label a generic render as semantic validation.
