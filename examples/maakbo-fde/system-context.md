# FDE System Context

## Modeling question

誰が `FDE` を担い、誰へ価値を届けるか。

## Reading

左のActor群が中央の `FDE` を担い、右の `主体者` に価値を届ける関係を表す。線は時間順序や情報フローを表さない。

```mermaid
---
title: FDE System Context
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
---
flowchart LR
  a_maakbo_fde@{ label: "maakbo / fde", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_fde_ai@{ label: "fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_subject@{ label: "主体者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  subgraph fde_core[" "]
    direction TB
    p_visible_choice(["見えるから、自分で選べる"])
    b_fde@{ label: "FDE", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
    p_visible_choice --> b_fde
  end

  a_maakbo_fde --- b_fde
  a_fde_ai --- b_fde
  b_fde --- a_subject

  class a_maakbo_fde,a_fde_ai,a_subject actor;
  class b_fde business;
  class p_visible_choice purpose;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef purpose fill:#EDF2EA,stroke:#7C8975,color:#25231F,stroke-width:1px;
  style fde_core fill:none,stroke:none;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  linkStyle 0 stroke:transparent,stroke-width:0px;
```

## Boundary

表示するのは、価値提供Actor、FDEというBusiness、価値を受けるActor、目的の補助注釈だけである。InformationとExternal Systemは、この最上位Viewでは表示しない。
