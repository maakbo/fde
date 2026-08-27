# Repair intake flow

Focused task flow for completeness checking and missing-detail rework.

```mermaid
---
title: 修理受付の業務フロー
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
  b_receive_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "依頼受付", pos: "b", w: 30, h: 30, constraint: "on" }
  d_information_complete@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", label: "情報は揃った？", pos: "b", w: 38, h: 38, constraint: "on" }
  b_request_details@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "不足情報を確認", pos: "b", w: 30, h: 30, constraint: "on" }
  b_book_repair@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "修理予約", pos: "b", w: 30, h: 30, constraint: "on" }

  b_receive_request --> d_information_complete
  d_information_complete -->|揃っている| b_book_repair
  d_information_complete -->|不足あり| b_request_details
  b_request_details --> d_information_complete

  class b_receive_request,b_request_details,b_book_repair activity;
  class d_information_complete decision;

  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## 読み方

依頼を受け、情報が揃っているかを確認する。不足があれば確認し、揃ったら修理を予約する。

## 未解決の問い

情報の確認は受付の一部か、それとも別の担当か？
