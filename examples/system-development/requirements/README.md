# 要求を整える

業務担当者や経営者が持つ期待を読み取り、プロジェクトとして向き合う業務要件と、合意できる対象範囲へ整える仕事です。

← [業務システム開発](../)

```mermaid
---
title: 要求を整える
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
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  a_business_user@{ label: "業務担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_executive@{ label: "経営者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_project_lead@{ label: "プロジェクトリーダー", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_customer_core@{ label: "得意先基幹システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_rfp@{ label: "RFP", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_interpret_request@{ label: "依頼を読み解く", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_requirement@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_shape_business_requirement@{ label: "業務要件を整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_project_plan@{ label: "プロジェクト計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_agree_scope@{ label: "対象を合意する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_business_user --- b_interpret_request
  a_executive --- b_interpret_request
  a_project_lead --- b_interpret_request
  a_project_lead --- b_shape_business_requirement
  a_executive --- b_agree_scope
  x_customer_core --- b_interpret_request
  i_rfp --- b_interpret_request
  b_interpret_request --- i_business_requirement
  i_business_requirement --- b_shape_business_requirement
  b_shape_business_requirement --- i_project_plan
  i_project_plan --- b_agree_scope
  b_agree_scope --- i_system_requirement

  click b_agree_scope href "https://github.com/maakbo/fde/blob/main/examples/system-development/requirements/alignment-flow.md" "対象を合意する流れを見る"

  class a_business_user,a_executive,a_project_lead actor;
  class b_interpret_request,b_shape_business_requirement,b_agree_scope business;
  class i_rfp,i_business_requirement,i_project_plan,i_system_requirement information;
  class x_customer_core external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

RFPや現場の話をそのまま工程名へ置き換えず、何を変えたいのか、どこまでを対象にするのかを関係者で確かめます。ここで整えた業務要件と対象範囲が、次の設計の出発点になります。

- [対象を合意する流れ](alignment-flow.md) — 差異を解消し、次へ渡す判断を見る
- [仕組みを設計する](../basic-design/) — 要件から責務と仕様を組み立てる
