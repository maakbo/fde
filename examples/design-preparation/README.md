# 要件を受けて、設計を開発へ渡す

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 64
    rankSpacing: 80
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  %% 架空の開発チームの現状。基本設計と変更実装という兄弟業務の関係。線は順序を示さない。
  %% b_prepare_designをcurrent-flow.mdとagent-assisted-flow.mdへ展開。
  a_se@{ label: "SE", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_designer@{ label: "設計担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_reviewer@{ label: "レビュー担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirement@{ label: "確定要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_prepare_design@{ label: "設計をまとめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "基本設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implement@{ label: "変更を実装する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_developer@{ label: "開発担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_se --- b_prepare_design
  a_designer --- b_prepare_design
  a_reviewer --- b_prepare_design
  i_requirement --- b_prepare_design
  b_prepare_design --- i_design
  i_design --- b_implement
  b_prepare_design --- a_developer
  b_implement --- a_developer

  class a_se,a_designer,a_reviewer,a_developer actor;
  class b_prepare_design,b_implement business;
  class i_requirement,i_design information;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

架空の開発チームの現状です。設計担当は確定要件を受け取り、不明点をSEへ確認し、独立したレビューと修正を経た基本設計を開発担当へ渡します。開発担当は設計を受けて実装・テストへ進みます。

設計をまとめる作業の順序と担当は、[現在の設計業務](current-flow.md)へ分けました。[変更案](agent-assisted-flow.md)は別の図です。

架空の例です。実際の現場の合意や効果を示すものではありません。

[この業務で作業Skillを試した結果](practice.md)／[同じ条件で始める架空の入力](intake.md)／[自分の仕事で始める](../../guides/field-work/README.md)
