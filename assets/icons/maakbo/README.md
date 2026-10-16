# maakbo diagram icons

図解の人・業務・情報・システムなどを、手で描き直せる少ない線で表す12種類のオリジナルSVGです。ユーザーが選択した形と大きさの調整を反映し、fdeの図解用素材として採用しています。

配布先では `.fde/config.json` の `icon_set` を `maakbo` にすると、新しい図でこのセットを使用できます。未設定の配布先はMDIです。[共通の選択・切り替え方法](../../../.agents/skills/mermaid-diagram-authoring/references/icon-selection.md)を参照してください。

## アイコンと使用寸法

Mermaidの正方形ノード枠の寸法です。SVG原本はすべて24×24 viewBoxで、下ラベルと組み合わせます。

| 意味 | SVG | 使用枠 | 形全体の倍率 |
| --- | --- | --- | --- |
| 人 | [user.svg](user.svg) | 28×28 | 1.05 |
| AI | [bot.svg](bot.svg) | 28×28 | 0.96 |
| 業務 | [ellipse.svg](ellipse.svg) | 28×28 | 1.03 |
| 判断 | [diamond.svg](diamond.svg) | 28×28 | 0.93 |
| 情報 | [file.svg](file.svg) | 28×28 | 1.00 |
| システム | [server.svg](server.svg) | 28×28 | 1.00 |
| リポジトリ | [folder-git-2.svg](folder-git-2.svg) | 28×28 | 1.08 |
| 外部サービス | [cloud.svg](cloud.svg) | 28×28 | 1.00 |
| 会話 | [message-square.svg](message-square.svg) | 28×28 | 1.00 |
| PC | [laptop.svg](laptop.svg) | 28×28 | 1.00 |
| スマホ | [smartphone.svg](smartphone.svg) | 28×28 | 1.00 |
| タブレット | [tablet.svg](tablet.svg) | 28×28 | 1.00 |

全12種類の使用枠を28×28pxに統一しています。見た目のバランスはSVG内部の倍率と重心補正で保ち、種類ごとのノード寸法は変えません。[制作比較の一覧](../../../experiments/maakbo-original-icons-2026-10-13/full-set.png)は採用前の寸法による履歴です。

## 採用した形

人は大きめの頭と小さめの肩。AIは軽い角丸の頭と縦向きの目。情報は軽い角丸と折り返し付きの紙、システムは短い状態表示付きの枠です。業務は少し縦にふっくらした横長楕円、端末は汎用的な角丸の輪郭です。

リポジトリは**上から下へ読む3地点と直線2本**。右の地点は上下の地点の中間に置き、上下への追加線はありません。`folder-git-2.svg` は参照互換のためのファイル名で、図形にはフォルダを使っていません。

## SVG仕様

- 正方形24×24 viewBox、透明背景、塗りなし、round cap / join。
- `currentColor` と既定色 `#25231F` を併記。単独の画像でもneutral inkで表示します。
- 表示線幅はviewBox上で **1.15相当**。内部groupを拡縮する素材は `stroke-width = 1.15 / scale` と逆補正し、形を大きくしても線が太くならないようにしています。
- 標準SVGのtransformを使い、`vector-effect`には依存しません。人の頭と肩の比率、端末の縦横比、リポジトリの丸の比率を保った均等拡縮です。

## Mermaidで利用するURL形式

このリポジトリのmainで公開しているraw URLの基底は次の形式です。全12 SVGの取得とGitHubのMermaid実表示を確認しています。

```text
https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/
```

ノードの指定例：

```text
a_requester@{ label: "依頼者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
```

既存のラベル・関係線・間隔の規約は、図解スキルのテンプレートを参照してください。

## 制作原本とライセンス

再生成する原本は [generate_full_set.py](../../../experiments/maakbo-original-icons-2026-10-13/generate_full_set.py) です。`GLYPHS` が形、`BALANCE` が倍率と重心補正です。承認済み制作原本の `maakbo-handdrawn/` から、このフォルダへSVGとLICENSEを内容変更なしで昇格しました。

[サイズ調整の説明](../../../experiments/maakbo-original-icons-2026-10-13/optical-balance.md)と[手書きの順序](../../../experiments/maakbo-original-icons-2026-10-13/handwriting-guide.md)も参照できます。

この12 SVGは [MIT License](LICENSE) で配布します。制作方法と確認の範囲は [PROVENANCE.md](PROVENANCE.md) に記録しています。
