# 内部結合テスト

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
  %% parent: ../README.md / b_internal_integration ; 人手の通常経路と工程内の修正。保留・工程外への戻りは本文。
  b_internal_integration_1@{ label: "結合を準備", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_internal_integration_2@{ label: "内部を通す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_internal_integration_3@{ label: "結果を照合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_internal_integration_ready@{ label: "進められる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_internal_integration_4@{ label: "結合版を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_internal_integration_1 --> b_internal_integration_2
  b_internal_integration_2 --> b_internal_integration_3
  b_internal_integration_3 --> d_internal_integration_ready
  d_internal_integration_ready -->|はい| b_internal_integration_4
  d_internal_integration_ready -->|要修正| b_internal_integration_1
  class b_internal_integration_1,b_internal_integration_2,b_internal_integration_3,b_internal_integration_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_internal_integration_ready decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

開発対象のWeb・AP・DB・バッチを組み合わせ、内部の受渡しを確認する。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 単体確認済みコード、基本・詳細設計、内部IF仕様、テスト環境。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 結合を準備 | テスト担当・実装担当 | 対象版を手動配置し、内部結合の項目・期待値・データを用意する。外部会計はスタブを用いる | 内部結合テスト仕様、環境・データ |
| 内部を通す | テスト担当 | 画面からDBまでの更新、内部API、バッチ、権限・排他・例外の連動を手動で試す | 実行結果・証跡、不具合票 |
| 結果を照合 | テスト責任者・開発責任者 | 仕様と結果を照合し、不具合修正後の再テストと関連箇所の回帰結果を確認する | 内部結合報告、残件一覧 |
| 結合版を渡す | 開発責任者 | 統合済み版、環境条件、確認範囲と未確認範囲を外部結合担当へ渡す | 内部結合済みビルド、結果一式 |

**次へ進む判断**: テスト責任者が計画した内部接続と異常系の結果を確認し、PMが残件の扱いと次工程への移行を承認する。

**差戻し・待ち**: 不具合は担当する設計・実装へ戻す。修正後は単体、該当結合、影響範囲の回帰を再実行する。

**受渡し先**: 外部結合テスト担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。
