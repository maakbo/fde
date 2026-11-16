# 基本設計 — ビジネスユースケース

[システム開発の全体に戻る](../README.md)

「仕様を具体化する」という親業務を展開します。ここでは、承認済み要件を受け取り、開発・検証担当が実装や確認に使える設計仕様に具体化する場面を扱います。対象は架空の受託開発As-Isです。

```mermaid
---
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
  a_it@{ label: "顧客IT担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_design@{ label: "設計担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_review@{ label: "レビュー担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_dev@{ label: "実装担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  x_accounting@{ label: "既存会計システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirements@{ label: "合意済み要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "設計仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_review@{ label: "レビュー結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_ui@{ label: "画面・操作を定める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_interface@{ label: "外部連携を定める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_data@{ label: "データを定める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_review@{ label: "設計をレビューする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_design --- b_ui
  a_design --- b_interface
  a_design --- b_data
  a_design --- b_review
  a_it --- b_interface
  x_accounting --- b_interface
  a_review --- b_review
  a_dev --- b_review
  i_requirements --- b_ui
  i_requirements --- b_interface
  i_requirements --- b_data
  i_requirements --- b_review
  i_design --- b_ui
  i_design --- b_interface
  i_design --- b_data
  i_design --- b_review
  i_review --- b_review

  b_ui --- b_review
  b_interface --- b_review
  b_data --- b_review
  class a_it,a_design,a_review,a_dev actor;
  class x_accounting external;
  class i_requirements,i_design,i_review information;
  class b_ui,b_interface,b_data,b_review business;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef external fill:none,stroke:none,color:#5F5A52;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

画面・外部連携・データの設計は、親業務を具体化する子業務です。レビューでは、合意済み要件と設計仕様を照合し、指摘や修正の結果を次の判断に渡します。実装担当は成果を受け取る役割であり、実務でレビューへ参加するかは現場確認の対象です。

**この業務で扱う情報**は[情報モデル](../information-model.md)の「合意済み要件」「設計仕様」「レビュー結果」と同じ意味で使います。

**次の展開**： [設計レビューの業務フロー](review-flow.md) — 誰がどの順に確認し、修正や引渡しを行うか。

この初版は設計者・レビュアーの役割や作業を仮置きしたものです。実際の組織構造・レビュー方式・承認権限を断定しません。
