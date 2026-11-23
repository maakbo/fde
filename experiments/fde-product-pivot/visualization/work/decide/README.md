# 取り組みを決める

[ルートの業務ユースケースに戻る](../../README.md#uc-decide) · [用語辞書](../../README.md#概念データモデル用語辞書)

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
  %% 親: ../../README.md#業務コンテキスト図 / b_decide
  %% 線は参加・情報の扱い。手順は下のスイムレーン。
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_decide@{ label: "取り組みを決める", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_direction@{ label: "取り組みの判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members --- b_decide
  a_build_agent --- b_decide
  a_product_owner --- b_decide
  i_work_model --- b_decide
  b_decide --- i_direction
  classDef element fill:none,stroke:none,color:#25231F;
  class a_work_members,a_build_agent,a_product_owner,i_work_model,b_decide,i_direction element;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

**扱う情報**：業務モデル → 取り組みの判断。 **対応する要求**：R3・R4。

## 業務フロー（たたき台）

```mermaid
swimlane-beta TB
  %% 展開対象: b_decide。仕事関係者の確認を飛ばさない。
  subgraph people [仕事関係者]
    ask["気になる点を伝える"]
    check["納得できるか確かめる"]
  end
  subgraph assistant_role [fde AI]
    prepare["現状と選択肢を整理する"]
  end
  subgraph engineer [fdeエンジニア]
    record["方針と判断理由を残す"]
  end
  ask --> prepare --> check --> record
```

1. 仕事関係者がどこに納得できないか伝える。
2. fde AIが続ける・試す・見送る案を比べる。
3. 仕事関係者が「実際にはどうか」を確認し、fdeエンジニアが進め方と確かめ方を決める。

試す場合だけ、期待する変化・比較する対象・担当を先に決める。続ける・見送る場合も理由を残す。

既存設計とのつながり：[業務要件定義](../../../../../work/planning/README.md)・[協働設計](../../../../../work/design/README.md)。
