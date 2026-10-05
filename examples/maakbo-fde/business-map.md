# FDEの業務

FDEは、七つの業務を行き来しながら、現場で使い続けられる仕組みをつくります。

## モデル

```mermaid
---
title: FDEの業務
config:
  layout: elk
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
  b_fde@{ label: "FDE", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_context_understanding@{ label: "現場理解", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_business_structuring@{ label: "業務構造化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_change_design@{ label: "変化設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_collaboration_design@{ label: "協働設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_realization@{ label: "仕組み化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_context_fit@{ label: "現場適合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_autonomy_transition@{ label: "自律移行", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_fde --- b_context_understanding
  b_fde --- b_business_structuring
  b_fde --- b_change_design
  b_fde --- b_collaboration_design
  b_fde --- b_realization
  b_fde --- b_context_fit
  b_fde --- b_autonomy_transition

  class b_fde,b_context_understanding,b_business_structuring,b_change_design,b_collaboration_design,b_realization,b_context_fit,b_autonomy_transition business;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

七つは工程の順番ではありません。同じ業務が複数の段階で現れ、試して分かったズレから現場理解へ戻るなど、必要な仕事を行き来します。

案件をどんな順番で進めるかは、[FDEの進め方](delivery-process.md)で見られます。

- [業務の変化を描く](shape-change-context.md): 現場理解、業務構造化、変化設計を使って、対象選定と要件の叩き台まで進める
- [協働の仕組みをつくる](build-collaboration-context.md): 協働設計、仕組み化、現場適合を使って、設計と小さな検証まで進める
- [仕組みを現場へ根づかせる](establish-work-context.md): 現場適合と自律移行を使って、限定導入、Outcome観測、知識循環、段階展開を進める

← [FDEの全体へ](README.md)
