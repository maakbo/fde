# 導入

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
  %% parent: ../README.md / b_deployment ; 本番開始の判断と保留。許可後は正常切替経路。異常時の切戻しは本文。
  b_deployment_1@{ label: "切替を準備", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_deployment_start@{ label: "開始できる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_deployment_hold@{ label: "保留し再計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_deployment_3@{ label: "本番へ移す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_deployment_confirm@{ label: "稼働を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_deployment_4@{ label: "運用へ渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_deployment_1 --> d_deployment_start
  d_deployment_start -->|許可| b_deployment_3
  d_deployment_start -->|不可| b_deployment_hold
  b_deployment_hold --> b_deployment_1
  b_deployment_3 --> b_deployment_confirm
  b_deployment_confirm --> b_deployment_4
  class b_deployment_1,b_deployment_hold,b_deployment_3,b_deployment_confirm,b_deployment_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_deployment_start decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

受入済みのシステムとデータを本番へ移し、利用と運用を開始できる状態にする。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 受入記録、リリース対象版、移行・切戻し計画、運用手順、利用開始条件。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 切替を準備 | 導入担当・運用担当・業務担当 | 移行リハーサル、データ照合、バックアップ、切戻し条件、連絡網、教育・操作説明を実施する | リハーサル結果、移行計画、教育記録 |
| 開始を確認 | 顧客IT担当・業務責任者・PM | 受入、残件、要員、作業時間、復旧可能性を点検し、本番作業の開始可否を決める | 本番作業の開始判断 |
| 本番へ移す | 導入担当・運用担当 | 許可された作業者が手動配置・データ移行・件数照合・疎通確認を行い、業務担当が利用可能か確認する | 本番作業記録、移行・稼働確認結果 |
| 運用へ渡す | 導入担当・運用担当 | 本番版、設定、監視・復旧手順、問合せ窓口、残件を受け渡し、運用担当が受領する | 本番構成記録、運用引継ぎ記録 |

**次へ進む判断**: 顧客IT担当と業務責任者が本番作業の開始と、移行後の利用開始をそれぞれ判断する。運用責任者が運用移管を受け入れる。

**差戻し・待ち**: 開始不可なら作業を保留する。切替中の異常は合意した条件で利用を止め、導入責任者が切戻しを指示する。復旧・原因対処後に再計画し、再度開始判断を受ける。

**受渡し先**: 利用部門・運用保守担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。

開始不可なら保留・再計画し、準備をやり直して開始判断を受けます。許可後の正常な切替経路では、稼働確認と利用開始の判断を経て運用へ渡します。切替中の異常時はこの経路を進めず、作業停止・切戻し・原因対処後に再計画します。受入と利用開始、本番切替と運用移管はそれぞれ別の判断です。
