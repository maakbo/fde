# アイデアを表現にする — ユースケース・シーンコンテキスト

This Business Context cuts the scene in which a loose idea becomes a reviewable
first expression through dialogue. All non-business nodes are selected from
the canonical master maps.

```mermaid
---
title: アイデアを表現にする
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 64
    rankSpacing: 80
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  a_creator@{ label: "つくる人", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_idea_seed@{ label: "アイデアの種", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_shape_expression@{ label: "形にする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  a_dialogue_partner@{ label: "対話相手", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_expression_draft@{ label: "表現の初稿", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_github@{ label: "GitHub", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_reader@{ label: "読み手", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_creator --- b_shape_expression
  i_idea_seed --- b_shape_expression
  b_shape_expression --- a_dialogue_partner
  b_shape_expression --- i_expression_draft
  b_shape_expression --- x_github
  b_shape_expression --- a_reader

  class a_creator,a_dialogue_partner,a_reader actor;
  class b_shape_expression business;
  class i_idea_seed,i_expression_draft information;
  class x_github external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

アイデアの種を、つくる人と対話相手が表現の初稿へ形にする。GitHubは
履歴を残す外部システムとして置き、読み手は成果を受け取る主体として
仮置きする。線はこのシーンの関係を表し、作業順は示さない。

## Master references

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_creator` | つくる人 | 種を置き、判断する主体 |
| [Actor master](master-actor-map.md) | `a_dialogue_partner` | 対話相手 | 初稿を一緒に検討する相手 |
| [Actor master](master-actor-map.md) | `a_reader` | 読み手 | 初稿の価値を受け取る主体（仮） |
| [External-system master](master-system-map.md) | `x_github` | GitHub | 履歴と差分を残す接点 |
| [Information master](master-information-model.md) | `i_idea_seed` | アイデアの種 | 入力となる素材 |
| [Information master](master-information-model.md) | `i_expression_draft` | 表現の初稿 | このシーンの成果 |

## 未解決の問い

GitHubをこのシーンの外部システムとして残すか。それとも作業環境の前段
（別の環境コンテキスト図）へ分け、ここでは表現と対話に集中するか？
