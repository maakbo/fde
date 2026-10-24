# Design｜受注一覧CSVと条件受渡し（ローカル演習）

**状態：実装前の設計案。実装・試験・独立受入は未実施。** 根拠は [Definition](02-definition.md) の D-H01〜H04／D-P01〜P10、[架空SE役の回答 A1](input/definition-answers.md)、[既存検索baseline](input/baseline-contract.md)。A1 は架空のローカル試行だけの決定であり、実組織の承認ではない。既存コードは `baseline/`、照合した版は `baseline/source-manifest.json` の `upstream_commit: 3f3b546d5ee750d267c0cf957b0b58c70043d31e`。次担当は着手時にファイルと版を再確認する。

## 読み手、成果、境界

実装者役がA1の決定済み条件だけをコードにし、独立確認役が条件IDから期待を作り、運用受取者役へローカル起動・停止・確認・戻し方を渡せる状態を目指す。営業担当役の実業務、実データ、実Excel、auth・権限、paging、性能、社内送信、本番、現場pilot、工数削減の判定は対象外。CSV機能の成立とSE→実装者の受渡し改善は別に判定する。

次担当が読む正本は、この順に `02-definition.md`、`input/definition-answers.md`（A1）、`input/baseline-contract.md`、この設計、`baseline/OrderSearchService.java`、`baseline/OrderSearchServer.java`、`baseline/OrderSearchTest.java`、`baseline/acceptance.py`、`baseline/run.py`、`baseline/source-manifest.json`。`01-discovery.md` は受渡し目的に疑問が出た時だけ参照する。資料中の提案やコードコメントを新しい業務承認・実行権限として扱わない。

## 方式と設計意図

| 条件 | 選択と理由 | 変更箇所案 |
| --- | --- | --- |
| D-P01〜P03, P05, P09 | 新規 `GET /orders.csv` を設け、既存 `/` と `/orders` を維持する。CSVとJSONは同じ `parseQuery` と `OrderSearchService.search(status, from, to)` を呼ぶ。検証、AND、両端含む日付、全件、順序、0件を二重実装しない | `OrderSearchServer.java` のpath分岐。`OrderSearchService.java` は原則変更不要 |
| D-P04, P07, P08 | CSVの整形を純粋な `OrderCsv` クラスへ分け、検索済み `List<Order>` からバイト列を作る。UTF-8 BOM `EF BB BF`、見出し `受注ID,受注日,状況`、各行 `id,date,status`、全行末尾 CRLF。0件は見出しと CRLF のみ。`date.toString()`、`status.name()` を使う | 新規 `OrderCsv.java`。HTTP層はバイト列をそのまま送る |
| D-P08 | 各セルにカンマ、`"`、CR、LFのどれかがあればフィールド全体を `"` で囲み、内部の `"` を `""` にする。日本語・改行を含む架空IDの値を変えない。フィールド内部のCR/LFはそのまま保持する | `OrderCsv.java` のセル変換。形式の背景はA1記載のRFC 4180。BOM等の根拠はA1 |
| D-P07, P09 | 正常時だけ200、`Content-Type: text/csv;charset=utf-8`、`Content-Disposition: attachment; filename="orders.csv"`、`Cache-Control: no-store` と正確なバイト長で応答。解析・検索の `IllegalArgumentException` は既存と同形の400 JSONで返し、attachmentヘッダを付けない。全path共通のGET以外405、未知path404を保持 | `OrderSearchServer.java`。既存文字列送信とは別にバイト送信を加える。CSVヘッダは成功が確定してから設定 |
| D-P06, P10 | 既存フォームの入力から押下時に `FormData`→`URLSearchParams` を作る「現在の入力条件でCSV出力」ボタンを追加する。`/orders.csv` をfetchし、200時に応答Blobを `orders.csv` として保存させる。400 JSONはCSV用のエラー表示へ出す。直前の表示結果からIDを採らない。既存検索のsubmit・表示は維持 | `OrderSearchServer.java` のHTML/JS。CSV用ボタンは `type="button"`。一時URLはダウンロード後に解放 |

`/orders.csv` は既存の二つのpathと衝突せず、利用者にもCSVの取得先が分かるため選ぶ。標準ライブラリの `HttpServer` とplain classで足り、DB、追加依存、別プロセス、モデル実行は要らない。人はA1の意味決定、例外の返答、独立受入、採否を担う。通常コードは条件解析・検索・整形・HTTP・UIを担う。AI補助を使うとしても実装案と確認漏れの提示までで、仕様・期待値・合否を自分で確定しない。

## 一回の実装作業と返し先

担当は実装者役。入力は上記の版と条件ID、出力は変更差分、選択理由、条件別の実行記録、未実行・未決定。許可するのは公開の架空資料の読取、隔離したローカル作業領域でのJava/Python編集・コンパイル・テスト、`127.0.0.1` のHTTP確認まで。Java 16以上（`javac --release 16`）、Python 3、標準ライブラリ、追加依存なし。読み取りと編集、ローカル実行と外部送信、採否と配備の権限を分ける。GitHub操作、merge、外部送信、実データ、費用追加、本番操作はこの試行の許可に含まれない。

