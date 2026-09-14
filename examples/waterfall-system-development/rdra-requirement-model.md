# PDF帳票作成システム — RDRA Requirement Model

System Contextで置いた境界に対して、評価用sampleで会話したい主要要求を
まとめます。要求の詳細や優先度を確定するページではなく、開発業務へ降りる
ためのtop-layer Viewです。

← [RDRA System Context](rdra-system-context.md)

## モデル

```mermaid
---
title: PDF帳票作成システムのRequirement Model
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
  h_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  h_business_user@{ label: "帳票利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_business_data@{ label: "業務データ源", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/cloud.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  subgraph bd_pdf_system["PDF帳票システム"]
    direction LR
    s_pdf_report_system@{ label: "PDF帳票作成", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  end
  k_report_specification@{ label: "帳票仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  k_data_contract@{ label: "データ契約", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  k_report_quality@{ label: "帳票品質", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  k_operation_safety@{ label: "運用安全", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  k_acceptance_condition@{ label: "受入条件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  h_business_owner --- s_pdf_report_system
  h_business_user --- s_pdf_report_system
  x_business_data --- s_pdf_report_system
  h_business_owner --- k_acceptance_condition
  s_pdf_report_system --- k_report_specification
  s_pdf_report_system --- k_data_contract
  s_pdf_report_system --- k_report_quality
  s_pdf_report_system --- k_operation_safety
  s_pdf_report_system --- k_acceptance_condition

  class h_business_owner,h_business_user human;
  class s_pdf_report_system system;
  class k_report_specification,k_data_contract,k_report_quality,k_operation_safety,k_acceptance_condition artifact;
  class x_business_data external;

  classDef human fill:none,stroke:none,color:#25231F;
  classDef system fill:none,stroke:none,color:#5F5A52;
  classDef artifact fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  style bd_pdf_system fill:#FAF8F2,stroke:#C8C1B6,stroke-width:0.75px,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

主要要求は、帳票の内容・形式を定める帳票仕様、入力を保証するデータ契約、
正確性や再現性を含む帳票品質、保管や再実行を含む運用安全、そして業務側が
受け入れられる条件に分けて会話できます。

## 次のView

- [PDF帳票システムの要件定義](requirements-context.md) — 要求を開発業務へ降ろすpilot →
