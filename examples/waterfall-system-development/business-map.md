# システム開発の業務マップ

ウォーターフォール型システム開発を、Layer 2 の13工程で俯瞰します。

この図は工程順序を厳密に表すフローではありません。各工程は、下位の Business Use Case / Context / Flow へ展開するための上位 Business として扱います。

```mermaid
---
title: システム開発の業務
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  b_system_development@{ label: "システム開発", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_estimation@{ label: "見積", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_requirements@{ label: "要件定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_basic_design@{ label: "基本設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_detailed_design@{ label: "詳細設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_implementation_unit@{ label: "実装・単体", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_internal_test_design@{ label: "内結設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_internal_test@{ label: "内結試験", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_external_test_design@{ label: "外結設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_external_test@{ label: "外結試験", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_system_test_design@{ label: "ST設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_system_test@{ label: "ST", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_uat@{ label: "UAT", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_deployment@{ label: "導入", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_system_development --- b_estimation
  b_system_development --- b_requirements
  b_system_development --- b_basic_design
  b_system_development --- b_detailed_design
  b_system_development --- b_implementation_unit
  b_system_development --- b_internal_test_design
  b_system_development --- b_internal_test
  b_system_development --- b_external_test_design
  b_system_development --- b_external_test
  b_system_development --- b_system_test_design
  b_system_development --- b_system_test
  b_system_development --- b_uat
  b_system_development --- b_deployment

  class b_system_development,b_estimation,b_requirements,b_basic_design,b_detailed_design,b_implementation_unit,b_internal_test_design,b_internal_test,b_external_test_design,b_external_test,b_system_test_design,b_system_test,b_uat,b_deployment business;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 読み方

13工程はシステム開発を分解する最初の共通言語です。実務では変更、差戻し、レビュー、再試験があるため、工程間の正確な順序はこの Map ではなく下位 Flow で扱います。

各工程の初期分解は [業務分解カタログ](decomposition-catalog.md) を参照します。

## この Map だけでは答えないこと

- 誰が各工程を担うか
- どの Information が入力 / 出力になるか
- どの External System を使うか
- レビュー、判断、差戻しの順序
- 横断管理業務が各工程へどう関係するか

これらは各 Business Context / Flow と master で表します。