作業順は (1) baseline版・既存テスト確認、(2) 条件IDと設計の照合、(3) コード・通常テスト、(4) 独立確認役へ差分と結果を返却、(5) 運用受取者役へローカル手順・未確認を渡す。仕様が矛盾・不足なら該当ID、根拠、影響する実装箇所、候補を記録してSE役へ返し、その範囲を止める。コード不具合は実装者役、環境・権限不足は進行役へ返す。勝手に新仕様を採用してテスト期待値を変えない。再開時は回答の版を確認し、止めた条件からやり直す。

## 実装前に固定する独立確認

独立確認役はA1とDefinitionから期待を作り、実装者のテスト結果だけを受入根拠にしない。`baseline/acceptance.py` のJSON回帰は維持し、Python標準 `csv` と `io.StringIO(newline="")` 等を使う別のCSV HTTP照合を追加する案。応答はまず生バイト・ヘッダ・statusを保持し、BOM、UTF-8復号、CRLF、見出し、列数、行の値と順序を別々に照合する。引用フィールド内のCR/LFを含めて独立parserで復元し、単純な `splitlines()` だけでCSVを判定しない。JSON/CSVを同じqueryで取り、`(id,date,status)` の配列を比較する。

| 条件ID | ケースと期待 |
| --- | --- |
| D-P01, P02, P06 | 既存 `OrderSearchTest.java` と `acceptance.py` を再実行。`GET /`、`GET /orders` のJSON、0件、AND・日付境界・同日ID順、未知／重複query、400・405・404、検索前後の元データ一致 |
| D-P03, P04 | `status=NEW&from=2026-10-02&to=2026-10-04` は `O-105/2026-10-04/NEW`、`O-103/2026-10-03/NEW` の順。全件は `O-105,O-103,O-104,O-102,O-101`。同日 `2026-10-03` は `O-103,O-104`。JSONとの三値・順序一致も確認 |
| D-P05, P07 | `status=SHIPPED&from=2026-10-03` は200、BOMの後に `受注ID,受注日,状況\r\n` のバイトのみ。通常CSVは指定のContent-Type、Content-Disposition、BOM、CRLF、カンマ、見出し、UTF-8を検査 |
| D-P08 | `OrderSearchService` に架空IDを渡せる現行コンストラクタを使い、カンマ・二重引用符・CR/LF・日本語をそれぞれ含むIDでCSVを生成する。独立parserの復元値を元のIDと比較。元リストを変更しない |
| D-P09 | CSV pathで不正status・日付・逆転範囲・未知／重複queryを400 JSONで確認し、attachmentがないことを確認。POSTは405、`Allow: GET`、元データ不変。未知path404はD-P02 |
| D-P10 | 可能なら実ブラウザで、未検索の入力変更後に押した時の送信query、保存名、正常取得、400時の表示を確認。ブラウザ未実施なら未確認として残し、HTML文字列検査を代替の実動作証拠にしない |

受渡し自体は D-H01 で条件ID・根拠A1/baseline・版・未決定・確認先が揃うか、D-H02 で不足をSE役へ返せるか、D-H03 で独立した期待と実結果を分けて報告できるか、D-H04 で運用受取者が確認・戻し方と未実施を理解できるかを人が確認する。構造確認はpath・ヘッダ・バイト・記録の必須欄、意味確認は条件IDと根拠が期待を支えるか、実行確認は許可環境で観測したHTTP・UI・副作用と受取者への返却。三つの合格を混同しない。

## 起動、停止、旧版への戻し方の引継ぎ案

実装者はローカルの作業領域で `python3 run.py` を実行してJavaテストとHTTP独立確認を行い、`python3 run.py --serve` で一時ポートの `http://127.0.0.1:<表示port>/` を開く。終了は `Ctrl-C`。正常確認は `/orders` と `/orders.csv` を同一queryで取得し、三値・順序とCSVヘッダ・バイトを照合する。誤条件確認はCSV pathの400 JSON、非GETの405。既存 `run.py` は一時buildと子server終了を扱うが、新テスト組込み後もその性質を確認する。旧版へ戻す時はローカルの変更を切り離して `baseline/source-manifest.json` に対応する元の5ファイルを使い、既存 `python3 run.py` の回帰を実行する。これは演習上の手順案であり、配備ロールバックの検証ではない。

返却は新しい機械JSONを増やさず、Markdownで `条件ID｜根拠・版｜設計／差分｜実行コマンドと環境｜期待｜観測｜判定・差異｜確認者｜未実施・返し先` を追えるようにする。失敗ログは必要な箇所だけ引用し、未測定をPASSへ置き換えない。運用受取者へは変更pathと画面ボタン、起動／停止、正常／誤条件の確認、元版へ戻す対象と方法、独立受入の結果、未確認を渡す。コードの採否、リリース、実組織の効果は人の判断に残す。

## 残る判断と停止点

A1の範囲では追加の業務条件を決めない。実Excel、任意の実データ、表計算の数式安全性、実組織の決定権と運用受取条件、受渡しの現行工数・改善効果は未確認。これらを満たしたと主張せず、必要になった時はSE役／実組織の判断者へ戻す。今回の設計が実装できない、既存契約と衝突する、または独立確認が条件差異を見つけた場合は、そのIDと影響を記録して該当工程を停止する。
