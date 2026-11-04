# 外部結合テスト

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
  %% parent: ../README.md / b_external_integration ; 人手の通常経路と工程内の修正。保留・工程外への戻りは本文。
  b_external_integration_1@{ label: "接続を調整", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_external_integration_2@{ label: "外部と通す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_external_integration_3@{ label: "双方で照合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_external_integration_ready@{ label: "進められる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_external_integration_4@{ label: "連携版を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_external_integration_1 --> b_external_integration_2
  b_external_integration_2 --> b_external_integration_3
  b_external_integration_3 --> d_external_integration_ready
  d_external_integration_ready -->|はい| b_external_integration_4
  d_external_integration_ready -->|要修正| b_external_integration_1
  class b_external_integration_1,b_external_integration_2,b_external_integration_3,b_external_integration_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_external_integration_ready decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

境界の外にある会計システムと、合意したデータを正しく受け渡せるか確認する。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 内部結合済み版、外部IF仕様、相手側の検証環境・接続許可・日程。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 接続を調整 | 外部連携担当・テスト担当・相手側担当 | 両側の版、接続先、認証、テストデータ、送受信時刻、復旧手順を合わせる | 外部結合テスト仕様、実施日程 |
| 外部と通す | テスト担当・相手側担当 | 送受信、項目・コード変換、認証失敗、タイムアウト、再送・重複時の結果を両側で手動確認する | 双方の実行結果・ログ、不具合票 |
| 双方で照合 | テスト責任者・外部連携担当・相手側担当 | 送信件数と受信・反映結果、異常からの復旧を照合し、修正後に再確認する | 外部結合報告、相手側確認記録 |
| 連携版を渡す | テスト担当 | 確認した接続・版・条件と残件をシステムテスト担当へ渡す | 外部結合済み版、連携結果一式 |

**次へ進む判断**: テスト責任者と相手側担当が双方の結果を確認し、顧客IT担当・PMが残件と次工程移行を判断する。

**差戻し・待ち**: 相手側が使えなければ日程を再調整し待つ。スタブ成功を外部結合の合格にしない。不良は責任側へ戻し、両側で再確認する。

**受渡し先**: システムテスト担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。
