# 外部結合テスト

外部システムとの接続・契約・異常時の責任境界が成立するかを、双方で確かめる場面です。

← [システム開発](business-map.md)

## モデル

```mermaid
---
title: 外部結合テスト
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

  b_establish_connection@{ label: "接続確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_verify_contract@{ label: "契約検証", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_exchange_evidence@{ label: "送受信証跡", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_isolate_boundary@{ label: "原因特定", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_confirm_recovery@{ label: "復旧確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  x_external_integration_env@{ label: "外結環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_external_business_system@{ label: "外部システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_external_test_result@{ label: "外結結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_tester --- b_establish_connection
  a_external_system_owner --- b_establish_connection
  i_connection_condition --- b_establish_connection
  b_establish_connection --- x_external_integration_env
  b_establish_connection --- x_external_business_system
  i_external_test_specification --- b_verify_contract
  a_tester --- b_verify_contract
  a_external_system_owner --- b_verify_contract
  b_establish_connection --- b_verify_contract
  b_verify_contract --- i_exchange_evidence
  i_exchange_evidence --- b_isolate_boundary
  a_tester --- b_isolate_boundary
  a_external_system_owner --- b_isolate_boundary
  b_isolate_boundary --- b_confirm_recovery
  b_confirm_recovery --- x_external_business_system
  b_confirm_recovery --- i_external_test_result

  click b_isolate_boundary href "https://github.com/maakbo/fde/blob/eval/waterfall-system-development-modeling/examples/waterfall-system-development/external-integration-flow.md" "原因特定の流れを見る"
  click b_verify_contract href "https://github.com/maakbo/fde/blob/eval/waterfall-system-development-modeling/examples/waterfall-system-development/interface-specification-detail.md" "外部IF仕様の設計観点を見る"

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

## 図の業務

| 業務 | 何をしているか |
| --- | --- |
| **接続確認** | ネットワーク・認証・基本疎通を揃え、双方が試験できる状態にする。 |
| [**契約検証**](interface-specification-detail.md) | データ、順序、タイミング、異常応答が取り決めどおりか確かめる。 |
| [**原因特定**](external-integration-flow.md) | 問題が起きたとき、双方の証跡からどの責任境界に原因があるか突き止める。 |
| **復旧確認** | 修正後に再接続し、連携とデータ整合が回復したことを確かめる。 |

## この図が表していること

外部結合は、自システムだけの試験ではありません。外部担当と同じ証跡を見ながら接続条件と連携契約を確かめ、問題時には責任境界を共同で切り分けます。

## Master references

この図で使う Actor / Information / External System は、次のマスタで同じIDを管理しています。

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_tester` | テスター | 外部結合を検証する主体 |
| [Actor master](master-actor-map.md) | `a_external_system_owner` | 外部担当 | 接続先を代表する主体 |
| [Information master](master-information-model.md) | `i_external_test_specification` | 外結仕様 | 契約検証の入力 |
| [Information master](master-information-model.md) | `i_connection_condition` | 接続条件 | 接続確認の入力 |
| [Information master](master-information-model.md) | `i_exchange_evidence` | 送受信証跡 | 原因特定の判断材料 |
| [Information master](master-information-model.md) | `i_external_test_result` | 外結結果 | 外部結合の成果 |
| [External-system master](master-system-map.md) | `x_external_integration_env` | 外結環境 | 接続確認を行う環境 |
| [External-system master](master-system-map.md) | `x_external_business_system` | 外部システム | 契約の相手となるシステム |

## 関連

- [原因特定の流れ](external-integration-flow.md) →
- [外部IF仕様の設計観点](interface-specification-detail.md) →
- [Actor](master-actor-map.md)
- [Information](master-information-model.md)
- [External System](master-system-map.md)
