<a name="context"></a>

# 業務・モデル見直し

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
  accTitle: 業務・モデル見直し：関わる人と情報
  %% 親: ../../README.md#try-revise / b_maintain
  %% 線は参加・情報の扱い。手順は下のスイムレーン。
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_trial@{ label: "試行結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_maintain@{ label: "業務・モデル見直し", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_change@{ label: "変更記録", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members --- b_maintain
  a_build_agent --- b_maintain
  a_product_owner --- b_maintain
  i_trial --- b_maintain
  b_maintain --- i_change
  i_work_example@{ label: "仕事の事例", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_example --- b_maintain
  i_work_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_model --- b_maintain
  classDef element fill:none,stroke:none,color:#25231F;
  class a_work_members,a_build_agent,a_product_owner,i_trial,b_maintain,i_change,i_work_example,i_work_model element;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  click a_work_members href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-work-members" "仕事関係者の説明を開く" _blank
  click a_build_agent href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-build-agent" "fde AIの説明を開く" _blank
  click a_product_owner href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-product-owner" "fdeエンジニアの説明を開く" _blank
  click i_trial href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-trial" "試行結果の説明を開く" _blank
  click b_maintain href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/work/maintain/README.md#flow" "業務・モデル見直しの手順を開く" _blank
  click i_change href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-change" "変更記録の説明を開く" _blank
  click i_work_example href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-example" "仕事の事例の説明を開く" _blank
  click i_work_model href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-model" "業務モデルの説明を開く" _blank
```

仕事と図が違うと分かったら、試行を待たずに直せます。仕事の手順と図のどちらを直すかは、分けて決めます。

[いまの問いに戻る](../../README.md#uc-maintain) / [ここにつながる仕事を見る](../../README.md#try-revise)

[![](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](../../README.md#actor-work-members) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](../../README.md#actor-build-agent) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](../../README.md#actor-product-owner)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 試行結果](../../README.md#info-trial)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 業務・モデル見直し](#flow)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 変更記録](../../README.md#info-change) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 仕事の事例](../../README.md#info-work-example) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 業務モデル](../../README.md#info-work-model)

<a name="flow"></a>

## 指摘を確かめて直す

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
  accTitle: 指摘を確かめて直す
  accDescr: 仕事関係者が事例や結果を持ち寄り、fde AIが影響を探します。仕事関係者が見直すかを決め、fdeエンジニアが図や記録を更新し、理由を残します。
  %% 手順は上から下。誰が判断し、どこで情報を受け渡すかを示す。
  subgraph people [仕事関係者]
    note["仕事の事例や試行結果を持ち寄る"]
    confirm["仕事はそのままか、見直すかを決める"]
  end
  subgraph ai [fde AI]
    impact["図・用語・手順への影響を探す"]
  end
  subgraph engineer [fdeエンジニア]
    update["確認した図や記録を更新する"]
    record["変えた箇所と理由を残す"]
  end
  note --> impact --> confirm --> update --> record
```

[![](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](../../README.md#actor-work-members) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](../../README.md#actor-build-agent) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](../../README.md#actor-product-owner)

図の前提が変わったら[実態を確かめ直す](../understand/README.md#context)。進め方や試行条件が変わるなら、[方針選定](../decide/README.md#context)。

[この仕事の関係に戻る](#context)

## 情報

| いつ、何を使うか | いつ作る・直す・手を離れるか |
| --- | --- |
| [仕事の事例](../../README.md#info-work-example) | 日々の指摘は事例と照らす。試行していなくても、見直しの根拠になる。 |
| [試行結果](../../README.md#info-trial) | 改善を試した場合だけ使う。採否を決めるときの根拠になる。 |
| [業務モデル](../../README.md#info-work-model) | 現状と照合し、関係者が確かめた箇所だけを更新する。 |
| [変更記録](../../README.md#info-change) | 判断がついた時点で残す。仕事を変えない場合も、図を直した理由を後からたどれる。 |

## 関連リンク

- [問いに戻る：図と実際の仕事が、どこか違う](../../README.md#uc-maintain)
- [業務可視化](../understand/README.md)
- [方針選定](../decide/README.md)
- [試行・評価](../validate/README.md)
- 参考：[導入・運用改善](https://github.com/maakbo/fde/blob/7d5649d952569543862a58c6a8934200e4436203/work/operations/README.md)。
