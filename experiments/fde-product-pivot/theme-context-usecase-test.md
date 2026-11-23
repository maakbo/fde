# テーマコンテキスト図：ユースケース図の楕円テスト

横長ボタン形ではなく、Mermaidのユースケース図の楕円を試す。既存アイコンを使ったA〜Cとは別の描画方式。

```mermaid
---
config:
  layout: dagre
  theme: neutral
  usecase:
    usecaseFontWeight: bold
---
usecase-beta
direction LR
actor planner("企画担当")
actor assistant("AI（開発支援）")
b_fde_product("fdeを育てる"):::themeNode
actor first_user("初期利用者")
actor members("仕事の関係者")
note for b_fde_product "`**仕事が、もっと心地よく進む。**\n立場が違えば、見え方も違う。`"
planner -- b_fde_product
assistant -- b_fde_product
b_fde_product -- first_user
b_fde_product -- members
classDef themeNode fill:#F8F7F3,stroke:#4A4640,stroke-width:1.25px,font-weight:700,font-size:20px
```

[比較に戻る](theme-context-design-options.md) · [Mermaid公式：ユースケース図](https://mermaid.js.org/syntax/usecase.html)
