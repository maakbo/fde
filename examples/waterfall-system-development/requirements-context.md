# 要件定義

業務の期待を、人とシステムの責務が分かる要件へ整える場面です。

← [システム開発](business-map.md)

## モデル

```mermaid
---
title: 要件定義
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

  b_understand_current@{ label: "現行理解", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_shape_requirements@{ label: "要件化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_requirement@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_define_system@{ label: "責務設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
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
  b_shape_requirements --- a_business_owner
  i_business_requirement --- b_define_system
  a_ba --- b_define_system
  b_define_system --- i_system_requirement
  i_system_requirement --- b_align_requirements
  a_ba --- b_align_requirements
  b_align_requirements --- x_requirements_management
  b_align_requirements --- a_business_owner
  b_align_requirements --- i_acceptance_criteria

  click b_align_requirements href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/requirements-alignment-flow.md" "要件合意の流れを見る"

  class a_business_user,a_ba,a_business_owner actor;
  class b_understand_current,b_shape_requirements,b_define_system,b_align_requirements business;
  class i_current_business,i_business_requirement,i_system_requirement,i_acceptance_criteria information;
  class x_requirements_management external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 図の業務

| 業務 | 何をしているか |
| --- | --- |
| **現行理解** | 現在の業務・ルール・例外・制約を、関係者が同じ前提で話せる状態にする。 |
| **要件化** | 業務で実現したい変化を、業務要件として整理する。 |
| **責務設計** | 人が担うこととシステムが担うことを分け、システム要件へ落とす。 |
| [**要件合意**](requirements-alignment-flow.md) | 抜けや矛盾を解き、受入条件まで含めて合意できる要件にする。 |

## この図が表していること

業務担当が提供する現行業務を、要件担当が業務要件として構造化します。そのうえで人とシステムの責務を分け、業務責任者と要件を合意します。

線は厳密な手順ではなく、この場面を成立させる関係です。差戻しや再確認の順序は [要件合意の流れ](requirements-alignment-flow.md) で見ます。

## Master references

この図で使う Actor / Information / External System は、次のマスタで同じIDを管理しています。

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_business_user` | 業務担当 | 現行業務を提供する主体 |
| [Actor master](master-actor-map.md) | `a_ba` | 要件担当 | 要件を構造化する主体 |
| [Actor master](master-actor-map.md) | `a_business_owner` | 業務責任者 | 要件を合意する責任者 |
| [Information master](master-information-model.md) | `i_current_business` | 現行業務 | 要件化の入力 |
| [Information master](master-information-model.md) | `i_business_requirement` | 業務要件 | 責務設計の入力・成果 |
| [Information master](master-information-model.md) | `i_system_requirement` | システム要件 | 責務設計の成果 |
| [Information master](master-information-model.md) | `i_acceptance_criteria` | 受入条件 | 合意の判断材料 |
| [External-system master](master-system-map.md) | `x_requirements_management` | 要件管理 | 要件の追跡と状態管理を支えるシステム |

## 関連

- [要件合意の流れ](requirements-alignment-flow.md) →
- [Actor](master-actor-map.md)
- [Information](master-information-model.md)
- [External System](master-system-map.md)
