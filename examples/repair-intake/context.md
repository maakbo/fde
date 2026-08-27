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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { transform: translateY(-6px); }"
---
flowchart LR
  a_customer@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "顧客", pos: "b", w: 38, h: 38, constraint: "on" }
  i_repair_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "修理依頼", pos: "b", w: 38, h: 38, constraint: "on" }
  b_receive_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "依頼受付", pos: "b", w: 30, h: 30, constraint: "on" }
  i_intake_record@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "受付記録", pos: "b", w: 38, h: 38, constraint: "on" }
  x_scheduling_service@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", label: "予約管理", pos: "b", w: 38, h: 38, constraint: "on" }
  i_repair_booking@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "修理予約", pos: "b", w: 38, h: 38, constraint: "on" }
  a_repair_team@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "修理担当", pos: "b", w: 38, h: 38, constraint: "on" }

  a_customer --> i_repair_request
  i_repair_request --> b_receive_request
  b_receive_request --> i_intake_record
  i_intake_record --> x_scheduling_service
  x_scheduling_service --> i_repair_booking
  i_repair_booking --> a_repair_team

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

顧客から修理依頼を受け、依頼受付が受付記録をつくる。記録は予約管理へ渡り、修理予約として修理担当へ届く。矢印は時間の順序ではなく、価値・情報の受け渡しを示す。

## 未解決の問い

予約管理は受付の外部システムか、それとも修理業務の一部か？
