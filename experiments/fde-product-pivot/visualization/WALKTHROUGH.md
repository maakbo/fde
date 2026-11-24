# 備品の引継ぎ：今の手順を続けるか決める

```mermaid
---
config:
  theme: neutral
  swimlane:
    ignoreCrossLaneEdges: false
    optimizeRanksByCrossings: false
  themeVariables:
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
---
swimlane-beta TB
  accTitle: 架空事例：備品の引継ぎの方針を決める
  accDescr: 受け渡し双方の記録を照合し、現行手順を暫定継続する。次の一件で受け手が同じ記録を見つけられなければ、方針選定を再開する。
  %% 親業務: work/decide/README.md の b_decide。次回の確認結果は未観測。
  subgraph people [仕事関係者]
    report["引継ぎ担当と受け手が見た記録・保管場所を持ち寄る"]
    verify["同じ記録を開き、受け手が内容を確認する"]
    choose["現行の手順を続け、次の一件で確かめると決める"]
    check{"次の一件で受け手が同じ記録を見つけられたか？"}
    revisit["見つからなかった状況を持ち寄り、方針を決め直す"]
  end
  subgraph ai [fde AI]
    compare["記録と参照先を照らし合わせ、違いを示す"]
  end
  subgraph engineer [fdeエンジニア]
    record["続ける理由と次に確かめる条件を残す"]
    close["次の確認結果を記録し、今回の確認を終える"]
  end
  report --> compare --> verify --> choose --> record --> check
  check -->|見つかった| close
  check -->|見つからない| revisit
```

**架空事例。** 引継ぎ担当は備品の引継ぎを終えたつもりでしたが、受け手にはその記録が見つかりませんでした。引継ぎ記録には更新時刻と次の担当者がありました。二人は別の保管場所を見ていて、同じ記録を開くと受け手も内容を確認できました。

この一件では、通知や承認の手順自体に問題があるとは判断できません。仕事関係者は今の手順を続け、次の一件で受け手が同じ記録を見つけられるか、確かめることにしました。fdeエンジニアは、続ける理由と見直す条件を「取り組みの判断」に残します。

次の一件の結果はまだありません。見つからなければ、どこを見たかを記録として持ち寄り、保管先の共有や通知方法を変える必要があるかを判断し直します。

[方針選定の手順に戻る](work/decide/README.md#flow)
