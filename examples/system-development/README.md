# 業務システム開発

経営上・業務上の課題や実現したいことを、仕組みにする仕事です。ここでは、現場で使われる言葉を手がかりに、誰が何を整え、次に何を渡すのかを一枚からたどります。

```mermaid
---
title: 業務システム開発
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
  a_designer@{ label: "設計者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_developer@{ label: "開発者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_customer_core@{ label: "得意先基幹システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_rfp@{ label: "RFP", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_shape_needs@{ label: "要求を整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_requirement@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_design_solution@{ label: "仕組みを設計する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_external_specification@{ label: "外部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_implement_solution@{ label: "仕組みを実装する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_verify_external@{ label: "外部と確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_transition_operation@{ label: "運用へ渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_operation_plan@{ label: "運用計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_dev_environment@{ label: "開発環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_staging_environment@{ label: "ステージング環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_production_environment@{ label: "本番環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_business_user --- b_shape_needs
  a_executive --- b_shape_needs
  a_project_lead --- b_shape_needs
  a_project_lead --- b_design_solution
  a_designer --- b_design_solution
  a_designer --- b_implement_solution
  a_developer --- b_implement_solution
  a_developer --- b_verify_external
  x_customer_core --- b_design_solution
  i_rfp --- b_shape_needs
  b_shape_needs --- i_business_requirement
  b_shape_needs --- i_system_requirement
  i_business_requirement --- b_design_solution
  b_design_solution --- i_external_specification
  i_system_requirement --- b_implement_solution
  i_external_specification --- b_implement_solution
  b_implement_solution --- b_verify_external
  b_verify_external --- b_transition_operation
  b_transition_operation --- i_operation_plan
  b_implement_solution --- x_dev_environment
  b_verify_external --- x_staging_environment
  b_transition_operation --- x_production_environment

  click b_shape_needs href "https://github.com/maakbo/fde/tree/main/examples/system-development/requirements/" "要求を整える仕事を見る"
  click b_design_solution href "https://github.com/maakbo/fde/tree/main/examples/system-development/basic-design/" "仕組みを設計する仕事を見る"
  click b_implement_solution href "https://github.com/maakbo/fde/tree/main/examples/system-development/implementation/" "仕組みを実装する仕事を見る"
  click b_verify_external href "https://github.com/maakbo/fde/tree/main/examples/system-development/external-integration/" "外部と確かめる仕事を見る"
  click b_transition_operation href "https://github.com/maakbo/fde/tree/main/examples/system-development/deployment/" "運用へ渡す仕事を見る"

  class a_business_user,a_executive,a_project_lead,a_designer,a_developer actor;
  class b_shape_needs,b_design_solution,b_implement_solution,b_verify_external,b_transition_operation business;
  class i_rfp,i_business_requirement,i_system_requirement,i_external_specification,i_operation_plan information;
  class x_customer_core,x_dev_environment,x_staging_environment,x_production_environment external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

業務担当者や経営者の意図をプロジェクト側が受け取り、業務要件からシステム要件と外部仕様へ整えます。設計者と開発者が仕組みに変え、外部との確認を経て、運用計画とともに本番へ渡します。

現場では、提案依頼、要求定義、各種テスト、移行、運用保守などの言葉も使われます。ここではそれらをいったん同じ工程名として固定せず、仕事のまとまりごとに具体化します。

## 仕事へ入る

- [要求を整える](requirements/) — RFPや業務の期待を、合意できる要件へ整える
- [仕組みを設計する](basic-design/) — 要件から責務と外部仕様を組み立てる
- [仕組みを実装する](implementation/) — 設計をコードへ変え、検証できる状態にする
- [外部と確かめる](external-integration/) — 外部システムとの契約と境界を確かめる
- [運用へ渡す](deployment/) — 移行・本番確認を経て、運用へ引き継ぐ

それぞれのディレクトリが、その仕事について考え、作業し、成果を残す入口です。必要になった成果物やさらに具体的な仕事は、その仕事の入口の下に置きます。
