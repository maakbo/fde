# 改善を試して確かめる

[ルートの業務ユースケースに戻る](../../../README.md#uc-validate) · [用語辞書](../../../README.md#概念データモデル用語辞書)

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
  %% 親: ../../../README.md#業務コンテキスト図 / b_validate
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
```

**扱う情報**：取り組みの判断 → 試行結果。 **対応する要求**：R4。

## 業務フロー（たたき台）

```mermaid
swimlane-beta TB
  %% 展開対象: b_validate。仕事関係者の確認を飛ばさない。
  subgraph people [仕事関係者]
    ask["どこで試せるか伝える"]
    check["使って変化を確かめる"]
  end
  subgraph assistant_role [fde AI]
    prepare["試す形を用意する"]
  end
  subgraph engineer [fdeエンジニア]
    record["結果と次の判断を残す"]
  end
  ask --> prepare --> check --> record
```

1. 仕事関係者が試行の条件を確かめる。
2. fde AIが試作と結果の整理を支援する。
3. 仕事関係者が「実際にはどうか」を確認し、fdeエンジニアが根拠を見て次の扱いを決める。

事前に合意した条件と実際の変化を比べる。測れなかった効果は推測で埋めず、判断保留にできるようにする。

既存設計とのつながり：[実装・テスト](../../implementation/README.md)・[PoC・導入評価](../../evaluation/README.md)。
