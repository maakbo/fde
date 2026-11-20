# システム開発

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
  %% View: whole-work System Context; participation, not phase order.
  %% Position: primary value role, not affiliation or one-way handoff.
  %% Detail: requirements-agreement/README.md expands b_work as one tentative scene.
  a_owner@{ label: "事業責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_staff@{ label: "業務担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_pm@{ label: "PM", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_developer@{ label: "開発者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_work@{ label: "システム開発", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  p_goal("事業の目指す姿や利用者のニーズを捉え、関係者とともに、価値を生むシステムを開発する。")
  a_user@{ label: "利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_operator@{ label: "運用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_owner --- b_work
  a_staff --- b_work
  a_pm --- b_work
  a_developer --- b_work
  b_work -.- p_goal
  b_work --- a_user
  b_work --- a_operator
  click b_work "https://github.com/maakbo/fde/blob/skill/spatial-context-and-abstraction-gates-20261117/examples/system-development/work-context/requirements-agreement/README.md"
  class a_owner,a_staff,a_pm,a_developer,a_user,a_operator actor;
  class b_work business;
  class p_goal purpose;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  classDef purpose fill:#FFFFFF,stroke:#9E988E,color:#25231F,stroke-width:0.75px;
```

開発・運用・保守・改善を通じて、継続的に価値を提供する。事業責任者・業務担当者・PM・開発者・利用者・運用者が関わる架空の仕事の草案であり、具体的な責任分担と外部システムは未確認。

[要求の具体化と開発範囲の合意](requirements-agreement/README.md) / [BtoB Web業務システムの開発と運用](../README.md)
