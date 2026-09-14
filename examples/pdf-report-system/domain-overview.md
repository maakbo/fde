# PDF帳票業務のDomain Overview

業務担当は業務システムのデータを使ってPDF帳票を作ります。業務責任者は、業務で使える
帳票になっているかを確認します。このViewは、帳票業務の中心と周囲の関係を俯瞰します。

## モデル

```mermaid
---
title: PDF帳票業務のDomain Overview
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
  b_pdf_reporting@{ label: "帳票業務", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_pdf_report@{ label: "PDF帳票", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_report_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_report_user --- b_pdf_reporting
  x_business_system --- b_pdf_reporting
  i_report_data --- b_pdf_reporting
  b_pdf_reporting --- i_pdf_report
  b_pdf_reporting --- a_report_owner

  click b_pdf_reporting href "https://github.com/maakbo/fde/blob/main/examples/pdf-report-system/report-creation-context.md" "代表BUCの詳細を見る"

  class a_report_user,a_report_owner actor;
  class b_pdf_reporting business;
  class i_report_data,i_pdf_report information;
  class x_business_system external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 図の業務

| 業務 | 何をしているか |
| --- | --- |
| **帳票業務** | 業務データを帳票として使える形にし、内容を確認できる状態にする。 |

## この図が表していること

線は、帳票業務を成立させる参加者とInformationの関係を表します。厳密な実行順では
ありません。`帳票業務`の中をBusiness → BUC → Activity → UCへ展開したViewは、下の
[代表BUC「帳票を用意する」](report-creation-context.md)で確認できます。

## Master references

このViewのActor / External System / Informationは、次のmaster mapと同じID・label・iconを
使っています。

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_report_user` | 業務担当 | 帳票業務を実行する主体 |
| [Actor master](master-actor-map.md) | `a_report_owner` | 業務責任者 | 帳票を確認する主体 |
| [External-system master](master-system-map.md) | `x_business_system` | 業務システム | 業務データを提供する外部システム |
| [Information master](master-information-model.md) | `i_report_data` | 業務データ | 帳票業務の入力 |
| [Information master](master-information-model.md) | `i_pdf_report` | PDF帳票 | 帳票業務の成果 |

## Supporting model

- [モデル索引](model-set-index.md) — RDRA要素の階層とViewの対応
- [Actor / External System / Information master](master-model-index.md) — 正規IDと定義
