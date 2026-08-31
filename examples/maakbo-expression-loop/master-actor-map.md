# maakbo表現制作 — アクターマスタ

Canonical actor candidates for the maakbo expression-production example. The
relationship between the creator and dialogue partner is observed as
collaboration; the reader's position remains a working hypothesis.

```mermaid
---
title: maakbo表現制作のアクターマスタ
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
  a_creator@{ label: "つくる人", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_dialogue_partner@{ label: "対話相手", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_reader@{ label: "読み手", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_creator --- a_dialogue_partner

  class a_creator,a_dialogue_partner,a_reader actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

つくる人と対話相手は協働関係として置く。読み手との関係は、今回の入力
だけでは直接の関係線を確定しないため、候補を残している。

## 未解決の問い

読み手は対話相手から独立した主体か、発信シーンでだけ現れる役割か？
