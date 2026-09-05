# Portable FDE v0.1 visual portability comparison

This is a synthetic review surface. It does not replace the canonical templates or change the FDE business model. Open the same Markdown in GitHub preview, macOS VS Code, and Windows VS Code + GitHub Copilot; record renderer/version and any label, endpoint, spacing or image difference.

## Current-style baseline

```mermaid
---
title: Portable Context baseline
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
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  a_provider@{ label: "提供者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_shape@{ label: "形にする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_result@{ label: "結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_recipient@{ label: "受け手", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_provider --- b_shape --- i_result --- a_recipient
```

## Candidate: MDI URL and system font

```mermaid
---
title: Portable Context candidate
config:
  theme: neutral
  flowchart:
    htmlLabels: false
  themeVariables:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Yu Gothic UI, Hiragino Sans, Meiryo, sans-serif"
---
flowchart LR
  a_provider@{ label: "提供者", img: "https://api.iconify.design/mdi/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_shape@{ label: "形にする", img: "https://api.iconify.design/mdi/circle-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_result@{ label: "結果", img: "https://api.iconify.design/mdi/file-document-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_recipient@{ label: "受け手", img: "https://api.iconify.design/mdi/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_provider --- b_shape --- i_result --- a_recipient
```

## Near-bare candidate

```mermaid
flowchart LR
  a_provider@{ label: "提供者", img: "https://api.iconify.design/mdi/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_shape@{ label: "形にする", img: "https://api.iconify.design/mdi/circle-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_result@{ label: "結果", img: "https://api.iconify.design/mdi/file-document-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_recipient@{ label: "受け手", img: "https://api.iconify.design/mdi/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_provider --- b_shape --- i_result --- a_recipient
```

## Review record

| Surface | Renderer/version | Baseline result | MDI/font candidate | Near-bare candidate | Difference / decision |
| --- | --- | --- | --- | --- | --- |
| GitHub preview | | | | | |
| macOS VS Code | | | | | |
| Windows VS Code + GitHub Copilot | | | | | |

Do not change a canonical icon, font or Mermaid configuration until this table has a concrete cross-environment observation.
