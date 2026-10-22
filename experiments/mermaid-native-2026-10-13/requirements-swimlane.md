# 要件合意 — スイムレーン試作

[比較時の図](baselines/requirements-flow.md) · [比較へ戻る](README.md)

矢印で順序・分岐・戻りを読み、レーンで試作上の担当案を読む。

```mermaid
---
config:
  theme: neutral
  look: classic
  themeVariables:
    background: "#FFFFFF"
    fontFamily: "Hiragino Sans, sans-serif"
---
swimlane-beta TB
  subgraph project_lead ["プロジェクトリーダー（仮置き）"]
    b_prepare_review["論点整理"]
    b_resolve_gap["差異解消"]
    b_update_requirements["要件更新"]
    b_baseline_requirements["基準化"]
  end
  subgraph joint ["関係者の共同確認（仮置き）"]
    b_review_requirements["要件確認"]
    d_requirements_agreed{"合意できる？"}
  end

  b_prepare_review --> b_review_requirements
  b_review_requirements --> d_requirements_agreed
  d_requirements_agreed -->|合意| b_baseline_requirements
  d_requirements_agreed -->|差異| b_resolve_gap
  b_resolve_gap --> b_update_requirements
  b_update_requirements --> b_review_requirements
```

## 担当案と保持した意味

論点整理・差異解消・要件更新・基準化をプロジェクトリーダー、要件確認・合意判断を関係者の共同レーンへ仮置きする。これは見た目を試す担当案であり、元図から確定できる責任分担ではない。関係者の構成と決裁者は未確定。

| 工程 | 試作限定の担当案 |
| --- | --- |
| 論点整理 | プロジェクトリーダー（仮置き） |
| 差異解消 | プロジェクトリーダー（仮置き） |
| 要件更新 | プロジェクトリーダー（仮置き） |
| 基準化 | プロジェクトリーダー（仮置き） |
| 要件確認 | 関係者の共同確認（仮置き） |
| 合意できる？ | 関係者の共同確認（仮置き） |

元図の 6ノード・6本の矢印をID・ラベル・方向・条件ごと保持した。新しい工程や決裁条件は追加していない。矩形と菱形は新記法の標準図形。現行の固定アイコン・下ラベルとの違いも比較する。
