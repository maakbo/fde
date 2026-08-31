# Actor master map

Use this as the canonical map of actors, roles, organizations, and parties.
`---` shows a peer or affiliation relationship. `-->` shows an intentional
parent-to-child, accountability, or ownership direction; it is not a process
sequence.

```mermaid
---
title: アクターマスタ
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:10px !important; }"
---
flowchart TB
  a_organization@{ label: "組織", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_team@{ label: "担当チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_partner@{ label: "協力先", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_organization --> a_team
  a_team --- a_partner

  class a_organization,a_team,a_partner actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

この図の矢印は組織上の親子・責任方向、線は同列の関係を表す。業務の
順序や価値の受け渡しは、業務コンテキスト図またはフロー図で表す。

## 未解決の問い

どのアクターの境界、親子関係、責任関係を確定するか？
