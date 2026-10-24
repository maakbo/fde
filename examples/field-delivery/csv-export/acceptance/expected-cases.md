# 受入期待（実装閲覧前に固定）

固定時点: 2026-10-24。根拠は `02-definition.md`、`input/definition-answers.md` (A1)、`input/baseline-contract.md`。独立確認役のローカルHTTP試行用。以下は実行結果でも、現場の承認でもない。CSVのHTTP path、特殊IDのfixture投入方法、画面操作の自動化方法はDesign待ちとし、期待値は後から実装結果に合わせて変えない。

共通fixture（`id / date / status`）: `O-101 / 2026-10-01 / NEW`、`O-102 / 2026-10-02 / SHIPPED`、`O-103 / 2026-10-03 / NEW`、`O-104 / 2026-10-03 / CANCELLED`、`O-105 / 2026-10-04 / NEW`。全件順は O-105, O-103, O-104, O-102, O-101。同日はID昇順。`status`、`from`、`to` はAND、日付は両端含む。空値は未指定。

| ケース | 条件ID | 入力 | 固定した期待 |
| --- | --- | --- | --- |
| B01 | D-P01, P06 | `GET /orders` | 200 JSON、`count=5`、上記の全件順。`orders` の各 `id/date/status` がfixtureと一致。 |
| B02 | D-P01, P06 | `GET /orders?status=NEW` | 200 JSON、O-105, O-103, O-101、`count=3`。 |
| B03 | D-P01, P03, P06 | `GET /orders?status=NEW&from=2026-10-01&to=2026-10-03` | 200 JSON、O-103, O-101、`count=2`。同条件CSVと値・順序を比較。 |
| B04 | D-P01, P06 | `GET /orders?from=2026-10-03&to=2026-10-03` | 200 JSON、O-103, O-104。両端境界と同日ID順。 |
| B05 | D-P01, P06 | `GET /orders?status=SHIPPED&from=2026-10-03` | 200 JSON、`count=0`, `orders=[]`。 |
| B06 | D-P01, P06 | `GET /orders?status=&from=&to=` | 200 JSON、全件順。空値は未指定。 |
| E01–E06 | D-P02, P09 | JSON検索とCSVの各々へ、`status=INVALID`、`from=2026-02-30`、`to=bad`、`from=2026-10-04&to=2026-10-03`、`unknown=1`、`status=NEW&status=NEW` | いずれも400 JSON。CSV attachmentにしない。未知・重複queryを黙って受け入れない。 |
| E07 | D-P02, P09 | `POST /orders` とCSV pathへの `POST` | 405。 |
| E08 | D-P02 | 未知pathへのGET | 404。 |
| C01 | D-P03, P04, P07 | CSV pathへの無条件GET | 200、見出し `受注ID,受注日,状況`、全5件を全件順で出す。JSONと各行のID・日付・状況が一致。 |
| C02 | D-P03, P04 | `status=NEW&from=2026-10-01&to=2026-10-03` | O-103, O-101の2件。JSON同条件と一致。 |
| C03 | D-P03, P04 | `from=2026-10-03&to=2026-10-03` | O-103, O-104の2件。境界日と同日順。 |
| C04 | D-P05, P07 | `status=SHIPPED&from=2026-10-03` | 200、見出しだけの1レコード、データ行なし。 |
| C05 | D-P07 | すべての正常CSV | Content-Type `text/csv;charset=utf-8`、Content-Dispositionはattachmentでfilename `orders.csv`、UTF-8 BOMを先頭にちょうど1つ、レコード終端CRLF、カンマ区切り。UTF-8の厳密decodeと独立CSV parserで3列を確認。 |
| C06 | D-P08 | 特殊fixture ID `和文,"引用",末尾\r\n次行`、日付 `2026-10-05`、状況 `NEW` を含む別fixtureのCSV | parserでIDが改変なく1値として復元され、日付・状況・見出しが正しい。CRLFを含むIDを1レコードとして扱う。test seamはDesignから渡されるURLに接続する。 |
| S01 | D-P01, P09 | E01–E07前後の `GET /orders` | countと各行、順序がB01から変化しない。検索とCSV取得が元データを変更しない。 |
| U01 | D-P06, P10 | `GET /` と画面ボタン | 画面GETは既存どおり表示できる。ボタンは押下時の現在入力を送る。例えば検索表示後、未検索で `status` をNEWへ変更して押せばCSVはNEWの3件であり、直前表示の5件に拘束されない。ブラウザ実行ができない場合は未検証と記録する。 |

HTTP検証はPython標準ライブラリ `urllib` と `csv` で行う。JSONの余分なフィールドやエラーJSONの文言は契約外として指定しない。`date` はbaselineのJSON行の日付キーとして想定するが、公開契約は日付の値と意味を定めるのみでキー名を明示しないため、異なるキーなら意味の決定をrootへ戻し、実装に合わせて無断で期待を変えない。特殊fixtureの取得経路は未定。実Excel、任意実データ、数式安全性、性能、実組織の業務効果、正式受入はこのケースでは確かめない。
