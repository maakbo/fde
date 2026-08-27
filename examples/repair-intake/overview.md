# Repair service overview

One-level-higher view connecting intake, repair, and return.

```mermaid
---
title: 修理サービスの概要
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { transform: translateY(-6px); }"
---
flowchart TB
  b_manage_intake@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "受付管理", pos: "b", w: 30, h: 30, constraint: "on" }
  b_repair_item@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "修理品", pos: "b", w: 30, h: 30, constraint: "on" }
  b_return_item@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "返却", pos: "b", w: 30, h: 30, constraint: "on" }

  b_manage_intake --> b_repair_item
  b_repair_item --> b_return_item

  class b_manage_intake,b_repair_item,b_return_item activity;

  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## 読み方

修理サービスは受付から修理、返却へ進む。それぞれの業務は、詳細なMarkdown図へ展開できる。
