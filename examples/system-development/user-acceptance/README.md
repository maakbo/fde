# ユーザー受入テスト

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
  %% parent: ../README.md / b_user_acceptance ; 人手の通常経路と工程内の修正。保留・工程外への戻りは本文。
  b_user_acceptance_1@{ label: "受入を準備", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_user_acceptance_2@{ label: "業務を試す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_user_acceptance_3@{ label: "受入を判定", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_user_acceptance_ready@{ label: "進められる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_user_acceptance_4@{ label: "受入を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_user_acceptance_1 --> b_user_acceptance_2
  b_user_acceptance_2 --> b_user_acceptance_3
  b_user_acceptance_3 --> d_user_acceptance_ready
  d_user_acceptance_ready -->|はい| b_user_acceptance_4
  d_user_acceptance_ready -->|要修正| b_user_acceptance_1
  class b_user_acceptance_1,b_user_acceptance_2,b_user_acceptance_3,b_user_acceptance_4 activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  class d_user_acceptance_ready decision;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

利用部門が、自分たちの業務をシステムで遂行できるか確認し、受入可否を決める。

[開発・運用の全体](../README.md) / [受渡しと変更](../handoffs.md)

**開始時に受け取るもの**: 受入対象版、要件定義時の受入条件、操作手順、システムテスト結果・残件。

| 作業 | 実行・確認する人 | 人が行うこと | 残すもの |
| --- | --- | --- | --- |
| 受入を準備 | 業務担当・業務責任者 | 代表的な担当・権限・例外を含む実務シナリオと期待結果、匿名の試験データを用意する | 受入テスト仕様・データ |
| 業務を試す | 利用部門の受入担当 | 申請、差戻し、再申請、承認、締め・会計への受渡しを手動操作し、業務として成立するか記録する | 受入結果、業務上の指摘 |
| 受入を判定 | 業務責任者・顧客IT担当 | 受入条件を照合し、不具合と追加要望を区別する。未達があれば対処と再確認を求める | 受入判定、合意済み残件 |
| 受入を渡す | 業務責任者 | 受入可否、利用開始の前提、残件の責任者と期限を導入担当へ通知する | 受入記録、利用開始条件 |

**次へ進む判断**: 業務責任者が受入を決める。開発側のテスト合格だけで顧客の受入に代えない。条件付き受入は残件・期限・責任者を明記する。

**差戻し・待ち**: 不具合は開発側で修正・再検証して受入をやり直す。追加要望は変更管理へ回し、現行の受入条件を書き換えて合格にしない。

**受渡し先**: 導入担当・運用担当。対象範囲・成果物の版・確認結果・残件を説明し、受取側が着手または継続できることを確かめます。
