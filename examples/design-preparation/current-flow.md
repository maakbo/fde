# いま、基本設計をどうまとめているか

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
  %% Parent: README.md / b_prepare_design。As-Isは観察記録C17の一件。
  %% 第二記録は社外説明案件C17の条件。全件の工程とはしない。再レビューは観測されていない。
  b_read@{ label: "要件を読む", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_first_record@{ label: "観点を転記する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_clarify@{ label: "不明を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_draft@{ label: "下書きを作る", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_second_record@{ label: "第二記録を作る", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_review@{ label: "設計をレビュー", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fix@{ label: "指摘を直す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_handoff@{ label: "設計を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_read --> b_first_record
  b_first_record --> b_clarify
  b_clarify --> b_draft
  b_draft --> b_second_record
  b_second_record --> b_review
  b_review --> b_fix
  b_fix --> b_handoff

  class b_read,b_first_record,b_clarify,b_draft,b_second_record,b_review,b_fix,b_handoff activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

架空の観察記録C17をたどった現状です。不明点の確認では設計担当がSEへの問いを整理し、回答を待ちます。状態値は未確定と明記して下書きを作り、社外説明のあるこの案件ではレビュー前に第二記録を作っています。

独立したレビュー担当が確認した後、設計担当が指摘を修正して開発担当へ渡しました。修正後の再レビューや第二記録の再更新は、記録がなく未確認です。

| 作業 | 担当・渡すもの | C17の記録 |
| --- | --- | --- |
| 要件を読む・観点を転記 | 設計担当、R2から設計票へ | 人手5分と3分 |
| 不明を確かめる | 設計担当→SE。状態値は未決という回答 | 設計担当8分、回答待ち20分 |
| 下書きと第二記録 | 設計担当、設計下書きとチケットへの同じ要点 | 10分と5分。第二記録の目的/廃止権限は未確認 |
| レビュー | 別のレビュー担当、境界条件などを確認 | 人手10分 |
| 修正と受渡し | 設計担当→開発担当 | 合わせて2分。別々の時間は不明 |

[関係の全体](README.md)／[限定試行の変更案](agent-assisted-flow.md)。
