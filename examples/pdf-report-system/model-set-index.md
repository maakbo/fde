# PDF帳票システム — モデル索引

この索引は、current RDRAの小さなdomain modelと、そこから投影したreader-facing Viewをつなぎます。
最初に図を見る場合は[Domain Overview](domain-overview.md)から始めてください。

## View map

| View | 役割 | Focus | Parent / expanded node | Child Views |
| --- | --- | --- | --- | --- |
| [帳票業務の全体](domain-overview.md) | Overview | 帳票業務と主要参加者・Information | — | [帳票を用意する場面](report-creation-context.md) |
| [帳票を用意する場面](report-creation-context.md) | Detailed Business Context | BUC / Activity / UCと関係要素 | domain-overview.md / b_pdf_reporting | — |

## Model foundation

| RDRA type | Stable ID | Reader label | このsampleでの意味 |
| --- | --- | --- | --- |
| Business | `b_pdf_reporting` | 帳票業務 | 業務データをPDF帳票として使える状態にする領域 |
| BUC | `b_report_ready` | 帳票を用意する | 新規出力と再取得を話す代表的なBusiness Use Case |
| Activity | `b_prepare_report` | データを整える | 業務データを帳票に使える状態へ整える |
| UC | `b_generate_pdf` | PDFを出力 | 帳票仕様・出力条件に沿ってPDFを得る |
| Activity | `b_retrieve_report` | 帳票を探す | 必要な帳票を見つけ、再取得の対象を確認する |
| UC | `b_retrieve_pdf` | 帳票を再取得 | 既に得たPDF帳票を必要時に使う |
| Actor | `a_report_user` | 業務担当 | データを使い、帳票を作成・利用する主体 |
| Actor | `a_report_owner` | 業務責任者 | 帳票の内容を確認する主体 |
| External System | `x_business_system` | 業務システム | 業務データを提供する外部システム |
| Information | `i_report_data` | 業務データ | 帳票作成の入力となる業務上の情報 |
| Information | `i_report_definition` | 帳票仕様 | 帳票の内容・形式を決める情報 |
| Information | `i_output_condition` | 出力条件 | 出力可否や対象を判断する情報 |
| Information | `i_pdf_report` | PDF帳票 | 出力・再取得して業務で使う情報 |

## Hierarchy and relations

```text
Business b_pdf_reporting
  └─ BUC b_report_ready
       ├─ Activity b_prepare_report
       │    └─ UC b_generate_pdf
       └─ Activity b_retrieve_report
            └─ UC b_retrieve_pdf
```

代表BUCは新規出力と必要時の再取得を同じ利用場面として扱います。`b_prepare_report`が`x_business_system`からの`i_report_data`を扱い、
`b_generate_pdf`が`i_report_definition`と`i_output_condition`を参照して`i_pdf_report`を
得ます。`b_retrieve_report`が対象を探し、`b_retrieve_pdf`が同じ`i_pdf_report`を対象にします。
これは業務上の関係を要約した
もので、厳密な実行順や画面・項目仕様を確定するものではありません。

## Supporting master maps

- [Actor master](master-actor-map.md)
- [External-system master](master-system-map.md)
- [Information master](master-information-model.md)
- [Master model index](master-model-index.md)

## Boundary

このmodelはsynthetic evaluation sampleです。State / Condition / Variation、詳細な権限、
保存方式、例外処理は、必要な会話が生まれたときに別のViewへ展開します。13工程の開発業務は
[別sample](../waterfall-system-development/)に残し、このdomain modelの下位階層には置きません。
