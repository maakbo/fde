# 要件定義

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
  %% parent: ../README.md / b_requirements ; 人手の通常経路と工程内の修正。保留・工程外への戻りは本文。
  b_requirements_1@{ label: "業務を聞く", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_requirements_2@{ label: "要件を整理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_requirements_3@{ label: "条件を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_requirements_ready@{ label: "進められる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_requirements_4@{ label: "要件を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_requirements_1 --> b_requirements_2
  b_requirements_2 --> b_requirements_3
  b_requirements_3 --> d_requirements_ready
  d_requirements_ready -->|はい| b_requirements_4
  d_requirements_ready -->|要修正| b_requirements_1
  class b_requirements_1,b_requirements_2,b_requirements_3,b_requirements_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_requirements_ready decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

顧客の業務と制約を、開発・受入で確認できる要求へまとめる。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 開発依頼、現行の申請書・業務規程、利用部門の要望、予算・希望時期。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 業務を聞く | 業務担当・要件担当 | 申請者・承認者の通常例、取消・差戻し、月次締め、部門差を聞き、現行業務を整理する | 業務フロー、用語・課題一覧 |
| 要件を整理 | 要件担当・顧客IT担当 | 対象範囲、利用者・権限、機能、データ、会計連携、性能・可用性・セキュリティ・運用条件を記述する | 要件定義書、対象外、未決一覧 |
| 条件を確認 | 業務責任者・要件担当・テスト責任者 | 業務シナリオごとの期待結果と受入条件を照合し、優先順位と未決の扱いを決める | 受入条件、レビュー記録 |
| 要件を渡す | 要件担当・顧客IT担当 | 承認版と決定理由を説明し、基本設計担当が入力を受け取ったことを確かめる | 承認済み要件、受渡し記録 |

**次へ進む判断**: 業務責任者が業務範囲と受入条件、顧客IT担当が技術・運用制約、PMが計画への反映を確認する。

**差戻し・待ち**: 不足は業務担当への聞取りへ戻す。予算・範囲の折合いがつかなければPMと業務責任者が保留し、設計へ未承認要件を渡さない。

**受渡し先**: 基本設計担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。
