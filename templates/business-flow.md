# Business flow diagram

Edit the Mermaid block directly and preview this Markdown file. Record unresolved routes or responsibility questions below the diagram.

```mermaid
---
title: Business flow
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
    background: "#FAF8F2"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FAF8F2"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; } .image-shape foreignObject { overflow: visible; } .image-shape[id*='-flowchart-b_'] .label p { transform: translateY(-6px); }"
---
flowchart TB
  b_receive@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Receive", pos: "b", w: 30, h: 30, constraint: "on" }
  d_complete@{ img: "https://api.iconify.design/ph/diamond-thin.svg", label: "Complete?", pos: "b", w: 38, h: 38, constraint: "on" }
  b_create@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Create", pos: "b", w: 30, h: 30, constraint: "on" }
  b_review@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Review", pos: "b", w: 30, h: 30, constraint: "on" }

  b_receive --> d_complete
  d_complete -->|Yes| b_create
  b_create --> b_review
  d_complete -->|No| b_receive

  class b_receive,b_create,b_review activity;
  class d_complete decision;

  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## Open question

Which activity, decision, or return route could change the shared understanding?
