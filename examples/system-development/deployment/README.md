# 運用へ渡す

システム移行と本番確認を経て、業務で使える状態と運用の責任を引き継ぐ仕事です。

← [業務システム開発](../) ／ [外部と確かめる](../external-integration/)

```mermaid
---
title: 運用へ渡す
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
  a_migration_owner@{ label: "移行担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_quality_manager@{ label: "品質管理者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_operations_engineer@{ label: "インフラ担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_system_migration_plan@{ label: "システム移行計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_prepare_migration@{ label: "移行を準備する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_operation_plan@{ label: "運用計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_switch_production@{ label: "本番へ切り替える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_confirm_business_use@{ label: "業務利用を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_validation_result@{ label: "業務確認結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_transfer_operation@{ label: "運用を引き継ぐ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_runbook@{ label: "運用手順", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_staging_environment@{ label: "ステージング環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_production_environment@{ label: "本番環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_migration_owner --- b_prepare_migration
  a_quality_manager --- b_prepare_migration
  a_operations_engineer --- b_prepare_migration
  a_operations_engineer --- b_confirm_business_use
  a_operations_engineer --- b_transfer_operation
  i_system_migration_plan --- b_prepare_migration
  b_prepare_migration --- i_operation_plan
  b_prepare_migration --- x_staging_environment
  i_operation_plan --- b_switch_production
  b_switch_production --- x_production_environment
  b_switch_production --- b_confirm_business_use
  b_confirm_business_use --- i_business_validation_result
  i_business_validation_result --- b_transfer_operation
  b_transfer_operation --- i_runbook

  click b_confirm_business_use href "https://github.com/maakbo/fde/blob/main/examples/system-development/deployment/cutover-flow.md" "業務利用を確かめる流れを見る"

  class a_migration_owner,a_quality_manager,a_operations_engineer actor;
  class b_prepare_migration,b_switch_production,b_confirm_business_use,b_transfer_operation business;
  class i_system_migration_plan,i_operation_plan,i_business_validation_result,i_runbook information;
  class x_staging_environment,x_production_environment external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

移行計画と運用計画を確認して本番へ切り替え、業務で使えるかを確かめます。運用手順と確認結果を渡し、運用保守へ続く責任を引き継ぎます。

- [業務利用を確かめる流れ](cutover-flow.md) — 切替後の確認と判断を見る
- [業務システム開発](../) — 仕事全体へ戻る
