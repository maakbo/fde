# 業務要件定義の進め方

改善する業務が選ばれたら、顧客の業務責任者・担当者、実装・運用担当者とFDEが、変える範囲と達成条件を決めます。既にある現行業務と選定理由を使い、同じ聞取りを繰り返しません。

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
  %% 親: planningの業務Context。顧客とFDEの手順を展開する。
  b_step1@{ label: "目的と対象を確認する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step2@{ label: "変更案を具体化する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step3@{ label: "合格条件を決める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step4@{ label: "費用とリスクを比較", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_ready@{ label: "条件を合意できる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_next@{ label: "今回の範囲を判断する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_step1 --> b_step2
  b_step2 --> b_step3
  b_step3 --> b_step4
  b_step4 --> d_ready
  d_ready -->|はい| b_next
  d_ready -->|いいえ| b_step2
  class b_step1,b_step2,b_step3,b_step4,b_next activity;
  class d_ready decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

| 担当 | 作業 | 確認すること・残す成果 |
| --- | --- | --- |
| 顧客とFDE | 目的と対象を確認する | 変える業務、受取者、対象外 |
| FDE | 変更案を具体化する | 現行と変更後の差、必要な情報と体制 |
| 顧客とFDE | 合格条件を決める | 品質・負担・効果の基準、通常と例外 |
| FDE | 費用・効果・リスクを比較する | 見積りの前提、根拠、段階案 |
| 顧客の決定者 | 今回の範囲を判断する | 合意した条件と未決、次に進める範囲 |

顧客側の決定者・担当者と、FDE側の実装・確認・支援担当は、開始時に具体的な人へ割り当てます。FDEが案を作ることと、顧客が合意・開始を決めることを区別します。

## 判断と戻り先

対象、期待する結果、利用できる情報、責任者、許可範囲、合格条件が確認できた範囲を協働設計へ渡します。実現できない条件は黙って緩めず顧客へ返し、目的や対象が変わるなら業務理解・対象選定へ戻ります。

## システム開発での例

設計下書きの支援なら、「必要な要件を落とさず、根拠を追える下書きを返す」などを具体的な評価ケースへ落とします。作成時間が短くてもレビュー負担が増える案は、効果の見込みを再検討します。

[架空の実践例](../../examples/field-delivery/order-search/README.md)

## 作業の手順と成果物

FDEとAIエージェントは、今必要な作業の手順だけを使います。顧客は相談や具体例の確認から参加でき、全てのSkillを読む必要はありません。

- [業務改善案の比較](../../.agents/skills/redesign-process-options/SKILL.md)
- [変更後の業務設計](../../.agents/skills/design-future-work/SKILL.md)
- [現状・変更案の差分分析](../../.agents/skills/analyze-change-gaps/SKILL.md)
- [段階導入の合意形成](../../.agents/skills/agree-staged-change/SKILL.md)
- [AI利用料の見積り](../../.agents/skills/estimate-inference-cost/SKILL.md)
- [導入・運用費の見積り](../../.agents/skills/estimate-total-cost/SKILL.md)
- [導入効果の見積り](../../.agents/skills/estimate-benefit-conditions/SKILL.md)
- [投資判断の準備](../../.agents/skills/prepare-investment-decision/SKILL.md)
- [導入リスクの洗出し](../../.agents/skills/identify-adoption-risks/SKILL.md)

成果物は、次の型を既存の資料や記録にも対応させて使います。不明な項目は推測で埋めず、確認先とともに残します。

- [業務要件定義](../../templates/definition-brief.md)
- [現行から変更案と実行条件へ](../../templates/field-work/process-change-record.md)
- [総費用と効果の前提](../../templates/field-work/cost-benefit-record.md)
- [失敗と対応、運用の確認](../../templates/field-work/risk-and-operation-record.md)

[AIへ任せる仕事の判断](references/decision-foundations.md)。評価方法は[PoCの成功条件](../evaluation/workflow.md)で試行前に具体化します。

[次の業務：協働設計](../design/README.md)
