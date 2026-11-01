# 導入・運用改善の進め方

試行結果と残件を受け取り、顧客の業務責任者・運用担当者とFDEが、使い始める条件と支援体制を整えます。導入後も品質・利用・負担・効果を観測し、知識や仕組みを更新します。

[業務の目的と関係者](README.md) / [FDEの仕事全体](../README.md)

## 作業の流れ

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
  %% 親: operations。開始の判定と、開始後の運用改善を別の場面として扱う。
  b_prepare@{ label: "開始条件と体制を整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_practice@{ label: "作業を練習する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_start@{ label: "開始条件を満たす？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_start@{ label: "限定運用を始める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_hold@{ label: "未達を返し保留する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_share@{ label: "開始・保留を共有する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_prepare --> b_practice
  b_practice --> d_start
  d_start -->|はい| b_start
  d_start -->|いいえ| b_hold
  b_start --> b_share
  b_hold --> b_share
  class b_prepare,b_practice,b_start,b_hold,b_share activity;
  class d_start decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

開始条件を満たせば運用責任者が限定運用を始めます。未達なら確認先とともに保留を共有し、再開を決めた時に開始条件へ戻ります。

### 開始後の運用改善

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
  %% 親: operations。開始の判定と、開始後の運用改善を別の場面として扱う。
  b_observe@{ label: "利用と不具合を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_judge@{ label: "継続・更新・停止を判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_continue@{ label: "運用を続ける？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_update@{ label: "必要な更新を反映", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_return@{ label: "停止・再設計へ返す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_observe --> b_judge
  b_judge --> d_continue
  d_continue -->|はい| b_update
  b_update --> b_observe
  d_continue -->|いいえ| b_return
  class b_observe,b_judge,b_update,b_return activity;
  class d_continue decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

| 担当 | 作業 | 確認すること・残す成果 |
| --- | --- | --- |
| 顧客とFDE | 開始条件と体制を整える | 開始の決定者、利用者、支援担当、残件 |
| 利用者と支援担当 | 実際の作業で練習する | 自分で行った結果、困った点、問合せ先 |
| 運用責任者 | 限定運用を開始する | 対象、期間、監視、停止・復旧の担当 |
| 運用担当者とFDE | 利用と不具合を確認する | 品質、負担、使わない理由、費用、効果 |
| 顧客とFDE | 更新・継続・停止を判断する | 更新した知識と手順、再評価、次の改善 |

顧客側の決定者・担当者と、FDE側の実装・確認・支援担当は、開始時に具体的な人へ割り当てます。FDEが案を作ることと、顧客が合意・開始を決めることを区別します。

## 判断と戻り先

開始条件が未成立なら、未達と確認先を返して保留します。再開を決めたら開始条件の確認へ戻ります。継続・更新の場合は確認した変更を反映して観測を続け、停止の場合は定めた方法で従来手順へ戻します。

使う人と成果を受け取る人が、通常時・例外時の対応と相談先を説明できる状態にします。利用が少ない時は理由を確かめ、強制利用や対象外への自動展開をしません。知識更新は再評価へ、業務条件の変化は要件定義や対象選定へ戻します。

## システム開発での例

開発チームで設計支援を使い始めるなら、レビュー担当の時間、参照資料の更新責任、誤った下書きを使わない方法を確認します。新しい要件や開発規約が入った時は参照知識を更新し、評価ケースを再実行します。

[架空の実践例](../../examples/field-delivery/order-search/team-trial.md)

## 作業の手順と成果物

FDEとAIエージェントは、今必要な作業の手順だけを使います。顧客は相談や具体例の確認から参加でき、全てのSkillを読む必要はありません。

- [運用状況の棚卸し](../../.agents/skills/review-operating-inventory/SKILL.md)
- [技術・業務適合の再評価](../../.agents/skills/reassess-technology-fit/SKILL.md)
- [参照知識の更新・切替](../../.agents/skills/refresh-reference-release/SKILL.md)

成果物は、次の型を既存の資料や記録にも対応させて使います。不明な項目は推測で埋めず、確認先とともに残します。

- [AI導入の体制・定着計画](../../templates/team-adoption-brief.md)
- [失敗と対応、運用の確認](../../templates/field-work/risk-and-operation-record.md)
- [条件変化を受けた方式の再評価](../../templates/field-work/technology-reassessment.md)
- [次工程への移行判断](../../templates/delivery-review.md)

[チームへの導入手順](../../.agents/skills/team-adoption-facilitation/SKILL.md) / [知識の維持管理](../../.agents/skills/knowledge-stewardship/SKILL.md)
