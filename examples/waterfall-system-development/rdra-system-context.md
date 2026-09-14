# PDF帳票作成システム — RDRA System Context

このevaluation sampleでは、業務担当が業務データをもとにPDF帳票を作成し、
利用・保管できるシステムを開発対象として置きます。実案件の事実ではなく、
上位の境界から開発業務へ降りるためのsyntheticな前提です。

## モデル

```mermaid
---
title: PDF帳票作成システムのSystem Context
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  h_business_user@{ label: "帳票利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  h_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  h_development_team@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_business_data@{ label: "業務データ源", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/cloud.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  subgraph bd_pdf_system["PDF帳票システム"]
    direction LR
    s_pdf_report_system@{ label: "PDF帳票作成", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
    k_pdf_document@{ label: "PDF帳票", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  end
  x_document_storage@{ label: "帳票保管先", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/cloud.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  h_business_user --- s_pdf_report_system
  h_business_owner --- s_pdf_report_system
  h_development_team --- s_pdf_report_system
  x_business_data --- s_pdf_report_system
  s_pdf_report_system --- k_pdf_document
  k_pdf_document --- x_document_storage

  class h_business_user,h_business_owner,h_development_team human;
  class s_pdf_report_system system;
  class k_pdf_document artifact;
  class x_business_data,x_document_storage external;

  classDef human fill:none,stroke:none,color:#25231F;
  classDef system fill:none,stroke:none,color:#5F5A52;
  classDef artifact fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  style bd_pdf_system fill:#FAF8F2,stroke:#C8C1B6,stroke-width:0.75px,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

左側の業務担当・業務責任者・開発チームと業務データ源を、中央の
PDF帳票システムが受け止めます。生成されたPDF帳票は、利用されるだけでなく、
帳票保管先へ置ける成果物として扱います。

## 次のView

- [RDRA Requirement Model](rdra-requirement-model.md) →
- [システム開発 Business Map](business-map.md) →
