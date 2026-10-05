# 協働を設計し、小さく確かめる

定義した業務を、実際に試せる仕組みへ変えます。人とAIの責任を分け、AIへ渡す文脈、入出力、安全策を設計し、限られた環境で成立するかを確かめます。

## 流れ

```mermaid
---
title: 協働を設計し、小さく確かめる
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  b_split_roles@{ label: "役割を分ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_design_context@{ label: "文脈を設計する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_design_io@{ label: "入出力と安全を決める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_prototype@{ label: "試せる形にする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_verify@{ label: "成立性を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_ready@{ label: "本番へ進める?", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_prepare@{ label: "導入を準備する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_rework@{ label: "設計を見直す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_split_roles --> b_design_context
  b_design_context --> b_design_io
  b_design_io --> b_prototype
  b_prototype --> b_verify
  b_verify --> d_ready
  d_ready -->|進める| b_prepare
  d_ready -->|見直す| b_rework
  b_rework --> b_design_context

  class b_split_roles,b_design_context,b_design_io,b_prototype,b_verify,b_prepare,b_rework activity;
  class d_ready decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## この流れで確かめること

役割分担では、人に残す判断、AIに任せる処理、ルールやRPAで扱う処理、既存システムが担う処理を明らかにします。文脈設計では、目的、前提、制約、参照情報、判断例を揃えます。

入出力と安全の設計では、入力データ、JSONなどの出力形式、Schema、Validation、権限、機密性、Human-in-the-Loop、Guardrailsを決めます。必要な論点は、実装担当者だけでなく情報セキュリティや法務とも具体化します。

試作後はSandboxなどの安全な環境で、精度、速度、安全性、再現性、コスト、現場での使いやすさを確認します。合格基準を満たさないときは、設計を見直して再検証するか、方法を変えるか、導入をやめるかを判断します。

← [協働の仕組みをつくる場面へ](build-collaboration-context.md)
