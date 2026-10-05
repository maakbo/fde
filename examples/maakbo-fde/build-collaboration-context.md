# 協働の仕組みをつくる

対象と要件の叩き台をもとに、主体者と仲間、fde、fdeAIが、人、AI、RPA、既存システムの役割を分けます。文脈、入出力、権限、安全策を設計し、まずは安全な範囲で試せる仕組みにして、業務として成立するかを確かめます。

## モデル

```mermaid
---
title: 協働の仕組みをつくる
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
  i_business_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_target_priority@{ label: "対象と優先順位", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_requirement_basis@{ label: "要件の叩き台", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_collaboration_design@{ label: "協働設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_roles_constraints@{ label: "役割と責任", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_solution_design@{ label: "仕組みの設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_realization@{ label: "仕組み化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_prototype@{ label: "試せる仕組み", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_context_fit@{ label: "現場適合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_poc_result@{ label: "検証結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_subject@{ label: "主体者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_companions@{ label: "主体者の仲間", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_fde --- b_collaboration_design
  a_fde --- b_realization
  a_fde --- b_context_fit
  a_fde_ai --- b_collaboration_design
  a_fde_ai --- b_realization
  a_fde_ai --- b_context_fit
  i_business_model --- b_collaboration_design
  i_target_priority --- b_collaboration_design
  i_requirement_basis --- b_collaboration_design
  b_collaboration_design --- i_roles_constraints
  b_collaboration_design --- i_solution_design
  i_roles_constraints --- b_realization
  i_solution_design --- b_realization
  b_realization --- i_prototype
  i_prototype --- b_context_fit
  b_context_fit --- i_poc_result
  b_collaboration_design --- a_subject
  b_realization --- a_subject
  b_context_fit --- a_subject
  b_collaboration_design --- a_companions
  b_context_fit --- a_companions

  class a_fde,a_fde_ai,a_subject,a_companions actor;
  class b_collaboration_design,b_realization,b_context_fit business;
  class i_business_model,i_target_priority,i_requirement_basis,i_roles_constraints,i_solution_design,i_prototype,i_poc_result information;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

協働設計では、人に残す判断、AIに任せる処理、ルールやRPAで扱う処理、既存システムが担う処理を分けます。AIを使う場合は、目的、前提、制約、参照情報、入出力形式、Validation、権限、Human-in-the-Loop、Guardrailsまで設計します。

仕組み化では、まず試せる小さな形をつくります。現場適合では、本番へ一気に出さず、安全な環境で精度、速度、安全性、コスト、再現性、現場利用性を確認し、進める、見直す、やめるを判断します。

[協働を設計し、小さく確かめる流れを見る](design-and-poc-flow.md) →

← [FDEの進め方へ](delivery-process.md)
