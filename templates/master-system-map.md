# External-system master map

Use this as the canonical map of software and technical systems outside the
chosen business boundary. `---` shows cooperation or association. `-->` shows
an explicit integration or dependency direction.

```mermaid
---
title: 外部システムマスタ
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  x_system_a@{ label: "業務システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_system_b@{ label: "連携システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_system_c@{ label: "通知システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  x_system_a --> x_system_b
  x_system_b --- x_system_c

  class x_system_a,x_system_b,x_system_c external;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

矢印は外部システム間の連携または依存方向、線は関係があることだけを
表す。どの業務で使うかは、マスタを参照する業務コンテキスト図で確認
する。

## 未解決の問い

どのシステム間の連携、依存、責任境界を確定するか？
