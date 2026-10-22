# 不足を先に確かめて改修条件を整える案

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
  %% state: proposed, not adopted
  b_receive@{ label: "依頼を受ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_check@{ label: "前提を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_ready@{ label: "条件は揃う？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_ask@{ label: "不足を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_read@{ label: "根拠を調べる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_handoff@{ label: "条件を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_receive --> b_check
  b_check --> d_ready
  d_ready -->|揃う| b_read
  d_ready -->|不足| b_ask
  b_ask --> b_check
  b_read --> b_handoff

  class b_receive,b_check,b_ask,b_read,b_handoff activity;
  class d_ready decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

架空の改修受付の変更案。依頼者と仕様の責任者が、依頼の目的、通常時・未入力時の期待、有効な参照先を先に確かめる。開発担当は条件と根拠を照合して調べ、矛盾や新たな未決定が出たら調査を止め、該当する判断を仕様の責任者へ戻す。ここでは着手前の不足確認を主な相談範囲にしている。

「揃う」は、現行と同じ条件が説明できる状態。確認を前へ移す案であり、仕様を決定する権限や後続のレビューは省かない。調査結果と根拠位置は一つの記録で渡し、後続担当が利用できるかを確かめる。AIを使う場合も根拠と矛盾の整理までとし、未記載の仕様を決めさせない。

通常例と不足例をたどり、前倒しの確認に必要な情報がその時点で用意できるかを確かめる。調査後に初めて判明する条件は事前確認では解消できないため、その戻り先も別途確認する。着手後の差戻し、作業時間、返答待ち、後続担当の確認負担を測り、改善しなければ案を見直す。実務での効果は未測定。

**この案で確かめたいこと:** 先に決められない条件は何か。どこまでなら、前提確認を待たずに調査できるか。

[要求を整える](README.md) / [現行の進め方](change-intake-current.md)
