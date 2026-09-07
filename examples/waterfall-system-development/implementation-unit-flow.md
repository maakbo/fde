# 実装変更を単体検証する — Business Flow

親 View: `implementation-unit-context.md` / expanded node: `b_verify_unit`

```mermaid
---
title: 実装変更を単体検証する
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
  b_prepare_case@{ label: "条件を揃える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_run_unit@{ label: "単体実行", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_unit_passed@{ label: "期待どおり？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_fix_change@{ label: "実装を直す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_record_result@{ label: "結果を残す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_prepare_case --> b_run_unit
  b_run_unit --> d_unit_passed
  d_unit_passed -->|適合| b_record_result
  d_unit_passed -->|差異| b_fix_change
  b_fix_change --> b_run_unit

  class b_prepare_case,b_run_unit,b_fix_change,b_record_result business;
  class d_unit_passed decision;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

単体テストは「コードを書いた後に一度実行する作業」ではなく、期待との差異を検知したら実装へ戻り、同じ条件で再確認する短い反復です。ここではテストコード自身の不備を切り分ける枝はまだ省いています。
