# テーマコンテキスト図：中央の見せ方

[元の一枚](theme-context.md)から、テーマ名の見せ方と、ゴールの添え方を試した。AとBは中央の枠の形だけを変えている。Cは枠を控えめにし、文字を目立たせた案。アクターは個人名ではなく役割名で表示する。

## A｜楕円に近い横長の枠

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
  %% 点線は目指すゴールを添えるための注釈。業務フローではない。
  a_product_owner@{ label: "企画担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "AI（開発支援）", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fde_product@{ shape: stadium, label: "fdeを育てる" }
  a_first_user@{ label: "初期利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members@{ label: "仕事の関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  goal("仕事が、もっと心地よく進む。<br/>立場が違えば、見え方も違う。")

  a_product_owner --- b_fde_product
  a_build_agent --- b_fde_product
  b_fde_product -.- goal
  b_fde_product --- a_first_user
  b_fde_product --- a_work_members

  classDef icon fill:none,stroke:none,color:#25231F;
  classDef compass fill:#FBFAF7,stroke:#C6BFB4,stroke-width:0.8px,color:#25231F,font-weight:600;
  classDef themeNode fill:#F8F7F3,stroke:#4A4640,stroke-width:1.25px,color:#25231F,font-weight:700,font-size:20px;
  class a_product_owner,a_build_agent,a_first_user,a_work_members icon;
  class goal compass;
  class b_fde_product themeNode;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  linkStyle 2 stroke:#A0988E,stroke-width:1px,stroke-dasharray:2 4;
```

## B｜四角い枠

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
  %% 点線は目指すゴールを添えるための注釈。業務フローではない。
  a_product_owner@{ label: "企画担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "AI（開発支援）", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fde_product@{ shape: rect, label: "fdeを育てる" }
  a_first_user@{ label: "初期利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members@{ label: "仕事の関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  goal("仕事が、もっと心地よく進む。<br/>立場が違えば、見え方も違う。")

  a_product_owner --- b_fde_product
  a_build_agent --- b_fde_product
  b_fde_product -.- goal
  b_fde_product --- a_first_user
  b_fde_product --- a_work_members

  classDef icon fill:none,stroke:none,color:#25231F;
  classDef compass fill:#FBFAF7,stroke:#C6BFB4,stroke-width:0.8px,color:#25231F,font-weight:600;
  classDef themeNode fill:#F8F7F3,stroke:#4A4640,stroke-width:1.25px,color:#25231F,font-weight:700,font-size:20px;
  class a_product_owner,a_build_agent,a_first_user,a_work_members icon;
  class goal compass;
  class b_fde_product themeNode;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  linkStyle 2 stroke:#A0988E,stroke-width:1px,stroke-dasharray:2 4;
```

## C｜薄い四角と大きめの文字

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
  %% 点線は目指すゴールを添えるための注釈。業務フローではない。
  a_product_owner@{ label: "企画担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "AI（開発支援）", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fde_product@{ shape: rect, label: "fdeを育てる" }
  a_first_user@{ label: "初期利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members@{ label: "仕事の関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  goal("仕事が、もっと心地よく進む。<br/>立場が違えば、見え方も違う。")

  a_product_owner --- b_fde_product
  a_build_agent --- b_fde_product
  b_fde_product -.- goal
  b_fde_product --- a_first_user
  b_fde_product --- a_work_members

  classDef icon fill:none,stroke:none,color:#25231F;
  classDef compass fill:#FBFAF7,stroke:#C6BFB4,stroke-width:0.8px,color:#25231F,font-weight:600;
  classDef themeNode fill:#FFFFFF,stroke:#BFB8AE,stroke-width:0.8px,color:#25231F,font-weight:700,font-size:22px;
  class a_product_owner,a_build_agent,a_first_user,a_work_members icon;
  class goal compass;
  class b_fde_product themeNode;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  linkStyle 2 stroke:#A0988E,stroke-width:1px,stroke-dasharray:2 4;
```

[別枠の検証：ユースケース図の楕円](theme-context-usecase-test.md)
