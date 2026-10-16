# アイデアを形にする

```mermaid
---
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
  %% 親Contextの一つの業務を詳しくしたフロー。親図と展開対象のIDを記録する。
  %% 要確認: 「芯が見える？」を誰と確認し、どこまでを一周とするか。
  b_receive_seed@{ label: "種を受け取る", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_find_core@{ label: "芯を見つける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_make_draft@{ label: "初稿をつくる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_core_clear@{ label: "芯は見える？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_refine@{ label: "対話で磨く", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

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

受け取ったアイデアから芯を見つけ、初稿をつくります。芯が見えているかを確認し、まだ明確でなければ考え直します。確認できたら、対話しながら表現を磨きます。

芯を確認する相手と、一周の作業範囲はまだ決まっていません。
