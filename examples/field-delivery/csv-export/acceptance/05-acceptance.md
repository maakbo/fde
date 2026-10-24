# 独立受入記録｜受注一覧CSV（ローカル演習）

状態: **固定済みケースのHTTPとformatterはPASS。画面実操作と人の受渡しは未確認。** 実組織の受入、コード採否、リリース判断を意味しない。

## 根拠と独立性

受入期待は2026-10-24 17:13 JSTに、`02-definition.md`、`input/definition-answers.md` A1、`input/baseline-contract.md`、fde `ai-pilot-evaluation` Skill / `operational-learning` だけを読んで `expected-cases.md` に固定した。その時点でDesign、baselineコード、実装、実装者selftestは見ていない。後から `03-design.md` によりpath `/orders.csv` と `OrderCsv.format(List<OrderSearchService.Order>): byte[]` のtest seamを接続した。期待行と例外の値は実装結果に合わせて変更していない。JSON日付キー `date` は後から示された既存コード契約に限定した。

確認者: 独立受入担当。環境: ローカルのJava（`javac --release 16`）、Python 3、127.0.0.1の一時port。入力は公開架空fixtureのみ。実装者のselftestは合否根拠に使っていない。

## 実行と観測

```sh
javac --release 16 -d ./acceptance/build \
  ./implementation/OrderSearchService.java \
  ./implementation/OrderCsv.java \
  ./implementation/OrderSearchServer.java \
  ./acceptance/SpecialCsvHarness.java
java -cp ./acceptance/build SpecialCsvHarness \
  > ./acceptance/special.csv
java -cp ./acceptance/build OrderSearchServer 0
# 実際のPORT=53346。次の2コマンド後、Ctrl-Cでserver終了。
python3 ./acceptance/acceptance.py \
  --base-url http://127.0.0.1:53346 --csv-path /orders.csv \
  --special-csv-file ./acceptance/special.csv
python3 -O ./acceptance/acceptance.py \
  --base-url http://127.0.0.1:53346 --csv-path /orders.csv \
  --special-csv-file ./acceptance/special.csv
```

Javaコンパイル成功。特殊fixtureのformatter出力は81バイト。通常Pythonと `-O` は各 `132 checks passed; 0 failed`。serverは停止済み。期待差異・再現する失敗はなかった。

| 条件 | 観測した範囲と判定 |
| --- | --- |
| D-P01, D-P02 | `/orders` の全件、NEW、複合AND、同日境界、0件、空値、400の6種、POST 405、未知path 404は固定期待と一致。前後の全件結果も一致。PASS |
| D-P03, D-P04 | CSVの全件、複合、同日境界、NEW、空値のID・日付・状況と順序がfixtureと同条件JSONに一致。PASS |
| D-P05 | 0件は200、独立parserで見出し1レコード、データ0レコード。PASS |
| D-P06 | `/` は200、既存JSON検索のHTTP回帰はPASS。既存画面の表示や操作のブラウザ回帰は未検証。 |
| D-P07 | 正常CSVの200、Content-Type/charset、attachment filename、UTF-8 BOM、CRLFレコード終端、カンマ区切り、見出しを生バイトと独立parserで確認。PASS。実Excelは未検証。 |
| D-P08 | 別fixtureのID `和文,"引用",末尾\r\n次行` と日付/状況を `OrderCsv` に渡した生bytesをPython標準 `csv` で復元し、値が一致。日本語・カンマ・quote・CRLFを1件に含むケースはPASS。単独CR、単独LF、複数特殊行、実データは未検証。 |
| D-P09 | CSV pathの不正status・日付・範囲・未知/重複queryは400 JSONでattachmentなし。POSTは405。検索前後の元fixtureは一致。PASS。 |
| D-P10 | ブラウザでの現在入力送信、未検索の入力変更、ダウンロード名、400エラー表示は未実行。HTTPの同条件比較だけで画面動作のPASSとはしない。 |

D-H03について、実装者の期待変更に依存しない事前固定ケースと結果の対応は実施できた。D-H01の受渡し十分性、D-H02の不足返却の実演、D-H04の運用受取者の理解・戻し方は人による確認がまだない。受渡し負担の改善効果、現場pilot、実Excel、任意データの数式安全性も対象外または未確認。

## 返し先と判断

固定HTTP/formatterケースに実装不具合の指摘はない。D-P10とD-H01/H02/H04は確認者・SE役・運用受取者役で別に確かめる。現状で言えるのは**ローカルの固定ケースが通過した**ことまで。全体試行の採否やリリースは人の判断に残す。


この工程の時点の報告。後続の独立確認・ブラウザ・別条件の結果は[全体の記録](../README.md)を参照。
