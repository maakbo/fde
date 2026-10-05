# 現場で使い、学びながら広げる

検証で成立した仕組みを、限定した範囲から使い始めます。使った量だけでなく、業務や人にどんな変化が起きたかを確かめ、現場の知見を仕組みへ戻しながら育てます。

## 流れ

```mermaid
---
title: 現場で使い、学びながら広げる
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  b_limited_rollout@{ label: "限定導入する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_observe_use@{ label: "利用を観測する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_measure_outcome@{ label: "成果を測る", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_update_knowledge@{ label: "知識を更新する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_improve@{ label: "仕組みを改善する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_expand@{ label: "利用を広げる?", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_rollout@{ label: "利用を広げる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_continue@{ label: "限定で続ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_limited_rollout --> b_observe_use
  b_observe_use --> b_measure_outcome
  b_measure_outcome --> b_update_knowledge
  b_update_knowledge --> b_improve
  b_improve --> d_expand
  d_expand -->|広げる| b_rollout
  d_expand -->|続ける| b_continue
  b_continue --> b_observe_use

  class b_limited_rollout,b_observe_use,b_measure_outcome,b_update_knowledge,b_improve,b_rollout,b_continue activity;
  class d_expand decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## この流れで育てること

最初は同じ仕組みを限られた利用者や範囲で使い、現場とのズレを集めます。利用件数などのOutputだけでなく、処理時間、手戻り、判定の一致、顧客や利用者への価値などのOutcomeを見ます。短期で分かる変化と、時間をかけて追う変化は分けて扱います。

担当者が使う中で得た感覚や判断は、言葉にしてプロンプト、ルール、業務モデル、ナレッジベースへ戻します。改善された仕組みから人も新しい判断を学び、人とAIの両方が育つ循環をつくります。

同じ機能をより多くの利用者へ届けるときは段階的に広げます。処理能力を高める、新しい機能を追加する、別の業務へ適用する場合は、単なる利用者拡大とは分けて考え、必要なら再び対象の見極めから始めます。

← [仕組みを現場へ根づかせる場面へ](establish-work-context.md)
