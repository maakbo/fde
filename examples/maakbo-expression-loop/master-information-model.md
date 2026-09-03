# maakbo表現制作 — 情報マスタ

The draft is a possible result derived from the loose seed. This is a conceptual
relationship, not a detailed content or storage schema.

```mermaid
---
title: maakbo表現制作の情報マスタ
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
  i_idea_seed@{ label: "アイデアの種", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_expression_draft@{ label: "表現の初稿", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  i_idea_seed --> i_expression_draft

  class i_idea_seed,i_expression_draft information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

アイデアの種から表現の初稿が導かれると仮置きする。文章、図解、プレゼン
などの媒体差や、内容の項目はこの図に詰め込まない。

## 未解決の問い

「表現の初稿」は一つの概念でよいか。それとも文章、図解、プレゼンを
それぞれ別の情報としてマスタ化するか？
