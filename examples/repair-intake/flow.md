# Repair intake flow

Focused task flow for completeness checking and missing-detail rework.

```mermaid
---
title: Repair intake flow
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
  b_receive_request@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Receive request", pos: "b", w: 30, h: 30, constraint: "on" }
  d_information_complete@{ img: "https://api.iconify.design/ph/diamond-thin.svg", label: "Complete?", pos: "b", w: 38, h: 38, constraint: "on" }
  b_request_details@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Request details", pos: "b", w: 30, h: 30, constraint: "on" }
  b_book_repair@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Book repair", pos: "b", w: 30, h: 30, constraint: "on" }

  b_receive_request --> d_information_complete
  d_information_complete -->|Complete| b_book_repair
  d_information_complete -->|Missing| b_request_details
  b_request_details --> d_information_complete

  class b_receive_request,b_request_details,b_book_repair activity;
  class d_information_complete decision;

  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## Reading

Receive the request, check completeness, request missing details and recheck when necessary, then book the repair.

## Open question

Is completeness checking part of receiving, or a separate responsibility?
