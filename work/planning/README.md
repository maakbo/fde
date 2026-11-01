# 業務要件定義

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
  %% 提供する業務の概要。操作の順序はworkflowへ。顧客とFDEの分担は各案件で確認する。
  a_customer@{ label: "顧客の担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_fde@{ label: "FDEチーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_input@{ label: "改善対象と現状", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_prepare@{ label: "業務条件の具体化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_decide@{ label: "要件の合意", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_output@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_customer --- b_prepare
  a_customer --- b_decide
  a_fde --- b_prepare
  a_fde --- b_decide
  i_input --- b_prepare
  b_prepare --- b_decide
  b_decide --- i_output
  class a_customer,a_fde actor;
  class b_prepare,b_decide business;
  class i_input,i_output information;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

顧客の業務責任者・担当者とFDEが、改善対象を具体的な業務要件にし、設計へ渡します。

### 業務定義

対象の業務について、誰が関わり、何を受け取り、何を判断し、誰に何を渡すかを確かめます。前後の仕事との関係も含め、目的、関係者、作業、情報、システム、判断のつながりを業務構造図にまとめます。

熟練者の勘や例外への対応は、具体的な事例をもとに言葉にします。同じ仕事でも判断が異なるときは、その背景を聴き、共通にすることと、それぞれに委ねることを話し合います。

関係者と実装担当者、必要な専門家で、今回変える範囲、必要な機能、品質や速度、利用できる情報、法令や社内ルールなどの条件をそろえます。仕事がどう変わればよいか、何を確かめれば導入に進めるかを合格基準として決めます。

業務構造図、判断基準や例外、期待する変化と合格基準を、協働の設計へ引き継ぎます。

[顧客と進める手順](workflow.md) / [FDEの仕事全体](../README.md)
