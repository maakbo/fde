# 代表BUC「帳票を用意する」

`帳票業務`の中から、業務データを受け取り、新規出力や必要時の再取得でPDF帳票を使える状態にする
代表BUCを展開します。
このViewでは、Business / BUC / Activity / UCの階層と、UCに関わるActor・External System・
Informationを同じ場面で確認できます。

← [PDF帳票業務のDomain Overview](domain-overview.md)

## モデル

```mermaid
---
title: 代表BUC「帳票を用意する」
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
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  a_report_user@{ label: "業務担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_business_system@{ label: "業務システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_report_data@{ label: "業務データ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_report_definition@{ label: "帳票仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_output_condition@{ label: "出力条件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_report_ready@{ label: "帳票を用意", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_prepare_report@{ label: "データを整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_generate_pdf@{ label: "PDFを出力", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_retrieve_report@{ label: "帳票を探す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_retrieve_pdf@{ label: "帳票を再取得", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_pdf_report@{ label: "PDF帳票", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_report_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_report_user --- b_report_ready
  a_report_user --- b_prepare_report
  a_report_user --- b_generate_pdf
  a_report_user --- b_retrieve_pdf
  x_business_system --- b_prepare_report
  i_report_data --- b_prepare_report
  i_report_definition --- b_generate_pdf
  i_output_condition --- b_generate_pdf
  b_report_ready --- b_prepare_report
  b_report_ready --- b_retrieve_report
  b_prepare_report --- b_generate_pdf
  b_retrieve_report --- b_retrieve_pdf
  b_generate_pdf --- i_pdf_report
  b_retrieve_pdf --- i_pdf_report
  b_generate_pdf --- a_report_owner

  class a_report_user,a_report_owner actor;
  class b_report_ready,b_prepare_report,b_generate_pdf,b_retrieve_report,b_retrieve_pdf business;
  class i_report_data,i_report_definition,i_output_condition,i_pdf_report information;
  class x_business_system external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 図の業務

| RDRA type | 業務 | このViewでの意味 |
| --- | --- | --- |
| BUC | **帳票を用意する** | 新しく作る場合と、既存の帳票を再取得する場合を同じ利用場面にまとめる。 |
| Activity | **データを整える** | 業務システムのデータを帳票に使える状態へ整える。 |
| UC | **PDFを出力** | 帳票仕様と出力条件を使い、PDF帳票を得られるようにする。 |
| Activity | **帳票を探す** | 必要な帳票を見つけ、再取得できる状態を確認する。 |
| UC | **帳票を再取得** | 既に得たPDF帳票を、必要なときに再び使えるようにする。 |

## この図が表していること

線は、このBUCを成立させる関係を表し、実行順を確定しません。`業務担当`と`業務システム`
はデータ準備に関わり、`帳票仕様`と`出力条件`はPDF出力の判断材料になります。出力した
`PDF帳票`は業務担当と業務責任者が確認・利用します。

## Master references

このViewのActor / External System / Informationは、次のmaster mapと同じID・label・iconを
使っています。

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_report_user` | 業務担当 | BUCと各UCに参加する主体 |
| [Actor master](master-actor-map.md) | `a_report_owner` | 業務責任者 | PDF帳票を確認する主体 |
| [External-system master](master-system-map.md) | `x_business_system` | 業務システム | 業務データを提供する外部システム |
| [Information master](master-information-model.md) | `i_report_data` | 業務データ | データ準備の入力 |
| [Information master](master-information-model.md) | `i_report_definition` | 帳票仕様 | PDF出力の判断材料 |
| [Information master](master-information-model.md) | `i_output_condition` | 出力条件 | PDF出力の判断材料 |
| [Information master](master-information-model.md) | `i_pdf_report` | PDF帳票 | 出力・再取得の対象 |

## 次のView

- [モデル索引](model-set-index.md) — Business / BUC / Activity / UCの対応
- [PDF帳票作成システムの開発](../waterfall-system-development/) — 別空間の13工程
