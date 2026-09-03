# Information master model

Use this as the canonical conceptual model of business information. `---`
shows a conceptual association. `-->` shows a directional derivation or
containment only when that direction matters; neither connector is a database
schema or a detailed data-flow sequence.

```mermaid
---
title: 情報マスタ
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
  i_request@{ label: "依頼", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_record@{ label: "受付記録", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_booking@{ label: "予約", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  i_request --- i_record
  i_record --> i_booking

  class i_request,i_record,i_booking information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

依頼と受付記録は概念上関係し、受付記録から予約が導かれる。項目、型、
多重度、保存場所はこの図に詰め込まず、必要なら別のデータ設計資料へ
分ける。

## 未解決の問い

どの情報が同じ概念で、どの情報が派生・保持・状態の違いなのか？
