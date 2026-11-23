# 業務を捉える

[ルートの業務ユースケースに戻る](../../../README.md#uc-understand) · [用語辞書](../../../README.md#概念データモデル用語辞書)

## 業務コンテキスト図

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 24
    htmlLabels: false
    wrappingWidth: 280
    nodeSpacing: 38
    rankSpacing: 58
    padding: 18
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  %% 親: ../../../README.md#業務コンテキスト図 / b_understand
  %% 線は参加・情報の扱い。手順は下のスイムレーン。
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_example@{ label: "仕事の事例", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_understand@{ label: "業務を捉える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members --- b_understand
  a_build_agent --- b_understand
  a_product_owner --- b_understand
  i_work_example --- b_understand
  b_understand --- i_work_model
  classDef element fill:none,stroke:none,color:#25231F;
  class a_work_members,a_build_agent,a_product_owner,i_work_example,b_understand,i_work_model element;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

**扱う情報**：仕事の事例 → 業務モデル。 **対応する要求**：R2・R3。

## 業務フロー（たたき台）

```mermaid
swimlane-beta TB
  %% 展開対象: b_understand。仕事関係者の確認を飛ばさない。
  subgraph people [仕事関係者]
    ask["具体例を持ち寄る"]
    check["実態と照らして直す"]
  end
  subgraph assistant_role [fde AI]
    prepare["目的と仕事のつながりを描く"]
  end
  subgraph engineer [fdeエンジニア]
    record["範囲と未確認点を残す"]
  end
  ask --> prepare --> check --> record
```

1. 仕事関係者が事例と期待を渡す。
2. fde AIが目的・役割・情報を整理する。
3. 仕事関係者が「実際にはどうか」を確認し、fdeエンジニアが境界と未確認点を言葉にする。

図が現実と違うときは、どの場面・誰の視点で違うのかを聞き直す。

既存設計とのつながり：[業務理解・対象選定](../../discovery/README.md)。
