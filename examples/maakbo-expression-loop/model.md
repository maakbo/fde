# maakbo表現制作 — working model

## Modeling question

チャットでゆるく渡したアイデアの種を、対話しながら、言葉・図解・プレゼン
などの見える形へ育てる作業は、誰と何を介して成立しているか。

- Reader: まーくぼと、次に同じ環境を使うAIエージェントや協働者。
- Boundary: アイデアを受け取り、初稿をつくり、対話で磨く表現制作。
- State: 目指す制作ループの working hypothesis。現在の運用事実を確定しない。
- Context reading: 線は業務上の関係、矢印はフローの順序だけを表す。

## Candidate inventory

- Actors: つくる人; 対話相手; 読み手（仮）。
- Business activities: 表現制作; アイデアを形にする; 対話で磨く。
- Information: アイデアの種; 表現の初稿。
- External systems: GitHub（履歴と差分の接点）。
- Implementation details omitted from the first model: iPad、iPhone、MacBook、
  Obsidian、Mermaidのレンダリング手段。
- Unresolved: 読み手を常に主要主体とするか、発信シーンへ限定するか。

## Selected views

- [Overall context](overview.md)
- [Use-case context](context.md)
- [Business flow](flow.md)
- [Model-set trace](model-set-index.md)
- [Master model index](master-model-index.md)

Each working view contains one Mermaid block for immediate GitHub or VS Code
preview. The master maps are parallel canonical sources, not additional rungs.

## Text alternative

全体では、表現制作を中心に、つくる人・対話相手・読み手を主要主体として
置く。シーンでは、つくる人と対話相手がアイデアの種を表現の初稿へ形にし、
GitHubが履歴を支える。フローでは、種を受け取り、芯を見つけ、初稿をつくり、
芯が見えるまで戻りながら、対話で磨く。

## Assumptions and omissions

- 「対話相手」はAIや人を限定しない作業上の役割として扱う。
- GitHubを表現制作シーンに置くことは仮説。作業環境の別コンテキストへ移す
  可能性を残す。
- iPad、iPhone、MacBook、Obsidian、画像出力は、関係が主題になった時点で
  別の環境コンテキストへ展開する。

## Next discussion question

この全体像で、読み手を主要主体として残すことが、まーくぼの表現制作の
本質に近いか？
