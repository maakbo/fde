# FDEの進め方

FDEは、現場を見えるようにするだけで終わりません。何を変える価値があるかを見極め、必要な条件を言葉にし、人・AI・システムの協働を設計し、小さく試し、現場で使いながら育てます。

## 大きな流れ

```mermaid
---
title: FDEの進め方
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 60
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  b_discover@{ label: "対象を見極める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_define@{ label: "業務を定義する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_design@{ label: "協働を設計する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_validate@{ label: "小さく検証する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_embed@{ label: "根づかせ育てる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_discover --> b_define
  b_define --> b_design
  b_design --> b_validate
  b_validate --> b_embed

  class b_discover,b_define,b_design,b_validate,b_embed activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## それぞれで行うこと

**対象を見極める**では、現場の実態を見て、不要な作業を減らし、時間、ミス、待ち、属人化などのボトルネックを見つけます。そのうえで、人が担うのか、ルールやRPAで扱うのか、AIエージェントが向くのかを考え、効果、実現可能性、リスクから優先する対象を選びます。

**業務を定義する**では、対象と対象外を明らかにし、業務の流れ、判断、例外、暗黙知、前提、制約を見える形にします。何を実現したいか、どの品質を求めるか、何を扱ってよいか、どこを人に残すかを、関係者が一緒に具体化できる叩き台にします。

**協働を設計する**では、人、AI、RPA、既存システムの役割を分け、AIへ渡す文脈、入出力、参照情報、権限、Human-in-the-Loop、安全策を決めます。後続の業務やシステムが扱えるよう、出力形式と検証方法も決めます。

**小さく検証する**では、安全な環境で試せる仕組みをつくり、精度、速度、安全性、コスト、現場利用性を確かめます。動いたかではなく、業務として成立するかを見て、進める、見直す、やめるを判断します。

**根づかせ育てる**では、限定した範囲から使い始め、利用状況とOutcomeを追います。現場のフィードバックを業務モデル、ルール、プロンプト、ナレッジへ戻し、人とAIの両方が学べる状態をつくります。同じ仕組みを広げるときも、一気に全体へ展開せず段階的に進めます。

実際の仕事では一方向に進むとは限りません。試して分かったことから業務の定義へ戻ったり、利用結果から対象の選び方を見直したりしながら育てます。

## 詳しく見る

- [業務の変化を描く](shape-change-context.md): 対象を見極め、業務を定義する
- [協働の仕組みをつくる](build-collaboration-context.md): 人・AI・システムの協働を設計し、小さく検証する
- [仕組みを現場へ根づかせる](establish-work-context.md): 限定導入から学習・改善・展開へ進む

← [FDEの全体へ](README.md)

[FDEの業務を見る](business-map.md) →
