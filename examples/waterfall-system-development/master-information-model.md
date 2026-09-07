# システム開発 Information マスタ

システム開発の各 Business で、人が参照・判断・更新・共有する Information の初期候補です。

ここでは「ファイル」「チケット」「画面」といった保存形式ではなく、業務上の意味を stable ID にします。同じ概念が要件、設計、テスト、導入で姿を変えても、意味が同じなら一つの Information として追跡します。

## 1. 見積・計画

| ID | Information | 意味 |
| --- | --- | --- |
| `i_request_background` | 依頼背景 | なぜ開発が必要か |
| `i_expected_outcome` | 期待成果 | 開発で実現したい状態 |
| `i_scope` | 開発スコープ | 対象 / 対象外の境界 |
| `i_constraint` | 制約 | 期限、契約、技術、組織上の制約 |
| `i_estimate_assumption` | 見積前提 | 見積成立の前提条件 |
| `i_size_estimate` | 規模見積 | 機能・データ・IF等の規模 |
| `i_effort_estimate` | 工数見積 | 工程・役割ごとの必要工数 |
| `i_cost_estimate` | 費用見積 | 人件費・調達費・環境費等 |
| `i_staffing_plan` | 体制案 | 必要役割・人数・配置 |
| `i_schedule_outline` | 概算スケジュール | 主要工程とマイルストーン |
| `i_project_risk` | プロジェクトリスク | 納期・費用・品質へ影響する不確実性 |
| `i_estimate` | 見積 | 条件・費用・期間・前提をまとめた判断材料 |

## 2. 要件

| ID | Information | 意味 |
| --- | --- | --- |
| `i_current_business` | 現行業務 | 現在の業務の流れ・責任・例外 |
| `i_business_issue` | 業務課題 | 現行で解決したい問題 |
| `i_business_rule` | 業務ルール | 業務判断や制約を決める規則 |
| `i_business_term` | 業務用語 | ドメイン内で共有する概念 |
| `i_business_requirement` | 業務要件 | 業務として必要な変化・能力 |
| `i_to_be_business` | To-Be業務 | 変更後に目指す業務状態 |
| `i_system_boundary` | システム境界 | 人 / 対象システム / 外部システムの責任境界 |
| `i_system_requirement` | システム要件 | システムが満たすべき要求の集合 |
| `i_functional_requirement` | 機能要件 | システムが提供する振る舞い |
| `i_data_requirement` | データ要件 | 保持・生成・更新・参照すべきデータ |
| `i_external_interface_requirement` | 外部IF要件 | 外部システムとの情報交換条件 |
| `i_nonfunctional_requirement` | 非機能要件 | 性能、可用性、保守性等の品質条件 |
| `i_security_requirement` | セキュリティ要件 | 認証、認可、機密性、監査等の条件 |
| `i_operation_requirement` | 運用要件 | 監視、障害対応、バックアップ等の条件 |
| `i_migration_requirement` | 移行要件 | データ・業務・システム切替条件 |
| `i_acceptance_criteria` | 受入条件 | 業務側が受け入れ可能と判断する条件 |
| `i_requirement_trace` | 要件トレース | 要件と設計・実装・テスト・受入の対応 |

## 3. 基本設計 / 外部仕様

| ID | Information | 意味 |
| --- | --- | --- |
| `i_external_specification` | 外部仕様 | 利用者・外部システムから見た振る舞い |
| `i_ui_specification` | UI仕様 | 画面、操作、表示、入力の仕様 |
| `i_report_specification` | 帳票仕様 | 帳票の内容・形式・出力条件 |
| `i_api_specification` | API仕様 | APIの入出力・契約 |
| `i_interface_specification` | 外部IF仕様 | ファイル・メッセージ等の連携契約 |
| `i_logical_data_model` | 論理データモデル | 業務概念をシステム情報へ構造化したモデル |
| `i_code_definition` | コード定義 | コード体系・値・変換規則 |
| `i_authorization_design` | 権限設計 | ロール・権限・操作可能範囲 |
| `i_architecture_design` | アーキテクチャ | システム構造・責務・技術方式 |
| `i_batch_design` | バッチ仕様 | バッチ処理・起動条件・入出力 |
| `i_job_design` | ジョブ設計 | ジョブ順序・依存・スケジュール |
| `i_monitoring_design` | 監視設計 | 監視対象・しきい値・通知条件 |
| `i_logging_design` | ログ設計 | 記録対象・粒度・追跡可能性 |
| `i_error_design` | エラー設計 | エラー分類・利用者応答・復旧方針 |
| `i_environment_design` | 環境構成 | 開発〜本番の構成・差分・前提 |
| `i_nonfunctional_design` | 非機能方式 | 非機能要件を実現する技術方式 |

