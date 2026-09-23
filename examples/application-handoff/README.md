# アプリケーション作業を引き継ぐ

架空のアプリケーション変更を本番へ反映する場面です。アーキチームが実行してきた手順をアプリ保守チームへ渡すとき、目的と判断の責任を共有したうえで、実行作業を教える例にしています。特定案件の事実や標準手順ではありません。

この仕事の目的は、変更を安全に利用可能にし、問題があれば判断して回復できる状態を保つことです。「導入」「運用」は探すための工程名で、以下の業務の親子関係や一方向の工程順を表しません。

```mermaid
---
title: アプリケーション作業を引き継ぐ場面
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
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  a_arch@{ label: "アーキチーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_maintenance@{ label: "アプリ保守チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_change_scope@{ label: "変更範囲", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_procedure@{ label: "実行手順", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  b_prepare@{ label: "実施条件を整える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_apply@{ label: "変更を反映する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_verify@{ label: "結果を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  x_delivery@{ label: "反映環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_result@{ label: "確認結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_decider@{ label: "実施判断者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  a_arch --- b_prepare
  a_maintenance --- b_prepare
  i_change_scope --- b_prepare
  i_procedure --- b_prepare
  b_prepare --- a_decider
  b_prepare --- b_apply
  a_maintenance --- b_apply
  b_apply --- x_delivery
  b_apply --- b_verify
  b_verify --- i_result
  b_verify --- a_decider

  class a_arch,a_maintenance,a_decider actor;
  class b_prepare,b_apply,b_verify business;
  class i_change_scope,i_procedure,i_result information;
  class x_delivery external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

変更範囲と実行手順を確認して実施条件を整え、変更を反映し、結果を確かめます。アーキチームは手順の背景と例外を説明し、アプリ保守チームが実行できるようにします。実施可否と結果の受け入れは実施判断者が担う、という**この例だけの仮定**です。

[具体的なレクチャー例を見る](teaching-sheet.md) / [システム開発業務へ戻る](../system-development/README.md)
