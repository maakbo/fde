# 協働設計の進め方

合意した業務要件を、人・AI・システムの役割と動作へ具体化します。顧客の担当者、FDE、実装担当者、運用担当者が、入力から成果の確認までを一緒に確かめます。

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
  %% 親: designの業務Context。顧客とFDEの手順を展開する。
  b_step1@{ label: "担当と判断を分ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step2@{ label: "処理と情報を設計する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step3@{ label: "方式を比較する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_step4@{ label: "例外時の対応を確認する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_ready@{ label: "実装へ渡せる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_next@{ label: "設計を実装担当へ渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

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
| 顧客とFDE | 担当と判断を分ける | AIの提案、人の確定、実行できる操作 |
| FDEと実装担当者 | 処理と情報を設計する | 入出力、参照知識、接続先、起動条件 |
| FDEと実装担当者 | 方式を比較する | 通常処理・AI、モデル、単一・複数agent |
| 顧客と運用担当者 | 例外時の対応を確認する | 停止、担当への返却、継続と復旧 |
| FDE | 設計を実装担当へ渡す | 要件との対応、テスト条件、残る判断 |

顧客側の決定者・担当者と、FDE側の実装・確認・支援担当は、開始時に具体的な人へ割り当てます。FDEが案を作ることと、顧客が合意・開始を決めることを区別します。

## 判断と戻り先

入力・出力、操作権限、検証方法、停止と戻り先を実装担当が説明できる範囲を実装へ渡します。不明な接続や資料権限は確認先を残します。方式で要件を満たせない場合は業務要件定義へ戻ります。

## システム開発での例

設計下書きの支援なら、要件を読む、関連設計を参照する、下書きを保存する、担当者がレビューする、という作業を分けます。AIが下書きを作ることと、顧客が設計を承認することを別の操作として設計します。

[架空の実践例](../../examples/design-preparation/automation-practice.md)

## 作業の手順と成果物

FDEとAIエージェントは、今必要な作業の手順だけを使います。顧客は相談や具体例の確認から参加でき、全てのSkillを読む必要はありません。

### 役割・処理・方式

- [AIの役割の説明](../../.agents/skills/explain-agent-capability/SKILL.md)
- [作業目標の分解](../../.agents/skills/decompose-work-goals/SKILL.md)
- [自動化方式の比較](../../.agents/skills/compare-automation-options/SKILL.md)
- [変数・条件分岐の設計](../../.agents/skills/design-workflow-branches/SKILL.md)
- [AI出力の原因分析](../../.agents/skills/diagnose-context-quality/SKILL.md)
- [プロンプト設計](../../.agents/skills/design-task-prompt/SKILL.md)
- [AI入力の設計](../../.agents/skills/design-task-input/SKILL.md)
- [委任範囲の設計](../../.agents/skills/define-delegation-boundary/SKILL.md)
- [起動条件の設計](../../.agents/skills/design-trigger-contract/SKILL.md)
- [エージェントの役割分担](../../.agents/skills/partition-agent-roles/SKILL.md)
- [外部接続要件の整理](../../.agents/skills/prepare-connection-requirements/SKILL.md)
- [モデル候補の比較](../../.agents/skills/compare-model-options/SKILL.md)
- [リスク対応の設計](../../.agents/skills/design-risk-response/SKILL.md)

### 知識・情報・利用条件

- [判断知識の記録](../../.agents/skills/write-conditional-knowledge/SKILL.md)
- [参照資料の照合](../../.agents/skills/reconcile-knowledge-sources/SKILL.md)
- [情報処理の分担](../../.agents/skills/map-data-processing/SKILL.md)
- [資料属性の設計](../../.agents/skills/design-source-metadata/SKILL.md)
- [データ受渡しの設計](../../.agents/skills/define-data-handoff/SKILL.md)
- [検索用知識の整備](../../.agents/skills/prepare-retrieval-units/SKILL.md)
- [情報取得・記録の設計](../../.agents/skills/design-source-capture/SKILL.md)
- [法務・安全性の相談準備](../../.agents/skills/prepare-governance-review/SKILL.md)

成果物は、次の型を既存の資料や記録にも対応させて使います。不明な項目は推測で埋めず、確認先とともに残します。

- [自動化ワークフロー設計](../../templates/workflow-brief.md)
- [任せる範囲と実行役の契約](../../templates/field-work/delegation-record.md)
- [作業と手段の比較](../../templates/field-work/task-design-record.md)
- [接続の必要条件と実装への受渡し](../../templates/field-work/connection-requirements.md)

[知識の整備](references/knowledge-in-work.md) / [情報と処理](references/data-and-processing.md) / [接続方式](references/connection-options.md)

[次の業務：実装・テスト](../implementation/README.md)

[レビュー依頼の照合補助を設計した例](../../examples/design-preparation/prompt-practice.md)