## 4. 詳細設計 / 内部仕様

| ID | Information | 意味 |
| --- | --- | --- |
| `i_internal_specification` | 内部仕様 | 実装内部の責務・処理・契約 |
| `i_component_design` | コンポーネント設計 | コンポーネント / モジュールの責務と関係 |
| `i_processing_design` | 処理設計 | 条件分岐・状態変化・処理手順 |
| `i_transaction_design` | トランザクション設計 | commit / rollback / 境界条件 |
| `i_concurrency_design` | 並行・排他設計 | 同時実行・排他・再実行性 |
| `i_physical_data_model` | 物理データモデル | テーブル・索引・制約等の実装構造 |
| `i_data_access_design` | データアクセス設計 | SQL・アクセス方式・性能条件 |
| `i_internal_interface_design` | 内部IF設計 | モジュール間の入出力・例外契約 |
| `i_exception_design` | 例外設計 | 例外分類・伝播・処理責任 |
| `i_unit_test_viewpoint` | 単体テスト観点 | 実装単位で確認すべき正常・境界・異常条件 |

## 5. 実装・単体検証

| ID | Information | 意味 |
| --- | --- | --- |
| `i_source_code` | ソースコード | 実行可能なシステムロジック |
| `i_unit_test_code` | ユニットテストコード | 実装単位の自動検証ロジック |
| `i_build_definition` | ビルド定義 | ビルド・依存・生成物の条件 |
| `i_dependency_definition` | 依存ライブラリ定義 | 外部ライブラリと版の依存関係 |
| `i_runtime_configuration` | 実行設定 | 環境ごとの設定値・起動条件 |
| `i_code_review` | コードレビュー記録 | 差分に対する指摘・判断・合意 |
| `i_static_analysis_result` | 静的解析結果 | 品質・規約・脆弱性の機械検査結果 |
| `i_unit_test_result` | 単体テスト結果 | 単体検証の実績・成否・証跡 |
| `i_build_artifact` | ビルド成果物 | 配備・試験可能な版付き実行物 |

## 6. 内部結合テスト

| ID | Information | 意味 |
| --- | --- | --- |
| `i_internal_test_scope` | 内部結合テスト範囲 | 結合対象と対象外 |
| `i_internal_test_viewpoint` | 内部結合テスト観点 | 結合で確認すべき責務境界・リスク |
| `i_internal_test_specification` | 内部結合テスト仕様 | シナリオ・条件・操作・期待結果 |
| `i_internal_test_data` | 内部結合テストデータ | 再現可能な入力・状態 |
| `i_internal_test_result` | 内部結合テスト結果 | 実施結果・証跡・品質状態 |

## 7. 外部結合テスト

| ID | Information | 意味 |
| --- | --- | --- |
| `i_connection_condition` | 接続条件 | 接続先、ネットワーク、認証、時間帯等 |
| `i_external_test_scope` | 外部結合テスト範囲 | 対象IF・相手・責任境界 |
| `i_external_test_specification` | 外部結合テスト仕様 | 正常・異常・再送・復旧等のシナリオ |
| `i_external_test_data` | 外部結合テストデータ | 双方合意した送受信データ |
| `i_exchange_evidence` | 送受信エビデンス | 電文・時刻・ログ等の相互照合情報 |
| `i_external_test_result` | 外部結合テスト結果 | 接続・契約・異常動作の検証結果 |

## 8. システムテスト

| ID | Information | 意味 |
| --- | --- | --- |
| `i_system_test_strategy` | システムテスト方針 | システム全体で証明する品質 |
| `i_e2e_scenario` | E2Eシナリオ | 複数機能・IFを跨ぐ業務シナリオ |
| `i_nonfunctional_test_spec` | 非機能試験仕様 | 性能・可用性・セキュリティ等の試験条件 |
| `i_system_test_data` | システムテストデータ | 本番相当の量・特性を持つ試験データ |
| `i_system_test_result` | システムテスト結果 | E2E・非機能を含む全体品質の実績 |
| `i_quality_assessment` | 品質評価 | 欠陥・結果・リスクをまとめた工程判断材料 |

## 9. UAT / 受入

