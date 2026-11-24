<a name="theme"></a>

# maakbo fde

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
  accTitle: fdeを育てる仕事の関係
  %% テーマコンテキスト図：製品を育てる活動。fdeで描く個々の仕事は別のテーマ。
  %% 右の仕事関係者は一つのアクター群。複数人を表すが、人数や内訳は特定しない。
  %% 点線は目指すゴールを添えるための注釈。業務フローではない。
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fde_product("fdeを育てる")
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  x_github@{ label: "GitHub", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  goal["仕事をAIと一緒に可視化して、<br/>関わるものたちが納得して進められて、<br/>仕事がうまくいきます。"]

  a_product_owner --- b_fde_product
  a_build_agent --- b_fde_product
  b_fde_product -.- goal
  b_fde_product --- a_work_members
  b_fde_product --- x_github

  classDef icon fill:none,stroke:none,color:#25231F;
  classDef compass fill:none,stroke:none,color:#25231F,font-weight:600;
  classDef themeNode fill:#FFFFFF,stroke:#4A4640,stroke-width:1.25px,color:#25231F,font-weight:700,font-size:23px;
  class a_product_owner,a_build_agent,a_work_members,x_github icon;
  class goal compass;
  class b_fde_product themeNode;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  linkStyle 2 stroke:#A0988E,stroke-width:1px,stroke-dasharray:2 4;
  click a_product_owner href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-product-owner" "fdeエンジニアの説明を開く" _blank
  click a_build_agent href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-build-agent" "fde AIの説明を開く" _blank
  click a_work_members href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-work-members" "仕事関係者の説明を開く" _blank
  click x_github href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#github" "GitHubの説明を開く" _blank
```

**仕事をAIと一緒に可視化して、関わるものたちが納得して進められて、仕事がうまくいきます。**

仕事の話を持ち寄り、fde AIと一緒に、目的・役割・情報のつながりを一枚にします。図を見ながら進め方を決めるのは、仕事に関わる人たちです。ここでは、fdeを育てる仕事そのものを描いています。

<a name="questions"></a>

## いま、何を確かめたい？

- <a name="uc-understand"></a>**同じ仕事の話なのに、説明がかみ合わない**\
  [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 業務可視化](work/understand/README.md#context)：実際に起きた一件をたどり、誰が何を受け渡しているかを一枚にする。
- <a name="uc-decide"></a>**今のまま進めるか、別のやり方を試すか迷っている**\
  [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 方針選定](work/decide/README.md#context)：選択肢を見比べ、何を選んだかと、その理由を残す。
- <a name="uc-validate"></a>**試したやり方で、本当に仕事がよくなるか知りたい**\
  [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 試行・評価](work/validate/README.md#context)：何が変わったかと、まだ分からないことを分けて残す。
- <a name="uc-maintain"></a>**図と実際の仕事が、どこか違う**\
  [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 業務・モデル見直し](work/maintain/README.md#context)：ズレた箇所を確かめ、仕事を変えるのか、図だけを直すのかを決める。

[架空の一件をたどる：今の手順を続けると決めた理由](WALKTHROUGH.md)

## 関わる人と仕組み

[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](#actor-product-owner) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](#actor-build-agent) · [![](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](#actor-work-members) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg) GitHub](#github)

| 誰が | どう関わるか |
| --- | --- |
| <a name="actor-product-owner"></a>fdeエンジニア | fdeの設計を整え、使って分かったことを次の設計に生かす。自分で試すときは仕事関係者にもなる。 |
| <a name="actor-build-agent"></a>fde AI | 話し言葉を図や記録にし、ズレの指摘から、ほかに確かめる場所を探す。判断は人に返す。 |
| <a name="actor-work-members"></a>仕事関係者 | 仕事を進める人、判断や支援をする人、成果を受け取る人。立場ごとに見えていることを持ち寄る。 |
| <a name="github"></a>GitHub | 図、用語、判断の記録を共有し、何をなぜ直したかを後からたどれる場所。 |

## 業務

<a name="scope-decide"></a>

### 仕事を持ち寄り、進め方を決める

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
  accTitle: 仕事を持ち寄り、進め方を決める
  %% 線は業務に関わる人・情報の関係を示す。手順は各業務のページへ。
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_understand@{ label: "業務可視化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_decide@{ label: "方針選定", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_example@{ label: "仕事の事例", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_direction@{ label: "取り組みの判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members --- b_understand
  a_work_members --- b_decide
  a_build_agent --- b_understand
  a_build_agent --- b_decide
  a_product_owner --- b_understand
  a_product_owner --- b_decide
  i_work_example --- b_understand
  b_understand --- i_work_model
  i_work_model --- b_decide
  b_decide --- i_direction
  classDef element fill:none,stroke:none,color:#25231F;
  class a_work_members,a_build_agent,a_product_owner,b_understand,b_decide,i_work_example,i_work_model,i_direction element;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  click a_work_members href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-work-members" "仕事関係者の説明を開く" _blank
  click a_build_agent href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-build-agent" "fde AIの説明を開く" _blank
  click a_product_owner href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-product-owner" "fdeエンジニアの説明を開く" _blank
  click b_understand href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/work/understand/README.md" "業務可視化の説明を開く" _blank
  click b_decide href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/work/decide/README.md" "方針選定の説明を開く" _blank
  click i_work_example href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-example" "仕事の事例の説明を開く" _blank
  click i_work_model href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-model" "業務モデルの説明を開く" _blank
  click i_direction href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-direction" "取り組みの判断の説明を開く" _blank
```

一件の仕事を、関係者が照らし合わせられる図にします。今のまま続ける、改善を試す、見送るのどれでも、決めた理由を残します。

[![](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](#actor-work-members) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](#actor-build-agent) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](#actor-product-owner)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 業務可視化](work/understand/README.md#context) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 方針選定](work/decide/README.md#context)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 仕事の事例](#info-work-example) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 業務モデル](#info-work-model) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 取り組みの判断](#info-direction)

<a name="try-revise"></a>

### 試した結果や日々の気づきから見直す

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
  accTitle: 試した結果や日々の気づきから見直す
  %% 線は業務に関わる人・情報の関係を示す。手順は各業務のページへ。
  a_work_members@{ label: "仕事関係者", img: "https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_build_agent@{ label: "fde AI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_product_owner@{ label: "fdeエンジニア", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  x_github@{ label: "GitHub", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_validate@{ label: "試行・評価", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_maintain@{ label: "業務・モデル見直し", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_direction@{ label: "取り組みの判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_trial@{ label: "試行結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_example@{ label: "仕事の事例", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_work_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_change@{ label: "変更記録", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_work_members --- b_validate
  a_work_members --- b_maintain
  a_build_agent --- b_validate
  a_build_agent --- b_maintain
  a_product_owner --- b_validate
  a_product_owner --- b_maintain
  i_direction --- b_validate
  b_validate --- i_trial
  i_trial --- b_maintain
  i_work_example --- b_maintain
  b_maintain --- i_work_model
  b_maintain --- i_change
  b_maintain --- x_github
  classDef element fill:none,stroke:none,color:#25231F;
  class a_work_members,a_build_agent,a_product_owner,x_github,b_validate,b_maintain,i_direction,i_trial,i_work_example,i_work_model,i_change element;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
  click a_work_members href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-work-members" "仕事関係者の説明を開く" _blank
  click a_build_agent href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-build-agent" "fde AIの説明を開く" _blank
  click a_product_owner href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#actor-product-owner" "fdeエンジニアの説明を開く" _blank
  click x_github href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#github" "GitHubの説明を開く" _blank
  click b_validate href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/work/validate/README.md" "試行・評価の説明を開く" _blank
  click b_maintain href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/work/maintain/README.md" "業務・モデル見直しの説明を開く" _blank
  click i_direction href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-direction" "取り組みの判断の説明を開く" _blank
  click i_trial href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-trial" "試行結果の説明を開く" _blank
  click i_work_example href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-example" "仕事の事例の説明を開く" _blank
  click i_work_model href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-model" "業務モデルの説明を開く" _blank
  click i_change href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-change" "変更記録の説明を開く" _blank
```

試すと決めた場合は結果を持ち寄ります。改善を試していなくても、仕事と図が違うという指摘だけで見直せます。手順は変えず、図だけを直しても構いません。

[![](https://raw.githubusercontent.com/maakbo/fde/523072a59582f5d41d998c1b2f65929afc47270d/experiments/fde-product-pivot/work-group.svg) 仕事関係者](#actor-work-members) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg) fde AI](#actor-build-agent) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg) fdeエンジニア](#actor-product-owner) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg) GitHub](#github)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 試行・評価](work/validate/README.md#context) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg) 業務・モデル見直し](work/maintain/README.md#context)  
[![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 取り組みの判断](#info-direction) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 試行結果](#info-trial) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 仕事の事例](#info-work-example) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 業務モデル](#info-work-model) · [![](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 変更記録](#info-change)

<a name="information"></a>

## 情報

```mermaid
---
config:
  theme: neutral
  themeVariables:
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  class:
    hideEmptyMembersBox: true
---
classDiagram
  accTitle: 情報のつながり
  accDescr: 仕事の事例、業務モデル、取り組みの判断、試行結果、変更記録の関係。各用語の意味と使う仕事は図の下の表から開けます。
  direction LR
  %% 業務の中で使う情報と同じID。保存形式や件数は規定しない。
  class i_work_example["仕事の事例"]
  class i_work_model["業務モデル"]
  class i_direction["取り組みの判断"]
  class i_trial["試行結果"]
  class i_change["変更記録"]
  i_work_example -- i_work_model : 根拠
  i_work_model -- i_direction : 判断の前提
  i_direction -- i_trial : 試す条件
  i_trial -- i_change : 見直しの根拠
  i_work_example -- i_change : 指摘の根拠
  i_change -- i_work_model : 変更対象
  click i_work_example href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-example" "仕事の事例の説明を開く" _blank
  click i_work_model href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-work-model" "業務モデルの説明を開く" _blank
  click i_direction href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-direction" "取り組みの判断の説明を開く" _blank
  click i_trial href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-trial" "試行結果の説明を開く" _blank
  click i_change href "https://github.com/maakbo/fde/blob/draft/fde-product-pivot/experiments/fde-product-pivot/visualization/README.md#info-change" "変更記録の説明を開く" _blank
```

試行結果を残すのは、試すと決めた場合です。今の仕事を続ける判断も、理由とともに残します。

| この仕事で使う言葉 | 意味 | どこで使うか |
| --- | --- | --- |
| <a name="info-work-example"></a>![情報](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 仕事の事例 | 実際に起きた一件。誰が何を受け取り、どう判断して誰に渡したかをたどれる話や記録。 | [業務可視化](work/understand/README.md#context)・[業務・モデル見直し](work/maintain/README.md#context) |
| <a name="info-work-model"></a>![情報](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 業務モデル | 仕事の目的・関係者・業務・情報のつながりを、関係者の言葉で表したもの。 | [業務可視化](work/understand/README.md#context)・[方針選定](work/decide/README.md#context)・[業務・モデル見直し](work/maintain/README.md#context) |
| <a name="info-direction"></a>![情報](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 取り組みの判断 | 今のやり方を続ける、改善を試す、見送るなど、次の方針と理由。試すときは確かめ方も含む。 | [方針選定](work/decide/README.md#context)・[試行・評価](work/validate/README.md#context) |
| <a name="info-trial"></a>![情報](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 試行結果 | 事前に合意した条件で試し、分かった変化と、まだ測れていないことを残したもの。 | [試行・評価](work/validate/README.md#context)・[業務・モデル見直し](work/maintain/README.md#context) |
| <a name="info-change"></a>![情報](https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg) 変更記録 | 何を直すか、何を変えないか、その理由と影響範囲の記録。 | [業務・モデル見直し](work/maintain/README.md#context) |

[情報のつながりを見る](#information)

## 関連リンク

- [業務可視化](work/understand/README.md#context)
- [方針選定](work/decide/README.md#context)
- [試行・評価](work/validate/README.md#context)
- [業務・モデル見直し](work/maintain/README.md#context)
- [FDEの実務ガイド](https://github.com/maakbo/fde/blob/7d5649d952569543862a58c6a8934200e4436203/work/README.md)：業務理解から導入・運用までの進め方。
