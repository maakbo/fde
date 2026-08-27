# Repair intake context

Working view of the actors, information, and outside service around repair intake.

```mermaid
---
title: Repair intake context
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
  a_customer@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "Customer", pos: "b", w: 38, h: 38, constraint: "on" }
  b_receive_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "Receive request", pos: "b", w: 30, h: 30, constraint: "on" }
  i_repair_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "Repair request", pos: "b", w: 38, h: 38, constraint: "on" }
  i_intake_record@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "Intake record", pos: "b", w: 38, h: 38, constraint: "on" }
  x_scheduling_service@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", label: "Scheduling", pos: "b", w: 38, h: 38, constraint: "on" }

  a_customer --- b_receive_request
  i_repair_request --- b_receive_request
  b_receive_request --- i_intake_record
  x_scheduling_service --- b_receive_request

  class a_customer actor;
  class b_receive_request business;
  class i_repair_request,i_intake_record information;
  class x_scheduling_service external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## Reading

The customer, repair request, intake record, and scheduling service relate through receiving the repair request. The lines show business relationships, not time order.

## Open question

Does booking still belong inside the intake boundary?
