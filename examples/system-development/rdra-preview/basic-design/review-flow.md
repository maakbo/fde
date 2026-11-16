# 設計レビュー — 業務フロー

[親のビジネスユースケースに戻る](README.md) / [全体に戻る](../README.md)

「設計をレビューする」を一件の作業と判断へ展開した、**人が行う架空のAs-Is**。左右のレーンはそれぞれ担当者、**時系列は上から下**です。

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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
swimlane-beta TB
  subgraph designer [設計担当]
    b_prepare@{ label: "設計仕様と要件を揃える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
    b_revise@{ label: "指摘を踏まえて修正する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
    b_handover@{ label: "確定版と結果を引き渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  end

  subgraph reviewer [レビュー担当]
    b_check@{ label: "要件と設計を照合する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
    d_pass@{ label: "確認を終えられるか？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  end

  b_prepare -->|"合意済み要件・設計仕様"| b_check
  b_check --> d_pass
  d_pass -->|"要修正・レビュー結果"| b_revise
  b_revise -->|"修正版"| b_check
  d_pass -->|"確認完了・レビュー結果"| b_handover
  class b_prepare,b_revise,b_handover,b_check business;
  class d_pass decision;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

- **入力**：合意済み要件、設計仕様。
- **判断**：レビュー担当が整合性と未解決事項を確認する。判断基準の詳細は実際の規約・現場によって確認する。
- **修正**：設計担当がレビュー結果を受けて直し、レビュー担当へ戻す。
- **出力**：レビュー結果、確認済みの設計仕様。次の実装・検証担当に渡す。
- **未確認**：正式な承認者、記録先、レビューの種類、再レビュー範囲、関係者の兼務・異常時の判断。

この図の担当者別スイムレーンにはMermaid v11.16以降の `swimlane-beta TB` を使っています。GitHubやプレビュー側のMermaidバージョンによっては未表示となる可能性があります。その場合も上の箇条書きが作業意味の代替説明になります。視覚レンダリングと現場合意はまだ未検証です。
