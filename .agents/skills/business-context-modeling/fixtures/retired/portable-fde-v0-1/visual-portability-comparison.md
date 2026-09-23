# Portable FDE v0.1 visual portability comparison

This is a synthetic icon-vocabulary review surface. It does not replace canonical templates or change the FDE business model. The question is whether each mark keeps its meaning when redrawn by hand: a person, an ellipse-shaped use case, a simple file, a generic external application, and ordinary contact devices should be recognizable without product-specific detail.

## 1. Current maakbo-owned baseline

```mermaid
---
config:
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_system@{ label: "外部システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
```

## 2. Portable core: application interpretation

The same four roles use fixed-tag upstream MDI assets. `application-outline` is the first External System candidate because an external business system need not be infrastructure.

```mermaid
---
config:
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_system@{ label: "外部システム", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/application-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
```

## 3. External System alternative: server interpretation

`server-outline` preserves continuity with the current server symbol, but can imply infrastructure. It is an alternative, not a mechanical replacement.

```mermaid
---
config:
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_system@{ label: "外部システム", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/server-outline.svg", pos: "b", w: 32, h: 32, constraint: "on" }
```

## 4. Portable contact surfaces

These are generic devices, not Apple-specific product marks. The nodes are intentionally unconnected: this is an icon comparison, not a relationship model.

