# FDEが目指すこと

見えることは、ゴールではありません。自分たちで理解し、選び、変え、育てられる状態を支えます。

## モデル

```mermaid
---
title: FDEが目指すこと
config:
  layout: elk
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: true
    nodeSpacing: 64
    rankSpacing: 80
    padding: 12
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
---
flowchart BT
  o_enabling(["見えるから、自分で選べる"])
  s_desired(["自分たちで理解し、選び、変え、育てられる"])
  p_ultimate(["個も仲間も、自然と自分たちらしく居られる"])

  o_enabling --> s_desired
  s_desired --> p_ultimate

  class o_enabling,s_desired,p_ultimate meaning;
  classDef meaning fill:#FFFFFF,stroke:#9E988E,color:#25231F,stroke-width:0.75px;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

業務が見えると、自分たちで選べるようになります。その理解を手元に残すことで、仕組みを自分たちで変え、育てていけます。

その先に、個も仲間も、それぞれの違いを失わず、自然と自分たちらしく居られる状態を目指します。

← [FDEの全体へ](README.md)

[誰と実現するかを見る](system-context.md) →
