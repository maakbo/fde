# 業務の変化を描く — ユースケース試作

[現行図](../../examples/maakbo-fde/shape-change-context.md) · [比較へ戻る](README.md)

アクターがどの業務に関わるかを、線に沿って読む。順序・指揮命令・担当責任を示す線ではない。

```mermaid
---
config:
  theme: neutral
  look: classic
  layout: elk
  themeVariables:
    background: "#FFFFFF"
    fontFamily: "Hiragino Sans, sans-serif"
---
usecase-beta
direction LR
actor a_fde("fde")
actor a_fde_ai("fdeAI")
b_context_understanding("現場理解")
b_business_structuring("業務構造化")
b_change_design("変化設計")
actor a_subject("主体者")
actor a_companions("主体者の仲間")

a_fde -- b_context_understanding
a_fde -- b_business_structuring
a_fde -- b_change_design
a_fde_ai -- b_context_understanding
a_fde_ai -- b_business_structuring
a_fde_ai -- b_change_design
b_context_understanding -- a_subject
b_business_structuring -- a_subject
b_change_design -- a_subject
b_context_understanding -- a_companions
b_business_structuring -- a_companions
b_change_design -- a_companions
```

## 元図との対応

元図のActor 4件、Business 3件と、その間の関係 12本を同じID・ラベルで保持した。業務の楕円をUMLユースケースとして確定したわけではなく、表現を比較する試作である。

情報・外部システムを業務やアクターへ読み替えず、下表の関係を図から外した。

| 図から外した関係の一方 | もう一方 |
| --- | --- |
| 業務の現状 | 現場理解 |
| 業務の現状 | 業務構造化 |
| 業務課題 | 現場理解 |
| 業務課題 | 変化設計 |
| ありたい状態 | 変化設計 |
| 現場理解 | 業務モデル |
| 業務構造化 | 業務モデル |
| 業務モデル | 変化設計 |
| 変化設計 | 対象と優先順位 |
| 変化設計 | 要件の叩き台 |

外した情報・目的・外部システムは現行図が正本。省略により図がすっきりしても、同等のContextを表現できたとは判定しない。システム境界、include、extendは追加していない。
