# MDI direct-reference license information

MDIはfde内に画像を配布せず、Iconifyへ直接参照します。

```text
https://api.iconify.design/mdi/{icon-name}.svg
```

図解の参照先とライセンス情報を分け、このフォルダには**ライセンス文のみ**を保持しています。SVG・PNG・アイコンのJSONデータは含みません。

## 出典とライセンス

Material Design Iconsの作者はPictogrammersです。上流のPictogrammers Free Licenseは、アイコンとフォントにApache系のライセンス、アイコン以外のコードにMITを適用すると説明しています。アイコンの基本ライセンスはApache-2.0で、個別の再配布元に別ライセンスがある場合はその条件も適用されます。

- アイコンコレクション：[Material Design Icons](https://github.com/Templarian/MaterialDesign)
- 上流ライセンス：[MaterialDesign/LICENSE](https://github.com/Templarian/MaterialDesign/blob/master/LICENSE)
- 配信元：[Iconify API](https://api.iconify.design) / [APIの説明](https://iconify.design/docs/api/)
- 一般ライセンス：[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

[LICENSE](LICENSE) はApache License 2.0全文。[UPSTREAM-LICENSE](UPSTREAM-LICENSE) は2026-10-14に取得・確認した[MaterialDesign-SVG v7.4.47のPictogrammers Free License](https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/LICENSE)の原文です。この固定版は**ライセンス説明文の取得版**であり、Iconify APIが返す図形のバージョンを固定するものではありません。

## API参照とexport

通常の図解はIconify URLを原本に保持します。APIの図形は更新され得るため、特定のpackage版や図形のSHAに固定されているとは扱いません。以前の `@iconify-json/mdi@1.2.3` の確認結果も、現在のAPI応答そのものの版や権利についての証明には使用しません。

exportで取得したSVGを図の中へ埋め込み、その図を再配布する場合は、MDI由来の図形が含まれることを記録し、Apache Licenseと上流の権利・出典表示を保持してください。このフォルダのLICENSE、UPSTREAM-LICENSE、および本出典情報を添付する形で保持できます。取得した素材に追加の通知があれば、それも保持してください。

MDIのライセンス表示は、maakboオリジナルのMIT素材とは別に保持します。
