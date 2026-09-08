# 実装・単体

内部仕様をコードへ変え、単体で成立する変更として確かめる場面です。

← [システム開発](business-map.md)

## モデル

```mermaid
---
title: 実装・単体
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
  a_developer@{ label: "開発者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_dev_lead@{ label: "開発PL", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_internal_specification@{ label: "内部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_unit_test_viewpoint@{ label: "単体観点", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  b_implement_change@{ label: "実装", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_source_code@{ label: "ソースコード", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_verify_unit@{ label: "単体検証", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_unit_test_result@{ label: "単体結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_review_change@{ label: "品質確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_integrate_change@{ label: "統合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  x_dev_environment@{ label: "開発環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_static_analysis@{ label: "静的解析", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_code_review@{ label: "コードレビュー", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_scm@{ label: "構成管理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_build_artifact@{ label: "ビルド成果物", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_developer --- b_implement_change
  i_internal_specification --- b_implement_change
  b_implement_change --- x_dev_environment
  b_implement_change --- i_source_code
  i_unit_test_viewpoint --- b_verify_unit
  i_source_code --- b_verify_unit
  a_developer --- b_verify_unit
  b_verify_unit --- i_unit_test_result
  i_source_code --- b_review_change
  i_unit_test_result --- b_review_change
  b_review_change --- x_static_analysis
  b_review_change --- x_code_review
  a_dev_lead --- b_review_change
  b_review_change --- b_integrate_change
  a_developer --- b_integrate_change
  b_integrate_change --- x_scm
  b_integrate_change --- i_build_artifact

  click b_verify_unit href "https://github.com/maakbo/fde/blob/eval/waterfall-system-development-modeling/examples/waterfall-system-development/implementation-unit-flow.md" "単体検証の流れを見る"

  class a_developer,a_dev_lead actor;
  class b_implement_change,b_verify_unit,b_review_change,b_integrate_change business;
  class i_internal_specification,i_unit_test_viewpoint,i_source_code,i_unit_test_result,i_build_artifact information;
  class x_dev_environment,x_static_analysis,x_code_review,x_scm external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 図の業務

| 業務 | 何をしているか |
| --- | --- |
| **実装** | 内部仕様を、実行可能なソースコードへ変える。 |
| [**単体検証**](implementation-unit-flow.md) | 実装単位で期待どおりに動くかを確かめ、差異があれば修正へ戻す。 |
| **品質確認** | 単体結果、静的解析、他者レビューから、変更を次へ渡せる品質か確かめる。 |
| **統合** | 確認済みの変更を構成管理へ取り込み、次の結合検証で扱える版にする。 |

## この図が表していること

内部仕様と単体観点をもとに開発者が実装し、単体検証と品質確認を経て統合可能な変更へ整えます。ツールは仕事の主体ではなく、それぞれの業務を支える外部システムとして置いています。

## Master references

この図で使う Actor / Information / External System は、次のマスタで同じIDを管理しています。

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_developer` | 開発者 | 実装と単体検証を担う主体 |
| [Actor master](master-actor-map.md) | `a_dev_lead` | 開発PL | 品質確認を担う責任者 |
| [Information master](master-information-model.md) | `i_internal_specification` | 内部仕様 | 実装の入力 |
| [Information master](master-information-model.md) | `i_unit_test_viewpoint` | 単体観点 | 単体検証の観点 |
| [Information master](master-information-model.md) | `i_source_code` | ソースコード | 実装の成果・検証対象 |
| [Information master](master-information-model.md) | `i_unit_test_result` | 単体結果 | 品質確認の判断材料 |
| [Information master](master-information-model.md) | `i_build_artifact` | ビルド成果物 | 統合後に扱う成果 |
| [External-system master](master-system-map.md) | `x_dev_environment` | 開発環境 | 実装を支える環境 |
| [External-system master](master-system-map.md) | `x_static_analysis` | 静的解析 | 品質確認を支える検査 |
| [External-system master](master-system-map.md) | `x_code_review` | コードレビュー | 品質確認を支えるレビュー基盤 |
| [External-system master](master-system-map.md) | `x_scm` | 構成管理 | 統合版を管理するシステム |

## 関連

- [単体検証の流れ](implementation-unit-flow.md) →
- [Actor](master-actor-map.md)
- [Information](master-information-model.md)
- [External System](master-system-map.md)
