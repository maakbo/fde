# 対象を見極め、業務を定義する

現場を見えるようにしたら、すぐにAI化へ進むのではなく、そもそも必要な業務かを問い直します。残った課題からボトルネックを絞り、最も意味のある対象を選び、次に設計できる要件の叩き台へ変えます。

## 流れ

```mermaid
---
title: 対象を見極め、業務を定義する
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
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
flowchart TB
  b_overview@{ label: "業務を見渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_simplify@{ label: "不要を減らす", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_bottleneck@{ label: "ボトルネックを絞る", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_choose_means@{ label: "手段を見極める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_prioritize@{ label: "対象を選ぶ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_scope@{ label: "境界を定める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_requirements@{ label: "要件を言葉にする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_overview --> b_simplify
  b_simplify --> b_bottleneck
  b_bottleneck --> b_choose_means
  b_choose_means --> b_prioritize
  b_prioritize --> b_scope
  b_scope --> b_requirements

  class b_overview,b_simplify,b_bottleneck,b_choose_means,b_prioritize,b_scope,b_requirements activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## このモデルが表していること

業務を見渡すときは、流れだけでなく、判断、例外、待ち、手戻り、ミス、属人化、使う情報を確認します。不要、統合可能、順序変更可能、単純化可能な作業は、AIを使う前に減らします。

残った課題から生産性や価値を最も阻害している部分を絞り、人が担う方がよいか、ルールやRPAで扱えるか、AIエージェントが向くかを見極めます。効果の大きさ、実現可能性、リスクを合わせて、優先して試す対象を選びます。

対象を選んだら、対象業務と対象外、前提、制約、合格基準を明らかにします。機能要件だけでなく、速度、可用性、品質などの非機能要件も、実装担当者と具体化できる叩き台として言葉にします。

← [業務の変化を描く場面へ](shape-change-context.md)
