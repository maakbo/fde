# 改善を試して確かめる

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
  %% 親: ../../README.md#try-revise / b_validate
  %% 線は参加・情報の扱い。手順は下のスイムレーン。
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_direction@{ label: "取り組みの判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_validate@{ label: "改善を試して確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_trial@{ label: "試行結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members --- b_validate
  a_build_agent --- b_validate
  a_product_owner --- b_validate
  i_direction --- b_validate
  b_validate --- i_trial
  classDef element fill:none,stroke:none,color:#25231F;
  class a_work_members,a_build_agent,a_product_owner,i_direction,b_validate,i_trial element;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  click a_work_members href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-work-members" "関連する説明を開く" _blank
  click a_build_agent href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-build-agent" "関連する説明を開く" _blank
  click a_product_owner href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-product-owner" "関連する説明を開く" _blank
  click i_direction href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-direction" "関連する説明を開く" _blank
  click b_validate href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/work/validate/README.md#flow" "関連する説明を開く" _blank
  click i_trial href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-trial" "関連する説明を開く" _blank
```

事前に決めた条件で、実際の仕事の一部を試します。結果と測れていないことを分けて残します。

[maakbo fde](../../README.md#theme) / [ここにつながる仕事を見る](../../README.md#try-revise)

[![仕事関係者](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](../../README.md#actor-work-members) · [![fde AI](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](../../README.md#actor-build-agent) · [![fdeエンジニア](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](../../README.md#actor-product-owner) · [![取り組みの判断](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 取り組みの判断](../../README.md#info-direction) · [![改善を試して確かめる](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 改善を試して確かめる](#flow) · [![試行結果](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 試行結果](../../README.md#info-trial)

<a name="flow"></a>

## 試して変化を確かめる

```mermaid
swimlane-beta TB
  %% 手順は上から下。誰が判断し、どこで情報を受け渡すかを示す。
  subgraph people [仕事関係者]
    agree["実際に試せる範囲を確かめる"]
    run["仕事の一件で試し、変化を記録する"]
  end
  subgraph ai [fde AI]
    prototype["試す形を用意する"]
  end
  subgraph engineer [fdeエンジニア]
    compare["期待した変化と結果を見比べる"]
    save["観測と分からなかったことを残す"]
  end
  agree --> prototype --> run --> compare --> save
```

[![仕事関係者](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](../../README.md#actor-work-members) · [![fde AI](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](../../README.md#actor-build-agent) · [![fdeエンジニア](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](../../README.md#actor-product-owner)

比較条件が合わなければ決め直す。結果がまとまったら、仕事や図のどこに反映するかを考える。

## 情報

| いつ、何を使うか | いつ作る・直す・手を離れるか |
| --- | --- |
| [取り組みの判断](../../README.md#info-direction) | 試す範囲と比較条件を確かめるときに使う。前提が変わったら決め直す。 |
| [試行結果](../../README.md#info-trial) | 試したときに観測を記録し、比較して追記する。仕事を見直す際の根拠として渡す。 |

## 関連リンク

- [全体の中での位置](../../README.md#uc-validate)：この仕事の入口に戻る。
- [取り組みを決める](../decide/README.md)
- [仕事とモデルを見直す](../maintain/README.md)
- 参考：[実装・テスト](../../../../../work/implementation/README.md)・[PoC・導入評価](../../../../../work/evaluation/README.md)。
