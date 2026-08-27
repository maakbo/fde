# Business flow diagram

Edit the Mermaid block directly and preview this Markdown file. Record unresolved routes or responsibility questions below the diagram.

```mermaid
---
title: 業務フロー
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape path { stroke:#FFFFFF !important; stroke-width:10px !important; }"
---
flowchart TB
  b_receive@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "受付", pos: "b", w: 30, h: 30, constraint: "on" }
  d_complete@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", label: "情報は揃った？", pos: "b", w: 38, h: 38, constraint: "on" }
  b_create@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "作成", pos: "b", w: 30, h: 30, constraint: "on" }
  b_review@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "確認", pos: "b", w: 30, h: 30, constraint: "on" }

  b_receive --> d_complete
  d_complete -->|揃っている| b_create
  b_create --> b_review
  d_complete -->|不足あり| b_receive

  class b_receive,b_create,b_review activity;
  class d_complete decision;

  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## 未解決の問い

どの業務・判断・戻り道が、共有認識を変えそうか？
