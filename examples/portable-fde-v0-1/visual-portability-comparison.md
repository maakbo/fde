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

## Portable mapping inventory

All candidate URLs use the upstream MaterialDesign-SVG `v7.4.47` tag at `https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/v7.4.47/svg/`. “GitHub result” is completed only after actual preview confirmation.

| Current role / asset | Portable MDI candidate | Hand-drawable recognition note | GitHub result | macOS / Windows |
| --- | --- | --- | --- | --- |
| Actor / `user.svg` | `account-outline.svg` | Head-and-shoulders keeps “person” immediate. | pending preview | unverified |
| Business / `ellipse.svg` | `ellipse-outline.svg` | An ellipse remains a use-case-like mark when hand-drawn. | pending preview | unverified |
| Information / `file.svg` | `file-outline.svg` | Outer paper and folded corner communicate file without text lines. | pending preview | unverified |
| External System / `server.svg` | `application-outline.svg` (first candidate) | A generic application avoids calling every external system infrastructure. | pending preview | unverified |
| External System / `server.svg` | `server-outline.svg` (alternative) | Keeps the current server continuity, but can read as infrastructure. | pending preview | unverified |
| Tablet / `tablet.svg` | `tablet.svg` | Plain large rectangle is device-generic and drawable. | pending preview | unverified |
| Smartphone / `smartphone.svg` | `cellphone.svg` | Plain narrow rectangle is device-generic and drawable. | pending preview | unverified |
| Laptop / `laptop.svg` | `laptop.svg` | Screen and base remain legible with few strokes. | pending preview | unverified |
| AI collaborator / `bot.svg` | `robot-outline.svg` | Robot outline stays distinct from a human actor. | URL checked; not in surface | unverified |
| External service / `cloud.svg` | `cloud-outline.svg` | Cloud keeps a broad external-service reading. | URL checked; not in surface | unverified |
| Repository / `folder-git-2.svg` | `source-repository.svg` | Repository meaning is explicit; this is less folder-like than the current mark. | URL checked; not in surface | unverified |
| Conversation / `message-square.svg` | `message-outline.svg` | Speech outline remains readable with few strokes. | URL checked; not in surface | unverified |
| Decision / `diamond.svg` | `rhombus-outline.svg` | Diamond remains a conventional decision mark. | URL checked; not in surface | unverified |

## Maakbo-owned dependency audit

Runtime visual-language references to `raw.githubusercontent.com/maakbo/fde/.../assets/icons/lucide-thin/` occur in the canonical Mermaid authoring reference, its context/flow checkers, reusable templates, and public examples. The `business-context-v0.1` consumer profile distributes the Mermaid authoring reference, `check_context_diagram.py`, `check_business_flow.py`, and five templates; those are the consumer-side replacement points if a later review adopts a portable vocabulary. The profile does not distribute public examples, architecture template, fixtures, or local asset files.

The current baseline remains intentionally maakbo-owned so the comparison exposes the dependency. No canonical reference, template, checker, consumer profile, or example is changed by this review.

## Review record

| Surface | Renderer/version | Core application candidate | External server alternative | Devices | Difference / decision |
| --- | --- | --- | --- | --- | --- |
| GitHub preview | pending | pending | pending | pending | Actual preview, not HTTP status, decides portability. |
| macOS VS Code | | | | | |
| Windows VS Code + GitHub Copilot | | | | | Unverified; do not infer from GitHub. |

Do not adopt a canonical icon mapping until this review record and the hand-drawable reading have been accepted by maakbo / matti.
