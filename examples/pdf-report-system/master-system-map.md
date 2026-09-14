# PDF帳票システム — External-system master

このsampleのBusiness boundaryの外側にある技術システムを管理します。

```mermaid
---
title: PDF帳票システムのExternal-system master
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
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  x_business_system@{ label: "業務システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  class x_business_system external;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## Dictionary

| ID | Label | Meaning in this sample | Confidence |
| --- | --- | --- | --- |
| `x_business_system` | 業務システム | 業務データを提供する、対象外の技術システム | synthetic working |

## 読み方

このmasterはシステム間の構造を決めるものではありません。どのBusinessで使われるかは
[代表BUC「帳票を用意する」](report-creation-context.md)で確認します。
