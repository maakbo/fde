# FDE Business Story — working hypothesis

## Modeling question

`FDE` は何のために存在し、何を提供し、どのようなBusinessによって実現するのか。

## Working natural-language story

主体者とその仲間には、それぞれの役割、経験、得意なことがある。仕事が成立している現場には、人だけでなく、目的・判断・行動・責務を持つAI Agentや、既存のSystemが関わることもある。

業務が複雑になり、役割、Information、Systemの関係が分断されると、全体を理解しにくくなる。その結果、特定の人への依存や、誰かに無理を強いる役割分担が生まれる。

`fde`と`fdeAI`は、主体者と仲間とともに、現場の業務、Information、Actor、Systemと、それらの関係を理解する。理解した意味をModelとして外に出し、現在の状態、ありたい状態、変えたいことを一緒に考えられるようにする。

見えることで、主体者と仲間は、自分たちで判断し、選べるようになる。その選択を基に、人、AI Agent、Systemが、それぞれの違いと強みを失わず、役割を持って協働できる業務の仕組みを設計する。

設計した仕組みは、実際に使える形にし、現場で使いながら確かめる。現場とのズレ、役割の無理、Informationの不足、Systemとの境界を見つけたら、実際の仕組みと、その意味を表すModelの両方へ戻して整える。

最終的には、`fde`がいなくても、主体者と仲間が仕組みとModelを理解し、自分たちで判断し、選び、変更し、育て続けられる状態へつなぐ。その結果として、人、AI Agent、Systemなどの異質な存在が同じ形に揃えられるのではなく、それぞれに役割と居場所があり、無理なく関係し、自律しながら協働することで、個も仲間も自然と自分たちらしく居られる状態を目指す。

## Meaning hierarchy

| Level | Working statement | Role in the story |
| --- | --- | --- |
| Ultimate Purpose | `個も仲間も、自然と自分たちらしく居られる` | FDEが最終的につくりたい状態。人だけを対象に限定せず、異質な存在が違いを失わずに関係できることを含む。 |
| Desired State | 主体者と仲間が、人・AI Agent・Systemを含む業務の仕組みを自然に理解し、自分たちで判断し、選び、変え、育て続けられる | Ultimate Purposeへ向かうために、FDEがつなぐ状態。`fde`への恒久的な依存を完成条件にしない。 |
| Enabling Outcome | `見えるから、自分で選べる` | 可視化・モデリングが生み出す重要なOutcome。Ultimate Purposeそのものではない。 |

意味の向きは、`Enabling Outcome` が `Desired State` を支え、`Desired State` が `Ultimate Purpose` へつながる、と読む。三つを一つのPurposeへ平坦化しない。

## What

> 人・AI Agent・Systemが協働する業務の仕組みをデザインし、形にする。

FDEの仕事は、仕組みを一方的に作って納品することではない。主体者、仲間、`fde`、`fdeAI`、実際に責務を持つAI Agent、Systemが、それぞれの役割を持って協働し、次を満たすところまでを含む。

- 現場で自然に成り立つ。
- 関係者が意味を理解できる。
- 特定の個人へ過度に依存しない。
- 主体者と仲間自身が運営し、変更できる。
- 利用しながら育て続けられる。

## 5W2H

| Lens | Story-consistent reading |
| --- | --- |
| Why | Ultimate Purposeは `個も仲間も、自然と自分たちらしく居られる`。そのためのDesired Stateとして、主体者と仲間が `自分たちで理解し、選び、変え、育てられる` 状態へつなぐ。その基盤をつくるEnabling Outcomeが `見えるから、自分で選べる` である。 |
| Who | 現在観測できる中心Actorは `主体者`、`主体者の仲間`、`fde`、`fdeAI`。今後、実務で目的・判断・行動・責務を持つAI Agentが観測された場合だけActorへ加える。選択したBusiness boundaryの外からInformationまたはvalueを提供・受領する技術SystemだけをExternal Systemとして扱う。 |
| What | 人・AI Agent・Systemが協働する業務の仕組みをデザインし、形にし、主体者たち自身が理解し、運営し、変更し、育てられる状態までつなぐ。 |
| When | 全体が見えない、分断や属人化がある、AIやSystemを取り入れたい、何を変えるべきか分からない、既存の仕組みが現場に合わなくなった、といった変化の必要が現れたとき。これは入口の例であり、すべてをBusiness Mapへ入れない。 |
| Where | 仕事が実際に成立している現場。物理空間に限らず、人の対話、業務、Information、System、AI Agent、組織境界が関係する環境を含む。 |
| How | 現場を理解し、意味をModelへ外在化し、ありたい状態と変化を考え、協働と仕組みを設計・具体化する。現場で使った結果からズレを検知し、Modelと仕組みへ戻して整え、理解と変更可能性を主体者側へ移す。ただしHowだけを単独で残さず、Why、Desired State、Business、Actor・Information・Systemの関係とのつながりをModelに残す。 |
| How much | 主体者が次の判断をできる最小単位から価値を返し、短いサイクルで育てる。最初から全体の完成を狙わず、`fde`がいなくても主体者たちが自然に扱えることも完成条件に含める。 |

## Candidate inventory

