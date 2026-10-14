# Material Design Icons — fixed local assets

Iconify形式のMaterial Design Iconsから、図解用12種類を取り出したローカルSVGです。**`@iconify-json/mdi@1.2.3` に固定**し、npm tarballのSHA-1とSHA-512 integrityを照合しました。Iconify APIへの描画時アクセスは不要です。

| 意味 | SVG | maakbo側の対応名 |
| --- | --- | --- |
| 人 | [account-outline.svg](account-outline.svg) | `user` |
| 業務 | [ellipse-outline.svg](ellipse-outline.svg) | `ellipse` |
| 情報 | [file-outline.svg](file-outline.svg) | `file` |
| システム | [application-outline.svg](application-outline.svg) | `server` |
| 判断 | [rhombus-outline.svg](rhombus-outline.svg) | `diamond` |
| AI | [robot-outline.svg](robot-outline.svg) | `bot` |
| リポジトリ | [source-repository.svg](source-repository.svg) | `folder-git-2` |
| 外部サービス | [cloud-outline.svg](cloud-outline.svg) | `cloud` |
| 会話 | [message-outline.svg](message-outline.svg) | `message-square` |
| タブレット | [tablet.svg](tablet.svg) | `tablet` |
| スマホ | [cellphone.svg](cellphone.svg) | `smartphone` |
| PC | [laptop.svg](laptop.svg) | `laptop` |

システムはインフラに寄せず、汎用アプリの輪郭を使います。`source-repository` は「履歴を持つソース保管庫」という記号で、maakboの3地点の分岐とは形が異なります。従来のフォルダという読みも弱くなるため、下ラベルでリポジトリの意味を確定してください。

全原本は24×24 viewBox、透明背景、既定色 `#25231F`。SVGのbodyは固定packageの `icons.json` から**そのまま保持**し、SVG外枠とtitle、既定色だけを付けました。MDIのoutlineは塗りの輪郭で、maakboの細線とは構造が異なります。`stroke-width`を付けて細くする加工はしていません。

## 固定版と再現

[source.json](source.json) にpackage名・版・tarball integrity・SHA、入力icons.jsonのSHA-256、全12bodyとSVGのSHA-256、対応表を記録しています。再現するときは `@iconify-json/mdi@1.2.3` の `icons.json` から指定名のbodyを取り出し、各SVGのtitle以降に同じbodyを保持します。ライセンス文の取得先も固定URLとSHAで記録しています。

Mermaidの使用URLは次の公開済み基底へSVG名を加えます。全12 SVGの取得とGitHubでのMermaid実表示を確認しています。

```text
https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/mdi/
```

## ライセンス

このセットのアイコンデータはpackageおよびicon-set metadataで **Apache-2.0** と宣言されています。maakboオリジナルのMIT Licenseとは別です。

[LICENSE](LICENSE) にApache License 2.0全文、[UPSTREAM-LICENSE](UPSTREAM-LICENSE) に固定版 `MaterialDesign-SVG v7.4.47` のPictogrammers Free Licenseを内容変更なしで保持しています。[NOTICE](NOTICE) と [source.json](source.json) は取得元と加工の範囲を記録したローカルの出典情報です。固定版のupstream NOTICEパスは存在しませんでした。

上流の説明では、アイコンとフォントはApache系、アイコン以外のコードはMITと区別されています。上流のライセンス説明も含め、再配布時はこのフォルダの権利・出典情報を保持してください。
