# FDEの進め方

FDEは、現場を見えるようにするだけで終わりません。

現場を理解し、変える価値のある対象を選び、AIへ渡せる形まで業務を定義し、人・AI・システムの協働を設計し、小さく検証し、現場で使いながら育てます。

このページだけで、その流れを最初から最後まで読めます。

## モデル

```mermaid
---
title: FDEの進め方
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 60
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  b_discover@{ label: "対象を見極める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_define@{ label: "業務を定義する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_design@{ label: "協働を設計する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_validate@{ label: "小さく検証する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_embed@{ label: "根づかせ育てる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_discover --> b_define
  b_define --> b_design
  b_design --> b_validate
  b_validate --> b_embed

  class b_discover,b_define,b_design,b_validate,b_embed activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## このモデルが表していること

五つは5Dモデルの考え方をFDEの仕事として読み替えたものです。

**Discovery → Definition → Design → Development & PoC → Deployment & Scale** を、FDEでは **対象を見極める → 業務を定義する → 協働を設計する → 小さく検証する → 根づかせ育てる** と捉えます。

ただし、一方向に流して終わる工程ではありません。検証で分かったことからDefinitionへ戻り、利用後のOutcomeからDiscoveryを見直すなど、現場で学びながら何度も往復します。

## 1. 対象を見極める — Discovery

最初から「どこへAIを入れるか」は考えません。まず現場を見て、何が本当の課題なのかを捉えます。

業務の流れだけでなく、時間がかかるところ、待ち、手戻り、ミス、属人化、反復作業、判断の集中などを確認します。そのうえで、不要な作業はなくせないか、統合できないか、順番を変えられないか、もっと単純にできないかを先に考えます。不要な業務をAI化しないためです。

それでも残るボトルネックについて、人が担う方がよいか、ルールで処理できるか、RPAが向くか、AIエージェントが向くかを見極めます。

AIエージェントの候補は、次を合わせて判断します。

- **効果**: 工数、品質、速度、属人性、顧客や利用者への価値がどれだけ変わるか。
- **実現可能性**: 必要なデータや知識があるか、技術的に成立するか。
- **リスク**: 正確性、セキュリティ、法務、倫理、業務影響を許容できるか。
- **AI適合性**: 判断や例外対応が必要で、AIの強みを活かせるか。

100%の正確性が必須の判断、共感そのものが価値になる仕事、扱えない極秘データ、物理操作が中心の仕事などは、AIエージェントとの適合性を慎重に見ます。

### この段階で残すもの

- 現状の業務と課題
- ボトルネック
- 不要・統合・変更・単純化できる仕事
- 人 / ルール / RPA / AIエージェントの候補
- 効果・実現可能性・リスク
- 優先して扱う対象と、その理由

## 2. 業務を定義する — Definition

対象を選んだら、その業務をAIや実装担当者へ渡せる粒度まで理解します。

業務フローだけでなく、誰が関わり、どんな情報を使い、何を判断し、どんな例外があり、前後の仕事とどうつながっているかを見えるようにします。

特に重要なのが**暗黙知の表出**です。熟練者の勘や「普通こうする」という判断を暗黙のまま残すと、人とAIの責務境界を決められません。会話とモデルを行き来しながら、判断基準、例外、前提を言葉にします。

そのうえで、次を定義します。

- **対象業務**: 今回変える範囲。
- **対象外**: 今回は扱わない範囲。
- **機能要件**: AIや仕組みに何をさせるか。
- **非機能要件**: どの速度、品質、安定性などを求めるか。
- **制約条件**: 法令、社内ルール、扱ってはいけない情報など。
- **前提条件**: データ形式や既存システムの状態など、設計成立の前提。
- **合格基準**: 何を満たせば次へ進めるか。

FDEが一人で完成仕様を作るのではなく、**現場・実装担当者・専門家が具体化できる叩き台**をつくることを重視します。

### この段階で残すもの

- 業務モデル
- 判断・例外・暗黙知
- 人とAIへ分ける候補
- 対象 / 対象外
- 機能要件 / 非機能要件
- 制約 / 前提
- 合格基準

## 3. 協働を設計する — Design

Definitionで「何を実現するか」が見えたら、「どう実現するか」を設計します。

まず、人、AIエージェント、RPA、既存システムの役割を分けます。AIの自律性も高ければよいわけではなく、反応、支援、協働、自律のどこが今の業務に合うかを考えます。

AIエージェントを使う部分では、次を具体化します。

- **Context**: 目的、前提、制約、参照情報、判断例。
- **Trigger**: 指示、定時、条件のどれで起動するか。
- **Input / Output**: 何を受け取り、何を返すか。
- **Schema / Validation**: JSONなどの構造と、期待形式の自動検証。
- **Knowledge / RAG**: 何を参照させるか。
- **Tools / MCP / API**: 外部システムやツールへどう接続するか。
- **Human-in-the-Loop**: 人が確認・承認・介入する位置。
- **Guardrails**: してはいけないこと、出してはいけないこと。
- **Permission**: 誰の権限で何を参照・実行できるか。
- **Security / Legal / Ethics**: セキュリティ、法務、倫理上の確認事項。

再現性を高めるため、AIへ渡す文脈そのものを標準化します。複雑な判断は一度に任せず、抽出、照合、評価などに分けて設計することも考えます。

セキュリティや法務をFDEだけで判断せず、必要な専門家と一緒に決めます。

### この段階で残すもの

- 人 / AI / RPA / システムの責務
- 自律性と起動条件
- Context
- I/OとSchema
- 参照情報・Tool
- HITL
- Guardrails
- 権限と安全性
- 検証方法

## 4. 小さく検証する — Development & PoC

設計したら、いきなり本番へ出しません。

まず、動くかを確かめる**Prototype**をつくり、次に業務として成立するかを確かめる**PoC**を行います。価値を提供できる最小の実用品が必要になった段階で**MVP**へ進みます。

検証はSandboxなど、本番データや本番権限へ影響を与えにくい環境で行います。

見るのは精度だけではありません。

- 精度・品質
- 応答速度
- 安全性
- 再現性
- APIや運用を含むコスト
- 例外への対応
- 人の確認負荷
- 現場で本当に使えるか
- Definitionで決めた合格基準を満たすか

結果から、次の三つを明確に判断します。

- **Go**: 次へ進む。
- **No-Go**: 今回は進めない。
- **Pivot**: 条件、設計、対象、手段を変えて再検証する。

「AIが動いた」ことではなく、**業務として成立したか**を判定します。

### この段階で残すもの

- Prototype / PoC
- 評価結果
- 品質・速度・安全性・コスト
- 現場利用性
- Go / No-Go / Pivot
- 次の改善点

## 5. 根づかせ育てる — Deployment & Scale

PoCで成立した仕組みも、一気に全社展開しません。

まず、担当者や範囲を限定して使い始めます。そこで現場の反応、例外、困りごとを集め、仕組みを育てます。

評価では、AIが何件処理したかという**Output**だけを追いません。本当に見るのは、業務や人に何が起きたかという**Outcome**です。

たとえば、

- 1件あたりの処理時間
- 手戻りや差し戻し
- 担当者間の判断の一致
- 利用者や顧客に届いた価値
- 品質の変化
- 長期的な業務成果

を見ます。

短期で分かるOutcomeと、半年・一年など時間をかけて確認するOutcomeは分けて設計します。

現場で使う中で生まれた「この場合はこう見る」という暗黙の判断は、フィードバックとして言語化し、業務モデル、ルール、プロンプト、ナレッジベースへ戻します。改善されたAIの出力を通して、人も新しい判断を学びます。

この**人 → AI → 人**の知識循環を回し、AIだけでなく組織の知的資産そのものを育てます。

広げ方も分けて考えます。

- **Rollout**: 同じ機能を、より多くの利用者や範囲へ段階的に届ける。
- **Scaling**: 処理能力、新機能、別の対象業務など、仕組みそのものを拡張する。

まずRolloutで利用データとフィードバックを集め、そのあと必要に応じてScaleします。

### この段階で残すもの

- 限定導入の結果
- Output / Outcome
- 現場からのフィードバック
- 改善された業務モデル・ルール・ナレッジ
- 運用責任
- 教育・チェンジマネジメント
- Rollout / Scalingの判断
- 次のDiscoveryへ戻す学び

## FDEとして一番大事なこと

このプロセスの目的は、AIエージェントを導入することではありません。

**業務を理解し、不要な仕事を減らし、価値のある課題を選び、人とAIの強みを組み合わせ、小さく確かめ、使う人たち自身が理解し、選び、変え、育てられる状態をつくること**です。

そのため、業務モデルもAIエージェントも完成品として渡して終わりにはしません。現場で使った結果をまた理解へ戻し、何度も更新します。

---

さらに個々の場面を図として確認したいときだけ、以下の補助Viewを使います。

- [業務の変化を描く](shape-change-context.md)
- [協働の仕組みをつくる](build-collaboration-context.md)
- [仕組みを現場へ根づかせる](establish-work-context.md)

← [FDEの全体へ](README.md)
