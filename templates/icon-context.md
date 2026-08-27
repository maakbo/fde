# Icon context diagram

Edit the Mermaid block directly and preview this Markdown file. Keep assumptions and open questions below the diagram when they matter.

```mermaid
---
title: Business context
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 48
    rankSpacing: 64
    padding: 8
  themeVariables:
    background: "#FAF8F2"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; } .image-shape foreignObject { overflow: visible; } .image-shape[id*='-flowchart-b_'] .label p { transform: translateY(-6px); }"
---
flowchart TB
  a_requester@{ img: "https://api.iconify.design/lucide/user.svg", label: "Requester", pos: "b", w: 38, h: 38, constraint: "on" }
  b_receive@{ img: "https://api.iconify.design/lucide/ellipse.svg", label: "Receive request", pos: "b", w: 30, h: 30, constraint: "on" }
  i_request@{ img: "https://api.iconify.design/lucide/file.svg", label: "Request", pos: "b", w: 38, h: 38, constraint: "on" }
  i_record@{ img: "https://api.iconify.design/lucide/file.svg", label: "Intake record", pos: "b", w: 38, h: 38, constraint: "on" }
  x_service@{ img: "https://api.iconify.design/lucide/server.svg", label: "External service", pos: "b", w: 38, h: 38, constraint: "on" }

  a_requester --- b_receive
  i_request --- b_receive
  b_receive --- i_record
  x_service --- b_receive

  class a_requester actor;
  class b_receive business;
  class i_request,i_record information;
  class x_service external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## Open question

What boundary, grain, classification, or relationship should the group examine next?
