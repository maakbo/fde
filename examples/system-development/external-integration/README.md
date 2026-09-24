# 外部と確かめる

得意先基幹システムとの接続、契約、異常時の責任境界を、双方が同じ証跡で確かめる仕事です。

← [業務システム開発](../) ／ [仕組みを実装する](../implementation/)

```mermaid
---
title: 外部と確かめる
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
  a_quality_manager@{ label: "品質管理者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_external_owner@{ label: "得意先側担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_external_specification@{ label: "外部仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_test_plan@{ label: "テスト計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_establish_connection@{ label: "接続を成立させる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_verify_contract@{ label: "契約を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_test_result@{ label: "テスト結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_isolate_boundary@{ label: "境界を切り分ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  x_external_integration_environment@{ label: "検証環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_customer_core@{ label: "得意先基幹システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_quality_manager --- b_establish_connection
  a_quality_manager --- b_verify_contract
  a_quality_manager --- b_isolate_boundary
  a_external_owner --- b_establish_connection
  a_external_owner --- b_verify_contract
  a_external_owner --- b_isolate_boundary
  i_external_specification --- b_establish_connection
  i_test_plan --- b_verify_contract
  b_establish_connection --- b_verify_contract
  b_establish_connection --- x_external_integration_environment
  b_verify_contract --- i_test_result
  i_test_result --- b_isolate_boundary
  b_isolate_boundary --- x_customer_core

  click b_isolate_boundary href "https://github.com/maakbo/fde/blob/main/examples/system-development/external-integration/integration-flow.md" "境界を切り分ける流れを見る"
  click b_verify_contract href "https://github.com/maakbo/fde/blob/main/examples/system-development/basic-design/interface-specification.md" "外部仕様の設計観点を見る"

  class a_quality_manager,a_external_owner actor;
  class b_establish_connection,b_verify_contract,b_isolate_boundary business;
  class i_external_specification,i_test_plan,i_test_result information;
  class x_external_integration_environment,x_customer_core external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

接続確認と契約検証は、自分たちのシステムだけを見て終わりません。得意先側担当者と同じテスト結果を読み、問題が起きたときはどちらの境界で切り分けるかを確かめます。

- [境界を切り分ける流れ](integration-flow.md) — 問題の所在を共同で確かめる
- [運用へ渡す](../deployment/) — 確認できた仕組みを本番と運用へつなぐ
