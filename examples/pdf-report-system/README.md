# PDF帳票システム — RDRA domain model

これは、PDF帳票システムそのものを理解するためのsyntheticなRDRA version 0です。
業務担当は外部の業務システムから得たデータを使って帳票を作り、業務責任者は内容を
確認します。ここで示すdomain modelと、システムを開発する13工程は別の空間として扱います。

## 読み始める

1. [PDF帳票業務のDomain Overview](domain-overview.md) — 誰が、何を使い、どんな業務を支えるか
2. [代表BUC「帳票を用意する」](report-creation-context.md) — Activity / UCと参加者・情報の関係

モデルの要素とViewの対応は[モデル索引](model-set-index.md)で確認できます。Actor・External
System・Informationの正規IDは[master views](master-model-index.md)にまとめています。

開発の仕事を見たい場合は、別sampleの[PDF帳票作成システムの開発](../waterfall-system-development/)
を参照してください。13工程はRDRAの下位階層ではありません。

## このversion 0の前提

- 実案件の事実ではなく、会話を始めるためのsyntheticな前提です。
- 代表BUCは「帳票を用意する」。新規出力と、必要なときの再取得を同じ利用場面に置きます。
- State / Condition / Variationは、この小さなscenarioでは追加しません。
- 詳細な帳票項目、保存方式、権限、例外は、会話で必要になったときに別Viewへ展開します。
