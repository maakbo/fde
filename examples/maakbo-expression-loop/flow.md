# アイデアを表現にする — 業務フロー

This Business Flow expands `b_shape_expression` only far enough to show the
production loop and its one meaningful rework decision.

```mermaid
---
title: アイデアを表現にするフロー
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
  b_receive_seed@{ label: "種を受け取る", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_find_core@{ label: "芯を見つける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_make_draft@{ label: "初稿をつくる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_core_clear@{ label: "芯は見える？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_refine@{ label: "対話で磨く", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_receive_seed --> b_find_core
  b_find_core --> b_make_draft
  b_make_draft --> d_core_clear
  d_core_clear -->|はい| b_refine
  d_core_clear -->|まだ| b_find_core

  class b_receive_seed,b_find_core,b_make_draft,b_refine activity;
  class d_core_clear decision;

  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## 読み方

アイデアの種を受け取り、芯を見つけて初稿をつくる。芯がまだ見えなければ
見つけるところへ戻り、見えたら対話で磨く。ここでは順序と戻り道だけを
示し、関係者や情報の意味は親のシーンコンテキストで確認する。

## 未解決の問い

「芯が見える？」を判断するのはつくる人だけか、それとも対話相手との
合意を必要とするか？
