# 詳細設計

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  %% parent: ../README.md / b_detailed_design ; 人手の通常経路と工程内の修正。保留・工程外への戻りは本文。
  b_detailed_design_1@{ label: "処理を分ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_detailed_design_2@{ label: "処理を定める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_detailed_design_3@{ label: "設計を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_detailed_design_ready@{ label: "進められる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_detailed_design_4@{ label: "設計を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_detailed_design_1 --> b_detailed_design_2
  b_detailed_design_2 --> b_detailed_design_3
  b_detailed_design_3 --> d_detailed_design_ready
  d_detailed_design_ready -->|はい| b_detailed_design_4
  d_detailed_design_ready -->|要修正| b_detailed_design_1
  class b_detailed_design_1,b_detailed_design_2,b_detailed_design_3,b_detailed_design_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_detailed_design_ready decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

基本設計を、実装者が処理とデータ更新を判断できる具体的な設計へ変える。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 承認済み基本設計、外部IF仕様、開発規約。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 処理を分ける | 詳細設計担当 | 画面/API/バッチを処理単位へ分け、内部インターフェースと責務を定める | モジュール構成、内部IF仕様 |
| 処理を定める | 詳細設計担当 | 分岐、SQL、トランザクション、排他、例外、ログ、テーブル制約を記述する | 詳細設計書、DB定義 |
| 設計を確認 | 設計責任者・実装担当・テスト担当 | 基本設計との対応、正常・境界・異常系、単体・内部結合の確認観点をレビューする | レビュー記録、テスト観点 |
| 設計を渡す | 詳細設計担当 | 実装単位と依存関係、確定版、残る質問を実装担当へ説明する | 承認済み詳細設計、実装対象一覧 |

**次へ進む判断**: 設計責任者が基本設計との整合と処理の具体性を確認し、実装担当が着手可能か確かめる。

**差戻し・待ち**: 処理不明は詳細設計へ戻す。画面仕様や外部IFの変更は基本設計へ、業務要求の変更は要件定義へ戻す。

**受渡し先**: 実装担当・内部結合テスト担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。
