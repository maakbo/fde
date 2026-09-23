# Repair intake information master

Canonical information concepts for the synthetic repair-intake boundary. The
direction from the intake record to the booking is a working hypothesis about
derivation, not a detailed data-flow sequence.

```mermaid
---
title: 修理受付の情報マスタ
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
  i_repair_request@{ label: "修理依頼", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_intake_record@{ label: "受付記録", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_repair_booking@{ label: "修理予約", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  i_repair_request --- i_intake_record
  i_intake_record --> i_repair_booking

  class i_repair_request,i_intake_record,i_repair_booking information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

修理依頼と受付記録は概念上関係し、受付記録から修理予約が導かれると
仮置きする。項目や多重度は別のデータ設計資料で扱う。

## 未解決の問い

修理依頼と受付記録は別概念か、同じ情報の状態違いか？
