# 照合候補の確認ゲート

架空のレビュー依頼について、[前回の候補出力](../prompt-outputs.json)を再生し、構造/入力対応の検査から確認待ち・訂正・拒否へ進めるローカル試作です。コード内のreviewer-Aと確認記録は**架空のfixture**で、実人の本人確認/権限証明/同意ではありません。

[試したい条件](../poc-intake.md) / [実行結果と限界](../poc-results.md) / [設計業務の全体](../README.md)

## 動かす

Mac/Linuxでリポジトリのルートから実行します。前回の検証用環境があれば再利用できます。

```bash
python3 -m venv /tmp/fde-poc-check
/tmp/fde-poc-check/bin/python -m pip install jsonschema==4.26.0
/tmp/fde-poc-check/bin/python -m unittest discover -s examples/design-preparation/poc-lab -p 'test_*.py' -v
/tmp/fde-poc-check/bin/python examples/design-preparation/poc-lab/review_gate.py --case-id E2
/tmp/fde-poc-check/bin/python examples/design-preparation/poc-lab/replay_cases.py
/tmp/fde-poc-check/bin/python examples/design-preparation/poc-lab/check_boundaries.py
```

[保存した再生結果](replay-results.json)は最後のコマンドの出力です。モデルを生成実行せず、送信・登録・通知もしません。ネット接続機能はありませんが、OS/ネットワークの隔離や本番権限の制御を検証する試作ではありません。

## 処理と状態

入力のcase_idは、この試作のテストケースを識別するために使います。実業務のレビュー依頼の必須欄を追加する意味ではありません。実業務に必要な入力/権限の確定は別に残っています。

[review_gate.py](review_gate.py)のevaluateは、入力→既存schema/限定的な根拠対応→架空の確認記録の順に調べます。validでも確認がなければpending_review。記録が同じ対象に結び付き、演習の役/判断/理由が合う時だけ、use_as_review_draft、return_for_correction、rejectを返します。use_as_review_draftはレビュー資料の下書きまでで、受付・設計承認・実装開始ではありません。

入力/候補/契約を正規化JSONのhashへ結び、対象変更後の旧記録を流用しません。hashや役名は認証・署名ではなく、値が同じかを調べるものです。確認記録の作成関数も任意の呼出し元が使える演習用であり、信頼できない依頼者からの自己承認を防ぐサービスには使えません。

reviseは元と訂正後の候補を別スナップショットにし、理由/版とともに返します。訂正後は再検査して確認待ちへ戻ります。永続的な履歴保存、複数人の実認証、同時更新/競合、期限/失効、資料管理の権限連携は未実装です。契約引数は信頼するコード側のSCHEMA-v2を前提とし、任意の外部schemaを受けるAPIではありません。

型と根拠の所在が合っても、根拠の意味/見落とし/正本・発効版や権限は確認できません。自由文の偽承認は確認前には使用可能へ進みませんが、架空の確認記録を与えれば意味が不正でも通り得ます。実人が正しく確認できるかは別に検証が必要です。

[独立した境界検査](check_boundaries.py)は126のJSON型変異と、資料版・候補・契約の3変更を同じ条件から試します。[保存した結果](boundary-results.json)は例外と誤った使用可能化が0だった記録で、任意の入力や実認証の安全性を保証しません。
