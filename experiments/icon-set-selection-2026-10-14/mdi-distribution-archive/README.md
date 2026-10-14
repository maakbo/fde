# Previous local MDI distribution — metadata archive

2026-10-14。MDIをfde内の画像として配布する初回実装を、Iconify直接参照へ変更した際の出典・ライセンス履歴です。**現在のMDI配布方式を定義するものではありません**。

旧 `assets/icons/mdi/` から、次の4ファイルを内容変更なしで保存しました。

- `LICENSE`：Apache License 2.0全文。
- `UPSTREAM-LICENSE`：MaterialDesign-SVG v7.4.47のPictogrammers Free License。
- `NOTICE`：旧固定package由来のローカル出典記録。
- `source.json`：`@iconify-json/mdi@1.2.3`、tarball integrity・SHA、旧12図形のbody/SVGのSHAと対応表。

SVG・PNG・packageデータはこの履歴フォルダへ保存していません。source.json内の図形SHAは旧方式の記録であり、現在のAPI応答の照合用ではありません。

現行のライセンス情報は [MDI直接参照の記録](../../../.agents/skills/mermaid-diagram-authoring/references/mdi-license/README.md)を参照してください。Iconify APIの図形は更新され得るため、この固定packageの版を現在のAPI図形の版とみなしません。
