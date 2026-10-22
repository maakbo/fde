# 開発で受け渡す成果物

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
flowchart TB
  i_request@{ label: "開発要求", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirements@{ label: "要件定義書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "設計書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_code@{ label: "ソースコード", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_test_plan@{ label: "テスト仕様書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_results@{ label: "テスト結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_operation@{ label: "運用手順書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_incident@{ label: "障害・変更依頼", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  i_request --- i_requirements
  i_requirements --- i_design
  i_requirements --- i_test_plan
  i_design --- i_code
  i_design --- i_test_plan
  i_code --- i_results
  i_test_plan --- i_results
  i_results --- i_operation
  i_operation --- i_incident
  i_incident --- i_request

  class i_request,i_requirements,i_design,i_code,i_test_plan,i_results,i_operation,i_incident information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

開発要求は目的・課題・制約の出発点、要件定義書は合意した振る舞いと品質、設計書は実現方法と例外の仕様です。ソースコードは実装内容、テスト仕様書は前提・入力・期待結果、テスト結果は対象版と観測した結果を持ちます。運用手順書は監視・対応・復旧を説明し、障害・変更依頼は次の開発で扱う課題を記録します。これらの関係は開発の一方向の順番を意味せず、変更時には関連する成果物を照合します。

[システム開発の全体](README.md)
