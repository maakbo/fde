# maakbo FDE — model note

## Modeling question

`FDE`は何のために存在し、何を提供し、どのBusinessと関係によって実現するのか。さらに、主体者と仲間が`fde`へ恒久的に依存せず、その仕組みを育て続けられる状態へどうつなぐのか。

## Boundary

この公開sampleは、FDEのUltimate Purpose、Desired State、Enabling Outcome、What、5W2H、FDEを構成するBusinessのworking setを扱う。具体の顧客・組織・Systemは扱わず、実際のBusiness Contextで観測されたときだけ追加する。

## View map

| View | Role / level | Focus | Parent / expanded node | Children | Status |
| --- | --- | --- | --- | --- | --- |
| [Purpose / Outcome](purpose-outcome.md) | purpose / outcome view | Ultimate Purpose、Desired State、Enabling Outcomeの意味階層 | — | [System Context](system-context.md)、[Actor Requirement](actor-requirement.md) | working hypothesis |
| [Business Story / 5W2H](business-story.md) | companion semantic model | Why、Who、What、When、Where、How、How muchとBusiness naming | — | [Business Map](business-map.md)、[Model Axis](model-axis.md) | working hypothesis |
| [Model Axis](model-axis.md) | semantic trace | WhyからHowまでを往復できる意味の軸 | — | — | working principle |
| [FDE Business Map](business-map.md) | capability overview | FDEを構成する七つのpeer Business | — | [Business Context — 業務構造化](business-context.md) | working hypothesis |
| [System Context](system-context.md) | overall context | FDEを担うActor、価値をともに育てるActor、Ultimate Purpose | — | — | working hypothesis |
| [Actor Requirement](actor-requirement.md) | focused requirement view | Desired Stateのうち主体者が必要とする状態と対策 | — | — | working hypothesis |
| [Business Context — 業務構造化](business-context.md) | use-case / value-flow context | 業務構造化のprovider、Information、recipient | business-map.md / b_business_structuring | — | working hypothesis |

Purpose / OutcomeとBusiness Storyは意味の上位Model、Business MapはFDEのcapability構成、Business Contextは`業務構造化`を一段具体化する子Viewである。Actor RequirementはDesired State全体を定義する図ではなく、主体者の要求を確認するfocused Viewとして置く。

## Model / View

- **Model**: Purpose、状態、Business、Actor、Information、System、Howと、その意味関係を更新可能な形で残したもの。図だけでなく、自然文、候補、判断、未解決を含む。
- **View**: 一つの問い、boundary、abstraction levelからModelの一部を選んで見せるもの。Purpose / Outcome、Business Map、System Context、Business Context、Business Flowは別の問いに答える。

一枚へすべてを詰め込まず、詳細Viewから意味の違いが見つかったら上位Modelへ戻し、上位Modelが曖昧ならfocused Viewへ降りて確かめる。

## Candidate inventory

| Type | Candidates | Current treatment |
| --- | --- | --- |
| Actor | `主体者`、`主体者の仲間`、`fde`、`fdeAI` | 現在観測できる中心Actor。具体のAI Agentは目的・判断・行動・責務が観測された場合だけ追加する。 |
| Business | `FDE`、`現場理解`、`業務構造化`、`変化設計`、`協働設計`、`仕組み化`、`現場適合`、`自律移行` | `FDE`は全体、残り七つはpeer working set。 |
| Information | 現場の事実、業務の意味、各種Model、変化案、協働設計、実現構成、利用結果、ズレ | 具体のBusiness Contextで意味と関係を確かめるまでmaster化しない。 |
| External System | none observed at this boundary | System一般をExternal Systemの種類埋めとして発明しない。 |

## Meaning decisions

- Ultimate Purposeは`個も仲間も、自然と自分たちらしく居られる`というworking hypothesisである。
- `見えるから、自分で選べる`は可視化・モデリングによるEnabling Outcomeへ位置づけ直した。
- `業務モデリング`はBusiness名としては`業務構造化`へrenameした。同じconceptなので既存Business Contextのstable ID `b_business_modeling`は維持する。
- モデリングは一つのBusinessではなく、全Businessで意味を外在化する基本動作とする。
- `自律化`は`自律移行`へrenameした。理解と変更可能性を主体者側へ移すtransformationを表す。
- `共育`は責任境界が`現場適合`と`自律移行`に重なるため、今回はpeer Businessへ置かず、`共に育てる`というcross-business working principleにする。
- Business MapとBusiness Flowを分ける。Business Mapの線は構成関係であり、工程順ではない。

## Model principle

Why / Purpose → Desired State / Outcome → Business / Activity → Actor・Information・Systemの関係 → How / Flow / Implementationを、つながったModelとして残す。

これはwaterfallではない。詳細なHowから上位の意味との矛盾が見つかれば上へ戻り、上位Modelを修正する。Modelは、固定された正解ではなく`変化しても戻ってこられる意味の軸`として扱う。

## Assumptions and omissions

- Purpose、Business名、Actor分類は、このsampleで検証するworking hypothesisであり、確定taglineや普遍定義ではない。
- `fdeAI`の独立した目的・判断・行動・責務はまだ分解していない。
- Actor / Information / External System masterは、再利用すべき具体関係が観測されるまで作らない。
- Business Flowは、個別Businessの順序・判断・reworkが問いになったときだけ作る。
- `あらゆる業務をモデルで扱うための実践知`は方向性として保持するが、fde repository全体のtaglineにはしない。

## Local layout observation

System Contextでは、purpose relationをActor relationより前に記述するとpurpose注釈が右上寄りになった。これは現行rendererのlocal observationであり、汎用規則ではない。dummy node、transparent relation、export後調整は使わない。

## Review points

1. Ultimate Purpose → Desired State → Enabling Outcomeの階層が、最終目的と可視化のOutcomeを混同せずに読めるか。
2. 七つのBusiness名、とくに`業務構造化`と`自律移行`が、transformationと責任範囲を自然に表しているか。
3. `共に育てる`を独立Businessではなく全Businessのworking principleへ置いた判断が、Business Storyに合うか。

## Next

上の三点をreviewし、意味が合えば、七つのうち一つを選んでInput / transformation / OutputとActor・Information・System relationsを具体化する。順序やreworkが問いになった場合だけBusiness Flowへ降りる。
