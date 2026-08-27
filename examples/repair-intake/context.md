# Repair intake context

Working view of the actors, information, and outside service around repair intake.

```mermaid
---
title: 修理受付のコンテキスト
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 48
    rankSpacing: 64
    padding: 8
  themeVariables:
    background: "#FAF8F2"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FAF8F2 !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FAF8F2 !important; } .image-shape .label rect { fill:#FAF8F2 !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { transform: translateY(-6px); }"
---
flowchart TB
  a_customer@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "顧客", pos: "b", w: 38, h: 38, constraint: "on" }
  b_receive_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "依頼受付", pos: "b", w: 30, h: 30, constraint: "on" }
  i_repair_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "修理依頼", pos: "b", w: 38, h: 38, constraint: "on" }
  i_intake_record@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "受付記録", pos: "b", w: 38, h: 38, constraint: "on" }
  x_scheduling_service@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", label: "予約管理", pos: "b", w: 38, h: 38, constraint: "on" }

  a_customer --- b_receive_request
  i_repair_request --- b_receive_request
  b_receive_request --- i_intake_record
  x_scheduling_service --- b_receive_request

  class a_customer actor;
  class b_receive_request business;
  class i_repair_request,i_intake_record information;
  class x_scheduling_service external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

顧客、修理依頼、受付記録、予約管理が、依頼受付を中心につながっている。線は業務上の関係を示し、時間の順序は示さない。

## 未解決の問い

予約は、引き続き受付の境界内に置くか？
