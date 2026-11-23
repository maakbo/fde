# fdeをつくり、育てる

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 24
    htmlLabels: false
    wrappingWidth: 280
    nodeSpacing: 38
    rankSpacing: 58
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  %% テーマコンテキスト図：製品を育てる活動。fdeで描く個々の仕事は別のテーマ。
  %% 作り手と受け手は役割で区別する。同じ人でも役割が異なれば別ノード。
  %% ゴールへの不可視リンクは配置専用。業務上の関係ではない。
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "AI（開発支援）", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fde_product@{ label: "fdeを育てる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_first_user@{ label: "初期利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members@{ label: "仕事の関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  goal["仕事が、もっと心地よく進む。<br/>立場が違えば、見え方も違う。"]

  a_product_owner --- b_fde_product
  a_build_agent --- b_fde_product
  b_fde_product ~~~ goal
  b_fde_product --- a_first_user
  b_fde_product --- a_work_members

  classDef icon fill:none,stroke:none,color:#25231F;
  classDef compass fill:none,stroke:none,color:#25231F,font-weight:600;
  class a_product_owner,a_build_agent,b_fde_product,a_first_user,a_work_members icon;
  class goal compass;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  linkStyle 2 stroke:transparent,stroke-width:0px;
```

fdeエンジニアはAIの支援を受けてfdeをつくる。初期利用者は自分の仕事で使って確かめる。その先で、仕事の関係者が互いの前提や仕事のつながりを見ながら、納得して仕事を進められるようにする。

[コンセプトと設計の全体](README.md)
