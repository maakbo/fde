# 成果の型を選ぶ

入力から今作る成果を選び、型の「必須」「条件付き」「任意」を読む。全型を一度に作らない。共通項目は[成果と受渡し](artifact-contract.md)へまとめる。

新規成果は選んだ型の見出しと表列を保つ。既存の業務様式は同義欄との対応を示して使える。時間・役割・根拠は同じID/版を参照し、重複した値を別々に更新しない。

| 成果 | 主に使う作業/進行 |
| --- | --- |
| [PoC計画・評価](../../../templates/ai-trial-brief.md) | [decide-trial-next-step](../../../.agents/skills/decide-trial-next-step/SKILL.md), [design-trial-success](../../../.agents/skills/design-trial-success/SKILL.md) |
| [業務要件定義](../../../templates/definition-brief.md) | [definition-facilitation](../../../.agents/skills/definition-facilitation/SKILL.md) |
| [次工程への移行判断](../../../templates/delivery-review.md) | [decide-trial-next-step](../../../.agents/skills/decide-trial-next-step/SKILL.md) |
| [業務課題・改善候補の整理](../../../templates/discovery-brief.md) | [discovery-facilitation](../../../.agents/skills/discovery-facilitation/SKILL.md) |
| [現在の一件と暗黙の判断](../../../templates/field-work/case-observation-record.md) | [elicit-tacit-decisions](../../../.agents/skills/elicit-tacit-decisions/SKILL.md), [reconcile-procedure-and-practice](../../../.agents/skills/reconcile-procedure-and-practice/SKILL.md), [walkthrough-current-case](../../../.agents/skills/walkthrough-current-case/SKILL.md) |
| [判断を引き継ぐ知識記録](../../../templates/field-work/conditional-knowledge.md) | [reconcile-knowledge-sources](../../../.agents/skills/reconcile-knowledge-sources/SKILL.md), [write-conditional-knowledge](../../../.agents/skills/write-conditional-knowledge/SKILL.md) |
| [接続の必要条件と実装への受渡し](../../../templates/field-work/connection-requirements.md) | [prepare-connection-requirements](../../../.agents/skills/prepare-connection-requirements/SKILL.md) |
| [渡す情報と出力の根拠](../../../templates/field-work/context-and-evidence-record.md) | [design-task-input](../../../.agents/skills/design-task-input/SKILL.md), [verify-output-evidence](../../../.agents/skills/verify-output-evidence/SKILL.md) |
| [総費用と効果の前提](../../../templates/field-work/cost-benefit-record.md) | [estimate-benefit-conditions](../../../.agents/skills/estimate-benefit-conditions/SKILL.md), [estimate-total-cost](../../../.agents/skills/estimate-total-cost/SKILL.md), [prepare-investment-decision](../../../.agents/skills/prepare-investment-decision/SKILL.md) |
| [次の処理へ渡すデータの契約](../../../templates/field-work/data-handoff-contract.md) | [define-data-handoff](../../../.agents/skills/define-data-handoff/SKILL.md) |
| [情報と処理の対応](../../../templates/field-work/data-processing-record.md) | [design-source-capture](../../../.agents/skills/design-source-capture/SKILL.md), [design-source-metadata](../../../.agents/skills/design-source-metadata/SKILL.md), [map-data-processing](../../../.agents/skills/map-data-processing/SKILL.md), [prepare-retrieval-units](../../../.agents/skills/prepare-retrieval-units/SKILL.md) |
| [任せる範囲と実行役の契約](../../../templates/field-work/delegation-record.md) | [compare-automation-options](../../../.agents/skills/compare-automation-options/SKILL.md), [define-delegation-boundary](../../../.agents/skills/define-delegation-boundary/SKILL.md), [partition-agent-roles](../../../.agents/skills/partition-agent-roles/SKILL.md) |
| [データと人・AIの仕事を設計する](../../../templates/field-work/implementation-handoff.md) | [prepare-implementation-handoff](../../../.agents/skills/prepare-implementation-handoff/SKILL.md) |
| [推論費用の前提と計算](../../../templates/field-work/inference-cost-record.md) | [estimate-inference-cost](../../../.agents/skills/estimate-inference-cost/SKILL.md) |
| [別の一件で知識を使い、直す](../../../templates/field-work/knowledge-transfer.md) | [exercise-knowledge-transfer](../../../.agents/skills/exercise-knowledge-transfer/SKILL.md) |
| [現行から変更案と実行条件へ](../../../templates/field-work/process-change-record.md) | [agree-staged-change](../../../.agents/skills/agree-staged-change/SKILL.md), [analyze-change-gaps](../../../.agents/skills/analyze-change-gaps/SKILL.md), [design-future-work](../../../.agents/skills/design-future-work/SKILL.md), [redesign-process-options](../../../.agents/skills/redesign-process-options/SKILL.md) |
| [図を返し、具体例で訂正する](../../../templates/field-work/process-dialogue-record.md) | [facilitate-process-dialogue](../../../.agents/skills/facilitate-process-dialogue/SKILL.md) |
| [失敗と対応、運用の確認](../../../templates/field-work/risk-and-operation-record.md) | [design-risk-response](../../../.agents/skills/design-risk-response/SKILL.md), [identify-adoption-risks](../../../.agents/skills/identify-adoption-risks/SKILL.md), [prepare-governance-review](../../../.agents/skills/prepare-governance-review/SKILL.md), [review-operating-inventory](../../../.agents/skills/review-operating-inventory/SKILL.md) |
| [作業と手段の比較](../../../templates/field-work/task-design-record.md) | [classify-task-nature](../../../.agents/skills/classify-task-nature/SKILL.md), [compare-model-options](../../../.agents/skills/compare-model-options/SKILL.md) |
| [条件変化を受けた方式の再評価](../../../templates/field-work/technology-reassessment.md) | [reassess-technology-fit](../../../.agents/skills/reassess-technology-fit/SKILL.md) |
| [開始から受渡しまでの起動契約](../../../templates/field-work/trigger-contract.md) | [design-trigger-contract](../../../.agents/skills/design-trigger-contract/SKILL.md) |
| [仕事・業務・作業の位置と境界](../../../templates/field-work/work-grain-record.md) | [clarify-work-grain](../../../.agents/skills/clarify-work-grain/SKILL.md), [decompose-work-goals](../../../.agents/skills/decompose-work-goals/SKILL.md) |
| [人手・処理・待ちを分けた時間観測](../../../templates/field-work/work-time-record.md) | [measure-workload-and-wait](../../../.agents/skills/measure-workload-and-wait/SKILL.md) |
| [知識を使い、更新するための記録](../../../templates/knowledge-use-brief.md) | [evaluate-retrieval-evidence](../../../.agents/skills/evaluate-retrieval-evidence/SKILL.md), [refresh-reference-release](../../../.agents/skills/refresh-reference-release/SKILL.md) |
| [AI導入の体制・定着計画](../../../templates/team-adoption-brief.md) | [team-adoption-facilitation](../../../.agents/skills/team-adoption-facilitation/SKILL.md) |
| [自動化ワークフロー設計](../../../templates/workflow-brief.md) | [design-action-chain](../../../.agents/skills/design-action-chain/SKILL.md) |

この一覧の26型は記入区分を確認した範囲。型の分類と、別担当が実際に使えること、現場で効果が出ることは別に確認する。受渡しの段階判断は既存の成果を参照し、試行で不足が見つかれば該当する型/Skillへ戻して直す。