| Type | Current candidates | Treatment |
| --- | --- | --- |
| Actor | `主体者`、`主体者の仲間`、`fde`、`fdeAI` | 現在観測できる中心Actor。 |
| Business | `現場理解`、`業務構造化`、`変化設計`、`協働設計`、`仕組み化`、`現場適合`、`自律移行` | FDEを構成するworking set。工程順ではない。 |
| Information | 現場の事実、業務の意味、現状Model、ありたい状態、変化案、協働設計、実現構成、利用結果、ズレ | Business Storyから読める概念候補。個別Business ContextでInput / Outputを確かめるまでstable masterにはしない。 |
| External System | none observed at this boundary | System一般はWhatの対象に現れるが、FDE全体の選択boundary外からvalue / Informationを授受する具体Systemはまだ観測されていない。 |

`AI Agent`は種類を埋めるためにActorへ追加しない。現在の`fdeAI`はActorのworking hypothesisであり、実際の目的・判断・行動・責務の境界は今後の具体化で確かめる。

## Business naming review

| Source candidate | Natural business sentence | Input | Transformation | Output | Working business name | Verb check | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 現場理解 | 主体者と仲間とともに、断片的な事実や語りから、仕事が成立している現場像を捉える。 | 事実、語り、観察、既存Model | 断片を関係づけ、扱える現場像にする | 共有できる現場像 | `現場理解` | 現場を理解する | keep |
| 業務モデリング / 業務構造化 | 複雑なBusiness、Actor、Information、Systemの意味と関係を、考えられる業務Modelへする。 | 現場像、業務情報 | 意味と関係を区別し、構造として外在化する | 業務Model | `業務構造化` | 業務を構造化する | rename。モデリングは全Businessの基本動作であり、このBusinessだけの手法名にしない。 |
| 変化設計 | 現状とありたい状態の差から、守るものと変えるものを決め、変化案をつくる。 | 現状Model、ありたい状態、制約 | 差と影響を捉え、変化を選べる形にする | 変化案 | `変化設計` | 変化を設計する | keep |
| 協働設計 | 人・AI Agent・Systemの強み、責務、Informationの受け渡しを、無理なく協働できる関係へする。 | 変化案、Actor / Systemの特性と制約 | 役割、責務、境界、関係を組み合わせる | 協働設計 | `協働設計` | 協働を設計する | keep。変化設計とは、変える対象と協働責任の違いで分ける。 |
| 仕組み化 | 設計した協働を、現場で実際に利用できる業務の仕組みへ具体化する。 | 協働設計、実現上の制約 | 運用と技術を組み合わせ、利用可能な形にする | 利用できる仕組み | `仕組み化` | 仕組みにする | keep。特定の実装手法へ限定しない。 |
| 現場適合 | 利用結果からズレや無理を見つけ、Modelと仕組みを現場で自然に成り立つ状態へ整える。 | 仕組み、Model、利用結果 | 仮説と実際の差を戻し、両方を整える | 現場に適合した仕組みとModel | `現場適合` | 現場に適合させる | keep。`チューニング`のような手法名へ置き換えない。 |
| 自律化 | FDE側に偏っている理解と変更可能性を、主体者と仲間が自分たちで扱える状態へ移す。 | 仕組み、Model、運営・変更の知識 | 理解、判断、変更の可能性を主体者側へ移す | 自分たちで扱える状態 | `自律移行` | 自律できる状態へ移す | rename。相手を外から「自律化する」含意を弱め、移行責任を表す。 |
| 共育 | 主体者、仲間、AI Agent、Systemが、利用と変化を通じてModelと仕組みを育て続ける。 | 利用結果、変化、学び | 関係者が学びを戻し続ける | 育ち続けるModelと仕組み | `共に育てる` | 仕組みを共に育てる | peer Businessには置かない。現場適合と自律移行を含む全Businessのworking principleとして保持する。 |

## Modeling across every Business

モデリングは`業務構造化`だけの特殊な作業ではない。すべてのBusinessで、考えた意味を可能な限りModelとして外に出す。

| Business | Modelへ残す意味 |
| --- | --- |
| 現場理解 | 現在のActor、Information、System、Businessと、その関係 |
| 業務構造化 | 業務の意味、境界、関係 |
| 変化設計 | 現状、ありたい状態、課題、変化の関係 |
| 協働設計 | Actor、AI Agent、System、Information、責務の関係 |
| 仕組み化 | 実現構成、境界、Information exchange |
| 現場適合 | 仮説、利用結果、ズレ、修正の関係 |
| 自律移行 | 主体者が読み、変更し、育てられる意味と変更点 |

`あらゆる業務をモデルで扱うための実践知` は、このsampleで試すmodelingの方向性として保持する。fde repository全体の確定taglineにはしない。

## Unresolved

- `自律移行`が初見で責任範囲を十分に伝えるか。代案は、意味を狭めすぎない範囲で具体のBusiness Contextから検討する。
- `共に育てる`が将来、独立したInput / transformation / Outputを持つBusinessとして分かれるか。今回はcross-business principleとする。
- `fdeAI`および今後のAI Agentを、どの目的・判断・行動・責務が観測された時点で独立Actorとするか。
- Information masterとExternal System masterは、具体のBusiness Contextで実在する関係が観測されてから作る。
