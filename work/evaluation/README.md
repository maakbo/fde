# PoC・導入評価

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
  i_input@{ label: "試作品と評価条件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_prepare@{ label: "試行・測定", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_decide@{ label: "導入可否の判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_output@{ label: "評価結果と次の判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

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

顧客の担当者・成果を受け取る人とFDEが、試行の事実を合格条件と比べ、次の範囲を判断します。

### 協働検証

協働仕様に沿った試作品で動作を確かめ、実際の仕事に近い場面で、業務に使えるかを検証します。試作品（Prototype）、実現性や効果の検証（PoC）、価値を届ける最小限の仕組み（MVP）は、確かめたいことに応じて使い分けます。

本番のデータや権限に影響を与えにくい環境で、次の点を確認します。

- 業務への効果と使い心地：期待した変化があるか。大切にしたいことを守れ、関係者が無理なく納得して使えるか。
- 品質と負担：精度、速度、例外への対応。人が確認する負担や、前後の仕事への影響。
- 安全性と継続性：権限や情報の扱い、再現性、利用料と運用コスト。

評価内容と使う人の実感を協働検証結果にまとめます。合格基準と照らし合わせ、導入へ進む、今回は進めない、対象・設計・手段を変えて再検証する、のいずれかを関係者で決めます。AIを使わない方法も含めて選び、判断の根拠と次に確かめることを残します。

検証で業務の条件や役割分担に不足が分かれば、業務定義や協働設計に戻ります。

[顧客と進める手順](workflow.md) / [FDEの仕事全体](../README.md)
