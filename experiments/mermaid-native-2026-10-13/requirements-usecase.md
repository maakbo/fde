# 要求を整える — ユースケース試作

[比較時の図](baselines/requirements-context.md) · [比較へ戻る](README.md)

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
actor a_business_user("業務担当者")
actor a_executive("経営者")
actor a_project_lead("プロジェクトリーダー")
b_interpret_request("依頼を読み解く")
b_shape_business_requirement("業務要件を整える")
b_agree_scope("対象を合意する")

a_business_user -- b_interpret_request
a_executive -- b_interpret_request
a_project_lead -- b_interpret_request
a_project_lead -- b_shape_business_requirement
a_executive -- b_agree_scope
```

## 元図との対応

元図のActor 3件、Business 3件と、その間の関係 5本を同じID・ラベルで保持した。業務の楕円をUMLユースケースとして確定したわけではなく、表現を比較する試作である。

情報・外部システムを業務やアクターへ読み替えず、下表の関係を図から外した。

| 図から外した関係の一方 | もう一方 |
| --- | --- |
| 得意先基幹システム | 依頼を読み解く |
| RFP | 依頼を読み解く |
| 依頼を読み解く | 業務要件 |
| 業務要件 | 業務要件を整える |
| 業務要件を整える | プロジェクト計画 |
| プロジェクト計画 | 対象を合意する |
| 対象を合意する | システム要件 |

外した情報・目的・外部システムは現行図が正本。省略により図がすっきりしても、同等のContextを表現できたとは判定しない。システム境界、include、extendは追加していない。
