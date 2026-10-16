# 作業環境とAIエージェント

家ではiPad＋iPadトレイ＋Elimkeys Elytraを中心に、平日の外出先ではiPhone、必要に応じてMacBookを使います。

ChatGPTでは、学びや思いつきをマティに渡し、理解を深めたり、実践を振り返ったり、やりたいことや次の一歩を一緒に考えたりします。Codexでは、相談しながら文章・図・スキルを作成し、検証してGitHubへ反映します。maakboに残した共通記憶を参照し、対話で決めたことを次の作業につなげます。

活動記録はmaakboリポジトリに、公開するノウハウやスキルはfdeリポジトリに残します。fdeをクローンまたはフォークした個別プロジェクトで、それぞれの作業を進めます。

```mermaid
---
title: 私の作業環境とAIエージェント
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
    fontFamily: "Noto Sans Mono CJK JP, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; } text, .nodeLabel, .image-shape p { font-family: 'Noto Sans Mono CJK JP', sans-serif !important; }"
---
flowchart LR
  %% View: personal workspace architecture. Relations describe use and shared work, not sequence.
  %% Device notation follows mermaid-diagram-authoring; AI/repository notation follows architecture-modeling.
  h_me@{ label: "maakbo", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  v_ipad@{ label: "iPad", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/tablet.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  v_phone@{ label: "iPhone", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/smartphone.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  v_mac@{ label: "MacBook", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/laptop.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  g_matti@{ label: "ChatGPT", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  g_codex@{ label: "Codex", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/bot.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  r_memory@{ label: "maakbo", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/folder-git-2.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  r_skills@{ label: "fde", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/folder-git-2.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  r_projects@{ label: "プロジェクト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/folder-git-2.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  h_me --- v_ipad
  h_me --- v_phone
  h_me --- v_mac
  v_ipad --- g_matti
  v_ipad --- g_codex
  v_phone --- g_matti
  v_phone --- g_codex
  v_mac --- g_matti
  v_mac --- g_codex
  g_matti --- r_memory
  g_codex --- r_memory
  g_codex --- r_skills
  g_codex --- r_projects
  r_skills --- r_projects

  class h_me human;
  class v_ipad,v_phone,v_mac device;
  class g_matti,g_codex agent;
  class r_memory,r_skills,r_projects repository;

  classDef human fill:none,stroke:none,color:#25231F;
  classDef device fill:none,stroke:none,color:#25231F;
  classDef agent fill:none,stroke:none,color:#25231F;
  classDef repository fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

[画像を開く](previews/architecture-overview.png)
