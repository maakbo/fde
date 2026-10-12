# FDEを誰と実現するか — Mermaid既定の外観

[現行図](../../examples/maakbo-fde/system-context.md) · [比較へ戻る](README.md)

アクターがどの業務に関わるかを、線に沿って読む。順序・指揮命令・担当責任を示す線ではない。

```mermaid
usecase-beta
direction LR
actor a_maakbo_fde("fde")
actor a_fde_ai("fdeAI")
b_fde("FDE")
actor a_subject("主体者")
actor a_companions("主体者の仲間")

a_maakbo_fde -- b_fde
a_fde_ai -- b_fde
b_fde -- a_subject
b_fde -- a_companions
```

## 元図との対応

元図のActor 4件、Business 1件と、その間の関係 4本を同じID・ラベルで保持した。業務の楕円をUMLユースケースとして確定したわけではなく、表現を比較する試作である。

目的「個も仲間も、自然と自分たちらしく居られる」は本文へ移した。目的への線も図から外れる。

| 図から外した関係の一方 | もう一方 |
| --- | --- |
| FDE | 個も仲間も、自然と自分たちらしく居られる |

外した情報・目的・外部システムは現行図が正本。省略により図がすっきりしても、同等のContextを表現できたとは判定しない。システム境界、include、extendは追加していない。
