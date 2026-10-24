# Implementation｜受注一覧CSV（ローカル演習）

**状態：実装者のローカル実装とself-testを完了。独立受入、実ブラウザ、実Excel、実組織の採否は未実施。** 根拠は `../02-definition.md` の D-P01〜P10、`../input/definition-answers.md` の架空SE役回答 A1、`../input/baseline-contract.md`、`../03-design.md`。この記録とコードは演習の一時作業領域にあり、public/private repo の編集・commit・push・本番操作は行っていない。

## 入力と変更

`../baseline/source-manifest.json` の `upstream_commit` は `3f3b546d5ee750d267c0cf957b0b58c70043d31e`。作業前に5ファイルのSHA-256がmanifestと一致することを確認し、5ファイルをこのフォルダへ複製した。`OrderSearchService.java`、`OrderSearchTest.java`、`acceptance.py` はbaselineと同一のまま。baselineの `python3 run.py` は `PASS 25 checks`、HTTP 9検索例・4不正例を通過した。

| 条件ID | 差分と理由 |
| --- | --- |
| D-P01〜P03, P05, P09 | `OrderSearchServer.java` に `GET /orders.csv` を追加。JSONとCSVは既存の同じ `parseQuery` と `OrderSearchService.search` を呼ぶ。検索のAND、日付境界、順序、0件、入力エラーを二重実装しない。無効条件は従来と同じ400 JSON、CSV attachmentなし。GET以外405、未知path404を維持 |
| D-P04, P07, P08 | 新規 `OrderCsv.java` の公開署名は `public static byte[] format(List<OrderSearchService.Order> orders)`。検索済み・順序済みリストを変更せず、UTF-8 BOM、`受注ID,受注日,状況` 見出し、CRLF、必要なセル引用を持つバイト列へ整形する。任意の架空IDのfixtureを別担当が直接渡せる。正常CSVのみ指定のContent-Type、Content-Disposition、Cache-Control、バイト長を設定 |
| D-P06, P10 | 画面に `type="button"` の「現在の入力条件でCSV出力」を追加。押下時の `FormData(form)` をURL queryへ変換し、200のBlobを `orders.csv` で保存。400 JSONは別のCSVメッセージ欄へ表示する。既存検索submitと結果表示は維持 |
| D-P01〜P10 の実装者確認 | 新規 `OrderCsvTest.java`、`csv_selftest.py` を `run.py` に組込み、Java整形とlocalhost HTTPをself-test。これらは独立受入の代わりではない |

## 実行証拠

環境は macOS のローカル作業領域、OpenJDK `16.0.1`、Python `3.9.12`、Java標準ライブラリのみ。`run.py` は `javac --release 16` で一時ディレクトリへビルドし、`127.0.0.1` の一時portを使う。

| コマンド・対象 | 期待と観測 | 判定の範囲 |
| --- | --- | --- |
| `cd ./implementation && python3 run.py` | `PASS 25 checks`（既存Java）、`PASS CSV formatter 5 checks`、既存HTTP 9検索例・4不正例、`PASS CSV HTTP implementation self-test: 17 checks` | 実装者self-testのみ。D-P01〜P09の代表ケース |
| `python3 -m py_compile run.py acceptance.py csv_selftest.py` | exit 0 | Python構文。生成されたpycacheは作業領域から削除 |
| `python3 run.py --serve` を子processで起動し表示portへ `GET /orders.csv`、次にSIGINT | `Demo: http://127.0.0.1:53153/`、CSV 200とBOM、終了後のport閉鎖を確認 | 起動・port表示・cleanupのみ。portは実行ごとに変わる |
| baselineと実装のSHA-256比較 | `OrderSearchService.java`、`OrderSearchTest.java`、`acceptance.py` は一致 | 既存の検索ロジック・テストを維持 |

self-testのCSV HTTP例は複合条件 `status=NEW&from=2026-10-02&to=2026-10-04` で `O-105, O-103` の順と三値のJSON一致、0件見出しのみ、BOM・CRLF・ヘッダ・長さを確認。無効status/日付/逆転範囲/未知・重複queryは400 JSONでattachmentなし、POSTは405と`Allow: GET`を確認。Java整形例は日本語・カンマ・引用符・CR/LFを含む架空IDと元値不変を確認した。HTMLのボタン文字列とfetch先はself-testで確認したが、実ブラウザ動作の証拠ではない。

## 未実施と返し先

独立確認役にはA1/Definitionから独立に期待値を作り、HTTP生バイト・ヘッダ・CSV parserでD-P01〜P10を照合してもらう。特に実ブラウザの押下時入力、保存名、400表示は未確認。任意の実データ、実Excel、表計算の数式安全性、負荷、本番、現場効果は対象外。これらをCSV成立や実組織の採用と解釈しない。A1とbaselineの間に実装を止める仕様衝突は見つからなかった。独立確認で差異が出た場合は条件IDと入力・実結果を実装者へ戻し、新しい業務仕様が必要ならSE役へ戻す。

ローカル確認はこのフォルダで `python3 run.py`、手動表示は `python3 run.py --serve`、終了は `Ctrl-C`。正常時は同一queryの `/orders` と `/orders.csv` を比較し、誤条件では `/orders.csv?status=BAD` の400 JSONを確認する。旧版へ戻すにはこの作業フォルダを切り離し、`../baseline/source-manifest.json` に対応する元の5ファイルで `python3 run.py` を実行する。これは演習用の戻し方であり、配備ロールバックは検証していない。


この工程の時点の報告。後続の独立確認・ブラウザ・別条件の結果は[全体の記録](../README.md)を参照。
