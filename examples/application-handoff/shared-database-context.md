# 共有データ構造を整合させる

複数のサブシステムから生じるデータ変更を、共通データベースとアプリケーションで矛盾なく扱い、各環境へ反映できる状態にする場面です。アプリ保守チームが実行を引き継ぎ、アーキチームは全体設計や例外判断を支援する想定の架空例です。

[引き継ぎの全体像へ戻る](README.md)

```mermaid
---
title: 共有データ構造を整合させる
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
  i_data_change@{ label: "データ変更要求", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_align_concepts@{ label: "データ概念を整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_logical_model@{ label: "論理データモデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_design_database@{ label: "DB構造へ具体化する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_physical_model@{ label: "物理データモデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_schema_change@{ label: "DB変更定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_align_application@{ label: "アプリの表現を揃える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_entity_definition@{ label: "エンティティ定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_apply_schema@{ label: "各環境の構造を揃える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  x_shared_database@{ label: "共通データベース", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_dev_team@{ label: "サブシステム開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_maintenance --- b_align_concepts
  a_maintenance --- b_design_database
  a_maintenance --- b_align_application
  a_maintenance --- b_apply_schema
  i_data_change --- b_align_concepts
  b_align_concepts --- i_logical_model
  i_logical_model --- b_design_database
  b_design_database --- i_physical_model
  b_design_database --- i_schema_change
  i_physical_model --- b_align_application
  b_align_application --- i_entity_definition
  i_schema_change --- b_apply_schema
  b_apply_schema --- x_shared_database
  b_align_concepts --- a_dev_team
  b_align_application --- a_dev_team
  b_apply_schema --- a_dev_team

  class a_dev_team,a_maintenance actor;
  class b_align_concepts,b_design_database,b_align_application,b_apply_schema business;
  class i_data_change,i_logical_model,i_physical_model,i_schema_change,i_entity_definition information;
  class x_shared_database external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

論理データモデル設計、物理データモデル設計、DDL作成、エンティティ実装、各環境へのDB差分適用を、ばらばらの操作ではなく一つの整合責任として見ています。実案件では、モデル・DDL・エンティティの正本、レビュー権限、競合や適用失敗時の判断者を確認します。
