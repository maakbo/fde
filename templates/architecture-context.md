# Human–Agent Workspace — Architecture Context

An operator and an AI collaborator use a repository-centered workspace with one external service.

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
  h_operator@{ label: "operator", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  c_conversation@{ label: "conversation", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/message-square.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  subgraph bd_workspace["Workspace boundary"]
    direction LR
    g_collaborator@{ label: "AI collaborator", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/bot.svg", pos: "b", w: 38, h: 38, constraint: "on" }
    r_repository@{ label: "repository", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/folder-git-2.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  end
  x_external_service@{ label: "external service", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/cloud.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  h_operator --- c_conversation
  c_conversation --- g_collaborator
  g_collaborator --- r_repository
  r_repository --- x_external_service

  class h_operator human;
  class g_collaborator agent;
  class r_repository repository;
  class x_external_service external;
  class c_conversation channel;

  classDef human fill:none,stroke:none,color:#25231F;
  classDef agent fill:none,stroke:none,color:#25231F;
  classDef repository fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  classDef channel fill:none,stroke:none,color:#5F5A52;
  style bd_workspace fill:#FAF8F2,stroke:#C8C1B6,stroke-width:0.75px,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## このモデルが表していること

The repository is a durable part of the workspace boundary. The external service participates
without moving inside that responsibility boundary.
