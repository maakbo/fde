# PDF帳票システム — Information master

このsampleで人が参照・確認・共有できるInformationを、stable IDで管理します。線は、
同じ帳票業務で扱う情報の関連を表し、項目や保存方式までは決めません。

```mermaid
---
title: PDF帳票システムのInformation master
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
flowchart TB
  i_report_data@{ label: "業務データ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_report_definition@{ label: "帳票仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_output_condition@{ label: "出力条件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_pdf_report@{ label: "PDF帳票", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  i_report_data --- i_report_definition
  i_report_definition --- i_output_condition
  i_output_condition --- i_pdf_report
  i_report_data --- i_pdf_report

  class i_report_data,i_report_definition,i_output_condition,i_pdf_report information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## Dictionary

| ID | Label | Meaning in this sample | Confidence |
| --- | --- | --- | --- |
| `i_report_data` | 業務データ | 帳票作成の入力となる業務上の情報 | synthetic working |
| `i_report_definition` | 帳票仕様 | 帳票の内容・形式を決める情報 | synthetic working |
| `i_output_condition` | 出力条件 | 出力可否や対象を判断する情報 | synthetic working |
| `i_pdf_report` | PDF帳票 | 出力・再取得して業務で使う情報 | synthetic working |

## 読み方

業務データを帳票仕様と出力条件に合わせ、PDF帳票として確認できるようにします。Informationの
作成・参照・提供先は、[PDF帳票システム](README.md)と各Business Contextの関係として確認し、
項目定義や保存方式はこのmasterに詰め込みません。
