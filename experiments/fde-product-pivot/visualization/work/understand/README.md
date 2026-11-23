# 業務を捉える

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
  %% 親: ../../README.md#scope-decide / b_understand
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
  click a_work_members href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-work-members" "関連する説明を開く" _blank
  click a_build_agent href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-build-agent" "関連する説明を開く" _blank
  click a_product_owner href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-product-owner" "関連する説明を開く" _blank
  click i_work_example href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-example" "関連する説明を開く" _blank
  click b_understand href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/work/understand/README.md#flow" "関連する説明を開く" _blank
  click i_work_model href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-model" "関連する説明を開く" _blank
```

仕事の説明が噛み合わないとき、実際に起きた一件から始めます。見え方が違うところは残し、何をもう一度聞けばよいかを確かめます。

[maakbo fde](../../README.md#theme) / [ここにつながる仕事を見る](../../README.md#scope-decide)

[![仕事関係者](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](../../README.md#actor-work-members) · [![fde AI](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](../../README.md#actor-build-agent) · [![fdeエンジニア](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](../../README.md#actor-product-owner) · [![仕事の事例](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 仕事の事例](../../README.md#info-work-example) · [![業務を捉える](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 業務を捉える](#flow) · [![業務モデル](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 業務モデル](../../README.md#info-work-model)

<a name="flow"></a>

## 一件の仕事を図にする

```mermaid
swimlane-beta TB
  %% 手順は上から下。誰が判断し、どこで情報を受け渡すかを示す。
  subgraph people [仕事関係者]
    bring["実際に起きた一件を持ち寄る"]
    compare["図と実際の仕事を見比べる"]
  end
  subgraph ai [fde AI]
    draw["目的・役割・受け渡しを図にする"]
  end
  subgraph engineer [fdeエンジニア]
    save["業務モデルと未確認点を残す"]
  end
  bring --> draw --> compare --> save
  compare -->|違う箇所がある| draw
```

[![仕事関係者](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](../../README.md#actor-work-members) · [![fde AI](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](../../README.md#actor-build-agent) · [![fdeエンジニア](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](../../README.md#actor-product-owner)

図と実態が合えば、進め方を決める。運用中にズレが見つかったら見直す。

## 情報

| いつ、何を使うか | いつ作る・直す・手を離れるか |
| --- | --- |
| [仕事の事例](../../README.md#info-work-example) | 話を始めるときに受け取り、図の根拠として残す。 |
| [業務モデル](../../README.md#info-work-model) | 話を図にして作る。図を確かめた結果と、分からない点を反映する。 |

## 関連リンク

- [全体の中での位置](../../README.md#uc-understand)：この仕事の入口に戻る。
- [取り組みを決める](../decide/README.md)
- [仕事とモデルを見直す](../maintain/README.md)
- 参考：[業務理解・対象選定](../../../../../work/discovery/README.md)。
