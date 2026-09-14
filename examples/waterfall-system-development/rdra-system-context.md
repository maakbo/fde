# Legacy evaluation — PDF帳票作成システム System Context

このページは過去のevaluation orientationを残したlegacy Viewです。current RDRA domain modelは
[PDF帳票システム sample](../pdf-report-system/)で確認してください。ここで示す開発業務や13工程は
このViewの下位RDRA階層ではありません。

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
  x_business_data@{ label: "業務データ源", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/cloud.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  subgraph bd_pdf_system["PDF帳票システム"]
    direction LR
    s_pdf_report_system@{ label: "PDF帳票作成", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  end

  h_business_user --- s_pdf_report_system
  h_business_owner --- s_pdf_report_system
  x_business_data --- s_pdf_report_system

  class h_business_user,h_business_owner human;
  class s_pdf_report_system system;
  class x_business_data external;

  classDef human fill:none,stroke:none,color:#25231F;
  classDef system fill:none,stroke:none,color:#5F5A52;
  classDef artifact fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  style bd_pdf_system fill:#FAF8F2,stroke:#C8C1B6,stroke-width:0.75px,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

左側の帳票利用者・業務責任者と業務データ源を、中央のPDF帳票システムが受け止めます。
開発チームや開発工程はこのViewの対象ではなく、下位の「システム開発 Business Map」で
扱います。PDF帳票の仕様・品質・保管などは、ここで示す利用文脈から下位の要求・設計へ
具体化します。

## Legacy navigation

- [PDF帳票システムのcurrent RDRA domain model](../pdf-report-system/) →
- [development-work model（13工程）](business-map.md) →
