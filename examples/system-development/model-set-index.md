# システム開発業務 — Model set index

この索引は、reader-facing rootから必要な業務へ降りる親子関係を記録します。13工程は固定標準ではなく、業務を話すための候補です。

## View map

| View | 役割 | Focus | Parent / expanded node | Child Views |
| --- | --- | --- | --- | --- |
| [システム開発業務](README.md) | Overview | 主題、目的、主要Actor、業務、情報 | — | [業務マップ](business-map.md) |
| [業務マップ](business-map.md) | Business Map | 見積から導入までの候補 | README.md / b_system_development | [要件定義](requirements-context.md), [実装・単体](implementation-unit-context.md), [外部結合](external-integration-context.md), [導入](deployment-context.md) |
| [要件定義](requirements-context.md) | Business Context | 業務要件とシステム要件の境界 | business-map.md / b_requirements | [要件合意](requirements-alignment-flow.md) |
| [要件合意](requirements-alignment-flow.md) | Business Flow | 差異解消と再確認 | requirements-context.md / b_align_requirements | — |
| [実装・単体](implementation-unit-context.md) | Business Context | 実装、単体検証、品質確認 | business-map.md / b_implementation_unit | [単体検証](implementation-unit-flow.md) |
| [単体検証](implementation-unit-flow.md) | Business Flow | 失敗から修正へ戻るループ | implementation-unit-context.md / b_verify_unit | — |
| [外部結合](external-integration-context.md) | Business Context | 接続、契約、責任境界の確認 | business-map.md / b_external_test | [原因特定](external-integration-flow.md) |
| [原因特定](external-integration-flow.md) | Business Flow | 証跡照合と担当確定 | external-integration-context.md / b_isolate_boundary | — |
| [導入](deployment-context.md) | Business Context | 本番反映と運用移管 | business-map.md / b_deployment | [本番確認](deployment-flow.md) |
| [本番確認](deployment-flow.md) | Business Flow | 継続・切戻し・移管の判断 | deployment-context.md / b_decide_release | — |

## Supporting model

- [業務分解カタログ](decomposition-catalog.md) — 13工程を下位候補へ分解する辞書
- [Actor master](master-actor-map.md)
- [Information master](master-information-model.md)
- [External System master](master-system-map.md)
- [評価メモ](evaluation-notes.md) — reader-facingではなく、Skill改善用の観察

マスタはContextを読む前提資料ではありません。図を見て「この人は誰か」「この情報は何か」「この環境は何か」を確認したくなったときに参照します。
