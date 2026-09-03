# Human–Agent Workspace — Handoff and Review Flow

This View follows one request from matti's handoff through kubox's repository work and back to the
next conversation.

## モデル

```mermaid
---
title: Handoff and Review Flow
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
  b_matti_handoff@{ label: "mattiが依頼", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_kubox_work@{ label: "kuboxが作業", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_review@{ label: "独立確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_kubox_reply@{ label: "記録して返す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_matti_read@{ label: "mattiが読む", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_human_decision@{ label: "判断が必要？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_maakbo_decide@{ label: "maakboが決める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_next_handoff@{ label: "次の依頼へ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_matti_handoff --> b_kubox_work
  b_kubox_work --> b_review
  b_review --> b_kubox_reply
  b_kubox_reply --> b_matti_read
  b_matti_read --> d_human_decision
  d_human_decision -->|はい| b_maakbo_decide
  d_human_decision -->|いいえ| b_next_handoff
  b_maakbo_decide --> b_next_handoff

  class b_matti_handoff,b_kubox_work,b_review,b_kubox_reply,b_matti_read,b_maakbo_decide,b_next_handoff activity;
  class d_human_decision decision;

  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## このモデルが表していること

matti writes the intent; kubox works, validates, obtains an independent review, commits, and
returns the result. matti reads the response and prepares the next handoff. maakbo steps in only
when the unresolved meaning or priority needs a human decision.

← [Architecture Overview](architecture-overview.md)
