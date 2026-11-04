# 協働設計

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: true
    nodeSpacing: 64
    rankSpacing: 80
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  %% 提供する業務の概要。操作の順序はworkflowへ。顧客とFDEの分担は各案件で確認する。
  a_customer@{ label: "顧客の担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_fde@{ label: "FDEチーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_input@{ label: "業務要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_prepare@{ label: "役割・情報の設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_decide@{ label: "実装条件の整理", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_output@{ label: "協働仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_customer --- b_prepare
  a_customer --- b_decide
  a_fde --- b_prepare
  a_fde --- b_decide
  i_input --- b_prepare
  b_prepare --- b_decide
  b_decide --- i_output
  class a_customer,a_fde actor;
  class b_prepare,b_decide business;
  class i_input,i_output information;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

顧客の担当者、実装・運用担当者とFDEが、業務要件を役割と処理の設計へ具体化し、協働仕様として実装担当へ渡します。

人、AI、RPA、既存システムの役割と責任を決めます。人の強みをどう活かすか、AIに何を任せるか、誰が結果を確かめるかを、実際の仕事に合わせて考えます。

役割と責任、情報の受け渡しを協働仕様にまとめます。AIを使う部分では、次の事項を具体化します。

- 文脈と入出力：目的、前提、制約、参照情報、判断例。受け取る情報と返す情報、形式と内容の検証方法。
- 起動と接続：人の指示や定時実行などの起動条件。知識、文書、外部システムへの接続先と方法。
- 判断と権限：人が確認・承認・介入する箇所。参照・実行できる範囲と、禁止する操作。
- 検証と安全性：試す場面と評価方法。セキュリティ、法務、倫理上の条件。

JSONなどの出力形式や、RAG・MCP・APIなどの接続方法は、必要に応じて選びます。複雑な判断は抽出、照合、評価などに分け、判断の根拠や人に戻す条件を明確にします。専門的な条件は、必要な専門家と確認します。


顧客の担当者、実装・運用担当者とFDEが、要件を人・AI・システムの動作へ具体化します。設計した仕組みは実装・テストで動かし、PoC・導入評価で業務に役立つかを確かめます。

[顧客と進める手順](workflow.md) / [前：業務要件定義](../planning/README.md) / [次：実装・テスト](../implementation/README.md) / [FDEの仕事全体](../README.md)
