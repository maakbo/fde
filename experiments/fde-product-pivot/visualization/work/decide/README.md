<a name="context"></a>

# 取り組みを決める

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
  accTitle: 取り組みを決める：関わる人と情報
  %% 親: ../../README.md#scope-decide / b_decide
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
  click a_work_members href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-work-members" "仕事関係者の説明を開く" _blank
  click a_build_agent href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-build-agent" "fde AIの説明を開く" _blank
  click a_product_owner href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-product-owner" "fdeエンジニアの説明を開く" _blank
  click i_work_model href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-model" "業務モデルの説明を開く" _blank
  click b_decide href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/work/decide/README.md#flow" "取り組みを決めるの手順を開く" _blank
  click i_direction href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-direction" "取り組みの判断の説明を開く" _blank
```

見えてきた仕事を、そのまま続けるか、別のやり方を試すか考えます。前提となる仕事の見え方が合わなければ、先に確かめ直します。

[いまの問いに戻る](../../README.md#uc-decide) / [ここにつながる仕事を見る](../../README.md#scope-decide)

[![](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](../../README.md#actor-work-members) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](../../README.md#actor-build-agent) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](../../README.md#actor-product-owner)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 業務モデル](../../README.md#info-work-model)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 取り組みを決める](#flow)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 取り組みの判断](../../README.md#info-direction)

<a name="flow"></a>

## 続けるか、試すかを選ぶ

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
  accTitle: 続けるか、試すかを選ぶ
  accDescr: fde AIが案を並べ、仕事関係者が進め方を選びます。試す場合は条件と確かめ方、続けるか見送る場合は理由を残します。前提が合わなければ確かめ直します。
  %% 手順は上から下。誰が判断し、どこで情報を受け渡すかを示す。
  subgraph people [仕事関係者]
    choose["仕事の進め方を選ぶ"]
    recheck["ズレを確かめ直す"]
  end
  subgraph ai [fde AI]
    options["今の進め方と試せる案を並べる"]
  end
  subgraph engineer [fdeエンジニア]
    trial["試す条件と確かめ方を残す"]
    keep["続ける・見送る理由を残す"]
  end
  options --> choose
  choose -->|試す| trial
  choose -->|続ける・見送る| keep
  choose -->|前提が合わない| recheck
```

[![](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](../../README.md#actor-work-members) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](../../README.md#actor-build-agent) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](../../README.md#actor-product-owner)

前提が合わなければ[業務を捉え直す](../understand/README.md#context)。試すと決めたら[実際の変化を確かめる](../validate/README.md#context)。続ける場合は日々の仕事に戻り、[ズレが出たときだけ見直す](../maintain/README.md#context)。

[架空の一件を見る：今の手順を続けると決めた理由](../../WALKTHROUGH.md)

[この仕事の関係に戻る](#context)

## 情報

| いつ、何を使うか | いつ作る・直す・手を離れるか |
| --- | --- |
| [業務モデル](../../README.md#info-work-model) | 選択肢を比べる前提。実態と合わなければ先に図へ戻る。 |
| [取り組みの判断](../../README.md#info-direction) | 結論が出たときに作る。試すときは次の仕事に渡し、続ける・見送るときは判断の理由として残す。 |

## 関連リンク

- [問いに戻る：今のまま進めるか、別のやり方を試すか迷っている](../../README.md#uc-decide)
- [業務を捉える](../understand/README.md)
- [改善を試して確かめる](../validate/README.md)
- [仕事とモデルを見直す](../maintain/README.md)
- 参考：[業務要件定義](https://github.com/maakbo/fde/blob/7d5649d952569543862a58c6a8934200e4436203/work/planning/README.md)・[協働設計](https://github.com/maakbo/fde/blob/7d5649d952569543862a58c6a8934200e4436203/work/design/README.md)。
