# 業務理解・対象選定の進め方

「どこにAIを使えるか」「まず何を変えるか」が決まっていない相談から始めます。顧客の担当者とFDEが、最近の仕事を依頼から成果の受取りまで一緒にたどります。

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
  %% 親: discoveryの業務Context。顧客とFDEの手順を展開する。
  b_step1@{ label: "最近の仕事を話す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step2@{ label: "現状と課題を整理する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step3@{ label: "具体例で訂正する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step4@{ label: "改善候補を比較する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_ready@{ label: "対象を選べる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_next@{ label: "対象と理由を決める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

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
| 顧客 | 最近の仕事を話す | 依頼、担当者、使った資料、渡した成果 |
| FDE | 現状と課題を整理する | 業務の関係、作業の流れ、待ちと手戻り |
| 顧客 | 具体例で訂正する | 実際と違う点、例外、熟練者の判断 |
| FDE | 改善候補を比較する | 業務の見直し、人・通常処理・AIの選択肢 |
| 顧客とFDE | 対象と理由を決める | 最初に変える業務、期待する変化、対象外 |

顧客側の決定者・担当者と、FDE側の実装・確認・支援担当は、開始時に具体的な人へ割り当てます。FDEが案を作ることと、顧客が合意・開始を決めることを区別します。

## 判断と戻り先

顧客が「この仕事の、この課題に取り組む」と説明でき、選定理由と不足する根拠が残れば業務要件定義へ進みます。情報が足りなければ、担当者の具体例や作業時間の確認へ戻ります。

## システム開発での例

例えば設計レビューの差戻しを減らしたい場合、まず最近の要件・設計・レビュー指摘をたどります。設計の下書きと要件照合を候補に挙げ、発生頻度、確認できる資料、誤りの影響から比較します。

[架空の実践例](../../examples/design-preparation/practice.md)

## 作業の手順と成果物

FDEとAIエージェントは、今必要な作業の手順だけを使います。顧客は相談や具体例の確認から参加でき、全てのSkillを読む必要はありません。

- [改善対象の選定](../../.agents/skills/select-improvement-target/SKILL.md)
- [業務範囲の整理](../../.agents/skills/clarify-work-grain/SKILL.md)
- [現行業務の聞取り](../../.agents/skills/walkthrough-current-case/SKILL.md)
- [暗黙の判断の聞取り](../../.agents/skills/elicit-tacit-decisions/SKILL.md)
- [手順と実態の照合](../../.agents/skills/reconcile-procedure-and-practice/SKILL.md)
- [工数・待ち時間の測定](../../.agents/skills/measure-workload-and-wait/SKILL.md)
- [作業特性の分類](../../.agents/skills/classify-task-nature/SKILL.md)
- [業務図による認識合わせ](../../.agents/skills/facilitate-process-dialogue/SKILL.md)

成果物は、次の型を既存の資料や記録にも対応させて使います。不明な項目は推測で埋めず、確認先とともに残します。

- [業務課題・改善候補の整理](../../templates/discovery-brief.md)
- [仕事・業務・作業の位置と境界](../../templates/field-work/work-grain-record.md)
- [現在の一件と暗黙の判断](../../templates/field-work/case-observation-record.md)
- [人手・処理・待ちを分けた時間観測](../../templates/field-work/work-time-record.md)

[業務分析の考え方](references/work-analysis-methods.md)

[次の業務：業務要件定義](../planning/README.md)

関係者の懸念や過去の導入経験が対象選定に影響する時は、[導入条件のすり合わせ](../../.agents/skills/clarify-adoption-conditions/SKILL.md)で具体的な確認条件へ返します。
