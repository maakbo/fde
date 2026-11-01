# 分岐Skillの別条件適用（先に置いた期待）

- 対象: 架空の開発チームによる受注一覧の検索条件UI追加。条件版は独立の v2。実チームの許可・承認は仮定しない。
- 実行前の期待: 閾値7は一致を含む。互換性影響なし (`false`) なら点数6は標準、7と8は詳細。点数0も有効な標準。`ui`/`api`/`data` は各同名の `*-review` 準備経路へ進む。これは人のレビュー完了や通知を意味しない。
- 資料の期待: `allowed=true`、対象scope一致、`approved`、版v2を全て満たす資料だけ選ぶ。参照不可、旧版、scope違いはそれぞれ理由を残す。同一ID衝突は選別前に確認待ちに戻す。全件除外も準備済みとしない。
- 例外の期待: null点数/互換性は不正、未知区分は未知として停止、取得不能は手動取得案を伴って停止。どの停止経路でも作業ID/版を保持し、承認権限・人の確認待ちを付けない。
- 再評価の期待: 同じpayload/policyを二度評価して同一結果。入力は変えない。
- 未実施と境界: このコードに保存、通知、権限判定、実資料取得、実レビューはない。保存後失敗、通知失敗、返却経路失敗、実際の許可不足はこの試行で検証できず、呼出側・実装設計で別途確認が必要。

## 実行結果

実行前の期待を上に固定。以下に実測を追記する。
### 実行環境・照合

- 2026-11-01、ローカルの公開checkout 公開リポジトリ の未commit版 `review_branch.py` を Python 3.9.12 で直接 import して実行。`PYTHONDONTWRITEBYTECODE=1`。公開checkoutは変更していない。
- 独立条件 v2: `full_review_from=7`、`source_version=v2`、既存と同名の api/ui/data 経路。UIの混合集合は U2（現行・許可・UI）、A-denied（参照不可・API）、D-old（旧版・Data）、A-v2（現行・API）。
- 10ケースの照合はすべて期待どおり。UIの6点と0点は標準、APIの7点とDataの8点は詳細。混合集合では U2 のみ採用し、他3件には参照不可・scope違い・旧版の該当理由を個別に返した。同一ID衝突は `clarification_needed`、全件除外は `sources_excluded`、null点数とnull互換性は `invalid_input`、未知区分は `unknown_category`、取得不能は `source_unavailable` と手動取得理由を返した。
- 各ケースで `retained_work={id: ORDER-SEARCH-9, revision: r3}`、`authorization=false`。準備成功だけ `pending_human_review=true`。同一payload/policyを二度評価した結果は一致し、入力の変更もなかった。保存、通知、人の承認、実資料取得、実接続、現場効果は未実施・未測定。

### 追加の境界ケースで見つかった問題

- **P2候補**: `source_retrieval` を省略し、妥当な資料メタデータを添えると `review_packet_ready` になる。`null` または `unknown` を渡すと `invalid_input` になる。`branch-intake.md` の値契約では取得状態は available と資料リスト、または unavailable とされる。Skillも未指定と確定値の区別を要求する。取得状態を証明できない呼出しが準備完了へ進むため、省略時の扱いを契約で明示し、必要なら停止させるべき。
- 前回のP2は手順6で各該当例外経路の確認IDまたは未検証理由・影響を要求し、設計書にも追跡欄が追加されたため、Skillと型の指示としては解消。今回の純粋関数では保存・通知・実権限の経路は存在せず、その実装結果の保証はできない。

## 修正後の独立再試行

- 修正前: `source_retrieval` 未指定かつ妥当な資料メタデータで `review_packet_ready` / `ui-review` を返した。取得状態を証明できない入力を準備済みにしていた。
- 修正後: 同一入力で `invalid_input` / `invalid_source_retrieval_state`、`route=null`、`selected_source_ids=[]`、`pending_human_review=false`、`authorization=false` を返した。明示の `null` と `unknown` も不正のまま。
- 元の別条件10ケースを同じ期待で再実行して全件一致。混合資料の採否理由、閾値6/7/8、false/0、同一ID衝突、全件除外、null、未知区分、取得不能は退行なし。同一payloadの二度評価も同一結果で入力不変。
- 再現スクリプト: `examples/design-preparation/branch-lab/test_forward.py`。公開cloneのルートで `PYTHONDONTWRITEBYTECODE=1 python3 examples/design-preparation/branch-lab/test_forward.py` を実行し、Python 3.9.12 で12テスト全件PASS。コード内にローカル絶対パスを埋めていない。`--module` で対象コードを別パス指定できる。
- 修正されたSkillの手順2は、既定値のない必須値を他の情報から推定して正常扱いしないと明記。手順6と型の各例外経路追跡も維持。今回確認した例・コード・Skillに残る重大な指摘はない。
- 制限: 単体の決定関数のみの確認。人のレビュー、実資料アクセス権、保存、通知、実接続、本番効果は行っておらず、実施済みとは扱わない。

[レビュー準備の実践](branch-practice.md) / [別条件の再現テスト](branch-lab/test_forward.py)
