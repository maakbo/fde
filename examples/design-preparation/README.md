# 要件を受けて、設計を開発へ渡す

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
  %% 架空の開発チームの現状。基本設計と変更実装という兄弟業務の関係。線は順序を示さない。
  %% b_prepare_designをcurrent-flow.mdとagent-assisted-flow.mdへ展開。
  a_se@{ label: "SE", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_designer@{ label: "設計担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_reviewer@{ label: "レビュー担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirement@{ label: "確定要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_prepare_design@{ label: "設計をまとめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "基本設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implement@{ label: "変更を実装する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_developer@{ label: "開発担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_se --- b_prepare_design
  a_designer --- b_prepare_design
  a_reviewer --- b_prepare_design
  i_requirement --- b_prepare_design
  b_prepare_design --- i_design
  i_design --- b_implement
  b_prepare_design --- a_developer
  b_implement --- a_developer

  class a_se,a_designer,a_reviewer,a_developer actor;
  class b_prepare_design,b_implement business;
  class i_requirement,i_design information;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

架空の開発チームの現状です。設計担当は確定要件を受け取り、不明点をSEへ確認し、独立したレビューと修正を経た基本設計を開発担当へ渡します。開発担当は設計を受けて実装・テストへ進みます。

設計をまとめる作業の順序と担当は、[現在の設計業務](current-flow.md)へ分けました。[変更案](agent-assisted-flow.md)は別の図です。

架空の例です。実際の現場の合意や効果を示すものではありません。

[この業務で作業Skillを試した結果](practice.md)／[同じ条件で始める架空の入力](intake.md)／[自分の仕事で始める](../../work/README.md)

## 設計の判断も引き継ぐ

[経験者の判断を次の設計へ渡す](knowledge-practice.md)では、承認済み手順と新しい未承認メモを照合し、別の受取役が新しい依頼へ使えるかを試します。

[要件から設計下書きへ渡す情報](data-practice.md)では、文章・ID・数値の処理を分け、型が合っていても意味が違う出力を戻すところを試します。

[設計の根拠を探し、条件が落ちた場所を確かめる](retrieval-practice.md)では、分割・検索・回答入力・回答を追い、同じ資料の照合結果を引き継ぎます。小さな文字検索もローカルで実行できます。

[設計書をAIへ渡してよいか、判断できる材料をそろえる](governance-practice.md)では、情報経路と契約・方針・操作許可を分け、相談結果を制御と次の試行へつなぎます。

[設計メモを記録し、参照する仕様の版をそろえる](lifecycle-practice.md)では、曖昧なコメント・表の意味を確かめ、発効時点や更新途中の参照を分けて試します。

[設計下書きが速くなったら、次に何を試すか](next-step-practice.md)では、品質の確認だけで対象を広げず、レビューと引継ぎを含めて次の一歩を決めます。

[基本設計のAI支援を、何で成功と判断するか](success-practice.md)では、望む余力から必要な利用と品質をつなぎ、試す前の条件を作ります。

[設計の下書きと仕様の確定を分ける](automation-practice.md)では、自動化の候補を比較し、根拠不足・許可外・確認者不在の時に何を進めるかを試します。

[準備済みの要件から、レビューできる下書きを届ける](action-practice.md)では、起動と処理の成果をつなぎ、保存/受渡し失敗からの再開をローカルで試します。

[設計のAI支援を選び、次の担当へ渡す](standard-handoff/README.md)では、候補・業務境界・現行・役割・評価・判断の6成果を同じIDでつなぎます。

[実践例の一覧](../../examples/README.md) / [FDEの仕事と業務](../../work/README.md)

[変更レビューの準備](branch-practice.md)では、変更種別・影響度・資料の利用条件から、担当と確認範囲を振り分けます。

[検索機能の設計レビュー](context-practice.md)では、作業へ渡す要件・API契約・許可を選び、根拠が欠ける時の返却まで確認します。

[設計支援の導入準備](adoption-practice.md)では、担当者の懸念を試せる条件へ整理し、依頼・確認・訂正・受渡しを練習します。
