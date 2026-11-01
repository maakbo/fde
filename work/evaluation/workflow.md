# PoC・導入評価の進め方

小規模な試行で、品質、使われ方、業務への効果を確かめます。成功条件と評価ケースは結果を見る前に決め、顧客の担当者・受取者とFDEが、続行・修正・保留・停止を判断します。

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
  %% 親: evaluation。開始と継続の判断を作業から分け、保留・停止を可能にする。
  b_prepare@{ label: "成功条件を決める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_trial@{ label: "許可範囲で試す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_compare@{ label: "結果を照合する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_judge@{ label: "次の範囲を判断する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_retry@{ label: "修正し再試行？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fix@{ label: "原因を直す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_return@{ label: "判断と残件を返す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_prepare --> b_trial
  b_trial --> b_compare
  b_compare --> b_judge
  b_judge --> d_retry
  d_retry -->|はい| b_fix
  b_fix --> b_trial
  d_retry -->|いいえ| b_return
  class b_prepare,b_trial,b_compare,b_judge,b_fix,b_return activity;
  class d_retry decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

| 担当 | 作業 | 確認すること・残す成果 |
| --- | --- | --- |
| 顧客とFDE | 成功条件と測り方を決める | 比較対象、評価ケース、必須条件、期間と費用 |
| 担当者とFDE | 許可された範囲で試す | 実際の入力、出力、時間、失敗の記録 |
| FDEと確認者 | 結果を照合する | 品質、利用理由、全作業の負担と効果 |
| 顧客の決定者 | 次の範囲を判断する | 限定導入、再試行、保留または停止 |
| 実装担当者とFDE | 修正再試行を選んだ場合に直す | 修正内容、別条件の再試行、残る未検証 |

顧客側の決定者・担当者と、FDE側の実装・確認・支援担当は、開始時に具体的な人へ割り当てます。FDEが案を作ることと、顧客が合意・開始を決めることを区別します。

## 判断と戻り先

証拠が足りない場合は保留でき、費用やリスクから停止も選べます。再試行する場合だけ原因と条件を見直し、予算・期間の上限内で別条件も確かめます。

必須条件の未達を他の成功で相殺せず、未測定は未測定のまま返します。実装上の問題は実装・テストへ、方式の問題は協働設計へ、目的や条件の不一致は業務要件定義へ戻します。限定運用へ進む場合も、運用責任者と開始条件の確認が必要です。

## システム開発での例

下書きが速くできても、レビューや修正に同じだけ時間が増えれば改善とは判断できません。作成・確認・修正までの時間と品質を比べ、別の担当者や異なる要件でも確かめます。

[架空の実践例](../../examples/design-preparation/standard-handoff/README.md)

## 作業の手順と成果物

FDEとAIエージェントは、今必要な作業の手順だけを使います。顧客は相談や具体例の確認から参加でき、全てのSkillを読む必要はありません。

- [PoCの成功条件の設計](../../.agents/skills/design-trial-success/SKILL.md)
- [AI出力の原因分析](../../.agents/skills/diagnose-context-quality/SKILL.md)
- [出力と根拠の照合](../../.agents/skills/verify-output-evidence/SKILL.md)
- [検索・回答品質の評価](../../.agents/skills/evaluate-retrieval-evidence/SKILL.md)
- [判断知識の適用確認](../../.agents/skills/exercise-knowledge-transfer/SKILL.md)
- [試行後の判断](../../.agents/skills/decide-trial-next-step/SKILL.md)

成果物は、次の型を既存の資料や記録にも対応させて使います。不明な項目は推測で埋めず、確認先とともに残します。

- [PoC計画・評価](../../templates/ai-trial-brief.md)
- [次工程への移行判断](../../templates/delivery-review.md)
- [別の一件で知識を使い、直す](../../templates/field-work/knowledge-transfer.md)

[評価指標の考え方](references/success-measures.md) / [試行評価の手順](../../.agents/skills/ai-pilot-evaluation/SKILL.md)

[次の業務：導入・運用改善](../operations/README.md)
