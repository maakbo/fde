# 下書きにAIを使う限定試行案

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
  %% Parent: README.md / b_prepare_design。To-Be限定試行案。現場の実合意/実装は未実施。
  %% AIは許可済みR2から下書き。記録とレビュー、修正と受渡しは人。第二記録の廃止は含めない。
  b_prepare@{ label: "入力をそろえる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_agent_draft@{ label: "下書きを作る", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_record@{ label: "記録をそろえる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_review@{ label: "設計をレビュー", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_findings@{ label: "指摘はある？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fix@{ label: "指摘を直す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_handoff@{ label: "設計を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_prepare --> b_agent_draft
  b_agent_draft --> b_record
  b_record --> b_review
  b_review --> d_findings
  d_findings -->|ある| b_fix
  d_findings -->|ない| b_handoff
  b_fix --> b_handoff

  class b_prepare,b_agent_draft,b_record,b_review,b_fix,b_handoff activity;
  class d_findings decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

現状をそのままAIへ置き換えず、まず許可済みのR2、判断の根拠、未決を入力に揃える案です。AIが設計下書きを返し、設計担当が内容と記録をそろえ、別の人による設計レビューを残します。

第二記録は、必要な案件では人がレビュー前に作る段階案です。廃止の権限と目的が分からないため削っていません。AIによるチケット更新も含めていません。仕様不足なら仮の状態値を作らず、SEへの確認または未決の明記へ戻します。

演習回答N1は「この試行なら検討できる」であり、実組織の導入・支出・本番開始の承認ではありません。修正後の再レビュー/再記録の要否は調整課題です。新しい所要時間・削減効果は未測定です。

[現状](current-flow.md)／[関係の全体](README.md)／[試した内容と結果](practice.md)。
