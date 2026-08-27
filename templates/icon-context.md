# 業務コンテキスト図

Edit the Mermaid block directly and preview this Markdown file. Keep assumptions and open questions below the diagram when they matter.

```mermaid
---
title: 業務コンテキスト
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape path { stroke:#FFFFFF !important; stroke-width:10px !important; }"
---
flowchart LR
  a_requester@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "依頼者", pos: "b", w: 38, h: 38, constraint: "on" }
  i_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "依頼内容", pos: "b", w: 38, h: 38, constraint: "on" }
  b_receive@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "依頼受付", pos: "b", w: 30, h: 30, constraint: "on" }
  i_record@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "受付記録", pos: "b", w: 38, h: 38, constraint: "on" }
  x_service@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", label: "予約管理", pos: "b", w: 38, h: 38, constraint: "on" }
  i_booking@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "修理予約", pos: "b", w: 38, h: 38, constraint: "on" }
  a_recipient@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "修理担当", pos: "b", w: 38, h: 38, constraint: "on" }

  %% 通常の関係は---。-->は強い依存性を強調するときだけ使う。
  a_requester --- b_receive
  i_request --- b_receive
  b_receive --- i_record
  b_receive --- x_service
  x_service --- b_receive
  b_receive --- i_booking
  b_receive --- a_recipient

  class a_requester,a_recipient actor;
  class b_receive business;
  class i_request,i_record,i_booking information;
  class x_service external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 未解決の問い

次に、どの境界・粒度・分類・関係性を検討するか？
