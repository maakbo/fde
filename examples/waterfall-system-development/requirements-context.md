# 要件を合意可能な形にする — Business Use Case Context

要件定義を、現行理解から業務要件化、システム責務化、合意までの一つの scene として見ます。

親 View: `business-map.md` / expanded node: `b_requirements`

```mermaid
---
title: 要件を合意可能な形にする
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

  b_understand_current@{ label: "現行を捉える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_shape_requirements@{ label: "業務要件化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_requirement@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_define_system@{ label: "責務を分ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_system_requirement@{ label: "システム要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_align_requirements@{ label: "要件を整合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  x_requirements_management@{ label: "要件管理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_acceptance_criteria@{ label: "受入条件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_business_user --- b_understand_current
  a_ba --- b_understand_current
  i_current_business --- b_understand_current
  b_understand_current --- b_shape_requirements
  a_ba --- b_shape_requirements
  b_shape_requirements --- i_business_requirement
  a_business_owner --- b_shape_requirements
  i_business_requirement --- b_define_system
  a_ba --- b_define_system
  b_define_system --- i_system_requirement
  i_system_requirement --- b_align_requirements
  a_ba --- b_align_requirements
  x_requirements_management --- b_align_requirements
  b_align_requirements --- a_business_owner
  b_align_requirements --- i_acceptance_criteria

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

## 読み方

業務担当が提供する現行業務を、要件担当が業務要件として構造化し、人とシステムの責務を分けてシステム要件へ変換します。業務責任者は業務要件の形成と最終整合に参加し、合意された要件から受入条件が定まります。

この Context は正確な手順を表しません。レビュー差戻しと再合意の順序は [要件合意 Flow](requirements-alignment-flow.md) で扱います。

## Master references

- Actors: `a_business_user`, `a_ba`, `a_business_owner`
- Information: `i_current_business`, `i_business_requirement`, `i_system_requirement`, `i_acceptance_criteria`
- External System: `x_requirements_management`

## あえて省いたもの

- アーキテクト、システム企画、PM、運用担当などの参加。要件定義全体では重要だが、この scene で Business backbone を読めなくするほど詰め込まない。
- 非機能・移行・運用・セキュリティ要件。次の Detailed Context 候補として分ける。
- 議事録やレビュー記録。合意そのものと保存形式を混同しないため、この View の中心から外した。

## 次の問い

「責務を分ける」は要件定義の一 Business として十分に具体か、それとも「システム化範囲を定める」「機能要件化する」「外部IF要件化する」へさらに分ける方が実務感に合うか？
