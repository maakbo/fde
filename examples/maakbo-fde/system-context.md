# FDEを誰と実現するか

主体者と仲間、fde、fdeAIが、それぞれの役割を持ってFDEを育てます。

## モデル

```mermaid
---
title: FDEを誰と実現するか
config:
  layout: elk
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: true
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
  a_maakbo_fde@{ label: "fde", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_fde_ai@{ label: "fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_fde@{ label: "FDE", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  a_subject@{ label: "主体者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_companions@{ label: "主体者の仲間", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  p_ultimate_purpose(["個も仲間も、自然と自分たちらしく居られる"])

  a_maakbo_fde --- b_fde
  a_fde_ai --- b_fde
  b_fde --- p_ultimate_purpose
  b_fde --- a_subject
  b_fde --- a_companions

  class a_maakbo_fde,a_fde_ai,a_subject,a_companions actor;
  class b_fde business;
  class p_ultimate_purpose purpose;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef purpose fill:#FFFFFF,stroke:#9E988E,color:#25231F,stroke-width:0.75px;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

fdeとfdeAIだけで仕組みを作るのではありません。主体者と仲間も、現場を知り、選び、使いながら、一緒に仕組みを育てます。

業務の中で役割を持つAIやシステムは、それぞれの業務を詳しく見るときに加えていきます。

← [FDEの全体へ](README.md)

[主体者が必要とする状態を見る](actor-requirement.md) →
