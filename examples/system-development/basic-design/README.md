# 基本設計

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
  %% parent: ../README.md / b_basic_design ; 人手の通常経路と工程内の修正。保留・工程外への戻りは本文。
  b_basic_design_1@{ label: "仕様を描く", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_basic_design_2@{ label: "構成を設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_basic_design_3@{ label: "設計を照合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_basic_design_ready@{ label: "進められる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_basic_design_4@{ label: "設計を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_basic_design_1 --> b_basic_design_2
  b_basic_design_2 --> b_basic_design_3
  b_basic_design_3 --> d_basic_design_ready
  d_basic_design_ready -->|はい| b_basic_design_4
  d_basic_design_ready -->|要修正| b_basic_design_1
  class b_basic_design_1,b_basic_design_2,b_basic_design_3,b_basic_design_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_basic_design_ready decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

承認済み要件を、利用者と外部システムから見える振る舞いと構成へ変える。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 承認済み要件、受入条件、現行業務・会計連携資料。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 仕様を描く | 設計担当・業務担当 | 画面遷移、画面モック、項目・入力チェック、帳票、権限と業務上の例外を定める | 画面・帳票・機能仕様 |
| 構成を設計 | 設計担当・顧客IT担当・運用担当 | Web/AP/DB構成、データモデル、会計連携の項目・時機・エラー、認証、監視・移行方式を定める | 基本設計書、外部IF仕様、運用・移行方針 |
| 設計を照合 | 設計責任者・業務担当・外部連携担当 | 要件との対応、画面操作、品質条件の実現方法とシステムテスト観点をレビューする | 要件対応表、設計レビュー記録 |
| 設計を渡す | 設計担当 | 承認版を詳細設計・テスト・運用担当へ説明し、用語や境界の疑問を解消する | 承認済み基本設計、確認事項 |

**次へ進む判断**: 業務責任者が利用者に見える仕様、顧客IT担当が構成・品質条件、設計責任者が技術的整合を確認する。外部IFは相手側担当とも合意する。

**差戻し・待ち**: 設計の不足は仕様・構成の作成へ戻す。要求自体を変える必要があれば要件定義へ変更依頼を出す。

**受渡し先**: 詳細設計担当・テスト担当・運用担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。
