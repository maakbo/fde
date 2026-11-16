# 基本設計 — ビジネスユースケース

[システム開発の全体に戻る](../README.md)

「仕様を具体化する」という親業務を展開します。ここでは、承認済み要件を受け取り、開発・検証担当が実装や確認に使える設計仕様に具体化する場面を扱います。対象は架空の受託開発As-Isです。

```mermaid
flowchart LR
  a_it["顧客IT担当"]
  a_design["設計担当"]
  a_review["レビュー担当"]
  a_dev["実装担当"]
  x_accounting[("既存会計システム")]
  i_requirements[/"合意済み要件"/]
  i_design[/"設計仕様"/]
  i_review[/"レビュー結果"/]

  b_ui(["画面・操作を定める"])
  b_interface(["外部連携を定める"])
  b_data(["データを定める"])
  b_review(["設計をレビューする"])

  a_design --- b_ui
  a_design --- b_interface
  a_design --- b_data
  a_design --- b_review
  a_it --- b_interface
  x_accounting --- b_interface
  a_review --- b_review
  a_dev --- b_review
  i_requirements --- b_ui
  i_requirements --- b_interface
  i_requirements --- b_data
  i_requirements --- b_review
  i_design --- b_ui
  i_design --- b_interface
  i_design --- b_data
  i_design --- b_review
  i_review --- b_review

  b_ui --- b_review
  b_interface --- b_review
  b_data --- b_review
```

画面・外部連携・データの設計は、親業務を具体化する子業務です。レビューでは、合意済み要件と設計仕様を照合し、指摘や修正の結果を次の判断に渡します。実装担当は成果を受け取る役割であり、実務でレビューへ参加するかは現場確認の対象です。

**この業務で扱う情報**は[情報モデル](../information-model.md)の「合意済み要件」「設計仕様」「レビュー結果」と同じ意味で使います。

**次の展開**： [設計レビューの業務フロー](review-flow.md) — 誰がどの順に確認し、修正や引渡しを行うか。

この初版は設計者・レビュアーの役割や作業を仮置きしたものです。実際の組織構造・レビュー方式・承認権限を断定しません。
