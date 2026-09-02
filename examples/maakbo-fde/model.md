# maakbo FDE — model note

## Modeling question

`maakbo / fde` と `fdeAI` が担う `FDE` は、どのように主体者が理解し、考え、選び、改善できる状態を支えるか。

## Boundary

この公開sampleは、FDEというBusinessの最上位の関係と、主体者の要求を扱う。
具体的な業務、外部System、Information、提供側の内部構成は範囲外とする。

## Candidate inventory

| Type | Candidates | This sample |
| --- | --- | --- |
| Actor | `maakbo / fde`、`fdeAI`、`主体者` | 3 Actorを表示 |
| Business | `FDE`（working name） | System Contextの中心 |
| Information | none observed in this boundary | 表示しない |
| External System | none observed in this boundary | 表示しない |

## Views

| View | Question | Reading |
| --- | --- | --- |
| [System Context](system-context.md) | 誰がFDEを担い、誰へ価値を届けるか | 左の価値提供Actor、中央のFDE、右の主体者の関係。線はBusiness Flowではない。 |
| [Actor Requirement](actor-requirement.md) | 主体者が何をできる状態を必要とするか | 左のActor、中央の要求、右の対策を対応として読む。時間順序は表さない。 |

## Assumptions and omissions

- `FDE`、Actor名、対策は公開レビューのためのworking hypothesisである。
- `fdeAI` の内部構成や個別の役割分担は、このsampleの境界外である。
- 要求・対策は主体者の判断を支えるための仮説であり、実装仕様ではない。

## Next review question

この2枚で、FDEが目指す状態と主体者への価値が過不足なく読めるか。
