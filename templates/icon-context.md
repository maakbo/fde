# Icon context diagram

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
    nodeSpacing: 48
    rankSpacing: 64
    padding: 8
  themeVariables:
    background: "#FAF8F2"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FAF8F2 !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FAF8F2 !important; } .image-shape .label rect { fill:#FAF8F2 !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { transform: translateY(-6px); }"
---
flowchart TB
  a_requester@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", label: "依頼者", pos: "b", w: 38, h: 38, constraint: "on" }
  b_receive@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", label: "依頼受付", pos: "b", w: 30, h: 30, constraint: "on" }
  i_request@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "依頼内容", pos: "b", w: 38, h: 38, constraint: "on" }
  i_record@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", label: "受付記録", pos: "b", w: 38, h: 38, constraint: "on" }
  x_service@{ img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", label: "外部サービス", pos: "b", w: 38, h: 38, constraint: "on" }

  a_requester --- b_receive
  i_request --- b_receive
  b_receive --- i_record
  x_service --- b_receive

  class a_requester actor;
  class b_receive business;
  class i_request,i_record information;
  class x_service external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 未解決の問い

次に、どの境界・粒度・分類・関係性を検討するか？
