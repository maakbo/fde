# maakboの表現制作 — 全体コンテキスト

The first rung names the whole work and the major actor subjects. It does not
describe process order or every tool used along the way.

```mermaid
---
title: maakboの表現制作
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
flowchart TB
  a_creator@{ label: "つくる人", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_expression_practice@{ label: "表現制作", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  a_dialogue_partner@{ label: "対話相手", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_reader@{ label: "読み手", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_creator --- b_expression_practice
  b_expression_practice --- a_dialogue_partner
  b_expression_practice --- a_reader

  class a_creator,a_dialogue_partner,a_reader actor;
  class b_expression_practice business;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

maakboの表現制作は、つくる人が対話相手と関わりながら、読み手へ届く
表現を育てる仕事として仮置きする。配置は見やすさのためで、線は順序や
依存を表さない。

## Master references

この図のアクターは、次のアクターマスタから正規ID・ラベル・アイコン定義を
選択している。

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| [Actor master](master-actor-map.md) | `a_creator` | つくる人 | 表現の芯を置く主体 |
| [Actor master](master-actor-map.md) | `a_dialogue_partner` | 対話相手 | 形にする対話の相手 |
| [Actor master](master-actor-map.md) | `a_reader` | 読み手 | 表現を受け取る主体（仮） |

## 未解決の問い

「読み手」は全体コンテキストの主要主体として残すか。それとも個別の
発信・共有シーンでだけ登場させるか？
