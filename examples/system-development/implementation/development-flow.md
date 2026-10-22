# 実装から単体テスト・レビューへ進める

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  %% parent: ../README.md / b_build; current synthetic workflow, implementation through review entry
  b_read@{ label: "変更を調べる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implement@{ label: "実装する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_test@{ label: "テストする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_pass@{ label: "テスト合格？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fix@{ label: "失敗を調べる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_review@{ label: "レビューする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_read --> b_implement
  b_implement --> b_test
  b_test --> d_pass
  d_pass -->|合格| b_review
  d_pass -->|不合格| b_fix
  b_fix --> b_implement

  class b_read,b_implement,b_test,b_fix,b_review activity;
  class d_pass decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

開発者は、設計と既存コードから変更の影響を調べ、実装して単体テストを実行します。失敗したら原因を調べて修正し、再実行します。合格したら差分・変更理由・結果・未確認をまとめ、レビュアーに確認してもらいます。

仕様の不足は設計・要件の担当へ戻します。レビューに指摘があれば実装やテストを直して再レビューします。ここでの一周はレビューに出すまでで、mergeや結合テスト完了は含みません。架空の進め方として、実際の担当・合格条件を話すたたき台にします。

[実装・単体テスト](README.md) / [AIエージェントと進める案](agent-assisted-flow.md)
