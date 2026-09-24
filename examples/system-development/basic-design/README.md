# 仕組みを設計する

業務要件をもとに、人と仕組みの責務を分け、外部とやり取りできる仕様と実現方式へ整える仕事です。

← [業務システム開発](../) ／ [要求を整える](../requirements/)

```mermaid
---
title: 仕組みを設計する
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
  a_project_lead@{ label: "プロジェクトリーダー", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_designer@{ label: "設計者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_architect@{ label: "アーキテクト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_customer_core@{ label: "得意先基幹システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_business_requirement@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_define_responsibility@{ label: "責務を分ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_external_specification@{ label: "外部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_shape_external_specification@{ label: "外部仕様を整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_internal_specification@{ label: "内部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_choose_approach@{ label: "実現方式を選ぶ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_design_rule@{ label: "設計ルール", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_project_lead --- b_define_responsibility
  a_designer --- b_define_responsibility
  a_architect --- b_define_responsibility
  x_customer_core --- b_shape_external_specification
  i_business_requirement --- b_define_responsibility
  i_system_requirement --- b_define_responsibility
  b_define_responsibility --- i_external_specification
  i_external_specification --- b_shape_external_specification
  b_shape_external_specification --- i_internal_specification
  i_internal_specification --- b_choose_approach
  a_architect --- b_choose_approach
  b_choose_approach --- i_design_rule

  click b_shape_external_specification href "https://github.com/maakbo/fde/blob/main/examples/system-development/basic-design/interface-specification.md" "外部仕様の設計観点を見る"

  class a_project_lead,a_designer,a_architect actor;
  class b_define_responsibility,b_shape_external_specification,b_choose_approach business;
  class i_business_requirement,i_system_requirement,i_external_specification,i_internal_specification,i_design_rule information;
  class x_customer_core external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

業務要件とシステム要件を見ながら、どこを人が担い、どこを仕組みに任せるかを決めます。外部仕様は一度で固定せず、内部仕様と実現方式へつなぎながら、開発できる形へ整えます。

- [外部仕様の設計観点](interface-specification.md) — 仕様を試行と証跡へ戻しながら整える
- [仕組みを実装する](../implementation/) — 設計をコードと検証へ変える
