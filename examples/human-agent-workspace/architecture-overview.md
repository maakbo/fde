# Human–Agent Workspace — Architecture Overview

maakbo, matti, and kubox cooperate through a private control plane while keeping reusable public
work on a separate surface.

## モデル

```mermaid
---
title: Human–Agent Workspace
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  h_maakbo@{ label: "maakbo", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  g_matti@{ label: "matti", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/bot.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  subgraph bd_private["Private on GitHub"]
    r_private_repo@{ label: "private repo", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/folder-git-2.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  end
  g_kubox@{ label: "kubox", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/bot.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  subgraph bd_public["Public on GitHub"]
    r_public_fde@{ label: "public fde", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/folder-git-2.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  end

  h_maakbo --- g_matti
  h_maakbo --- r_private_repo
  g_matti --- r_private_repo
  r_private_repo --- g_kubox
  g_kubox --- r_public_fde

  class h_maakbo human;
  class g_matti,g_kubox agent;
  class r_private_repo,r_public_fde repository;

  classDef human fill:none,stroke:none,color:#25231F;
  classDef agent fill:none,stroke:none,color:#25231F;
  classDef repository fill:none,stroke:none,color:#5F5A52;
  style bd_private fill:#FAF8F2,stroke:#C8C1B6,stroke-width:0.75px,color:#5F5A52;
  style bd_public fill:#FAF8F2,stroke:#C8C1B6,stroke-width:0.75px,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

maakbo is the decision maker, not the message carrier. matti shapes intent through the private
shared post, and kubox performs repository work from that control plane. Only reusable skills and
examples move to the public FDE surface; private reasoning stays private.

← [Human–Agent Workspace](README.md)

[Handoff and Review Flow](handoff-review-flow.md) →
