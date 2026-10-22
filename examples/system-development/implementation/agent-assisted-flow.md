# AIエージェントと実装・テストを進める

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  %% parent: ../README.md / b_build; proposed agent-assisted workflow, not field-tested
  b_assign@{ label: "作業を渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_read@{ label: "変更を調べる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implement@{ label: "実装する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_test@{ label: "テストする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_pass@{ label: "テスト合格？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fix@{ label: "失敗を調べる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_report@{ label: "結果を返す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_review@{ label: "レビューする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_assign --> b_read
  b_read --> b_implement
  b_implement --> b_test
  b_test --> d_pass
  d_pass -->|合格| b_report
  b_report --> b_review
  d_pass -->|不合格| b_fix
  b_fix --> b_implement

  class b_assign,b_read,b_implement,b_test,b_fix,b_report,b_review activity;
  class d_pass decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

最初の「作業を渡す」と最後の「レビューする」は開発者が担い、その間の調査・実装・テスト・修正・結果の報告をエージェントへ任せます。

開発者が、対象機能、合意した設計、変更範囲、実行できるテストをエージェントへ渡します。エージェントは調査から実装・テストまでを進め、失敗の原因を調べて修正します。開発者は途中の仕様判断と最後のレビューを担います。この役割分担は架空の導入案で、実務の効果は未測定です。

## 注文登録の実装を頼む

例えば、設計で合意した注文登録APIの作業を渡します。

> 注文登録APIを実装したい。関連する設計、既存の受付・保存処理、テストを読み、変更範囲を確認して。決定済みの条件に沿って単体テストと実装を進め、テストを実行してほしい。失敗したら原因を調べて修正して。仕様が足りないところは決めずに質問し、差分・変更理由・実行結果・未解決を返して。

| 場面 | エージェントが行うこと | 開発者が決めること |
| --- | --- | --- |
| 影響調査 | 呼出し元、関連データ、既存テスト、設計との違いを根拠付きで提示 | 対象範囲、設計の変更や未決定仕様 |
| 実装・検証 | 合意済み条件からテストとコードを作り、許可された環境で実行し、失敗を調査・修正 | 新しい仕様が必要な時の採否、変更を止める条件 |
| レビュー | 差分、根拠、実行したテストと残件を返す | 要件への適合、保守性、変更の採用 |

今回はローカルの差分作成とテストまでを任せる想定です。利用する資料と環境の許可、実行範囲はチームで確認し、mergeや本番反映は別の判断にします。正しいテストが書けたかは設計の条件と照合します。エージェント自身が書いたテストの成功だけで合格にしません。

導入前後で、同程度の変更にかかる調査・実装・修正・レビューの負担、仕様の見落としや不具合を見ると、何が改善したかを話せます。テストが通るまでの回数や生成コード量だけを成果にしません。代表例と例外を一件ずつたどり、合わなければ任せる範囲と情報の渡し方を直します。

[実装・単体テスト](README.md) / [開発者が進める一周](development-flow.md)
