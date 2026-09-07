# `business-context-modeling` 評価メモ — ウォーターフォール型システム開発

このファイルは reader-facing model ではなく、Skill を鍛えるための評価メモです。

## 1. 今回のケースで見えてきた強み

### 抽象→具体の親子トレースは機能している
Layer 2 の工程を固定したうえで、代表工程を Context と Flow へ展開すると、上位の一語が実際には複数の transformation を含むことが見えやすい。

特に以下は、単純な工程表からは見えにくい。

- 要件定義: 現行理解 → 業務要件化 → システム責務化 → 合意
- 実装・単体: コード化 → 単体検証 → 他者検証 → 統合可能化
- 外部結合: 接続成立 → 契約確認 → 境界切り分け → 復旧確認
- 導入: 実施判断 → 本番反映 → 本番確認 → 復旧 / 運用移管

### Flow を分けることで「戻り」が自然に出る
ウォーターフォールを直線で描くと現実から離れるが、Context と Flow を分けることで、工程自体は上位の共通言語として保ちながら、差戻し・再試験・再合意・ロールバックを下位へ置ける。

### Actor を肩書きで終わらせない圧力が働く
Context ごとに直接参加する Actor だけを選ぶため、「PMは全部に関係するから毎図に置く」のようなノイズを避けやすい。

## 2. Skill の弱点 / 改善候補

### 2.1 Phase と Business Use Case の区別をもっと明示したい
今回の Layer 2 はユーザー指定で「工程」を固定した。しかし `business-context-modeling` の語彙では Business Use Case と Business Activity を中心にしている。

そのため、Skill に以下の扱いを明文化するとよい。

- phase / stage / lifecycle step は、ユーザーが共有している上位索引として保持してよい
- ただし phase 名をそのまま transformation 名とみなさない
- 下位 Context を作った結果、phase の境界を跨ぐ Business が見つかることを許容する
- 横断 Business を無理に一工程へ所属させない

### 2.2 Information と technical artifact の境界が曖昧
`ソースコード`、`ビルド成果物`、`環境設定`、`証明書`、`テストエビデンス` などは、業務上参照・判断される一方で技術 Artifact でもある。

現 Skill の Information 定義だけで扱えるが、ケースが技術寄りになるほど違和感が出る。

改善候補:

- Information の中に business concept と technical artifact の subkind を持つ
- あるいは Architecture Modeling 側の Artifact と Business Context の Information の投影ルールを定める
- 「ファイルだから Information」ではなく「判断対象として名前が付いているから Information」という既存原則は維持する

### 2.3 Environment を External System とする基準が必要
開発環境、外部結合環境、UAT環境、本番環境を `x_` として置いたが、厳密には system / runtime environment / deployment target が混在する。

改善候補:

- Business Context の external boundary として「Business が直接働きかける runtime surface」は x_ へ投影可能、と明記する
- Architecture View では environment / service / platform をより厳密に分ける
- Business Context から Architecture Context へ深掘りする切替条件を定める

### 2.4 Tool と Business の混同を検知したい
CI/CD、Git、コードレビュー基盤、テスト管理ツールは Business を自動化・支援するが、図に置くと主語に見えやすい。

改善候補:

- External System node が Business backbone の複数 activity を連続して支える場合、「System が仕事そのものに見えていないか」を smell として出す
- Business の executor は原則 Actor とし、自動化主体を表したいときは Architecture Modeling へ切り替える判断基準を示す

### 2.5 横断 Business の表現がまだ弱い
変更管理、品質保証、構成管理、環境管理、プロジェクト統制は複数工程へ横断する。

13工程と同じ Business Map へ混ぜると粒度が崩れ、各 Context へ毎回入れるとノイズになる。

改善候補:

- lifecycle axis と cross-cutting Business を分けた supporting View を許容する
- Cross-cutting Business がどの Layer 2 Business に関係するかを matrix で持つ
- Context ではその scene の意味を変える横断 Business だけを投影する

### 2.6 Context の Business backbone が「順番」に見えやすい
複数 Business を中央に並べると、`---` でも人は左→右の工程順として読む可能性が高い。

改善候補:

- Context の説明文で「continuity / relationship であり exact sequence ではない」をより強くする
- exact sequence を読みたくなる Business 名が3つ以上並んだ場合、Flow の追加を促す smell を検討する

## 3. 今回のモデル自体でまだ未解決の論点

### 要件定義
- システム企画、業務主管、BA、アーキテクトの責任境界
- 非機能・運用・移行・セキュリティ要件を一つの Context に入れるか分けるか
- 「受入条件」は要件定義の出力か、UAT設計時に具体化される Information か

### 基本設計 / 詳細設計
- 外部仕様 / 内部仕様による境界だけで実務を十分に表せるか
- 論理データモデルは基本設計、物理データモデルは詳細設計という一般化が妥当か
- アーキテクチャ設計を基本設計の一活動として置くと狭すぎないか

### 実装・単体
- 実装と単体テストを一つの Layer 2 とする利点と欠点
- CIによる build / unit test / static analysis を別 Business とするか
- `ビルド成果物` を Information として扱うか

### 各テスト工程
- テスト設計とテスト実施を工程として分ける上位構造は自然だが、下位 Business の共通化をどこまで行うか
- 不具合切り分けを各テスト工程内に置くか、横断 Business に寄せるか
- テストエビデンスを独立 Information とする必要があるか

### UAT
- UAT は「テスト」より「業務受入判断」の Business Use Case として再命名した方が自然か
- ユーザー要望と不具合の分類 Business をどこへ置くか

### 導入
- 導入の完了点を本番反映、業務確認、運用移管、初期流動終了のどこに置くか
- ロールバックは導入 scene の一 Business か、リリース管理の横断 Business か

## 4. 次にモデルを増やすなら

代表4工程で Skill の特性は十分見え始めている。次の量的拡張は、闇雲に13工程すべての図を作るより以下の順が有効。

1. 基本設計 Context — Information の粒度と architecture の境界を評価
2. システムテスト Context — E2E / 非機能 / 運用観点を同じ scene に置けるか評価
3. UAT Context — 「テスト」から「受入判断」への semantic compression を評価
4. 変更管理 Context — 横断 Business の扱いを評価
5. 13工程 × Actor / Information / External System matrix — master と Context 投影の一貫性を評価

## 5. 今回の評価で大事にすること

完成度の高い「教科書」を作るより、ユーザーが実務経験から

- この名前は違う
- この責任はこの人ではない
- この情報はもっと前からある
- この工程境界を跨いでいる
- このツールは業務ではない
- この流れはもっと戻る

と具体的に指摘できるモデルを作る。

その指摘が Skill の naming / boundary / classification / projection rule の改善へ戻れば、この評価ケースの目的を果たしている。
