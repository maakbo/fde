# 要求の具体化と開発範囲の合意

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
  %% View: Business Context, tentative human As-Is.
  %% parent: ../README.md / b_work
  %% Assumptions: role participation is provisional; operator participation and external systems unreviewed.
  %% Dense observation canvas: visual acceptance pending; do not treat source PASS as readability.
  %% Relations: participation and Information use, not phase order.
  a_user@{ label: "利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_staff@{ label: "業務担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_developer@{ label: "開発者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_vision@{ label: "事業の目指す姿", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_needs@{ label: "利用者ニーズ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_clarify@{ label: "要求を具体化する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_agree@{ label: "開発範囲を合意する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirements@{ label: "要求", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_scope@{ label: "開発範囲", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_owner@{ label: "事業責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_pm@{ label: "PM", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_user --- b_clarify
  a_staff --- b_clarify
  a_developer --- b_clarify
  i_vision --- b_clarify
  i_needs --- b_clarify
  a_user --- b_agree
  a_staff --- b_agree
  a_developer --- b_agree
  b_clarify --- a_owner
  b_clarify --- a_pm
  i_vision --- b_agree
  b_clarify --- b_agree
  b_clarify --- i_requirements
  b_agree --- i_requirements
  b_agree --- i_scope
  b_agree --- a_owner
  b_agree --- a_pm
  class a_user,a_staff,a_developer,a_owner,a_pm actor;
  class b_clarify,b_agree business;
  class i_vision,i_needs,i_requirements,i_scope information;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

利用者のニーズと業務の実態を事業の目指す姿と照らし、要求を具体化する。関係者は要求を踏まえて開発範囲を合意し、設計・実装や次の改善の判断につなぐ。

架空の業務の草案であり、参加の仕方と判断責任は未確定。運用者がこの場面でどう関わるか、外部システムとの関係も確認が必要。要求と開発範囲の区分を含め、関係者と見直す。

[システム開発](../README.md)
