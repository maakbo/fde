# 導入・運用改善

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: true
    nodeSpacing: 64
    rankSpacing: 80
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  %% 親: b_fde。限定導入、現場での調整、継続的な改善を扱う。
  %% i_collaboration_spec は前の場面と同じ協働仕様。現場での実際の動作に合わせて更新する。
  %% 業務運用基準は、現場の判断基準、例外対応、変更手順をまとめた情報。情報名は文書形式を指定しない。
  %% 業務運用基準を現場への調整に活用する関係を残す。関連線は時系列や自動実行を表さない。
  %% 主体者は参加者かつ価値の受け手として右に置く。線の順序を変えたら交差を再確認する。
  %% 主体者と関係者が運用・判断・変更を担えることは、目的を育て続けるための条件。
  i_poc_result@{ label: "協働検証結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_support@{ label: "fde・fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_context_fit@{ label: "現場導入・調整", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_collaboration_spec@{ label: "協働仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_knowledge@{ label: "業務運用基準", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_improve@{ label: "業務運用改善", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_participants@{ label: "主体者と関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_context_fit --- a_participants
  i_poc_result --- b_context_fit
  a_support --- b_context_fit
  b_context_fit --- i_collaboration_spec
  i_collaboration_spec --- b_improve
  b_improve --- a_participants
  a_support --- b_improve
  i_knowledge --- b_improve
  b_context_fit --- i_knowledge

  class a_participants,a_support actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  class b_context_fit,b_improve business;
  classDef business fill:none,stroke:none,color:#25231F;
  class i_poc_result,i_collaboration_spec,i_knowledge information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

検証を通った仕組みを限られた範囲で使い、主体者と関係者が運用と改善を担えるようにします。

### 現場導入・改善

担当者や範囲を限定して使い始め、普段の仕事とのずれを直します。処理件数などの実績と、業務や人に起きた変化を分けて確かめます。

時間や品質、顧客に届いた価値に加え、やりたい仕事に時間を使えているか、判断しやすくなったか、負担が誰かに偏っていないかを聴きます。本人たちの実感と業務や事業の成果を照らし合わせ、組織と関係者が目指した状態に近づいているかを振り返ります。短期間で分かる変化と、時間をかけて追う成果は分けて扱います。

現場で得た経験や判断を協働仕様に反映し、実際の仕組みやプロンプトも更新します。判断基準、例外対応、変更手順を業務運用基準として共有します。運用、判断、変更の担当を決め、必要な教育や周知を行い、主体者と関係者が自分たちで改善を続けられるようにします。

同じ仕組みを使う人や範囲を広げることと、処理能力の増強、新機能の追加、別業務への適用は分けて判断します。新たに関わる人の事情や仕事も確かめ、必要なら対象業務選定からやり直します。目指すことや関係者の状況が変わったときも、取り組む対象を見直します。

使える仕組みと判断の根拠を残し、状況や思いの変化に合わせて、自分たちの仕事を育てていきます。

運用責任者、使う人、成果を受け取る人とFDEが、開始条件・日々の支援・改善を担います。動作確認の合格だけで本番導入を決めず、現場で使い続けられる体制と効果を確認します。

[顧客と進める手順](workflow.md) / [前：PoC・導入評価](../evaluation/README.md) / [FDEの仕事全体](../README.md)
