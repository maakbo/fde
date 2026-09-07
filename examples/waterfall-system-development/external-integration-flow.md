# 外部連携障害を切り分ける — Business Flow

親 View: `external-integration-context.md` / expanded node: `b_isolate_boundary`

```mermaid
---
title: 外部連携障害を切り分ける
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
  b_collect_evidence@{ label: "証跡を揃える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_compare_exchange@{ label: "送受信を照合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_boundary_known@{ label: "所在が分かる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_add_observation@{ label: "観測を増やす", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_assign_owner@{ label: "修正先を定める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_collect_evidence --> b_compare_exchange
  b_compare_exchange --> d_boundary_known
  d_boundary_known -->|判明| b_assign_owner
  d_boundary_known -->|未判明| b_add_observation
  b_add_observation --> b_compare_exchange

  class b_collect_evidence,b_compare_exchange,b_add_observation,b_assign_owner business;
  class d_boundary_known decision;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

双方のログ・電文・時刻を照合し、問題の所在を判断できなければ観測情報を増やして再度突き合わせます。所在が分かった時点で、初めて修正責任を割り当てます。
