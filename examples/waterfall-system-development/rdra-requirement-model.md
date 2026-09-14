# PDF帳票作成システム — RDRA Requirement Model

System Contextで置いた境界に対して、評価用sampleで会話したい重要要求を
まとめます。ここでいう要求は機能・非機能の分類ではなく、Actorが実現したい
価値を短い自然言語で置いたものです。詳細や優先度を確定するページではなく、
開発業務へ降りるためのtop-layer Viewです。

図中のfile iconは共有する要求文（knowledge artifact）を表し、下位の仕様分類そのものではありません。

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
  subgraph bd_pdf_system["PDF帳票システム"]
    direction LR
    s_pdf_report_system@{ label: "PDF帳票作成", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  end
  k_accurate_report@{ label: "帳票を正確に得る", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  k_reproducible_report@{ label: "同じ帳票を再現する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  k_retrievable_report@{ label: "帳票を後から取得する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  k_safe_report_operation@{ label: "安全に業務を続ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  h_business_user --- k_accurate_report
  h_business_user --- k_reproducible_report
  h_business_user --- k_retrievable_report
  h_business_owner --- k_reproducible_report
  h_business_owner --- k_safe_report_operation
  s_pdf_report_system --- k_accurate_report
  s_pdf_report_system --- k_reproducible_report
  s_pdf_report_system --- k_retrievable_report
  s_pdf_report_system --- k_safe_report_operation

  class h_business_owner,h_business_user human;
  class s_pdf_report_system system;
  class k_accurate_report,k_reproducible_report,k_retrievable_report,k_safe_report_operation artifact;

  classDef human fill:none,stroke:none,color:#25231F;
  classDef system fill:none,stroke:none,color:#5F5A52;
  classDef artifact fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  style bd_pdf_system fill:#FAF8F2,stroke:#C8C1B6,stroke-width:0.75px,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

帳票利用者が「必要な帳票を正確に得る」「同じ帳票を再現する」「後から取得する」ことを
求め、業務責任者は再現性と安全な継続を重視します。これらの価値を実現するために、
下位の開発業務で帳票仕様・データ要件・品質条件・運用条件・受入条件へ具体化します。

## 下位へのtrace

要求の文言をそのまま仕様へ置き換えず、下位のInformationが何を具体化するかを追跡します。

| 上位の重要要求 | 下位で具体化するInformation | 開発業務への導線 |
| --- | --- | --- |
| 帳票を正確に得る | `i_report_specification` / `i_system_requirement` / `i_acceptance_criteria` | [PDF帳票システムの要件定義](requirements-context.md) |
| 同じ帳票を再現する | `i_report_specification` / `i_system_requirement` / `i_acceptance_criteria` | [PDF帳票システムの要件定義](requirements-context.md) |
| 帳票を後から取得する | `i_report_specification` / `i_external_interface_requirement` / `i_acceptance_criteria` | [PDF帳票システムの要件定義](requirements-context.md) |
| 安全に業務を続ける | `i_system_requirement` / `i_external_interface_requirement` / `i_acceptance_criteria` | [PDF帳票システムの要件定義](requirements-context.md) |

このtraceはrequirements Contextでの代表的な具体化を示すもので、PDF固有の詳細分解を
全体canonicalへ確定するものではありません。

## 次のView

- [システム開発 Business Map](business-map.md) — 上位要求から開発業務の入口へ →
- [PDF帳票システムの要件定義](requirements-context.md) — 要求を開発業務へ降ろすpilot →
