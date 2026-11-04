# 運用・保守

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
  %% parent: ../README.md / b_operations ; 一巡の確認と次当番への引継ぎ。未完は継続担当を手配して状態を保持する。
  b_operations_1@{ label: "稼働を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_operations_2@{ label: "受付を整理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_operations_3@{ label: "対処を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_operations_complete@{ label: "対応は完了？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_operations_continue@{ label: "継続を手配", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_operations_4@{ label: "結果を共有", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_operations_1 --> b_operations_2
  b_operations_2 --> b_operations_3
  b_operations_3 --> d_operations_complete
  d_operations_complete -->|完了| b_operations_4
  d_operations_complete -->|未完| b_operations_continue
  b_operations_continue --> b_operations_4
  class b_operations_1,b_operations_2,b_operations_3,b_operations_continue,b_operations_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_operations_complete decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

稼働状況を確認し、問合せ・障害・変更へ対応して業務利用を維持する。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 本番構成・引継ぎ記録、監視・復旧手順、残件、利用者の問合せ。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 稼働を確認 | 運用担当 | 定時に稼働・ログ・容量・処理結果を確認し、定めたバックアップやアカウント作業を手動で行う | 運用日誌、点検・作業結果 |
| 受付を整理 | 運用担当・業務担当 | 問合せ、監視で見つけた異常、変更要望を記録し、影響と緊急度、担当を判断する | 問合せ・障害・変更票 |
| 対処を確認 | 保守担当・運用責任者・業務担当 | 手順内の対処、復旧、原因調査を行い、業務の回復を確認する。変更が必要なら別途承認を受ける | 対応記録、復旧確認、変更依頼 |
| 継続を手配 | 運用責任者・保守担当 | 未復旧・改修待ちならエスカレーションし、次の担当・期限・暫定対処を手配する | 未完の状況、継続担当・期限 |
| 結果を共有 | 運用担当・保守担当 | 依頼者へ結果を伝え、未完は担当・期限付きで継続し、手順・構成を更新する | 完了または継続の記録、更新した手順 |

**次へ進む判断**: 運用責任者が手順内の対処と復旧、業務担当が業務回復を確認する。仕様変更・追加費用・停止を伴う作業は顧客IT担当や業務責任者の承認を受ける。

**差戻し・待ち**: 未復旧は障害対応を継続・エスカレーションする。改修は変更管理から必要な要件・設計・テスト・導入へ戻す。日次点検は翌稼働日も繰り返す。

**受渡し先**: 利用部門・次の運用当番・保守担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。

通常の点検から対応記録を次の当番へ渡す一巡です。受付がなければ定時点検の結果を共有します。障害継続や改修待ちは完了へ変更せず、未完のまま次の担当へ渡します。
