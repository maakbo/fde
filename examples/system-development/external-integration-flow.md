# 原因特定

外部連携で問題が起きたとき、双方の証跡から責任境界を突き止める流れです。

← [外部結合テスト](external-integration-context.md)

## フロー

```mermaid
---
title: 原因特定
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
  b_collect_evidence@{ label: "証跡収集", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_compare_exchange@{ label: "送受信照合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  d_boundary_known@{ label: "所在が分かる？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/diamond.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_add_observation@{ label: "観測追加", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_assign_owner@{ label: "担当確定", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_collect_evidence --> b_compare_exchange
  b_compare_exchange --> d_boundary_known
  d_boundary_known -->|判明| b_assign_owner
  d_boundary_known -->|未判明| b_add_observation
  b_add_observation --> b_compare_exchange

  class b_collect_evidence,b_compare_exchange,b_add_observation,b_assign_owner activity;
  class d_boundary_known decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

## 図の業務

- **証跡収集** — 双方のログ、電文、時刻、実行条件を揃える。
- **送受信照合** — 送った内容と受け取った内容を時間軸で突き合わせる。
- **観測追加** — 判断材料が足りない場合に、ログや計測点を増やす。
- **担当確定** — 原因の責任境界を特定し、修正主体を決める。

## この図が表していること

問題の所在を推測で決めず、双方が同じ証跡を見ながら切り分けます。判断できなければ観測を増やし、所在が分かった時点で修正責任を確定します。

## 設計観点へ

契約検証で扱う外部IF仕様を、根拠・成熟・差戻しまで含めて読むときは、[外部IF仕様の設計観点](interface-specification-detail.md) を参照します。
