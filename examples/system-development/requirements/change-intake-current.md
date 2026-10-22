# 改修条件を整える現行の進め方

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
  %% parent: README.md / b_interpret_request; fictional change-intake scene
  %% state: synthetic current, not workplace observation
  b_receive@{ label: "依頼を受ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_read@{ label: "根拠を調べる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_draft@{ label: "条件をまとめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_ready@{ label: "条件は揃う？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_ask@{ label: "不足を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_handoff@{ label: "条件を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_receive --> b_read
  b_read --> b_draft
  b_draft --> d_ready
  d_ready -->|揃う| b_handoff
  d_ready -->|不足| b_ask
  b_ask --> b_read

  class b_receive,b_read,b_draft,b_ask,b_handoff activity;
  class d_ready decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

架空の改修受付。依頼者から数量入力の困りごとを受け、開発担当が有効な設計書と現行コードを調べ、条件をまとめる。仕様の責任者が条件の不足を確認し、揃っていれば後続の要件整理担当へ渡す。不足していれば依頼者と仕様の責任者へ確かめ、根拠の調査へ戻る。

この例では、有効な根拠、通常時の期待、未入力時の扱いが説明できることを「揃う」としている。実案件の共通基準ではない。確認の返答待ちはあるが、時間と発生頻度は未測定。どの条件が未決定かと、その確認先を残す。

**この進め方で確かめたいこと:** 不足は条件をまとめた後で分かるのか。返答後は資料を調べ直すのか、条件の追記だけで済むのか。

[要求を整える](README.md) / [不足を先に確かめる案](change-intake-proposed.md)
