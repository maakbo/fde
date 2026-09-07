# 要件を整合する — Business Flow

親 View: `requirements-context.md` / expanded node: `b_align_requirements`

要件レビューで不整合が見つかった場合に、論点を解消して要件を更新し、再度確認する最小の戻りループを表します。

```mermaid
---
title: 要件を整合する
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
flowchart TB
  b_prepare_review@{ label: "論点を揃える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_review_requirements@{ label: "要件を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_requirements_agreed@{ label: "合意できる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_resolve_gap@{ label: "差異を解く", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_update_requirements@{ label: "要件を更新", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_baseline_requirements@{ label: "基準化する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_prepare_review --> b_review_requirements
  b_review_requirements --> d_requirements_agreed
  d_requirements_agreed -->|合意| b_baseline_requirements
  d_requirements_agreed -->|差異| b_resolve_gap
  b_resolve_gap --> b_update_requirements
  b_update_requirements --> b_review_requirements

  class b_prepare_review,b_review_requirements,b_resolve_gap,b_update_requirements,b_baseline_requirements business;
  class d_requirements_agreed decision;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

レビューは一度の承認作業ではありません。要件間、業務側とシステム側、要求と受入条件の差異を見つけ、解消し、要件へ戻して再確認する反復です。合意できた状態になったときだけベースライン化します。

## この Flow でまだ答えないこと

- 誰が承認権限を持つか
- 変更要求として扱う境界はどこか
- 合意後に変更が発生した場合の変更管理 Flow

これらは要件定義 Context と横断 Business「変更を統制する」の関係で追加します。
