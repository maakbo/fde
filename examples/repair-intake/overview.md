# Repair service overview

One-level-higher view connecting intake, repair, and return.

```mermaid
---
title: Repair service overview
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
  themeCSS: ".image-shape p { padding: 0 !important; } .image-shape foreignObject { overflow: visible; }"
---
flowchart TB
  b_manage_intake@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Manage intake", pos: "b", w: 22, h: 22, constraint: "on" }
  b_repair_item@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Repair item", pos: "b", w: 22, h: 22, constraint: "on" }
  b_return_item@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Return item", pos: "b", w: 22, h: 22, constraint: "on" }

  b_manage_intake --> b_repair_item
  b_repair_item --> b_return_item

  class b_manage_intake,b_repair_item,b_return_item activity;

  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## Reading

Repair service moves from intake to repair and then return. Each activity may expand into a focused Markdown view.
