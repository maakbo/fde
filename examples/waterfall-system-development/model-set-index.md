# ウォーターフォール型システム開発モデルセット

## 目的

ウォーターフォール型のシステム開発を、工程表ではなく業務コンテキストとして捉えます。

「誰が、何の情報をもとに、何を変化させ、何を次へ渡すのか」を上位から下位へ段階的に展開し、下位で見つかった違和感を上位の業務境界・名称・情報定義へ戻せるモデルセットを目指します。

この題材は `business-context-modeling` Skill の評価ケースでもあります。ユーザーがシステム開発の実務を高い解像度でレビューできるため、抽象度・責任境界・情報の意味・ツールの分類に曖昧さが残れば意図的に表へ出します。

## 抽象レイヤー

| Layer | 意味 | このモデルでの扱い |
| --- | --- | --- |
| 1 | Business Area | システム開発 |
| 2 | 大きな Business Use Case / 工程 | 見積〜導入の13工程 |
| 3 | 工程を成立させる Business Use Case / scene | 例: 要件を発見する、要件を構造化する、要件を合意する |
| 4 | scene 内の Business Activity | 例: 現行業務を把握する、業務ルールを抽出する、受入条件を定める |
| 5 | Business Flow | 判断、差戻し、修正、再確認を含む具体的な流れ |

Layer 2 は以下を基準線として固定し、まずこの順で全体を眺めます。

1. 見積
2. 要件定義
3. 基本設計
4. 詳細設計
5. 実装・単体テスト
6. 内部結合テスト設計
7. 内部結合テスト
8. 外部結合テスト設計
9. 外部結合テスト
10. システムテスト設計
11. システムテスト
12. ユーザー受入テスト
13. 導入

工程名そのものを Business Activity と決めつけず、各工程の input / transformation / output を下位で確認してから名称と境界を再評価します。

## 横断業務

次の業務は一つの工程へ押し込まず、複数工程を横断する関係として扱います。

- プロジェクト計画・進捗管理
- スコープ・変更管理
- 課題・リスク管理
- 品質計画・品質保証
- レビュー・承認管理
- 構成・版管理
- 環境管理
- セキュリティ管理
- 外部システム / ベンダ調整
- リリース管理
- 運用移管
- 意思決定・合意記録

## View map

| View | Role | Level | Parent / expanded node | Child views | Status |
| --- | --- | --- | --- | --- | --- |
| [システム開発の業務](business-map.md) | 全体業務マップ | Layer 1→2 | — | 各工程 Context | working hypothesis |
| [13工程の分解](decomposition-catalog.md) | 業務分解辞書 | Layer 2→4 | `business-map.md` の各工程 | 各工程 Context / Flow | working hypothesis |
| [Actor master](master-actor-map.md) | Actor master | reusable | — | 各 Context | working hypothesis |
| [Information master](master-information-model.md) | Information master | reusable | — | 各 Context | working hypothesis |
| [External System master](master-system-map.md) | External System master | reusable | — | 各 Context | working hypothesis |
| [要件定義 Context](requirements-context.md) | focused context | Layer 3→4 | `b_requirements` | [要件合意 Flow](requirements-alignment-flow.md) | working hypothesis |
| [実装・単体 Context](implementation-unit-context.md) | focused context | Layer 3→4 | `b_implementation_unit` | [単体検証 Flow](implementation-unit-flow.md) | working hypothesis |
| [外部結合 Context](external-integration-context.md) | focused context | Layer 3→4 | `b_external_test` | [障害切り分け Flow](external-integration-flow.md) | working hypothesis |
| [導入 Context](deployment-context.md) | focused context | Layer 3→4 | `b_deployment` | [切替判断 Flow](deployment-flow.md) | working hypothesis |
| [評価メモ](evaluation-notes.md) | Skill feedback | cross-cutting | — | Skill improvement | working |

## 代表 Context で試していること

### 要件定義
現行業務 → 業務要件 → システム要件 → 受入条件という意味の変換を中心に置き、レビュー差戻しを Flow として分離します。

### 実装・単体テスト
内部仕様をソースコードへ変換するだけでなく、単体検証・静的解析・コードレビューを通じて「統合可能な変更」にすることを Business Use Case として捉えます。

### 外部結合テスト
テストケース消化ではなく、外部担当と証跡を突き合わせながら接続契約と責任境界を共同確認する場面として捉えます。

### 導入
本番配備を終点にせず、Go / No-Go、本番確認、必要時のロールバック、運用責任移管までを一つの導入 scene として捉えます。

## 重点評価ポイント

- 工程、Business Use Case、Business Activity、Task の粒度を区別できているか。
- Information が単なる「成果物ファイル」ではなく、業務で参照・判断・更新される概念になっているか。
- Actor は肩書きの一覧ではなく、各 Business への直接参加関係で読めるか。
- 対象システム、外部接続先、開発支援ツール、実行環境を混同していないか。
- 要件 → 設計 → コード → テスト → 受入 → 導入の意味の trace が追えるか。
- レビュー差戻し、欠陥修正、変更要求、再テストなど、ウォーターフォールでも実際に起きる反復が Flow に現れるか。
- 下位の具体化によって上位の名前や境界を修正できる構造になっているか。

## 読み方

最初に [13工程の分解](decomposition-catalog.md) をレビューし、粒度と名前の違和感を見つけます。次に4つの代表 Context / Flow を見て、「誰・何・どの業務・どのシステムの関係が変か」を具体的に指摘します。その指摘を master と上位分解へ戻します。

このモデルは「正しいウォーターフォール標準」を定義するものではありません。実務経験から具体的に違和感を指摘できる評価面をつくることが目的です。
