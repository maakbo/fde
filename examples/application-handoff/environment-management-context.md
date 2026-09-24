# 実行環境を利用可能に保つ

開発・試験・検証・本番の環境を、それぞれの用途で継続利用でき、問題があれば回復できる状態へ保つ場面です。新規構築が少なくなった後も、管理・改修・保守は続きます。

[引き継ぎの全体像へ戻る](README.md)

```mermaid
---
title: 実行環境を利用可能に保つ
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
  a_maintenance@{ label: "アプリ保守チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_change_environment@{ label: "環境を構築・改修する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_environment_definition@{ label: "環境構成", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_maintain_resources@{ label: "DBと容量を保守する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_keep_recoverable@{ label: "回復可能な状態を保つ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_backup@{ label: "バックアップ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_delivery_definition@{ label: "CI/CD定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_maintain_delivery@{ label: "変更経路を保つ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  x_environments@{ label: "各実行環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_delivery@{ label: "CI/CD基盤", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_dev_team@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_maintenance --- b_change_environment
  a_maintenance --- b_maintain_resources
  a_maintenance --- b_keep_recoverable
  a_maintenance --- b_maintain_delivery
  b_change_environment --- i_environment_definition
  b_change_environment --- x_environments
  i_environment_definition --- b_maintain_resources
  b_maintain_resources --- b_keep_recoverable
  b_maintain_resources --- x_environments
  b_keep_recoverable --- i_backup
  b_keep_recoverable --- x_environments
  b_keep_recoverable --- b_maintain_delivery
  i_delivery_definition --- b_maintain_delivery
  b_maintain_delivery --- x_delivery
  b_maintain_delivery --- x_environments
  b_maintain_delivery --- a_dev_team

  class a_dev_team,a_maintenance actor;
  class b_change_environment,b_maintain_resources,b_keep_recoverable,b_maintain_delivery business;
  class i_environment_definition,i_backup,i_delivery_definition information;
  class x_environments,x_delivery external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

環境構築、環境管理、DBメンテナンス、バックアップ、ディスク管理、CI/CD管理を、環境を使い続けられる状態へ保つ責任として見ています。実案件では環境ごとの権限、定期作業、閾値、復旧確認、変更承認、異常時の判断者を具体化します。
