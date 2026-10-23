# fde

人、AI、システムが、それぞれの強みを活かして協働できる業務の仕組みをつくる。maakboなりの Forward Deployed Engineering を、Modelと実践知の両方から育てる公開リポジトリです。

## モデルを見る

### [システム開発業務を見る](examples/system-development/)

システムエンジニアを中心に、業務の期待を要件・設計・検証へつなぎ、運用へ渡す仕事を、会話を始めるための小さな例で確認できます。

### [FDEの業務モデルを見る](examples/maakbo-fde/)

FDEが何を目指し、誰と実現し、どんな業務で成り立っているのかを、MermaidのModelで見られます。

### [作業環境とAIエージェントを見る](examples/human-agent-workspace/)

iPad・iPhone・MacBookからChatGPTやCodexを使い、GitHubへ記憶と成果を残す作業環境を、1枚のアーキテクチャ図で見られます。

## 実務で試す

[相談から一件を試して仕事へ戻す](.agents/skills/discovery-facilitation/references/field-delivery-loop.md): 業務理解・対象選択・条件と責任・任せ方の設計・試行・評価・運用引継ぎを、同じ記録でつなぎます。

[機能追加を、要件定義からリリース準備まで進める](examples/field-delivery/order-search/README.md): 開発チームがAIと要件・設計・実装・テストを引き継ぐ、通常のシステム開発の一件。

[仕事を動かす条件を設計する](.agents/skills/workflow-design-facilitation/SKILL.md): 自動化の範囲、起動、値の受渡し、分岐と再開を一件で確かめます。

[業務フローで対話する](.agents/skills/business-flow-facilitation/SKILL.md): コンテキストの一つの業務から、現行・変更案・判断・差戻しを具体化します。

[AIエージェントと実装・テストを進める](examples/system-development/implementation/agent-assisted-flow.md): 調査から実装・テスト・修正を任せ、差分と結果をレビューする導入案。

[チームで使える仕事にする](.agents/skills/team-adoption-facilitation/SKILL.md): 使う人と受取者の懸念、役割、練習、支援、受渡し全体の効果を確かめます。

## モデルを作る

整理されていない事業や業務の話から、目的、業務、関わる人、情報、システムの関係をModelへ外に出します。Howだけでなく、その背景にあるWhyも残すことで、状況が変わったあとも新しいHowを考え直せるようにします。

- [AGENTS.md](AGENTS.md): このリポジトリで共有する作業原則
- [discovery-facilitation Skill](.agents/skills/discovery-facilitation/SKILL.md): 現場の話から、何を変えるべきか・AIが適切か・次に何を定義するかを見極める手順
- [AIへ任せる仕事の見立て](.agents/skills/discovery-facilitation/references/agent-feasibility.md): 作業・起動・委任・接続・効果・運用リスクを確かめる手順と記入欄
- [現場の協力から始めるDiscovery Prompt](.github/prompts/field-discovery-collaboration.prompt.md): ベテランなど実務担当者と、1案件の小さな対話から共通理解を育てる声かけと進め方
- [business-context-modeling Skill](.agents/skills/business-context-modeling/SKILL.md): 対話から業務Modelをつくる手順
- [architecture-modeling Skill](.agents/skills/architecture-modeling/SKILL.md): 人、AI agent、system、repository、service、boundaryの関係をArchitecture Viewにする手順
- [mermaid-diagram-authoring Skill](.agents/skills/mermaid-diagram-authoring/SKILL.md): Markdown内でMermaidを作る手順
- [mermaid-diagram-export Skill](.agents/skills/mermaid-diagram-export/SKILL.md): 明示的にSVG / PNGが必要な場合のexport手順
- [reader-facing-artifact-review Skill](.agents/skills/reader-facing-artifact-review/SKILL.md): 業務主体者に向けた文章・構成・図を、第三者レビューで仕上げる手順
- [templates](templates/): Business Context、Architecture Context、Flow、master mapの開始点
- [validator](scripts/validate_repository.py): public bundleとMermaid sourceの検証

### Quick start

通常のモデリングとauthoringにはPython 3.9以上を使います。

```bash
git clone https://github.com/maakbo/fde.git
cd fde
python3 scripts/validate_repository.py
```

AI Agentへは、整っていない言葉のまま渡せます。

何を変えるべきかから考えたい場合は、ひと言だけで始めます。

```text
この業務を改善したい。
```

Skillが自動で選ばれない環境では、次の短い明示形を使います。

```text
$discovery-facilitation この業務を改善したい。
```

エージェント側が、一度に一つずつ問いかけて現場の話を聞き、業務の見直し、ボトルネック、手段の比較、最初の対象、Definitionへの引き渡しまで支援します。利用者が長い依頼文を暗記する必要はありません。

業務そのものを可視化したい場合:

```text
Use the business-modeler agent.

この業務を一緒に整理してください。
まず普通の文章で捉え、関わる人・業務・情報・外部システムを見つけ、
必要なModelをMarkdown内のMermaidで作ってください。
```

## モデリングの流れ

```text
loose conversation
  -> Business Story and 5W2H
  -> concrete candidates
  -> input / transformation / output
  -> Purpose, Map, Context, or Flow View
  -> Markdown Mermaid
  -> reader-facing model
```

裏側では、候補、境界、命名、比較、未解決事項を厳密に扱います。公開するsampleには、業務を理解するためのModel、短い説明、関連するViewへの導線だけを残します。詳しくは[Reader-facing model artifacts](.agents/skills/business-context-modeling/references/reader-facing-artifacts.md)を参照してください。

## Working source and export

通常は、Markdown内のMermaid blockが唯一の編集sourceです。`.mmd`、SVG、PNGは自動で作りません。

固定assetや、実際の描画によるプレビュー・視覚レビューを依頼された場合は、export Skillを使います。確認用の画像は一時出力にし、公開するassetとは分けます。

```bash
npm ci
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py \
  examples/system-development/README.md --type context --allow-complexity --output-dir /tmp/fde-export
```

## Visual language

アイコンはプロジェクトの `.fde/config.json` で `maakbo`／`mdi` を選びます。このfdeは[maakboオリジナル](assets/icons/maakbo/README.md)、未設定の配布先は[MDI](https://iconify.design/icon-sets/mdi/)です。MDIは公式GitHubのSVGを既定で参照し、`mdi_source: "iconify"` でIconify APIも選べます。どちらもこのリポジトリのアイコン保存先に依存しません。Actor、Business、Information、External Systemなどの対応は共通レジストリで解決します。白背景、一律28×28pxのicon size、0.75pxのneutral lineを保ち、arrowは関係の向きが必要な場合だけ使います。

[アイコンの選び方と切り替え](.agents/skills/mermaid-diagram-authoring/references/icon-selection.md)と[両セットの図解例](examples/icon-sets/README.md)を参照してください。設定変更だけでは既存の図を書き換えません。

## Project status

これはFDEと業務モデリングを育てる初期の公開実践です。新しい型は、実際の利用から再利用性が見えたものだけをSkillとreferenceへ戻します。

## License

Repository code, original documentation, and the [maakbo icon family](assets/icons/maakbo/README.md) are MIT licensed. MDI icons are Apache-2.0 licensed with [upstream license information](.agents/skills/mermaid-diagram-authoring/references/mdi-license/README.md). Historical comparison assets retain [their archived third-party notices](experiments/mermaid-native-2026-10-13/THIRD_PARTY_NOTICES.md).
