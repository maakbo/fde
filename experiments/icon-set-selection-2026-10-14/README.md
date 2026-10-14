# プロジェクトのアイコンセット選択

2026-10-14。公開する図解スキルについて、配布先がmaakboオリジナルかIconify MDIを選べる共通設定を採用しました。ユーザーは同時に旧Lucideフォルダと不要なルート第三者通知の削除を承認しています。

## 選択と所有

- `.fde/config.json` の `icon_set` は `maakbo`／`mdi`。fde自身はmaakbo、未設定の配布先はMDI。
- インストールの `--icon-set` は初期値を選びます。既存の選択は優先され、設定の他のキーも保持されます。
- 設定ファイルは配布のmanaged manifestに含めません。ビルダーとインストーラもmanaged configを拒否します。更新は既存の図と設定を書き換えません。
- 新規作成は `icon_registry.py create`、対応の確認は `show`、設定変更は `configure`。
- 既存の図は明示URLからfamilyを推定します。1図での混在や指定familyとの不一致は拒否し、URL置換は明示的な `migrate` に分離しました。

## 共通の意味と配布

人・業務・情報・システム・判断・AI・リポジトリ・外部サービス・会話・端末の対応、寸法を `icon-sets.json` に集約しました。コンテキスト、フロー、アーキテクチャ、マスター図、マスター参照の検証と画像出力が同じregistryを使用します。

MDIは固定版 `@iconify-json/mdi@1.2.3` の12種類を変更せず使用。元packageのintegrity、図形とSVGのSHA、ライセンスの取得元を `assets/icons/mdi/source.json` に記録しました。maakboのMIT、MDIのApache-2.0と上流の表示をそれぞれの素材フォルダに含めています。

`assets/icons/lucide-thin/` と `scripts/sync_icon_aliases.py` を削除。ルート `THIRD_PARTY_NOTICES.md` も削除しました。過去の比較SVGに埋め込んだ旧素材に必要な表示は、`experiments/mermaid-native-2026-10-13/THIRD_PARTY_NOTICES.md` に保存しています。

## 検証

- 全リポジトリvalidator：PASS。
- maakboの線幅・ローカル埋め込みの回帰3件と、両セット・設定・配布・マスター参照の回帰9件：PASS。
- 配布ZIPの59 managed filesに両familyの12 SVG、ライセンス、registryと手順が含まれ、project configは含まれないことを確認。
- ZIPを展開して新規consumerへインストールし、MDIでモデルを作成・検証：PASS。
- 同じMarkdownの図を両familyで描画し、7画像ノードずつの埋め込みと目視表示を確認。ソースを出力後に補正していません。
- 素材と切り替えUXのデザイナー役による読み取りレビュー：must-fixなし。
- `git diff --check`：PASS。

公開用の利用例は `examples/icon-sets/README.md`、共通手順はauthoring Skillの `references/icon-selection.md` です。

## 公開確認

実装commit `8497896` をmainへ反映しました。途中でmainへ入ったFDE例の1ページ統合（`ba960eb`）を保持し、検証スクリプトの競合は新しいセクション検証とMDI検証の両方を残して解消しています。統合後の全validatorもPASSです。

- 公開した24 SVGと両LICENSEのraw URLはHTTP 200で、ローカルファイルと完全一致。
- 公開revisionで旧Lucide SVGとルート第三者通知が存在しないことをHTTP 404で確認。
- GitHubのMermaidでmaakboとMDIの両使用例を確認。各7画像ノードが選んだfamilyのURLを使い、図形も正しく表示。

[切り替え方法](https://github.com/maakbo/fde/blob/main/.agents/skills/mermaid-diagram-authoring/references/icon-selection.md)・[比較と使用例](https://github.com/maakbo/fde/tree/main/examples/icon-sets)
