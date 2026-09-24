# 仕組みを実装する

設計を実行できる形へ変え、内部で確かめ、次の外部確認へ渡せる変更に整える仕事です。

← [業務システム開発](../) ／ [仕組みを設計する](../basic-design/)

```mermaid
---
title: 仕組みを実装する
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
  a_developer@{ label: "開発者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_quality_manager@{ label: "品質管理者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_infrastructure_engineer@{ label: "インフラ担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_internal_specification@{ label: "内部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_implement_change@{ label: "コードへ変える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_test_plan@{ label: "テスト計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_verify_internal@{ label: "内部で確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_test_result@{ label: "テスト結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_prepare_external_check@{ label: "外部確認へ整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  x_dev_environment@{ label: "開発環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_verification_environment@{ label: "検証環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_developer --- b_implement_change
  a_developer --- b_verify_internal
  a_quality_manager --- b_verify_internal
  a_quality_manager --- b_prepare_external_check
  a_infrastructure_engineer --- b_prepare_external_check
  i_internal_specification --- b_implement_change
  b_implement_change --- x_dev_environment
  b_implement_change --- i_test_plan
  i_test_plan --- b_verify_internal
  b_verify_internal --- i_test_result
  i_test_result --- b_prepare_external_check
  b_prepare_external_check --- x_verification_environment

  click b_verify_internal href "https://github.com/maakbo/fde/blob/main/examples/system-development/implementation/unit-flow.md" "内部で確かめる流れを見る"

  class a_developer,a_quality_manager,a_infrastructure_engineer actor;
  class b_implement_change,b_verify_internal,b_prepare_external_check business;
  class i_internal_specification,i_test_plan,i_test_result information;
  class x_dev_environment,x_verification_environment external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

設計者から受け取った内部仕様を、開発者がコードへ変えます。テスト計画と結果を使って内部の品質を確かめ、次の外部確認で扱える変更として検証環境へ渡します。

- [内部で確かめる流れ](unit-flow.md) — 条件準備から結果記録までを見る
- [外部と確かめる](../external-integration/) — 外部システムとの契約を確かめる
