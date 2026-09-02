# FDE Business Context — 業務モデリング

## Modeling question

`業務モデリング`では、誰がどのInformationをBusinessへ提供し、Businessが何を作成・更新して誰へ提供するか。

## Working natural-language description

主体者は、理解・判断したい対象業務に関する`業務情報`を、`fde`と`fdeAI`に提供する。`fde`と`fdeAI`はそれを基に業務モデリングを行い、`業務モデル`を作成・更新して主体者へ提供する。

## Reading

矢印は、`業務モデリング`を中心にしたInformationまたは価値のhandoff directionを表す。時間順序、判断、詳細な処理手順を表すBusiness Flowではない。`主体者`は入力の提供者と成果の受領者の両方だが、同じActorとして一度だけ置く。

## ASCII options considered

| Option | Reading | Result |
| --- | --- | --- |
| Ordinary relationship hub | Actor / InformationとBusinessの関連だけを`---`で表す | `主体者`が`業務情報`を提供し、`業務モデル`を受け取ることが図単体では弱い。 |
| Left/right relationship hub | 入力要素を左、出力要素と主体者を右へ置く | 左右配置は補助になるが、provider / recipientの意味は依然としてproseへ残る。 |
| Value-flow context | Businessをhubにし、必要な`-->`でhandoff directionを表す | **採用**。自然文の提供・作成／更新・受領を、時間順序にせず最小の6 relationで読める。 |

## Mermaid v0

```mermaid
---
title: FDE Business Context — 業務モデリング
config:
  layout: elk
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 64
    rankSpacing: 80
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:10px !important; }"
---
flowchart LR
  a_fde@{ label: "fde", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_fde_ai@{ label: "fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_subject@{ label: "主体者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business_modeling@{ label: "業務モデリング", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_business_information@{ label: "業務情報", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_business_model@{ label: "業務モデル", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_fde --> b_business_modeling
  a_fde_ai --> b_business_modeling
  a_subject --> b_business_modeling
  i_business_information --> b_business_modeling
  b_business_modeling --> i_business_model
  b_business_modeling --> a_subject

  class a_fde,a_fde_ai,a_subject actor;
  class b_business_modeling business;
  class i_business_information,i_business_model information;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## Boundary

- Actor: `主体者`、`fde`、`fdeAI`
- Business: `業務モデリング`（FDEの子Business）
- Information: `業務情報`、`業務モデル`
- External System: none observed

`業務情報`と`業務モデル`はstable masterではないworking nameである。具体化で実際の意味の違いが見えた場合だけsplitする。`fdeAI`の内部構成、External System、Detailed Business Context、Business FlowはこのViewの外側に置く。

## Unresolved

- `業務情報`を、実際の業務でどの意味Informationへsplitする必要があるか。
- `業務モデル`を主体者がどのように受け取り、利用・更新するか。
- `fdeAI`の判断・行動・責務をActorとしてどこまで区別するか。

## Next review question

このvalue-flow contextが、同じ主体者による入力提供と成果受領を、Business Flowに見せずに読めるか。
