# 実装・テストの進め方

設計と合格条件を受け取り、FDEと実装担当者がコード・設定・接続を作ります。顧客は業務上の期待と利用条件を確認し、実装担当者は動作の証拠を返します。

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
  %% 親: implementationの業務Context。顧客とFDEの手順を展開する。
  b_step1@{ label: "設計と実行条件を確認する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step2@{ label: "実装する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step3@{ label: "テストする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step4@{ label: "要件と結果を照合する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_ready@{ label: "合格条件を満たす？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_next@{ label: "評価へ引き継ぐ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

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
| FDEと実装担当者 | 設計と実行条件を確認する | 対象の版、入出力、権限、期待結果 |
| 実装担当者とAI | 実装する | コード、設定、接続、実行手順 |
| 実装担当者とAI | テストする | 正常・境界・例外、停止・再開の実結果 |
| 別の確認者 | 要件と結果を照合する | 満たした条件、指摘、不足する証拠 |
| 実装担当者とFDE | 修正し再確認する | 修正版、再テスト、評価へ渡す残件 |

顧客側の決定者・担当者と、FDE側の実装・確認・支援担当は、開始時に具体的な人へ割り当てます。FDEが案を作ることと、顧客が合意・開始を決めることを区別します。

## 判断と戻り先

合格条件に対応するコードとテスト結果をレビューし、試行可能な範囲をPoC・導入評価へ渡します。コードのテスト合格だけで業務効果や本番許可を判断しません。要件の曖昧さは業務要件定義へ、方式や権限の不足は協働設計へ戻します。

## システム開発での例

受注一覧の検索機能を追加する開発チームなら、AIへ既存コードの調査、実装、テスト、指摘修正を依頼し、エンジニアが差分と実行結果を確認します。顧客の受注業務にAI製品を導入する話とは区別します。

[架空の実践例](../../examples/field-delivery/order-search/README.md)

## 作業の手順と成果物

FDEとAIエージェントは、今必要な作業の手順だけを使います。顧客は相談や具体例の確認から参加でき、全てのSkillを読む必要はありません。

- [実装への引継ぎ](../../.agents/skills/prepare-implementation-handoff/SKILL.md)
- [処理・失敗・再開の設計](../../.agents/skills/design-action-chain/SKILL.md)

成果物は、次の型を既存の資料や記録にも対応させて使います。不明な項目は推測で埋めず、確認先とともに残します。

- [データと人・AIの仕事を設計する](../../templates/field-work/implementation-handoff.md)
- [自動化ワークフロー設計](../../templates/workflow-brief.md)
- [次工程への移行判断](../../templates/delivery-review.md)

実装の指示・検証は[作業設計](../../.agents/skills/architecture-modeling/references/agent-work-design.md)と[ワークフロー設計](../../.agents/skills/workflow-design-facilitation/SKILL.md)も使います。具体的な言語や基盤の実装手順は、案件の構成に応じて補います。

[次の業務：PoC・導入評価](../evaluation/README.md)
