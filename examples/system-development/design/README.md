# 基本設計・詳細設計

要件を、実装とテストで同じ振る舞いを作れる仕様へ具体化する仕事です。

## 要件から実装できる仕様へ

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
  %% parent: ../README.md / b_design
  a_team@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_ops@{ label: "運用担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirements@{ label: "要件定義書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_external@{ label: "外部仕様設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_internal@{ label: "内部処理設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_design_review@{ label: "設計レビュー", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "設計書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_team --- b_external
  a_team --- b_internal
  a_team --- b_design_review
  a_ops --- b_external
  a_ops --- b_design_review
  i_requirements --- b_external
  i_requirements --- b_design_review
  b_external --- b_internal
  b_external --- i_design
  b_internal --- i_design
  b_design_review --- i_design

  class a_team,a_ops actor;
  class i_requirements,i_design information;
  class b_external,b_internal,b_design_review business;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

開発チームが画面・API・データと内部処理を設計し、運用担当者とも必要な条件を確かめます。

## 基本設計と詳細設計

基本設計では、利用者や接続先から見える振る舞いを決めます。注文登録なら、画面の入力項目とエラー表示、APIの受付条件と応答、注文と明細のデータの関係などです。詳細設計では、入力の検証、保存までの処理、トランザクション、失敗時の戻し方を具体化します。

| 観点 | 実装する人・テストする人が知りたいこと |
| --- | --- |
| 画面・API | 何を受け取り、何を返すか。入力不足をどう伝えるか |
| データ | 何を保存し、どの識別子で扱うか。関連するデータの整合をどう保つか |
| 内部処理 | どの責務で判断・保存するか。途中で失敗した時に何が残るか |
| 非機能・運用 | 要件の性能・権限・監視・復旧をどこで実現するか |

レビューでは要件との対応、正常時と例外時、既存機能への影響を確かめます。設計で新たな業務判断が必要になれば要件へ戻し、採用した理由と見送った案も残します。設計書を細かく書く量より、解釈が分かれる点を解消することが重要です。

## AIエージェントの導入候補

関連する要件・既存設計・コードを調べ、影響範囲と設計案、抜けている例外を提示してもらえます。人が責務や方式を選び、決定理由を残します。出力の見栄えより、根拠が正しく、レビューで重要な論点を拾えるかを確かめます。

[システム開発の全体](../) / [実装・単体テストへ](../implementation/)

<!--
## Master references

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| `../people.md` | `a_team` | 開発チーム | 本文に示す担当・入出力・利用先 |
| `../people.md` | `a_ops` | 運用担当者 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_requirements` | 要件定義書 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_design` | 設計書 | 本文に示す担当・入出力・利用先 |
-->
