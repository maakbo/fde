# システム開発業務

システムエンジニアを中心に、業務の期待を使えるシステムへ変え、運用へ渡すまでの仕事を会話するための例です。特定の会社や案件の標準工程を示すものではなく、関係者・業務・情報のつながりを見直す入口として置いています。

```mermaid
---
title: システム開発業務
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
  p_system_purpose("業務の変化を、使えるシステムとして届ける")
  a_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_system_engineer@{ label: "システムエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_dev_environment@{ label: "開発環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_request_background@{ label: "依頼背景", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_system_development@{ label: "システム開発業務", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_release_plan@{ label: "リリース計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_ops@{ label: "運用担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_system_development -.- p_system_purpose
  a_business_owner --- b_system_development
  a_system_engineer --- b_system_development
  x_dev_environment --- b_system_development
  i_request_background --- b_system_development
  b_system_development --- i_system_requirement
  b_system_development --- i_release_plan
  b_system_development --- a_ops
  class a_business_owner,a_system_engineer,a_ops actor;
  class b_system_development business;
  class i_request_background,i_system_requirement,i_release_plan information;
  class x_dev_environment external;
  class p_system_purpose purpose;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  classDef purpose fill:#FFFFFF,stroke:#9E988E,color:#25231F,stroke-width:0.75px;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

業務責任者が期待する変化を、システムエンジニアが要件・設計・検証へつなぎ、運用担当が使い続けられるシステムとして引き受けます。開発環境は、その仕事を支えます。

## 実現したいこと

```mermaid
---
title: 実現したいこと
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
  a_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_system_engineer@{ label: "システムエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_ops@{ label: "運用担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  p_owner_goal("業務で変えたいことを、判断できる形にしたい")
  p_engineer_goal("要求から検証までを、つながった仕事にしたい")
  p_ops_goal("運用へ安心して引き継げる状態にしたい")
  p_shared_outcome("業務で使い続けられるシステムを届ける")

  a_business_owner -.- p_owner_goal
  a_system_engineer -.- p_engineer_goal
  a_ops -.- p_ops_goal
  p_owner_goal -.- p_shared_outcome
  p_engineer_goal -.- p_shared_outcome
  p_ops_goal -.- p_shared_outcome

  class a_business_owner,a_system_engineer,a_ops actor;
  class p_owner_goal,p_engineer_goal,p_ops_goal,p_shared_outcome purpose;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef purpose fill:#FFFFFF,stroke:#9E988E,color:#25231F,stroke-width:0.75px;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

立場の違う関係者が、要求・設計・検証・運用を別々の作業にせず、業務で使い続けられる状態へ向けて会話できることを目指します。

## 業務

### 開発業務の全体

```mermaid
---
title: システム開発業務の全体
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
  a_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_system_engineer@{ label: "システムエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_ops@{ label: "運用担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_request_background@{ label: "依頼背景", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_estimation@{ label: "見積", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_requirements@{ label: "要件定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_basic_design@{ label: "基本設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_external_specification@{ label: "外部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_implementation_unit@{ label: "実装・単体", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_build_artifact@{ label: "ビルド成果物", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_external_test@{ label: "外部結合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_deployment@{ label: "導入", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_release_plan@{ label: "リリース計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_dev_environment@{ label: "開発環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_external_business_system@{ label: "外部システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_production_env@{ label: "本番環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_business_owner --- b_estimation
  a_business_owner --- b_requirements
  a_system_engineer --- b_requirements
  a_system_engineer --- b_basic_design
  a_system_engineer --- b_implementation_unit
  a_system_engineer --- b_external_test
  a_ops --- b_deployment
  i_request_background --- b_estimation
  i_request_background --- b_requirements
  b_requirements --- i_system_requirement
  b_basic_design --- i_system_requirement
  b_basic_design --- i_external_specification
  i_external_specification --- b_implementation_unit
  b_implementation_unit --- i_build_artifact
  i_build_artifact --- b_external_test
  i_build_artifact --- b_deployment
  b_deployment --- i_release_plan
  b_implementation_unit --- x_dev_environment
  b_external_test --- x_external_business_system
  b_deployment --- x_production_env

  click b_requirements href "https://github.com/maakbo/fde/blob/main/examples/system-development/requirements-context.md" "要件定義の場面を見る"
  click b_implementation_unit href "https://github.com/maakbo/fde/blob/main/examples/system-development/implementation-unit-context.md" "実装・単体の場面を見る"
  click b_external_test href "https://github.com/maakbo/fde/blob/main/examples/system-development/external-integration-context.md" "外部結合の場面を見る"
  click b_deployment href "https://github.com/maakbo/fde/blob/main/examples/system-development/deployment-context.md" "導入の場面を見る"

  class a_business_owner,a_system_engineer,a_ops actor;
  class b_estimation,b_requirements,b_basic_design,b_implementation_unit,b_external_test,b_deployment business;
  class i_request_background,i_system_requirement,i_external_specification,i_build_artifact,i_release_plan information;
  class x_dev_environment,x_external_business_system,x_production_env external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

業務責任者が依頼背景を持ち込み、システムエンジニアがシステム要件と外部仕様へ整えます。実装・外部結合ではビルド成果物を確認し、運用担当がリリース計画と本番環境を引き継ぎます。開発環境と外部システムが各場面を支えます。詳しい役割と場面は [要件定義](requirements-context.md)、[実装・単体](implementation-unit-context.md)、[外部結合](external-integration-context.md)、[導入](deployment-context.md) で確認できます。

## 情報

```mermaid
---
title: システム開発業務で扱う情報
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: linear
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
  i_request_background@{ label: "依頼背景", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_business_requirement@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_external_specification@{ label: "外部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_source_code@{ label: "ソースコード", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_build_artifact@{ label: "ビルド成果物", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_acceptance_criteria@{ label: "受入条件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_release_plan@{ label: "リリース計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_runbook@{ label: "運用手順", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  i_request_background --- i_business_requirement
  i_business_requirement --- i_system_requirement
  i_system_requirement --- i_external_specification
  i_external_specification --- i_source_code
  i_source_code --- i_build_artifact
  i_system_requirement --- i_acceptance_criteria
  i_build_artifact --- i_release_plan
  i_release_plan --- i_runbook

  class i_request_background,i_business_requirement,i_system_requirement,i_external_specification,i_source_code,i_build_artifact,i_acceptance_criteria,i_release_plan,i_runbook information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

依頼の背景と業務要件をシステム要件・外部仕様へ整え、コードと成果物を確認し、リリース計画と運用手順へつなぎます。これらの情報が、関係者の判断と次の仕事を支えます。

## 詳しく見る

- [業務マップ](business-map.md) — 主な仕事のつながりを読む
- [要件定義](requirements-context.md) — 業務要件とシステム要件を整える場面を見る
- [実装・単体](implementation-unit-context.md) — 設計をコードと単体確認へ変える場面を見る
- [外部結合](external-integration-context.md) — 外部との契約と検証を確かめる場面を見る
- [導入](deployment-context.md) — 本番切替と運用移管の場面を見る

この例では、期待を要件へ落とし、設計・実装・検証を経て、導入と運用へ渡す仕事を、関係者と情報のつながりから読み始められます。気になる場面は、上のリンクから詳しく見られます。
