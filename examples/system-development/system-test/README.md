# システムテスト

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
  %% parent: ../README.md / b_system_test ; 人手の通常経路と工程内の修正。保留・工程外への戻りは本文。
  b_system_test_1@{ label: "総合を準備", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_system_test_2@{ label: "全体を試す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_system_test_3@{ label: "要件と照合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_system_test_ready@{ label: "進められる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_system_test_4@{ label: "検証版を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_system_test_1 --> b_system_test_2
  b_system_test_2 --> b_system_test_3
  b_system_test_3 --> d_system_test_ready
  d_system_test_ready -->|はい| b_system_test_4
  d_system_test_ready -->|要修正| b_system_test_1
  class b_system_test_1,b_system_test_2,b_system_test_3,b_system_test_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_system_test_ready decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

完成したシステム全体が、機能・品質・運用の要件を満たすか確認する。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 外部結合済み版、要件・基本設計、テスト計画、運用・移行手順案。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 総合を準備 | テスト担当・運用担当 | 要件から業務横断シナリオ、権限、性能、セキュリティ、障害復旧・移行の項目とデータを作る | システムテスト仕様、要件対応表 |
| 全体を試す | テスト担当・運用担当 | 申請から承認・会計連携まで操作し、応答・同時利用、権限拒否、バックアップ復元などを手動で実行・測定する | 実行結果、測定記録、不具合票 |
| 要件と照合 | テスト責任者・顧客IT担当 | 要件ごとの証跡、修正後の回帰、未達・未実施を照合する。必要な負荷を手動で再現できなければ未検証とする | システムテスト報告、残件と制約 |
| 検証版を渡す | テスト担当 | 受入用の版、手順、確認済み範囲と残件を利用部門へ説明する | 受入対象版、操作手順、試験結果 |

**次へ進む判断**: テスト責任者が要件への適合を確認し、顧客IT担当・PMが未達の扱いと受入へ進める条件を判断する。

**差戻し・待ち**: 不適合は原因の要件・設計・実装へ戻し、影響に応じた単体から総合までの再テストを行う。測れない条件は合格とせず残件にする。

**受渡し先**: 利用部門の受入担当・業務責任者。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。
