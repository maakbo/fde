# fde

対話から現場の構造を捉え、議論できるモデルと動く仕組みを一緒につくる、maakboなりの Forward Deployed Engineering。

`fde` は、まだ整理されていない事業や業務の話を、AIエージェントと一緒に素早く可視化するための公開実験です。最初の能力として、アクター・業務・情報・外部システムを抽出し、Mermaidでコンテキスト図と業務フロー図へ変換します。

図をきれいにすることだけが目的ではありません。自動配置に収まりにくい複雑さも観察しながら、具体と抽象を行き来し、粒度・境界・関係性を議論できる状態をつくります。

## What is included

- `AGENTS.md`: every agent should share these working principles.
- `.github/copilot-instructions.md`: a small GitHub Copilot adapter.
- `.github/agents/`: business modeler, Markdown diagram author, explicit exporter, and read-only reviewer agents.
- `.agents/skills/`: business modeling, Mermaid authoring, and explicit media-export Skills.
- `templates/`: Markdown-first Mermaid starting points.
- `templates/github-actions-validate.yml`: optional CI workflow; copy it to `.github/workflows/validate.yml` when the publishing credential allows workflow files.
- `examples/repair-intake/`: a synthetic three-level example linking overview, focused context, and focused flow.
- `examples/repair-intake/previews/`: explicit PNG review artifacts with tap-friendly links for mobile clients.
- `scripts/validate_repository.py`: one command to validate the public bundle.

## Quick start

Requirements for normal modeling and authoring: Python 3.9+.

```bash
git clone https://github.com/maakbo/fde.git
cd fde
python3 scripts/validate_repository.py
```

Open the cloned repository in an AI agent environment and start with loose language:

```text
Use the business-modeler agent.

A customer sends a repair request. The coordinator checks the scheduling
service, records the request, and asks for missing information before booking.
Create the first discussion-ready model. Keep assumptions visible.
Write the diagram inside Markdown for immediate preview. Do not export images.
```

In GitHub Copilot, repository instructions, custom agents, and project Agent Skills are loaded from the standard locations included here. Other compatible agents can begin with `AGENTS.md` and `.agents/skills/`.

## Modeling loop

```text
loose conversation
  -> concrete candidates
  -> actors / activities / information / external systems
  -> first Mermaid model in Markdown
  -> preview and inspect density / relationships
  -> discuss boundary, grain, and assumptions
  -> move upward or downward in abstraction
```

A focused diagram normally begins with 3–7 semantic nodes. More than seven is not an automatic failure. First preserve and inspect the complexity. Then decide whether to keep it, refine the subject or grain, or add focused diagrams and a one-level-higher overview. The repair-intake example demonstrates the reverse path too: a detail can change how its parent overview concept is understood.

Context views use undirected lines for ordinary business relationships. Use an arrow only to emphasize an explicitly strong dependency. When the question is specifically how value or information enters and leaves an activity, use the explicit left-to-right value-flow variant so the provider, output recipient, and supporting system remain visible.

## Working source and export

The default artifact is a Markdown file containing one `mermaid` code block. That same file carries its reading, assumptions, and next question, and is the single editable source for the diagram.

Ordinary modeling and diagram requests stop after source validation. They do not generate `.mmd`, SVG, or PNG files. This keeps the conversation fast in GitHub Copilot and lets VS Code preview the working file directly.

Media export is a separate, explicit action. When stable assets are needed for publication or visual review, install the optional renderer and invoke the export Skill:

```bash
npm ci
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py \
  examples/repair-intake/context.md --type context --output-dir /tmp/fde-export
```

The exporter reads the Mermaid block without changing the Markdown source. A standalone `.mmd` remains supported when a user or integration explicitly requires it.

The example's [review previews](examples/repair-intake/previews/) are tracked only because they are public, synthetic visual-review artifacts. New diagrams should remain Markdown-only unless media export is explicitly requested.

## Visual language

The visual object is an icon, not a text box. Labels sit below fixed-size icons, so longer wording does not change visual weight.

| Meaning | Thin Lucide asset |
| --- | --- |
| Actor | `lucide-thin/user.svg` |
| Business activity | `lucide-thin/ellipse.svg` |
| Information | `lucide-thin/file.svg` |
| External system | `lucide-thin/server.svg` |
| Decision | `lucide-thin/diamond.svg` |
| iPad / iPhone / laptop | `lucide-thin/tablet.svg`, `smartphone.svg`, `laptop.svg` |

Working Markdown blocks reference the repository's thin Lucide SVGs through stable raw URLs for portability and immediate preview where Mermaid v11 image nodes are supported. The shapes remain Lucide; only the shared stroke width is normalized to `1.35`. Explicit export embeds the retrieved SVG data into generated assets so those assets remain self-contained.

## Project status

This is an early public practice, not a universal definition of FDE. The first release intentionally stays small: business structure, context, and flow. New patterns should be added only after real use shows that they are reusable.

## License

Repository code and original documentation are MIT licensed. Icons remain under their upstream licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
