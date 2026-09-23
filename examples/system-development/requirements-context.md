# システム開発業務の要件定義

システム開発業務で、業務の期待を人と対象システムの責務が分かる要件へ整える
syntheticなBusiness Contextです。実案件の標準や特定製品の要件を確定するものではありません。

← [システム開発業務](README.md) ／ [業務マップ](business-map.md)

## モデル

```mermaid
---
title: システム開発業務の要件定義
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
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  a_business_user@{ label: "業務担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_ba@{ label: "要件担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_current_business@{ label: "現行業務", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_external_business_system@{ label: "外部システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  b_understand_current@{ label: "現行業務理解", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_shape_requirements@{ label: "要件化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_requirement@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_external_specification@{ label: "外部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_define_system@{ label: "責務設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_external_interface_requirement@{ label: "外部IF要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_align_requirements@{ label: "要件合意", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  x_requirements_management@{ label: "要件管理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_acceptance_criteria@{ label: "受入条件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_business_user --- b_understand_current
  a_ba --- b_understand_current
  i_current_business --- b_understand_current
  b_understand_current --- b_shape_requirements
  a_ba --- b_shape_requirements
  b_shape_requirements --- i_business_requirement
  b_shape_requirements --- i_external_specification
  i_external_specification --- b_define_system
  x_external_business_system --- b_define_system
  b_shape_requirements --- a_business_owner
  i_business_requirement --- b_define_system
  a_ba --- b_define_system
  b_define_system --- i_system_requirement
  b_define_system --- i_external_interface_requirement
  i_system_requirement --- b_align_requirements
  i_external_interface_requirement --- b_align_requirements
  a_ba --- b_align_requirements
  b_align_requirements --- x_requirements_management
  b_align_requirements --- a_business_owner
  b_align_requirements --- i_acceptance_criteria

  click b_align_requirements href "https://github.com/maakbo/fde/blob/main/examples/system-development/requirements-alignment-flow.md" "要件合意の流れを見る"

  class a_business_user,a_ba,a_business_owner actor;
  class b_understand_current,b_shape_requirements,b_define_system,b_align_requirements business;
  class i_current_business,i_business_requirement,i_external_specification,i_system_requirement,i_external_interface_requirement,i_acceptance_criteria information;
  class x_requirements_management,x_external_business_system external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 図の業務

| 業務 | 何をしているか |
| --- | --- |
| **現行業務理解** | 現行業務と例外を、関係者が同じ前提で話せる状態にする。 |
| **要件化** | 実現したい業務の変化を、業務要件として整理する。 |
| **責務設計** | 人が担うことと対象システムが担うことを分け、システム要件へ落とす。 |
| [**要件合意**](requirements-alignment-flow.md) | 外部仕様・外部IF・受入条件の抜けや矛盾を解き、合意できる要件にする。 |

## この図が表していること

業務担当が現行業務と業務データを提供します。要件担当は
外部仕様・外部IFを含む業務要件を構造化し、人と対象システムの責務を分け、
業務責任者と受入条件まで合意します。

線は厳密な手順ではなく、この場面を成立させる関係です。差戻しや再確認の順序は
[要件合意の流れ](requirements-alignment-flow.md) で見ます。

## 上位要求とのtrace

このContextでは、Requirement Modelで置いた価値を、要件定義で扱えるInformationへ具体化します。

| 上位の重要要求 | このContextで見るInformation | 具体化の焦点 |
| --- | --- | --- |
| 業務で必要な結果を得る | `i_external_specification` / `i_system_requirement` / `i_acceptance_criteria` | 外部仕様と受入可能性 |
| 同じ結果を再現する | `i_external_specification` / `i_system_requirement` / `i_acceptance_criteria` | 入力、期待結果、検証条件 |
| 安全に業務を続ける | `i_external_specification` / `i_external_interface_requirement` / `i_acceptance_criteria` | 保管・取得境界、外部連携、確認条件 |
| 安全に業務を続ける | `i_system_requirement` / `i_external_interface_requirement` / `i_acceptance_criteria` | 責務境界、異常時、運用上の判断 |

要求モデルの価値と下位Informationの対応はこのsampleでのtrace候補です。詳細な成果物要件や
保管方式を実案件の事実として確定するものではありません。

## Master references

この図で使う Actor / Information / External System は、次のマスタで同じIDを管理しています。

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_business_user` | 業務担当 | 現行業務を提供する主体 |
| [Actor master](master-actor-map.md) | `a_ba` | 要件担当 | 要件を構造化する主体 |
| [Actor master](master-actor-map.md) | `a_business_owner` | 業務責任者 | 要件を合意する責任者 |
| [Information master](master-information-model.md) | `i_current_business` | 現行業務 | 要件化の入力 |
| [Information master](master-information-model.md) | `i_business_requirement` | 業務要件 | 責務設計の入力・成果 |
| [Information master](master-information-model.md) | `i_external_specification` | 外部仕様 | 利用者・外部システムから見た振る舞い |
| [Information master](master-information-model.md) | `i_system_requirement` | システム要件 | 責務設計の成果 |
| [Information master](master-information-model.md) | `i_external_interface_requirement` | 外部IF要件 | 業務データ源との境界条件 |
| [Information master](master-information-model.md) | `i_acceptance_criteria` | 受入条件 | 合意の判断材料 |
| [External-system master](master-system-map.md) | `x_requirements_management` | 要件管理 | 要件の追跡と状態管理を支えるシステム |
| [External-system master](master-system-map.md) | `x_external_business_system` | 外部システム | 業務データ源との境界を確認する相手 |

## 関連

- [要件合意の流れ](requirements-alignment-flow.md) →
- [Actor](master-actor-map.md)
- [Information](master-information-model.md)
- [External System](master-system-map.md)
