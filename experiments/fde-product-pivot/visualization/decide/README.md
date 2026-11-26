<a name="context"></a>

# 方針決定

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
  accTitle: 方針決定を構成する二つの業務
  %% 親: ../README.md#uc-decide / b_decide
  %% 業務コンテキストの b_decide を「前提確認」と「方針決定」に分解する。線は参加・情報の関係。
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_confirm@{ label: "前提確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_select@{ label: "方針決定", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_direction@{ label: "方針判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members --- b_confirm
  a_work_members --- b_select
  a_build_agent --- b_select
  a_product_owner --- b_select
  i_work_model --- b_confirm
  i_work_model --- b_select
  b_select --- i_direction
  classDef element fill:none,stroke:none,color:#25231F;
  class a_work_members,a_build_agent,a_product_owner,i_work_model,b_confirm,b_select,i_direction element;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

まず**前提確認**で、仕事関係者が業務モデルと実態のズレを確かめます。**方針決定**では、fde AIが[業務モデル](../README.md#info-work-model)をもとに現行と変更案を比較し、仕事関係者が続ける・試す・見送るを選びます。fdeエンジニアは、前提と結論、その理由を[方針判断](../README.md#info-direction)に残します。

<a name="flow"></a>

## 方針決定の進め方

```mermaid
---
config:
  theme: neutral
  swimlane:
    ignoreCrossLaneEdges: false
    optimizeRanksByCrossings: false
  themeVariables:
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
---
swimlane-beta TB
  accTitle: 方針決定の業務フロー
  accDescr: 仕事関係者が現状の前提を確かめ、fde AIが案を比較します。仕事関係者が選び、fdeエンジニアが結論と次へ渡す内容を記録します。
  %% 対象: このページの b_select。前提確認の結果から開始し、ずれがあれば業務可視化へ戻る。
  subgraph engineer [fdeエンジニア]
    trial["試す範囲・比較条件を記録し、試行・評価へ渡す"]
    keep["続ける・見送る理由と見直す条件を記録する"]
  end
  subgraph ai [fde AI]
    options["現行と変更案の違い・制約を整理する"]
  end
  subgraph people [仕事関係者]
    check{"業務モデルは実態と合っているか？"}
    recheck["業務可視化に戻り、違う箇所を確かめ直す"]
    choose{"どの進め方を選ぶか？"}
  end
  check -->|合っている| options
  check -->|違いがある| recheck
  options --> choose
  choose -->|試す| trial
  choose -->|続ける・見送る| keep
```

業務モデルが実態と違う場合は、案を選ぶ前に[業務可視化](../README.md#uc-understand)へ戻ります。

試すときは、対象とする仕事、何と比べるか、何を見て判断するかを決めてから[試行・評価](../README.md#uc-validate)へ渡します。続けるときは今の仕事に戻ります。変更案を見送るときは、その案と理由を残します。どちらの場合も、見直す条件があれば記録します。

[全体の「方針決定」に戻る](../README.md#uc-decide)
