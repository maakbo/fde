# FDEの進め方

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
  %% 5DモデルをFDEの業務として整理した全体フロー。
  %% Discovery → Definition → Design → Development & PoC → Deployment & Scale に対応する。
  %% 図は主な進行順序を扱う。検証や運用の結果に応じた戻りは本文で補足する。
  %% 詳細な関係図: README.md。業務の分類と工程の順序を混同しない。
  b_discover@{ label: "対象を見極める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_define@{ label: "業務を定義する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_design@{ label: "協働を設計する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_validate@{ label: "小さく検証する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_embed@{ label: "根づかせ育てる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_discover --> b_define
  b_define --> b_design
  b_design --> b_validate
  b_validate --> b_embed

  class b_discover,b_define,b_design,b_validate,b_embed activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

現場の仕事を理解し、変える対象を選び、業務を定義します。人・AI・システムの役割を決め、小さく試してから導入し、使いながら改善します。

検証で要件の不足が分かれば業務の定義に戻り、導入後に別の課題が見つかれば対象を選び直します。現場で分かったことに応じて、理解、設計、検証を繰り返します。

## 対象を見極める

業務の流れをたどり、時間がかかる箇所、待ち、手戻り、ミス、反復作業、特定の人に集中している仕事や判断を確認します。なくせる作業、まとめられる作業、順番を変えられる作業、単純にできる作業を整理します。

残った課題に対して、人が担うか、ルールで処理するか、RPAやAIを使うかを比較します。AIを使う候補は、次の点から判断します。

- 効果：工数、品質、速度、特定の人への依存、顧客や利用者への価値がどう変わるか。
- 実現可能性：必要なデータや知識がそろい、技術的に実現できるか。
- リスク：正確性、セキュリティ、法務、倫理、業務への影響を許容できるか。
- 業務との相性：判断や例外への対応に、AIの強みを活かせるか。

完全な正確性が必要な判断、共感そのものに価値がある仕事、AIに渡せない機密情報を扱う仕事、物理的な操作が中心の仕事では、AIが担える範囲を慎重に判断します。

優先する対象と選んだ理由をまとめ、現状の課題、減らせる作業、手段の候補、効果とリスクを関係者で共有します。

## 業務を定義する

対象業務について、誰が関わり、どの情報を使い、何を判断し、どんな例外があるかを確かめます。前後の仕事とのつながりも含め、業務の流れと関係を図にまとめます。

熟練者の勘や「この場合はこうする」という判断を、具体的な事例とともに言葉にします。判断基準、例外、前提を共有し、人とAIがそれぞれ担う範囲を検討します。

現場、実装担当者、必要な専門家で、次の事項を具体化します。

- 対象と対象外：今回変える業務の範囲と、扱わない範囲。
- 機能要件：仕組みに必要な機能や処理。
- 非機能要件：速度、品質、安定性などの条件。
- 制約：法令、社内ルール、利用できない情報など。
- 前提：データ形式、既存システムの状態など。
- 合格基準：何を満たせば導入に進めるか。

業務の図、判断基準や例外、要件をまとめ、設計に関わる人へ引き継ぎます。

## 協働を設計する

人、AI、RPA、既存システムの役割と責任を決めます。AIが指示に応じて処理するのか、人を支援するのか、判断を分担するのか、自律的に実行するのかを、業務に合わせて選びます。

AIを使う部分では、次の事項を具体化します。

- 渡す文脈：目的、前提、制約、参照情報、判断例。
- 起動条件：人の指示、定時実行、条件の成立など。
- 入出力：受け取る情報と返す情報、JSONなどの形式、構造や内容の検証方法。
- 参照先と接続先：知識や文書、外部システム、ツールへの接続方法。RAG、MCP、APIなどを使う場合は、その範囲と方法。
- 人の関与：確認、承認、介入が必要な箇所。
- 禁止事項：実行してはいけない操作や、出力してはいけない情報。
- 権限：誰の権限で、何を参照・実行できるか。
- 安全性：セキュリティ、法務、倫理に関する条件。

AIに渡す情報の内容と形式をそろえ、結果を再現しやすくします。複雑な判断は、抽出、照合、評価などに分けて設計します。セキュリティや法務に関わる事項は、必要な専門家と確認します。

役割分担、入出力、権限、参照先、禁止事項とあわせて、検証方法を決めます。

## 小さく検証する

まず試作品（Prototype）をつくり、動作を確認します。次に、業務で使えるかを確かめる検証（PoC）を行います。実際に価値を提供する最小限の機能が必要になった段階で、MVPとして形にします。

サンドボックスなど、本番のデータや権限に影響を与えにくい環境で、次の点を確かめます。

- 精度、品質、応答速度。
- 安全性と再現性。
- API利用料や運用を含むコスト。
- 例外への対応と、人が確認する負担。
- 現場での使いやすさと、業務を定義した際の合格基準。

評価結果をもとに、導入へ進む（Go）、今回は進めない（No-Go）、条件や設計、対象、手段を変えて再検証する（Pivot）のいずれかを判断します。判断の根拠と、次に改善する点を共有します。

## 根づかせ育てる

検証を通った仕組みを、担当者や範囲を限定して使い始めます。現場の反応、例外、困りごとを集め、改善します。

処理件数などの実績（Output）と、業務や人に起きた変化（Outcome）を分けて確認します。処理時間、手戻りや差し戻し、担当者間の判断の一致、顧客や利用者に届いた価値、品質の変化を評価します。短期で分かる変化と、半年や一年かけて追う成果は分けて扱います。

担当者が使う中で得た判断や知見を言葉にし、業務モデル、ルール、プロンプト、ナレッジベースに反映します。改善されたAIの出力から、担当者も新しい判断を学びます。現場の経験と仕組みの改善を重ね、知識を組織に残します。

運用、判断、変更の担当を決め、使い方や変更手順を共有します。教育や、業務の変更に伴う周知も進め、主体者と仲間が自分たちで改善を続けられるようにします。

同じ機能を使う人や範囲を段階的に増やすこと（Rollout）と、処理能力の増強、新機能の追加、別業務への適用（Scaling）は分けて判断します。利用結果と現場の意見を確認しながら範囲を広げ、新たな課題が見つかったときは、対象の選定から見直します。
