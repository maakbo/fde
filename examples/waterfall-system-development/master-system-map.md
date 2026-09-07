# システム開発 External System マスタ

システム開発を支える外部システム・実行環境・接続先の初期候補です。

ここでは「開発支援ツール」「対象システムを動かす環境」「対象システムが接続する外部システム」を同じものとして扱いません。Context では Business が実際に利用・更新・参照するものだけを採用します。

## 1. 開発管理・コミュニケーション

| ID | External System | 主な役割 | 注意 |
| --- | --- | --- | --- |
| `x_task_management` | タスク / 課題管理システム | タスク、課題、不具合、変更要求の状態を管理する | 「課題」自体は Information、ツールは System |
| `x_requirements_management` | 要件管理ツール | 要件、トレーサビリティ、承認状態を管理する | Wikiと統合される場合がある |
| `x_documentation` | ドキュメント / Wiki | 設計・議事・手順などの共同編集・共有を支える | Information と保管場所を区別する |
| `x_communication` | チャット / コラボレーション基盤 | 調整・通知・会話を支える | 会話内容そのものを master Information にするかは別判断 |
| `x_test_management` | テスト管理ツール | テストケース、実施結果、証跡、進捗を管理する | 課題管理と一体の場合がある |
| `x_itsm` | ITSM / サービスデスク | 変更、障害、問い合わせ、リリースを運用側で管理する | 開発中の課題管理とは責任境界が異なる |

## 2. ソース・ビルド・品質

| ID | External System | 主な役割 | 注意 |
| --- | --- | --- | --- |
| `x_scm` | 構成管理 / Git | ソース、設定、テストコード等の版を管理する | 「構成管理」という Business と Git を同一視しない |
| `x_code_review` | コードレビュー基盤 | 差分レビュー、コメント、承認を支える | Gitホスティングと一体の場合がある |
| `x_cicd` | CI/CD | ビルド、テスト、配備を自動実行する | Business は「統合可能性を確認する」「配備する」等 |
| `x_artifact_repository` | Artifact Repository | ビルド成果物・パッケージの版を保管する | SCMとは別の構成要素を扱う |
| `x_static_analysis` | 静的解析 / SAST | コード品質・脆弱性を機械検査する | 品質判断主体ではなく検査支援システム |
| `x_test_automation` | テスト自動化基盤 | 自動テスト実行・結果収集を支える | CI/CDに包含される場合がある |
| `x_dependency_management` | 依存関係 / パッケージ管理 | ライブラリ依存と取得を管理する | Artifact Repositoryと境界確認 |

## 3. セキュリティ・アクセス管理

| ID | External System | 主な役割 | 注意 |
| --- | --- | --- | --- |
| `x_iam` | IAM | 人・サービスのアクセス権を管理する | 対象システム内IAMか開発基盤IAMかを区別する |
| `x_secrets` | Secrets / 証明書管理 | 秘密情報・鍵・証明書の保管・配布を管理する | Information として秘密値をモデルへ書かない |
| `x_security_scanner` | DAST / 脆弱性診断基盤 | 稼働システムの脆弱性確認を支える | SASTと分ける |

## 4. 開発・検証・本番環境

| ID | Environment / System | 主な役割 | 注意 |
| --- | --- | --- | --- |
| `x_dev_environment` | 開発環境 | 個別開発・デバッグを行う実行環境 | IDEそのものとは別 |
| `x_internal_integration_env` | 内部結合テスト環境 | 内部コンポーネント結合を検証する | 組織によって名称・統合範囲が異なる |
| `x_external_integration_env` | 外部結合テスト環境 | 外部システムとの接続を検証する | 接続先側環境と対になる |
| `x_system_test_env` | システムテスト / ステージング環境 | E2E・非機能を本番相当で検証する | staging と system test を分ける場合もある |
| `x_uat_env` | UAT環境 | ユーザーが受入確認する | システムテスト環境との共用有無を確認 |
| `x_production_env` | 本番環境 | 実業務を処理する | 「本番環境」と「本番クラウド管理基盤」を区別する |
| `x_cloud_platform` | クラウド / IaaS 管理基盤 | 実行環境・ネットワーク・ストレージ等を提供する | 対象環境の土台 |
| `x_container_platform` | コンテナ / 実行基盤 | アプリケーション実行と配備単位を管理する | 必須ではない |
| `x_database_platform` | DB管理基盤 | データストアを提供する | 対象システム内部要素として扱う場合もある |

## 5. 運用・観測

| ID | External System | 主な役割 | 注意 |
| --- | --- | --- | --- |
| `x_monitoring` | 監視基盤 | メトリクス・死活・アラートを管理する | 監視条件は Information |
| `x_logging` | ログ管理 / 可観測性基盤 | ログ・トレース・検索を提供する | ログ内容は Information / Evidence |
| `x_backup` | バックアップ基盤 | バックアップ・復元を提供する | System Test / 導入 / 運用で関与 |
| `x_job_scheduler` | ジョブ管理 / スケジューラ | バッチ・ジョブの実行を管理する | 対象システムの一部か外部基盤かを確認 |

## 6. 対象システム外の連携先

| ID | External System | 主な役割 | 注意 |
| --- | --- | --- | --- |
| `x_external_business_system` | 外部業務システム | 対象システムと業務データを授受する | 実案件では接続先ごとに stable ID を分ける |
| `x_external_api_service` | 外部API / SaaS | API経由で機能・情報を提供する | ベンダ Actor と System を区別する |
| `x_identity_provider` | 外部IdP | 認証・SSOを提供する | IAMとの境界を確認 |
| `x_notification_service` | メール / SMS / Push基盤 | 通知を配信する | 対象システム内部責務との境界を確認 |

## 7. System 同士の関係として確認したい代表例

- `x_scm` → `x_cicd`: 変更をトリガにビルド / テストを起動する。
- `x_cicd` → `x_artifact_repository`: ビルド成果物を登録 / 取得する。
- `x_cicd` → 各 Environment: 対象版を配備する。
- 各 Environment → `x_monitoring` / `x_logging`: 実行状態を観測可能にする。
- `x_external_integration_env` ↔ `x_external_business_system`: 外部結合で接続する。
- `x_production_env` ↔ `x_external_business_system`: 本番業務として接続する。

これらは一般的な候補であり、実際に same-type relationship を描くのは、評価モデル上でその関係を前提として採用した場合だけとします。

## 8. 分類で特に検証したいこと

1. 「開発環境」「検証環境」「本番環境」を単なる場所として扱うか External System として扱うか。
2. CI/CD を Business の主体のように描かず、誰の Business を支援しているか明示できるか。
3. Git / Wiki / テスト管理などの保存先を、そこに保存される Information と混同しないか。
4. 外部システム担当者（Actor）と外部システム（System）を分離できるか。
5. 対象システムの内部コンポーネントを External System master に誤って持ち込まないか。
6. 同じクラウド基盤上の複数環境を、必要以上に別 System として増殖させないか。
