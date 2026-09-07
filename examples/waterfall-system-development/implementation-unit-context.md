# 実装を統合可能な変更にする — Business Use Case Context

詳細設計を、レビュー可能かつ単体検証済みの変更へ変換し、構成管理へ取り込める状態にする scene です。

親 View: `business-map.md` / expanded node: `b_implementation_unit`

```mermaid
---
title: 実装を統合可能な変更にする
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

  b_implement_change@{ label: "コード化する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_source_code@{ label: "ソースコード", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_verify_unit@{ label: "単体で確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_unit_test_result@{ label: "単体結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_review_change@{ label: "変更を検証", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_integrate_change@{ label: "統合可能にする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  x_dev_environment@{ label: "開発環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_static_analysis@{ label: "静的解析", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_code_review@{ label: "コードレビュー", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_scm@{ label: "構成管理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_build_artifact@{ label: "ビルド成果物", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_developer --- b_implement_change
  i_internal_specification --- b_implement_change
  x_dev_environment --- b_implement_change
  b_implement_change --- i_source_code
  i_unit_test_viewpoint --- b_verify_unit
  i_source_code --- b_verify_unit
  a_developer --- b_verify_unit
  b_verify_unit --- i_unit_test_result
  i_source_code --- b_review_change
  i_unit_test_result --- b_review_change
  x_static_analysis --- b_review_change
  x_code_review --- b_review_change
  a_dev_lead --- b_review_change
  b_review_change --- b_integrate_change
  a_developer --- b_integrate_change
  x_scm --- b_integrate_change
  b_integrate_change --- i_build_artifact

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

## 読み方

内部仕様と単体テスト観点をもとに開発者がコード化し、単体検証と機械検査・他者レビューを通じて、次の統合検証へ渡せる変更へ整えます。コードレビューは単独の承認行為ではなく、単体結果や静的解析結果を含む変更全体の検証として扱います。

## Master references

- Actors: `a_developer`, `a_dev_lead`
- Information: `i_internal_specification`, `i_unit_test_viewpoint`, `i_source_code`, `i_unit_test_result`, `i_build_artifact`
- External Systems: `x_dev_environment`, `x_static_analysis`, `x_code_review`, `x_scm`

## 次の問い

`i_build_artifact` はこの scene の直接出力か、それとも CI/CD によるビルドを別 Business Context として切り出すべきか？
