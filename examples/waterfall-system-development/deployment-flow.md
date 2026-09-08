# 本番確認

本番反映後、技術と業務の両面から切替を継続できるか判断する流れです。

← [導入](deployment-context.md)

## フロー

```mermaid
---
title: 本番確認
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
  b_check_technical@{ label: "技術確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_check_business@{ label: "業務確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_continue_release@{ label: "継続できる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_rollback_release@{ label: "切戻し", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_handover_operation@{ label: "運用移管", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_check_technical --> b_check_business
  b_check_business --> d_continue_release
  d_continue_release -->|継続| b_handover_operation
  d_continue_release -->|中止| b_rollback_release
  b_rollback_release --> b_check_technical

  class b_check_technical,b_check_business,b_rollback_release,b_handover_operation activity;
  class d_continue_release decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## 図の業務

- **技術確認** — 起動、疎通、監視、ログなど、システムが技術的に成立しているか確かめる。
- **業務確認** — 重要業務が本番で成立するか、実利用に近い形で確かめる。
- **切戻し** — 継続できない場合に旧状態へ戻し、安全性を回復する。
- **運用移管** — 継続可能と判断した変更を、運用責任へ引き渡す。

## この図が表していること

本番配備が成功しただけでは導入成功とはみなしません。技術確認と業務確認を通して継続可否を判断し、継続できない場合は切り戻します。
