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
    nodeSpacing: 64
    rankSpacing: 80
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

  %% 通常の関係は---。-->は強い依存性を強調するときだけ使う。
  a_customer --- b_receive_request
  i_repair_request --- b_receive_request
  b_receive_request --- i_intake_record
  b_receive_request --- x_scheduling_service
  x_scheduling_service --- b_receive_request
  b_receive_request --- i_repair_booking
  b_receive_request --- a_repair_team

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

依頼受付を中心に、顧客、修理依頼、受付記録、予約管理、修理予約、修理担当との関係を整理する。左から右の配置は読みやすさのためで、通常の関係は線で表す。矢印は強い依存性を強調したい場合だけ使う。

## 未解決の問い

予約管理は受付の外部システムか、それとも修理業務の一部か？