| ID | Information | 意味 |
| --- | --- | --- |
| `i_uat_scenario` | UATシナリオ | ユーザーが業務として確認するシナリオ |
| `i_uat_result` | UAT結果 | 業務適合性・発見事項の実績 |
| `i_acceptance_issue` | 受入課題 | 受入判断に影響する未解決事項 |
| `i_acceptance_decision` | 受入判定 | 受入 / 条件付き受入 / 不受入の判断 |

## 10. 導入・運用移管

| ID | Information | 意味 |
| --- | --- | --- |
| `i_release_scope` | リリース範囲 | 本番へ反映する変更・版・対象 |
| `i_release_plan` | リリース計画 | 日時・役割・順序・判断点 |
| `i_release_note` | リリースノート | 変更内容・既知制約・利用上の注意 |
| `i_deployment_procedure` | 配備手順 | 本番へ変更を反映する具体手順 |
| `i_rollback_procedure` | ロールバック手順 | 異常時に安全な状態へ戻す手順 |
| `i_migration_procedure` | 移行手順 | データ・設定・業務切替の手順 |
| `i_migration_data` | 移行データ | 本番へ移すデータと変換結果 |
| `i_production_configuration` | 本番環境設定 | 本番固有の設定状態 |
| `i_smoke_result` | 本番疎通結果 | 配備後の最低限の技術確認結果 |
| `i_business_validation_result` | 業務確認結果 | 本番で重要業務が成立することの確認結果 |
| `i_runbook` | 運用手順 | 監視・障害・定常運用の実施方法 |
| `i_known_issue` | 既知問題 | 導入時点で残る制約・暫定対応 |
| `i_handover_record` | 運用引継ぎ | 運用責任を移すための共有内容 |
| `i_release_decision` | Go / No-Go判定 | 本番変更を実施・継続・中止する判断 |

## 11. 横断 Information

| ID | Information | 意味 |
| --- | --- | --- |
| `i_task` | タスク | 実施すべき作業と担当・状態 |
| `i_issue` | 課題 | 解決を必要とする問題 |
| `i_defect` | 不具合 | 期待結果との差異と再現条件 |
| `i_change_request` | 変更要求 | ベースライン済み内容への変更要求 |
| `i_change_impact` | 変更影響 | 要件・設計・実装・テスト・運用への影響 |
| `i_decision` | 意思決定記録 | 論点・選択・理由・決定者 |
| `i_review_record` | レビュー記録 | 指摘・対応・判断 |
| `i_quality_record` | 品質記録 | 品質指標・欠陥傾向・工程判断材料 |
| `i_configuration_baseline` | 構成ベースライン | ある時点で合意された構成要素の版集合 |
| `i_version` | バージョン | 対象構成の識別子 |
| `i_release_tag` | リリースタグ | リリース対象版の識別 |
| `i_environment_definition` | 環境定義 | 環境ごとの構成・接続・設定差分 |
| `i_minutes` | 議事記録 | 会話で確認された事実・論点・宿題 |

# Information trace の主要な線

以下は「ファイルの変換」ではなく、意味のトレースとして追うべき代表関係です。

- `i_business_issue` / `i_expected_outcome` → `i_business_requirement`
- `i_business_requirement` → `i_system_requirement`
- `i_system_requirement` → `i_external_specification` / `i_nonfunctional_design`
- `i_external_specification` → `i_internal_specification`
- `i_internal_specification` → `i_source_code` / `i_unit_test_code`
- `i_system_requirement` / `i_external_specification` → 各テスト仕様
- `i_acceptance_criteria` → `i_uat_scenario` → `i_acceptance_decision`
- `i_source_code` + `i_build_definition` → `i_build_artifact`
- `i_build_artifact` + `i_release_scope` → 本番配備対象
- `i_operation_requirement` / `i_monitoring_design` → `i_runbook`
- `i_change_request` → `i_change_impact` → 影響する要件・設計・コード・テストのベースライン更新

# 特にレビューしたい Information 境界

1. `i_system_requirement` と `i_functional_requirement` を親子概念として分ける意味があるか。
2. `i_external_specification` は一つの概念か、UI / API / 帳票 / バッチ等の集合を指すラベルに留めるか。
3. `i_architecture_design` は Information か、それとも複数 Information の View か。
4. 「テスト仕様」と「テストケース」「テストシナリオ」を同じ粒度に置いてよいか。
5. `i_configuration_baseline` は独立 Information か、複数構成情報を束ねる識別概念か。
6. `i_build_artifact` は Business Information として扱うべきか、技術 Artifact として別分類を導入すべきか。
7. 不具合・課題・変更要求を別概念として明確に区別できているか。
8. 受入条件とシステムテスト終了条件を混同していないか。
