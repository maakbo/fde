# PDF帳票システム — master views

Actor、External System、Informationは、Business / BUC / Activity / UCとは別の正規層です。
各Contextは必要なIDだけを選び、同じlabel・icon定義を再利用します。

## Master views

| Master | Role | Canonical prefix | Source |
| --- | --- | --- | --- |
| Actor map | 参加する人・役割 | `a_` | [Actor master](master-actor-map.md) |
| External-system map | 境界外の技術システム | `x_` | [External-system master](master-system-map.md) |
| Information model | 業務で参照する情報 | `i_` | [Information master](master-information-model.md) |

## Context selections

| Context view | Selected IDs | Selection reason |
| --- | --- | --- |
| [Domain Overview](domain-overview.md) | `a_report_user`, `a_report_owner` | 帳票業務の主要な参加者 |
| [Domain Overview](domain-overview.md) | `x_business_system` | 業務データを提供する外部システム |
| [Domain Overview](domain-overview.md) | `i_report_data`, `i_pdf_report` | 俯瞰に必要な入力と成果 |
| [帳票を用意する場面](report-creation-context.md) | `a_report_user`, `a_report_owner` | BUCに直接参加する主体 |
| [帳票を用意する場面](report-creation-context.md) | `x_business_system` | データ準備の外部依存 |
| [帳票を用意する場面](report-creation-context.md) | `i_report_data`, `i_report_definition`, `i_output_condition`, `i_pdf_report` | UCが扱うInformation |

同種要素の関係や、State / Condition / Variationの追加は、根拠が得られたときにこの層へ戻って
更新します。
