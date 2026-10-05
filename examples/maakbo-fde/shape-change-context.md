# 業務の変化を描く

主体者と仲間が、現場の実態、困りごと、暗黙知を持ち寄ります。fdeとfdeAIが言葉と絵にし、四者で業務を確かめながら、不要な仕事、ボトルネック、変える価値のある対象を見極め、設計へ渡せる要件の叩き台までつくります。

## モデル

```mermaid
---
title: 業務の変化を描く
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
flowchart LR
  a_fde@{ label: "fde", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_fde_ai@{ label: "fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_context_information@{ label: "業務の現状", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_business_issue@{ label: "業務課題", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_desired_state@{ label: "ありたい状態", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_context_understanding@{ label: "現場理解", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_business_structuring@{ label: "業務構造化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_change_design@{ label: "変化設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_target_priority@{ label: "対象と優先順位", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_requirement_basis@{ label: "要件の叩き台", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_subject@{ label: "主体者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_companions@{ label: "主体者の仲間", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_fde --- b_context_understanding
  a_fde --- b_business_structuring
  a_fde --- b_change_design
  a_fde_ai --- b_context_understanding
  a_fde_ai --- b_business_structuring
  a_fde_ai --- b_change_design
  i_context_information --- b_context_understanding
  i_context_information --- b_business_structuring
  i_business_issue --- b_context_understanding
  i_business_issue --- b_change_design
  i_desired_state --- b_change_design
  b_context_understanding --- i_business_model
  b_business_structuring --- i_business_model
  i_business_model --- b_change_design
  b_change_design --- i_target_priority
  b_change_design --- i_requirement_basis
  b_context_understanding --- a_subject
  b_business_structuring --- a_subject
  b_change_design --- a_subject
  b_context_understanding --- a_companions
  b_business_structuring --- a_companions
  b_change_design --- a_companions

  class a_fde,a_fde_ai,a_subject,a_companions actor;
  class b_context_understanding,b_business_structuring,b_change_design business;
  class i_context_information,i_business_issue,i_desired_state,i_business_model,i_target_priority,i_requirement_basis information;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

現場理解と業務構造化では、流れだけでなく、判断、例外、暗黙知、前提、制約まで話せる業務モデルへ近づけます。

変化設計では、まず不要な業務を減らし、残った課題のボトルネックを絞ります。人、ルール、RPA、AIエージェントなどの手段を比べ、効果、実現可能性、リスクから対象と優先順位を選びます。その対象について、範囲、対象外、前提、制約、機能・非機能要件、合格基準の叩き台を残します。

[対象を見極め、業務を定義する流れを見る](change-design-flow.md) →

← [FDEの進め方へ](delivery-process.md)
