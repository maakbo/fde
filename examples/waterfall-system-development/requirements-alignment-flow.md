# 要件合意

要件の抜けや矛盾を解き、関係者が合意できる状態まで繰り返し整える流れです。

← [要件定義](requirements-context.md)

## フロー

```mermaid
---
title: 要件合意
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
  b_prepare_review@{ label: "論点整理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_review_requirements@{ label: "要件確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_requirements_agreed@{ label: "合意できる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_resolve_gap@{ label: "差異解消", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_update_requirements@{ label: "要件更新", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_baseline_requirements@{ label: "基準化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

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

## 図の業務

- **論点整理** — レビューで確認すべき抜け・矛盾・判断点を揃える。
- **要件確認** — 業務要件、システム要件、受入条件の整合を確認する。
- **差異解消** — 合意できない理由を明らかにし、責任者と解決方針を決める。
- **要件更新** — 解決内容を要件へ戻す。
- **基準化** — 合意済みの要件として後続工程が参照できる状態にする。

## この図が表していること

要件レビューは一度の承認作業ではなく、差異があれば要件へ戻って再確認する反復です。合意できた状態だけを後続工程の基準にします。
