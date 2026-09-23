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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  a_customer@{ label: "顧客", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_repair_request@{ label: "修理依頼", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_receive_request@{ label: "依頼受付", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_intake_record@{ label: "受付記録", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_scheduling_service@{ label: "予約管理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_repair_booking@{ label: "修理予約", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_repair_team@{ label: "修理担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  %% 左に提供側、中央にBusiness、右に受領側を置く。通常relationは---。
  a_customer --- b_receive_request
  i_repair_request --- b_receive_request
  b_receive_request --- i_intake_record
  b_receive_request --- x_scheduling_service
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

## Master references

この図の `a_`、`x_`、`i_` ノードは、次のマスタ図から正規ID・ラベル・
アイコン定義を選択している。Mermaidにファイル間importはないため、図中
のノード定義は正規定義をそのままコピーする。

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_customer` | 顧客 | 価値の受け手 |
| [Actor master](master-actor-map.md) | `a_repair_team` | 修理担当 | 価値の提供者 |
| [External-system master](master-system-map.md) | `x_scheduling_service` | 予約管理 | 予約との接点 |
| [Information master](master-information-model.md) | `i_repair_request` | 修理依頼 | 入力 |
| [Information master](master-information-model.md) | `i_intake_record` | 受付記録 | 受付結果 |
| [Information master](master-information-model.md) | `i_repair_booking` | 修理予約 | 成果 |

## 未解決の問い

予約管理は受付の外部システムか、それとも修理業務の一部か？
