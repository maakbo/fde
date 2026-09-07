# 外部連携の契約成立を確かめる — Business Use Case Context

外部結合テストを、自システムだけの試験ではなく、接続先との契約・責任境界・異常時動作を共同で確認する scene として捉えます。

親 View: `business-map.md` / expanded node: `b_external_test`

```mermaid
---
title: 外部連携の契約成立を確かめる
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
  a_tester@{ label: "テスター", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_external_system_owner@{ label: "外部担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_external_test_specification@{ label: "外結仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_connection_condition@{ label: "接続条件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  b_establish_connection@{ label: "接続を成立", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_verify_contract@{ label: "契約を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_exchange_evidence@{ label: "送受信証跡", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_isolate_boundary@{ label: "境界を切り分け", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_confirm_recovery@{ label: "復旧を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  x_external_integration_env@{ label: "外結環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_external_business_system@{ label: "外部システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_external_test_result@{ label: "外結結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_tester --- b_establish_connection
  a_external_system_owner --- b_establish_connection
  i_connection_condition --- b_establish_connection
  x_external_integration_env --- b_establish_connection
  x_external_business_system --- b_establish_connection
  i_external_test_specification --- b_verify_contract
  a_tester --- b_verify_contract
  a_external_system_owner --- b_verify_contract
  b_establish_connection --- b_verify_contract
  b_verify_contract --- i_exchange_evidence
  i_exchange_evidence --- b_isolate_boundary
  a_tester --- b_isolate_boundary
  a_external_system_owner --- b_isolate_boundary
  b_isolate_boundary --- b_confirm_recovery
  x_external_business_system --- b_confirm_recovery
  b_confirm_recovery --- i_external_test_result

  class a_tester,a_external_system_owner actor;
  class b_establish_connection,b_verify_contract,b_isolate_boundary,b_confirm_recovery business;
  class i_external_test_specification,i_connection_condition,i_exchange_evidence,i_external_test_result information;
  class x_external_integration_env,x_external_business_system external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

外部結合では、接続そのものを成立させたうえで、送受信契約と異常時動作を双方で確認します。問題が起きたときは自システム・接続基盤・相手システムの境界を証跡から共同で切り分け、修正後の復旧まで確認して結果を確定します。

## Master references

- Actors: `a_tester`, `a_external_system_owner`
- Information: `i_external_test_specification`, `i_connection_condition`, `i_exchange_evidence`, `i_external_test_result`
- External Systems: `x_external_integration_env`, `x_external_business_system`

## 次の問い

「境界を切り分ける」は外部結合テストの中核 Business として置くべきか、それとも不具合管理の横断 Business へ分離した方がモデルとして自然か？
