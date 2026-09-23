# 外部IF仕様の設計観点

外部IF仕様を一度で確定せず、要件・試行・送受信証跡・外部結合テスト結果を往復しながら、次の工程が使える契約へ整える場面です。

外部IF仕様がどのように整っていくかを、一つの連携の例で示します。他の設計へ広げるルールは、ここでは決めません。

← [基本設計の分解](decomposition-catalog.md#3-%E5%9F%BA%E6%9C%AC%E8%A8%AD%E8%A8%88) / [外部結合テスト](external-integration-context.md) / [原因特定](external-integration-flow.md)

## 外部IF仕様を整える流れ

```mermaid
---
title: 外部IF仕様の設計観点
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
  i_external_interface_requirement@{ label: "外部IF要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_shape_interface@{ label: "IF設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_interface_specification@{ label: "外部IF仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_rehearse_contract@{ label: "試行", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_exchange_evidence@{ label: "送受信証跡", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_align_interface@{ label: "整合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_baseline_interface@{ label: "次へ渡せる版", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_external_test_specification@{ label: "外結仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_validate_contract@{ label: "外結テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_external_test_result@{ label: "外結結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  i_external_interface_requirement --- b_shape_interface
  b_shape_interface --- i_interface_specification
  i_interface_specification --- b_rehearse_contract
  b_rehearse_contract --- i_exchange_evidence
  i_interface_specification --- b_align_interface
  i_exchange_evidence --> b_align_interface
  b_align_interface --- b_baseline_interface
  b_baseline_interface --- i_external_test_specification
  i_external_test_specification --- b_validate_contract
  i_interface_specification --- b_validate_contract
  b_validate_contract --- i_external_test_result
  i_external_test_result --> b_align_interface

  class b_shape_interface,b_rehearse_contract,b_validate_contract,b_align_interface,b_baseline_interface business;
  class i_external_interface_requirement,i_interface_specification,i_exchange_evidence,i_external_test_specification,i_external_test_result information;

  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 設計観点の読み方

| 観点 | 根拠 | いつ見るか | 成熟の目安 | 差戻し | 次に使うところ |
| --- | --- | --- | --- | --- | --- |
| 項目・コード体系 | 外部IF要件、外部IF仕様 | IF設計・外結テスト前 | 設計中 → 次へ渡せる候補 | 不一致ならIF設計・整合へ戻る | 外結仕様 |
| 順序・再送・冪等性 | 外部IF仕様、送受信証跡、外結結果 | 試行・外結テスト | 試行で仮置き → 結果を反映した版 | 不整合なら試行・整合へ戻る | 外部結合テスト |
| 異常応答・責任境界 | 外部IF仕様、外結結果 | 外結テスト・原因特定 | いったん次へ渡せる状態にし、後続で再検討する | 所在不明なら原因特定・整合へ戻る | 外部担当・次のテスト |

この表はチェック項目の一覧ではありません。同じ`外部IF仕様`を、どの根拠から考え始め、何度見直し、どの状態で次へ渡すかを会話するための最小の読み方です。

## この図が表していること

外部IF仕様は、IF設計で書いて終わる成果物ではありません。次へ渡せる版を外結仕様として試し、送受信証跡と外結結果を整合へ戻す循環として整えます。図の矢印は、後続の証跡・結果から設計へ戻る関係だけを示しています。

## 関連

- [外部結合テスト](external-integration-context.md) — 親Context
- [原因特定](external-integration-flow.md) — 証跡から責任境界を確認するFlow
- [基本設計の分解](decomposition-catalog.md#3-%E5%9F%BA%E6%9C%AC%E8%A8%AD%E8%A8%88) — 設計側の親導線
- [Information](master-information-model.md)
