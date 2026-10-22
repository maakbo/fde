# 結合テスト・総合テスト・受入テスト

実装した機能がつながり、システム全体として動き、利用者の業務を満たすかを確認する仕事です。

## 接続・システム・業務の確認

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
  %% parent: ../README.md / b_test
  a_team@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_user@{ label: "業務担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirements@{ label: "要件定義書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "設計書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_test_plan@{ label: "テスト仕様書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_integration@{ label: "結合テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_system@{ label: "総合テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_acceptance@{ label: "受入テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  x_stage@{ label: "検証環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_results@{ label: "テスト結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_team --- b_integration
  a_team --- b_system
  a_team --- b_acceptance
  a_user --- b_acceptance
  i_design --- b_integration
  i_requirements --- b_system
  i_requirements --- b_acceptance
  i_test_plan --- b_integration
  i_test_plan --- b_system
  i_test_plan --- b_acceptance
  b_integration --- x_stage
  b_system --- x_stage
  b_acceptance --- x_stage
  b_integration --- i_results
  b_system --- i_results
  b_acceptance --- i_results

  class a_team,a_user actor;
  class i_requirements,i_design,i_test_plan,i_results information;
  class b_integration,b_system,b_acceptance business;
  class x_stage external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

開発チームと業務担当者が、要件・設計・対象版に基づいて結果を判断します。

## テストの観点と判断する人

| 業務 | 注文登録で確かめる例 | 主に確認する人 |
| --- | --- | --- |
| 結合テスト | 画面からAPIへ値が渡り、DBの結果が応答へ反映されるか | 開発チーム |
| 総合テスト | 登録・検索・変更の一連の操作や、性能・権限などの条件を満たすか | 開発チーム |
| 受入テスト | 営業担当者が業務の例を操作し、必要な結果を得られるか | 業務担当者。開発チームが準備・調査を支援 |

テスト仕様書には入力、前提、操作、期待結果を記載し、対象の版と実行結果を対応づけます。要件と設計から必要な観点を作るため、仕様書も実行の前にレビューします。

不合格なら、再現条件と期待／実際の違いを残します。コードの誤りは実装修正へ、仕様の曖昧さは設計や要件の確認へ戻します。修正後は該当ケースを再実行し、他の機能に影響していないかも確かめます。

## AIエージェントの導入候補

要件・設計・差分からテスト観点を挙げ、実行結果とログを整理し、不具合の再現や原因調査を進めてもらえます。期待結果はAIの推測で確定せず、要件や担当者と照合します。ケース数の増加より、見逃し、誤検知、確認・修正の負担を見ます。

[システム開発の全体](../) / [リリース・運用保守へ](../release-and-operations/)

<!--
## Master references

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| `../people.md` | `a_team` | 開発チーム | 本文に示す担当・入出力・利用先 |
| `../people.md` | `a_user` | 業務担当者 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_requirements` | 要件定義書 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_design` | 設計書 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_test_plan` | テスト仕様書 | 本文に示す担当・入出力・利用先 |
| `../environments.md` | `x_stage` | 検証環境 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_results` | テスト結果 | 本文に示す担当・入出力・利用先 |
-->
