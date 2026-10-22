# 実装・単体テスト

設計をコードにし、処理単位の動作と変更の妥当性を確認する仕事です。

## 実装と検証、レビューの仕事

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
  %% parent: ../README.md / b_build
  a_team@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "設計書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implement@{ label: "実装", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_code@{ label: "ソースコード", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_unit_test@{ label: "単体テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  x_repo@{ label: "ソース管理・CI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_code_review@{ label: "コードレビュー", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_results@{ label: "テスト結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_team --- b_implement
  a_team --- b_unit_test
  a_team --- b_code_review
  i_design --- b_implement
  i_design --- b_unit_test
  b_implement --- i_code
  i_code --- b_unit_test
  i_code --- b_code_review
  b_unit_test --- x_repo
  b_unit_test --- i_results
  b_code_review --- i_results

  class a_team actor;
  class i_design,i_code,i_results information;
  class b_implement,b_unit_test,b_code_review business;
  class x_repo external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

開発チームが実装・テスト・レビューを繰り返し、後続のテストへ渡せる版を作ります。

## コードを書き、確かめて渡す

注文登録の実装では、既存の入力処理や保存処理を読み、変更する責務と呼出し元を確認します。設計で決まった条件に沿ってコードを書き、単体テストで通常の登録と入力不足・保存失敗などを確かめます。テストで問題が出たら原因を調べ、修正して再実行します。

レビューでは差分だけでなく、変更理由、要件・設計との対応、実行したテストと未確認の範囲を共有します。仕様が足りない時は実装者が独断で決めず、設計・要件へ戻します。テスト担当へは、対象の版と確認結果が対応する状態で渡します。

[実装からレビューへ進める流れ](development-flow.md)では、テストに失敗した時の戻り先までたどれます。

## AIエージェントに一件を任せるなら

設計と対象コード、変更範囲、実行可能なテストを渡し、調査→テストとコードの作成→実行→失敗の調査と修正を任せます。返してもらうのはコード案だけでなく、差分、変更理由、実行結果、未解決です。開発者は仕様・設計の採否とレビューを担います。

[エージェントと実装・テストを進める](agent-assisted-flow.md)で、具体的な依頼と返る成果を見ます。

[システム開発の全体](../) / [結合・総合・受入テストへ](../testing/)

<!--
## Master references

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| `../people.md` | `a_team` | 開発チーム | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_design` | 設計書 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_code` | ソースコード | 本文に示す担当・入出力・利用先 |
| `../environments.md` | `x_repo` | ソース管理・CI | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_results` | テスト結果 | 本文に示す担当・入出力・利用先 |
-->
