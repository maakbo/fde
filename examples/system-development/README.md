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
  a_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_system_engineer@{ label: "システムエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_dev_environment@{ label: "開発環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_request_background@{ label: "依頼背景", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_system_development@{ label: "システム開発業務", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_release_plan@{ label: "リリース計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_ops@{ label: "運用担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  p_system_purpose(["業務の変化を、使えるシステムとして届ける"])

  a_business_owner --- b_system_development
  a_system_engineer --- b_system_development
  x_dev_environment --- b_system_development
  i_request_background --- b_system_development
  b_system_development --- i_system_requirement
  b_system_development --- i_release_plan
  b_system_development --- a_ops
  b_system_development --- p_system_purpose

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

業務責任者が期待する変化を、システムエンジニアが開発環境と要件・設計・検証の判断材料へつなぎ、運用担当へ渡せるシステムとして整えます。線は厳密な手順ではなく、この業務を成立させる関係です。

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
  p_owner_goal(["業務で変えたいことを、判断できる形にしたい"])
  p_engineer_goal(["要求から検証までを、つながった仕事にしたい"])
  p_ops_goal(["運用へ安心して引き継げる状態にしたい"])
  p_shared_outcome(["業務で使い続けられるシステムを届ける"])

  a_business_owner --- p_owner_goal
  a_system_engineer --- p_engineer_goal
  a_ops --- p_ops_goal
  p_owner_goal --- p_shared_outcome
  p_engineer_goal --- p_shared_outcome
  p_ops_goal --- p_shared_outcome

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
  b_system_development@{ label: "システム開発業務", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_estimation@{ label: "見積", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_requirements@{ label: "要件定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_basic_design@{ label: "基本設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_implementation_unit@{ label: "実装・単体", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_external_test@{ label: "外部結合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_deployment@{ label: "導入", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_release_plan@{ label: "リリース計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_ops@{ label: "運用担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_business_owner --- b_system_development
  a_system_engineer --- b_system_development
  b_system_development --- b_estimation
  b_system_development --- b_requirements
  b_system_development --- b_basic_design
  b_system_development --- b_implementation_unit
  b_system_development --- b_external_test
  b_system_development --- b_deployment
  b_requirements --- i_system_requirement
  b_deployment --- i_release_plan
  b_deployment --- a_ops

  click b_requirements href "https://github.com/maakbo/fde/blob/main/examples/system-development/requirements-context.md" "要件定義の場面を見る"
  click b_implementation_unit href "https://github.com/maakbo/fde/blob/main/examples/system-development/implementation-unit-context.md" "実装・単体の場面を見る"
  click b_external_test href "https://github.com/maakbo/fde/blob/main/examples/system-development/external-integration-context.md" "外部結合の場面を見る"
  click b_deployment href "https://github.com/maakbo/fde/blob/main/examples/system-development/deployment-context.md" "導入の場面を見る"

  class a_business_owner,a_system_engineer,a_ops actor;
  class b_system_development,b_estimation,b_requirements,b_basic_design,b_implementation_unit,b_external_test,b_deployment business;
  class i_system_requirement,i_release_plan information;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

ここでは、13工程の詳細をそのまま標準工程として押し出さず、会話を始めやすい代表的な業務を見せています。全工程の候補と分解は [業務マップ](business-map.md) と [業務分解カタログ](decomposition-catalog.md) で確認します。順番や差戻しを問うときは、各業務の詳細ページや流れのページへ降ります。

## 情報

```mermaid
---
title: システム開発業務で扱う情報
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

依頼背景と業務要件をシステム要件へ具体化し、外部仕様・コード・成果物・受入条件を経て、リリース計画と運用手順へつなぎます。線は情報概念の関係を示し、ファイル形式やツールそのものを正本にはしません。

## 関連するView

- [業務マップ](business-map.md) — 13工程を固定標準ではなく、開発業務を話すための候補として見る
- [要件定義のContext](requirements-context.md) — 業務要件とシステム要件の境界を見る
- [実装・単体のContext](implementation-unit-context.md) — 設計をコードと単体確認へ変える場面を見る
- [外部結合のContext](external-integration-context.md) — 外部との契約・検証・責任境界を見る
- [導入のContext](deployment-context.md) — 本番切替と運用移管を見る

このsampleは、まず全体・実現したいこと・業務・情報を読み、必要な業務だけ詳細へ降りるための入口です。現在の境界や命名に確定していない点が出たら、元の会話へ戻って更新します。
