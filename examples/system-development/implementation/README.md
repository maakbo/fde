# 実装・単体テスト

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
  %% parent: ../README.md / b_implementation ; 人手の通常経路と工程内の修正。保留・工程外への戻りは本文。
  b_implementation_1@{ label: "コードを書く", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implementation_2@{ label: "単体を試す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implementation_3@{ label: "コードを確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_implementation_ready@{ label: "進められる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implementation_4@{ label: "単体を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_implementation_1 --> b_implementation_2
  b_implementation_2 --> b_implementation_3
  b_implementation_3 --> d_implementation_ready
  d_implementation_ready -->|はい| b_implementation_4
  d_implementation_ready -->|要修正| b_implementation_1
  class b_implementation_1,b_implementation_2,b_implementation_3,b_implementation_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_implementation_ready decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

詳細設計どおりにコードを作成し、処理単位の振る舞いを確認する。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 承認済み詳細設計、DB定義、開発規約、単体テスト観点。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| コードを書く | 実装担当 | 設計を読み、ソースと設定を手で作成し、コンパイル・起動する | ソースコード、設定、ビルド結果 |
| 単体を試す | 実装担当 | 仕様からテスト項目・入力・期待値を作り、処理単位を手動実行して正常・境界・異常を照合する | 単体テスト仕様・結果・証跡 |
| コードを確認 | 別の開発担当・開発責任者 | コード、設計との対応、テスト期待値と証跡を読み、修正漏れを確認する | コードレビュー記録、指摘対応 |
| 単体を渡す | 実装担当 | 対象コードの版、設定、ビルド手順、単体結果、既知の残件を引き渡す | 単体確認済みコード一式、版一覧 |

**次へ進む判断**: 開発責任者がレビューと単体テストの完了、重大な未解決不具合がないことを確認する。

**差戻し・待ち**: 実装不良はコードへ戻して再テストする。仕様の曖昧さは設計担当へ質問し、設計承認前に独断で仕様を追加しない。

**受渡し先**: 内部結合テスト担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。