```mermaid
---
config:
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  v_tablet@{ label: "タブレット", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/tablet.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  v_phone@{ label: "スマートフォン", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/cellphone.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  v_laptop@{ label: "ラップトップ", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/laptop.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

## 5. Remaining portable candidates

These five candidates complete the runtime vocabulary inventory. The nodes stay unconnected so
this remains an icon comparison, not a relationship model.

```mermaid
---
config:
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_ai_collaborator@{ label: "AI協働者", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/robot-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_external_service@{ label: "外部サービス", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/cloud-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  x_repository@{ label: "リポジトリ", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/source-repository.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_conversation@{ label: "対話", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/message-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_decision@{ label: "判断", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/rhombus-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

## 6. Frontmatter / label background probes

The six probes below use the same three MDI nodes. Only frontmatter changes, so the comparison
isolates the default label surface, the current path-only guard, the smallest label-background
guard, two minimal combined guards, and the existing canonical guard.

### 6.1 Current baseline: no frontmatter

```mermaid
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

### 6.2 Current MDI comparison: path-only guard

```mermaid
---
config:
  themeCSS: ".image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

### 6.3 Minimal label-background guard

```mermaid
---
config:
  themeCSS: ".image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; }"
---
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

### 6.4 Minimal combined guard

```mermaid
---
config:
  themeCSS: ".image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

### 6.5 Existing canonical guard

```mermaid
---
config:
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

### 6.6 Minimal surface + icon guard

```mermaid
---
config:
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_actor@{ label: "人", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_information@{ label: "情報", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
```

## 7. Visual-weight follow-up

This scoped probe keeps the 6.6 label/background treatment and reduces only the Business and
Information image boxes. Actor remains the reference at `38 × 38`; the two wider/taller MDI paths
use `30 × 30` so their visible bounds can be compared on the same surface without changing the
icon mapping or any canonical rule.

```mermaid
---
config:
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape g:first-child path { fill: none !important; stroke: none !important; }"
---
flowchart LR
  a_actor@{ label: "人 (Actor · 38×38)", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/account-outline.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  b_business@{ label: "業務 (Business · 30×30)", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/ellipse-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  i_information@{ label: "情報 (Information · 30×30)", img: "https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/file-outline.svg", pos: "b", w: 30, h: 30, constraint: "on" }
```

## Visual finding — GitHub light theme, 2026-09-07

All five remaining MDI candidates and all six probes render in the GitHub Mermaid viewscreen. The
gray strip under a label is not caused by the MDI SVG path: the path-only guard removes the image
backing but leaves the Mermaid label surface unchanged. In this probe, the label-background-only
and label-background-plus-path guards also leave that strip visible. The smallest variant that
clears both symptoms is 6.6: it resets `.image-shape p`, `.labelBkg`, and `.label rect`, then clears
the image backing path. `foreignObject` overflow and the flow-specific margin rule remain outside
this minimal probe; the existing canonical guard keeps them for broader context/flow surfaces.

The follow-up probe keeps 6.6's white label/background treatment and shows the intended visual-weight
shift on GitHub light theme: `30 × 30` makes the ellipse's visible width and the file's visible
height close to the Actor's restrained `38 × 38` reference, without making Actor larger. This is a
comparison result only; it does not adopt a canonical size or roll the adjustment across the icon
vocabulary.

## Portable mapping inventory

All candidate URLs use the upstream MaterialDesign-SVG `v7.4.47` tag at `https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/`. “GitHub result” is completed only after actual preview confirmation.

| Current role / asset | Portable MDI candidate | Hand-drawable recognition note | GitHub result | macOS / Windows |
| --- | --- | --- | --- | --- |
| Actor / `user.svg` | `account-outline.svg` | Head-and-shoulders keeps “person” immediate. | rendered | unverified |
| Business / `ellipse.svg` | `ellipse-outline.svg` | An ellipse remains a use-case-like mark when hand-drawn. | rendered | unverified |
| Information / `file.svg` | `file-outline.svg` | Outer paper and folded corner communicate file without text lines. | rendered | unverified |
| External System / `server.svg` | `application-outline.svg` (first candidate) | A generic application avoids calling every external system infrastructure. | rendered | unverified |
| External System / `server.svg` | `server-outline.svg` (alternative) | Keeps the current server continuity, but can read as infrastructure. | rendered | unverified |
| Tablet / `tablet.svg` | `tablet.svg` | Plain large rectangle is device-generic and drawable. | rendered | unverified |
| Smartphone / `smartphone.svg` | `cellphone.svg` | Plain narrow rectangle is device-generic and drawable. | rendered | unverified |
| Laptop / `laptop.svg` | `laptop.svg` | Screen and base remain legible with few strokes. | rendered | unverified |
| AI collaborator / `bot.svg` | `robot-outline.svg` | Robot outline stays distinct from a human actor. | rendered | unverified |
| External service / `cloud.svg` | `cloud-outline.svg` | Cloud keeps a broad external-service reading. | rendered | unverified |
| Repository / `folder-git-2.svg` | `source-repository.svg` | Repository meaning is explicit; this is less folder-like than the current mark. | rendered | unverified |
| Conversation / `message-square.svg` | `message-outline.svg` | Speech outline remains readable with few strokes. | rendered | unverified |
| Decision / `diamond.svg` | `rhombus-outline.svg` | Diamond remains a conventional decision mark. | rendered | unverified |

## Maakbo-owned dependency audit

Runtime visual-language references to `raw.githubusercontent.com/maakbo/fde/.../assets/icons/lucide-thin/` occur in the two canonical Mermaid authoring references, their context/flow checkers, reusable templates, and public examples. The `business-context-v0.1` consumer profile distributes `references/icon-context.md`, `references/business-flow.md`, `check_context_diagram.py`, `check_business_flow.py`, and five templates: these nine files are the consumer-side replacement points if a later review adopts a portable vocabulary. The profile does not distribute public examples, architecture template, fixtures, or local asset files.

The current baseline remains intentionally maakbo-owned so the comparison exposes the dependency. No canonical reference, template, checker, consumer profile, or other example is changed by this review.

## Review record

| Surface | Renderer/version | Core application candidate | External server alternative | Devices | Difference / decision |
| --- | --- | --- | --- | --- | --- |
| GitHub preview | GitHub Mermaid viewscreen, 2026-09-06 | rendered | rendered | rendered | All four original blocks rendered with fixed-tag raw-GitHub sources and cleared backing paths. |
| GitHub preview | GitHub Mermaid viewscreen, 2026-09-07 | rendered | — | — | Five remaining MDI candidates rendered; all 13 inventory candidates now have GitHub results. |
| GitHub preview | GitHub Mermaid viewscreen, 2026-09-07 | rendered | — | — | Six frontmatter / label-background probes rendered; 6.6 is the smallest observed guard without gray label strips or image backing. |
| GitHub preview | GitHub Mermaid viewscreen, 2026-09-07 | rendered | — | — | Visual-weight follow-up rendered; `30 × 30` Business / Information keeps the 6.6 label treatment and reads close to Actor's restrained `38 × 38` reference. |
| macOS VS Code | | | | | |
| Windows VS Code + GitHub Copilot | | | | | Unverified; do not infer from GitHub. |

Do not adopt a canonical icon mapping until this review record and the hand-drawable reading have been accepted by maakbo / matti.
