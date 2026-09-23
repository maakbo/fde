# 単体検証

実装した変更が期待どおりに動くかを確かめ、差異があれば修正へ戻る流れです。

← [実装・単体](implementation-unit-context.md)

## フロー

```mermaid
---
title: 単体検証
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
  b_prepare_case@{ label: "条件準備", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_run_unit@{ label: "単体実行", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_unit_passed@{ label: "期待どおり？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_fix_change@{ label: "修正", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_record_result@{ label: "結果記録", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_prepare_case --> b_run_unit
  b_run_unit --> d_unit_passed
  d_unit_passed -->|適合| b_record_result
  d_unit_passed -->|差異| b_fix_change
  b_fix_change --> b_run_unit

  class b_prepare_case,b_run_unit,b_fix_change,b_record_result activity;
  class d_unit_passed decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## 図の業務

- **条件準備** — 入力値、前提状態、依存の置換など、同じ検証を再現できる条件を揃える。
- **単体実行** — 正常・境界・異常の観点で実装を動かす。
- **修正** — 期待との差異をコードへ戻して直す。
- **結果記録** — 確認済みの結果を後続の品質確認で参照できる形に残す。

## この図が表していること

単体テストは一度実行して終わる作業ではありません。差異を見つけたら実装へ戻り、同じ条件で再確認する短い反復です。
