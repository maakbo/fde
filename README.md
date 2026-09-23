# fde

人、AI、システムが、それぞれの強みを活かして協働できる業務の仕組みをつくる。maakboなりの Forward Deployed Engineering を、Modelと実践知の両方から育てる公開リポジトリです。

## モデルを見る

### [システム開発業務を見る](examples/system-development/)

システムエンジニアを中心に、業務の期待を要件・設計・検証へつなぎ、運用へ渡す仕事を、会話を始めるための小さな例で確認できます。

### [FDEの業務モデルを見る](examples/maakbo-fde/)

FDEが何を目指し、誰と実現し、どんな業務で成り立っているのかを、MermaidのModelで見られます。

### [Human–Agent Workspaceを見る](examples/human-agent-workspace/)

人、AI collaborator、private control plane、public reuse surfaceの関係とhandoffを、
Architecture OverviewとInteraction Flowで見られます。

## モデルを作る

整理されていない事業や業務の話から、目的、業務、関わる人、情報、システムの関係をModelへ外に出します。Howだけでなく、その背景にあるWhyも残すことで、状況が変わったあとも新しいHowを考え直せるようにします。

- [AGENTS.md](AGENTS.md): このリポジトリで共有する作業原則
- [business-context-modeling Skill](.agents/skills/business-context-modeling/SKILL.md): 対話から業務Modelをつくる手順
- [architecture-modeling Skill](.agents/skills/architecture-modeling/SKILL.md): 人、AI agent、system、repository、service、boundaryの関係をArchitecture Viewにする手順
- [mermaid-diagram-authoring Skill](.agents/skills/mermaid-diagram-authoring/SKILL.md): Markdown内でMermaidを作る手順
- [mermaid-diagram-export Skill](.agents/skills/mermaid-diagram-export/SKILL.md): 明示的にSVG / PNGが必要な場合のexport手順
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

固定assetが明示的に必要な場合だけ、export Skillを使います。

```bash
npm ci
python3 .agents/skills/mermaid-diagram-export/scripts/export_mermaid.py \
  examples/system-development/README.md --type context --output-dir /tmp/fde-export
```

## Visual language

Actor、Business、Information、External Systemには、リポジトリ内のthin Lucide iconを使います。白背景、固定icon size、0.75pxのneutral lineを保ち、arrowは関係の向きが必要な場合だけ使います。

## Project status

これはFDEと業務モデリングを育てる初期の公開実践です。新しい型は、実際の利用から再利用性が見えたものだけをSkillとreferenceへ戻します。

## License

Repository code and original documentation are MIT licensed. Icons remain under their upstream licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
