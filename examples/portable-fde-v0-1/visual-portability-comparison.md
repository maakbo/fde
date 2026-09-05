# Portable FDE v0.1 visual portability comparison

This is a synthetic visual-regression surface. It does not replace canonical templates or change the FDE business model. The four blocks intentionally change one portability concern at a time. Open the same Markdown in GitHub preview, macOS VS Code, and Windows VS Code + GitHub Copilot; record the renderer/version and any label, endpoint, spacing, image, or font difference.

## 1. GitHub baseline: existing image syntax

```mermaid
---
config:
  theme: neutral
  flowchart:
    htmlLabels: false
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_provider@{ label: "提供者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_shape@{ label: "形にする", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_result@{ label: "結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_recipient@{ label: "受け手", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_provider --- b_shape --- i_result --- a_recipient
```

## 2. Candidate: MDI source only

This changes only the image source from the baseline. The source is the upstream MaterialDesign-SVG GitHub repository at its `v7.4.47` tag, not a maakbo-owned URL.

```mermaid
---
config:
  theme: neutral
  flowchart:
    htmlLabels: false
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_provider@{ label: "提供者", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_shape@{ label: "形にする", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/circle-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_result@{ label: "結果", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-document-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_recipient@{ label: "受け手", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_provider --- b_shape --- i_result --- a_recipient
```

## 3. Candidate: system font only

This keeps the MDI source and changes only the font stack.

```mermaid
---
config:
  theme: neutral
  flowchart:
    htmlLabels: false
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Yu Gothic UI, Hiragino Sans, Meiryo, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_provider@{ label: "提供者", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_shape@{ label: "形にする", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/circle-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_result@{ label: "結果", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-document-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_recipient@{ label: "受け手", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_provider --- b_shape --- i_result --- a_recipient
```

## 4. Candidate: frontmatter removed

This keeps the MDI source and removes frontmatter/config. It is intentionally bare so that GitHub compatibility of image syntax and source is observable independently from configuration.

```mermaid
flowchart LR
  a_provider@{ label: "提供者", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_shape@{ label: "形にする", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/circle-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_result@{ label: "結果", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-document-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  a_recipient@{ label: "受け手", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_provider --- b_shape --- i_result --- a_recipient
```

## GitHub observation

On 2026-09-05, GitHub preview rendered the original raw-GitHub baseline but filled the image-node backing path with Mermaid's default `#eee`. Its long CSS overrode only the stroke, so the grey fill remained. Both original `api.iconify.design/mdi/*.svg` candidates failed with GitHub's `The source image cannot be decoded`, with and without frontmatter. A jsDelivr `@mdi/svg` URL produced the same error. The same image-node syntax therefore works; frontmatter is not the loading-error cause. HTTP 200 from a CDN is not a GitHub preview pass.

## Review record

| Surface | Renderer/version | Existing-source baseline | MDI source only | System font only | Frontmatter removed | Difference / decision |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub preview | GitHub Mermaid viewscreen, 2026-09-05 | Original rendered; backing fill was `#eee` | pending branch preview | pending branch preview | Original Iconify failure was independent of frontmatter | Do not call an external SVG portable until this surface renders it. |
| macOS VS Code | | | | | | |
| Windows VS Code + GitHub Copilot | | | | | | Unverified; do not infer from GitHub. |

Do not change a canonical icon, font, or Mermaid configuration until this table contains concrete cross-environment observations.
