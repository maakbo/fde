# 仕組みを現場へ根づかせる

検証で成立した仕組みを、主体者と仲間が限定した範囲から使います。fdeとfdeAIは、利用結果だけでなく業務や人に起きた変化を一緒に確かめ、現場の判断や知見を仕組みへ戻します。使う人たちが自分で理解し、変え、育てられる状態へ移していきます。

## モデル

```mermaid
---
title: 仕組みを現場へ根づかせる
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
  i_poc_result@{ label: "検証結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_roles_constraints@{ label: "役割と責任", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_usage_result@{ label: "利用結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_outcome@{ label: "業務の成果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_feedback@{ label: "現場の知見", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_context_fit@{ label: "現場適合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_work_system@{ label: "業務の仕組み", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_knowledge@{ label: "共有知識", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_autonomy_transition@{ label: "自律移行", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  a_subject@{ label: "主体者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_companions@{ label: "主体者の仲間", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_fde --- b_context_fit
  a_fde --- b_autonomy_transition
  a_fde_ai --- b_context_fit
  a_fde_ai --- b_autonomy_transition
  i_poc_result --- b_context_fit
  i_roles_constraints --- b_context_fit
  i_roles_constraints --- b_autonomy_transition
  i_usage_result --- b_context_fit
  i_outcome --- b_context_fit
  i_feedback --- b_context_fit
  b_context_fit --- i_business_model
  b_context_fit --- i_work_system
  b_context_fit --- i_knowledge
  i_business_model --- b_autonomy_transition
  i_work_system --- b_autonomy_transition
  i_knowledge --- b_autonomy_transition
  b_context_fit --- a_subject
  b_autonomy_transition --- a_subject
  b_context_fit --- a_companions
  b_autonomy_transition --- a_companions

  class a_fde,a_fde_ai,a_subject,a_companions actor;
  class b_context_fit,b_autonomy_transition business;
  class i_poc_result,i_roles_constraints,i_usage_result,i_outcome,i_feedback,i_business_model,i_work_system,i_knowledge information;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## この場面で行うこと

現場適合では、限定した範囲で利用を始め、利用件数などのOutputだけでなく、処理時間、手戻り、判断の一致、利用者への価値などのOutcomeを追います。短期で分かる変化と、時間をかけて追う変化を分けます。

使う中で担当者が得た感覚や判断を現場の知見として言葉にし、業務モデル、プロンプト、ルール、ナレッジへ戻します。改善された仕組みを使うことで人側の判断も育ち、人とAIの知識が循環する状態をつくります。

自律移行では、運営、判断、変更の責任を主体者と仲間へ移します。同じ仕組みを広げるときは段階的に利用者を増やし、新しい機能や別業務へ広げる場合は改めて対象と価値を見極めます。

[現場で使い、学びながら広げる流れを見る](deployment-learning-flow.md) →

← [FDEの進め方へ](delivery-process.md)
