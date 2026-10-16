# FDEの進め方

```mermaid
---
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
  %% README.md の3場面に対応。対象の見極め・業務定義／協働設計・検証／現場での利用と改善。
  b_discover@{ label: "対象を見極める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_define@{ label: "業務を定義する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_design@{ label: "協働を設計する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_validate@{ label: "小さく検証する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_embed@{ label: "根づかせ育てる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_discover --> b_define
  b_define --> b_design
  b_design --> b_validate
  b_validate --> b_embed

  class b_discover,b_define,b_design,b_validate,b_embed activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

組織の目指すことと、関わる人たちの思いや事情を確かめ、最初に変える仕事を選びます。人とAIの協働を小さく試し、日々の仕事に合わせながら育てます。全体の目的と関わる人は、[FDE](README.md)で共有しています。

検証や利用で分かったことに応じて、業務の定義や役割分担に戻ります。目指すことや関係者の状況が変わったときは、取り組む対象から見直します。

## 対象を見極める

組織の使命やビジョンと、その仕事が顧客や仲間に届けている価値を確かめます。関係者それぞれの思い、事情、得意なこと、仕事の経緯を聴き、続けたいことと変えたいことを話し合います。

実際の仕事をたどり、待ちや手戻り、繰り返し、特定の人に集中する作業や判断を確認します。なくす、まとめる、順番を変えるなどの方法を考え、人が担うか、ルールやRPA、AIを使うかを比較します。

最初に取り組む対象は、次の点から選びます。

- 目指す変化：組織が目指すことや、関係者が実現したいことにつながるか。守りたい仕事の良さや関係は何か。
- 効果：工数、品質、速度、顧客への価値がどう変わるか。関係者の負担や役割にどんな影響があるか。
- 実現可能性：必要な情報や知識、技術、協力が得られるか。
- リスクと適性：正確性、情報の扱い、法令、業務への影響を踏まえ、その手段に任せられるか。

共感そのものに価値がある仕事や、AIに渡せない情報を扱う仕事などは、人が担う範囲を確かめます。対象と選んだ理由、期待する変化を関係者で共有します。

## 業務を定義する

誰が関わり、何を受け取り、何を判断し、誰に何を渡すかを確かめます。前後の仕事との関係も含め、目的、作業、情報、システムのつながりを図と言葉にします。

熟練者の勘や例外への対応は、具体的な事例をもとに言葉にします。同じ仕事でも判断が異なるときは、その背景を聴き、共通にすることと、それぞれに委ねることを話し合います。

関係者と実装担当者、必要な専門家で、今回変える範囲、必要な機能、品質や速度、利用できる情報、法令や社内ルールなどの条件をそろえます。仕事がどう変わればよいか、使う人が何を確かめれば導入に進めるかも決めます。

仕事のつながり、判断基準や例外、期待する変化と合格基準を、協働の設計へ引き継ぎます。

## 協働を設計する

人、AI、RPA、既存システムの役割と責任を決めます。人の強みをどう活かすか、AIに何を任せるか、誰が結果を確かめるかを、実際の仕事に合わせて考えます。

AIを使う部分では、次の事項を具体化します。

- 文脈と入出力：目的、前提、制約、参照情報、判断例。受け取る情報と返す情報、形式と内容の検証方法。
- 起動と接続：人の指示や定時実行などの起動条件。知識、文書、外部システムへの接続先と方法。
- 判断と権限：人が確認・承認・介入する箇所。参照・実行できる範囲と、禁止する操作。
- 検証と安全性：試す場面と評価方法。セキュリティ、法務、倫理上の条件。

JSONなどの出力形式や、RAG・MCP・APIなどの接続方法は、必要に応じて選びます。複雑な判断は抽出、照合、評価などに分け、どこで人に戻すかを決めます。専門的な条件は、必要な専門家と確認します。

## 小さく検証する

試作品で動作を確かめ、実際の仕事に近い場面で、業務に使えるかを検証します。試作品（Prototype）、実現性や効果の検証（PoC）、価値を届ける最小限の仕組み（MVP）は、確かめたいことに応じて使い分けます。

本番のデータや権限に影響を与えにくい環境で、次の点を確認します。

- 業務への効果と使い心地：期待した変化があるか。仕事の流れに合い、関係者が納得して使えるか。
- 品質と負担：精度、速度、例外への対応。人が確認する負担や、前後の仕事への影響。
- 安全性と継続性：権限や情報の扱い、再現性、利用料と運用コスト。

合格基準と照らし合わせ、導入へ進む、今回は進めない、対象・設計・手段を変えて再検証する、のいずれかを関係者で決めます。判断の根拠と次に確かめることを残します。

## 根づかせ育てる

担当者や範囲を限定して使い始め、普段の仕事とのずれを直します。処理件数などの実績と、業務や人に起きた変化を分けて確かめます。

時間や品質、顧客に届いた価値に加え、やりたい仕事に時間を使えているか、判断しやすくなったか、負担が誰かに偏っていないかを聴きます。短期間で分かる変化と、時間をかけて追う成果を分け、組織と関係者が目指した状態に近づいているかを振り返ります。

現場で得た経験や判断を、業務の進め方、ルール、プロンプト、共有知識に反映します。運用、判断、変更の担当と手順を決め、必要な教育や周知を行い、主体者と関係者が自分たちで改善を続けられるようにします。

同じ仕組みを使う人や範囲を広げることと、処理能力の増強、新機能の追加、別業務への適用は分けて判断します。対象を広げるときも、新たに関わる人の事情や仕事を確かめ、必要なら対象の見極めからやり直します。
