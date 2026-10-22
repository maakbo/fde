# 要件定義

開発要求から、作る範囲と受入条件を合意する仕事です。

## 要求から要件合意まで

```mermaid
---
config:
  layout: dagre
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
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  %% parent: ../README.md / b_requirements
  a_user@{ label: "業務担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_team@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_request@{ label: "開発要求", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_interview@{ label: "業務ヒアリング", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_specify@{ label: "要件具体化", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_agree@{ label: "要件合意", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirements@{ label: "要件定義書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_user --- b_interview
  a_user --- b_agree
  a_team --- b_interview
  a_team --- b_specify
  a_team --- b_agree
  i_request --- b_interview
  b_interview --- b_specify
  b_specify --- i_requirements
  b_agree --- i_requirements

  class a_user,a_team actor;
  class i_request,i_requirements information;
  class b_interview,b_specify,b_agree business;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

業務担当者が困っていることを聞き、開発チームが機能と品質の条件へ具体化します。

## 何を聞き、何を決めるか

受注管理を作るなら、「注文を登録したい」だけでは十分ではありません。現在の受付方法、登録する担当、入力元、登録後に結果を使う人まで聞きます。最近の注文を一件たどり、確認漏れや例外がどこで起きるかを確かめます。

| 観点 | この例で具体化すること |
| --- | --- |
| 目的・対象範囲 | 二重入力を減らす。注文登録・変更・照会を対象にし、会計処理は今回の対象外とする |
| 機能 | 誰が注文を登録・変更し、何を検索できるか |
| 品質・運用 | 必要な応答性能、権限、障害時の業務。目標値は利用状況を確認して合意する |
| 受入条件 | 業務担当者がどの例を操作し、何を確認できればよいか |

要件定義書には、決定した条件と理由、対象外、未決定と確認先を残します。レビューで認識違いがあれば、該当する要件を修正して再確認します。要件を変えた時は、設計やテストへの影響も調べます。

## AIエージェントの導入候補

ヒアリング記録から要求と未決定を整理し、既存仕様との矛盾や追加で聞くべき問いを挙げてもらえます。要求の優先順位や受入条件の合意は、業務担当者と開発チームで行います。記録を短くできたかだけでなく、認識違いを早く見つけられたかを見ます。

[システム開発の全体](../) / [設計へ](../design/)

<!--
## Master references

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| `../people.md` | `a_user` | 業務担当者 | 本文に示す担当・入出力・利用先 |
| `../people.md` | `a_team` | 開発チーム | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_request` | 開発要求 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_requirements` | 要件定義書 | 本文に示す担当・入出力・利用先 |
-->
