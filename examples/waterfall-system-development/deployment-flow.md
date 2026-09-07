# 本番切替を継続または戻す — Business Flow

親 View: `deployment-context.md` / expanded node: `b_verify_production`

```mermaid
---
title: 本番切替を継続または戻す
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
  b_check_technical@{ label: "技術疎通を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_check_business@{ label: "業務疎通を確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_continue_release@{ label: "継続できる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_rollback_release@{ label: "旧状態へ戻す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_handover_operation@{ label: "運用へ渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_check_technical --> b_check_business
  b_check_business --> d_continue_release
  d_continue_release -->|継続| b_handover_operation
  d_continue_release -->|中止| b_rollback_release
  b_rollback_release --> b_check_technical

  class b_check_technical,b_check_business,b_rollback_release,b_handover_operation business;
  class d_continue_release decision;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

本番配備が成功しただけでは導入成功とはみなしません。技術疎通と重要業務の成立を確認し、継続できない場合は旧状態へ戻して安全性を回復します。継続可能と判断できたときだけ運用へ責任を移します。
