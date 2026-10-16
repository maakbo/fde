# Human–Agent Workspace

```mermaid
---
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
  %% 人とAIが協働する作業環境の責任範囲。構造上の関係を扱い、処理の順序は別のFlowで扱う。
  h_operator@{ label: "operator", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  c_conversation@{ label: "conversation", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/message-square.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  subgraph bd_workspace["Workspace boundary"]
    direction LR
    g_collaborator@{ label: "AI collaborator", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
    r_repository@{ label: "repository", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/folder-git-2.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  end
  x_external_service@{ label: "external service", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/cloud.svg", pos: "b", w: 28, h: 28, constraint: "on" }

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

The operator and AI collaborator work through a repository-centered workspace. The repository keeps the work available for later use; the external service participates outside the workspace responsibility boundary.
