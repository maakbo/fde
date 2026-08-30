# Repair intake actor master

Canonical actor candidates observed for this synthetic repair-intake boundary.
No same-type association or hierarchy was stated in the source example yet.

```mermaid
---
title: 修理受付のアクターマスタ
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
  a_customer@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "顧客", pos: "b", w: 38, h: 38, constraint: "on" }
  a_repair_team@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "修理担当", pos: "b", w: 38, h: 38, constraint: "on" }

  class a_customer,a_repair_team actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

この図は修理受付に関係する二つのアクター候補を示す。両者の直接の
親子・同列関係は、この例の入力だけでは観測されていないため、線を
足さずに残す。関係が分かれば、このマスタを先に更新する。

## 未解決の問い

修理担当の上位組織や受付担当を、この境界のアクターとして追加するか？
