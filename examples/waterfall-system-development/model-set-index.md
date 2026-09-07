# 作業用モデル索引

このファイルはモデル作成・評価のための索引です。**業務の認識合わせは [システム開発](business-map.md) から始めます。**

読者にこの索引を順番に読ませません。図から必要な詳細へ掘り、各図の直下で日本語の意味を確認できる構成を優先します。

## モデル構造

| View | 役割 | 詳細 |
| --- | --- | --- |
| [システム開発](business-map.md) | 認識合わせの入口 | 13工程を俯瞰し、図から各詳細へ移動する |
| [業務分解カタログ](decomposition-catalog.md) | 分解辞書 | 13工程の Layer 3〜4 候補をまとめて比較する |
| [要件定義](requirements-context.md) | Context | 現行理解・要件化・責務設計・要件合意 |
| [要件合意](requirements-alignment-flow.md) | Flow | 差異解消と再確認のループ |
| [実装・単体](implementation-unit-context.md) | Context | 実装・単体検証・品質確認・統合 |
| [単体検証](implementation-unit-flow.md) | Flow | 差異があれば修正へ戻るループ |
| [外部結合テスト](external-integration-context.md) | Context | 接続確認・契約検証・原因特定・復旧確認 |
| [原因特定](external-integration-flow.md) | Flow | 双方の証跡を使った責任境界の切り分け |
| [導入](deployment-context.md) | Context | 実施判断・本番反映・本番確認・切戻し・運用移管 |
| [本番確認](deployment-flow.md) | Flow | 継続 / 切戻しの判断 |

## 支えるモデル

- [Actor](master-actor-map.md)
- [Information](master-information-model.md)
- [External System](master-system-map.md)

これらは Context を読む前提資料ではありません。図を見て「この人は誰？」「この情報は何？」「この環境は何？」と確認したくなったときに参照します。

## 評価用

- [評価メモ](evaluation-notes.md) — reader-facing ではなく Skill 改善用

## 抽象レイヤー

| Layer | 意味 | このモデルでの扱い |
| --- | --- | --- |
| 1 | Business Area | システム開発 |
| 2 | 大きな工程 / 共通索引 | 見積〜導入の13工程 |
| 3 | Business Use Case / scene | 工程を成立させるまとまり |
| 4 | Business Activity | scene 内の意味ある業務単位 |
| 5 | Business Flow | 判断、差戻し、修正、再確認 |

Layer 2 の工程名をそのまま Business Activity とみなさず、下位の input / transformation / output から意味を再確認します。
