# 帳票を用意する場面

業務データを整え、帳票の内容と出力条件を確認しながらPDFを用意します。
必要な帳票は、あとから探して再取得できます。

← [帳票業務の全体](domain-overview.md)

```mermaid
---
title: 帳票を用意する場面
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
  b_report_ready@{ label: "帳票を用意する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_prepare_report@{ label: "データを整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_generate_pdf@{ label: "PDFを出力する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_retrieve_report@{ label: "帳票を探す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_retrieve_pdf@{ label: "帳票を再取得する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
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

`データを整える`では業務システムから得た情報を帳票に使える状態にし、`PDFを出力する`では
帳票仕様と出力条件に沿ってPDF帳票を作ります。必要なときは`帳票を探す`と`帳票を再取得する`
で、同じPDF帳票をもう一度使えるようにします。
