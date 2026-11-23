# 仕事とモデルを見直す

[ルートの業務ユースケースに戻る](../../../README.md#uc-maintain) · [用語辞書](../../../README.md#概念データモデル用語辞書)

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
  %% 親: ../../../README.md#業務コンテキスト図 / b_maintain
  %% 線は参加・情報の扱い。手順は下のスイムレーン。
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_trial@{ label: "試行結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_maintain@{ label: "仕事とモデルを見直す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_change@{ label: "変更記録", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members --- b_maintain
  a_build_agent --- b_maintain
  a_product_owner --- b_maintain
  i_trial --- b_maintain
  b_maintain --- i_change
  classDef element fill:none,stroke:none,color:#25231F;
  class a_work_members,a_build_agent,a_product_owner,i_trial,b_maintain,i_change element;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

**扱う情報**：試行結果 → 変更記録。 **対応する要求**：R1・R4。

## 業務フロー（たたき台）

```mermaid
swimlane-beta TB
  %% 展開対象: b_maintain。仕事関係者の確認を飛ばさない。
  subgraph people [仕事関係者]
    ask["実際の仕事の変化を伝える"]
    check["修正範囲と実態を確かめる"]
  end
  subgraph assistant_role [fde AI]
    prepare["図・手順への影響を洗い出す"]
  end
  subgraph engineer [fdeエンジニア]
    record["採用した変更と理由を残す"]
  end
  ask --> prepare --> check --> record
```

1. 仕事関係者が違和感や結果を持ち寄る。
2. fde AIが関係する図・情報・手順の修正を提案する。
3. 仕事関係者が「実際にはどうか」を確認し、fdeエンジニアが直す範囲を決めて更新する。

試行からだけでなく、仕事が変わった、図にズレを見つけた、といった指摘からも入れる。類似箇所は確認候補にとどめる。

既存設計とのつながり：[導入・運用改善](../../operations/README.md)。
