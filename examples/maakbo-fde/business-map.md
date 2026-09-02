# FDE Business Map — working hypothesis

## Modeling question

FDEというWhatを構成するBusinessには何があるか。

## Reading

中央の`FDE`と周囲の七つのBusinessの構成関係を読む。線は工程順、handoff、依存方向を表さない。どのBusinessから別のBusinessへ戻ることもあり、Business Flowとして読まない。

```mermaid
---
title: FDE Business Map
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
flowchart TB
  b_fde@{ label: "FDE", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_context_understanding@{ label: "現場理解", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_business_structuring@{ label: "業務構造化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_change_design@{ label: "変化設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_collaboration_design@{ label: "協働設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_realization@{ label: "仕組み化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_context_fit@{ label: "現場適合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_autonomy_transition@{ label: "自律移行", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_fde --- b_context_understanding
  b_fde --- b_business_structuring
  b_fde --- b_change_design
  b_fde --- b_collaboration_design
  b_fde --- b_realization
  b_fde --- b_context_fit
  b_fde --- b_autonomy_transition

  class b_fde,b_context_understanding,b_business_structuring,b_change_design,b_collaboration_design,b_realization,b_context_fit,b_autonomy_transition business;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## Working set

| Business | Transformation | Observable output |
| --- | --- | --- |
| 現場理解 | 断片的な事実や語りを、扱える現場像へする | 共有できる現場像 |
| 業務構造化 | 複雑な業務の意味と関係を、考えられる構造へする | 業務Model |
| 変化設計 | 現状とありたい状態の差を、選べる変化へする | 変化案 |
| 協働設計 | 異なる強み・責務・制約を、無理なく協働できる関係へする | 役割・責務・境界の設計 |
| 仕組み化 | 設計した協働を、現場で利用できる形へする | 利用できる業務の仕組み |
| 現場適合 | 利用で分かったズレを、現場で自然に成り立つ状態へ戻す | 整えられた仕組みとModel |
| 自律移行 | FDE側に偏る理解と変更可能性を、主体者たちが扱える状態へ移す | 自分たちで運営・変更できる状態 |

## Not a flow

七つは工程順ではない。例えば、現場適合で見つけたズレから業務構造化や現場理解へ戻り、変化設計や協働設計を更新することがある。順序、判断、分岐、reworkが必要になったBusinessだけを、別のBusiness Flowで扱う。

`共育`はこのMapのpeer Businessに置かない。現時点では、七つのBusinessを通じて、主体者、仲間、AI Agent、Systemと仕組みを`共に育てる`というworking principleとして扱う。

## Complexity note

中央のtitle-level Businessを含む8 nodeを、FDEのworking set全体を一度に比較するための意図的なoverviewとして保持する。詳細を詰め込んだ観察図ではなく、各Businessの責任範囲を比較する構成図である。
