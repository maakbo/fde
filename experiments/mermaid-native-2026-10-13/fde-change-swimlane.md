# 対象を見極め、業務を定義する — スイムレーン試作

[現行図](../../examples/maakbo-fde/change-design-flow.md) · [比較へ戻る](README.md)

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
  subgraph joint ["四者の共同作業（仮置き）"]
    b_overview["業務を見渡す"]
    b_simplify["不要を減らす"]
    b_bottleneck["ボトルネックを絞る"]
    b_choose_means["手段を見極める"]
    b_prioritize["対象を選ぶ"]
    b_scope["境界を定める"]
    b_requirements["要件を言葉にする"]
  end

  b_overview --> b_simplify
  b_simplify --> b_bottleneck
  b_bottleneck --> b_choose_means
  b_choose_means --> b_prioritize
  b_prioritize --> b_scope
  b_scope --> b_requirements
```

## 担当案と保持した意味

fde・fdeAI・主体者・主体者の仲間による共同レーンへ7工程を仮置きする。現行本文の共同作業に基づくが、工程ごとの責任者は未確定。複数アクターの参加を単一の責任者と同一視しない。共同レーンだけでは引き渡しを可視化できないことも比較結果とする。

| 工程 | 試作限定の担当案 |
| --- | --- |
| 業務を見渡す | 四者の共同作業（仮置き） |
| 不要を減らす | 四者の共同作業（仮置き） |
| ボトルネックを絞る | 四者の共同作業（仮置き） |
| 手段を見極める | 四者の共同作業（仮置き） |
| 対象を選ぶ | 四者の共同作業（仮置き） |
| 境界を定める | 四者の共同作業（仮置き） |
| 要件を言葉にする | 四者の共同作業（仮置き） |

元図の 7ノード・6本の矢印をID・ラベル・方向・条件ごと保持した。新しい工程や決裁条件は追加していない。矩形と菱形は新記法の標準図形。現行の固定アイコン・下ラベルとの違いも比較する。
