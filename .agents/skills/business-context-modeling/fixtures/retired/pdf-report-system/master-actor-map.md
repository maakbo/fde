# PDF帳票システム — Actor master

このsampleで再利用するActorを、短いreader labelとstable IDで管理します。今回のsynthetic
scenarioでは同種Actor間の階層や所属関係は観測していないため、線は引きません。

```mermaid
---
title: PDF帳票システムのActor master
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
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  a_report_user@{ label: "業務担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_report_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  class a_report_user,a_report_owner actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## Dictionary

| ID | Label | Meaning in this sample | Confidence |
| --- | --- | --- | --- |
| `a_report_user` | 業務担当 | 業務データを使い、帳票を作成・利用する主体 | synthetic working |
| `a_report_owner` | 業務責任者 | 帳票の内容を確認する主体 | synthetic working |

## 読み方

Actor masterは同じ種類の候補を管理する正本です。帳票業務での参加関係は各Contextで確認します。
