# 修理受付の価値関係コンテキスト

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
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; }"
---
flowchart LR
  a_customer@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "顧客", pos: "b", w: 38, h: 38, constraint: "on" }
  i_repair_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "修理依頼", pos: "b", w: 38, h: 38, constraint: "on" }
  b_receive_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "依頼受付", pos: "b", w: 30, h: 30, constraint: "on" }
  i_intake_record@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "受付記録", pos: "b", w: 38, h: 38, constraint: "on" }
  x_scheduling_service@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", label: "予約管理", pos: "b", w: 38, h: 38, constraint: "on" }
  i_repair_booking@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "修理予約", pos: "b", w: 38, h: 38, constraint: "on" }
  a_repair_team@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "修理担当", pos: "b", w: 38, h: 38, constraint: "on" }

  a_customer --> b_receive_request
  i_repair_request --> b_receive_request
  b_receive_request --> i_intake_record
  b_receive_request --> x_scheduling_service
  x_scheduling_service --> b_receive_request
  b_receive_request --> i_repair_booking
  b_receive_request --> a_repair_team

  class a_customer,a_repair_team actor;
  class b_receive_request business;
  class i_repair_request,i_intake_record,i_repair_booking information;
  class x_scheduling_service external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

依頼受付を中心に、顧客と修理依頼が入力として入り、受付記録と修理予約が出ていく。予約管理は依頼受付と予約情報をやり取りする外部システムで、修理担当は修理予約という価値を受け取る。矢印は業務を中心とした価値・情報の関係を示す。

## 未解決の問い

予約管理は受付の外部システムか、それとも修理業務の一部か？
