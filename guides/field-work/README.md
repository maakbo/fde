# 相談から、試せる仕事の条件を作る

「要件から設計をまとめる仕事にAIを使いたい。今分かることは……」という相談から始めます。
最近の一件をたどり、目的・受取者・現状を揃え、任せる範囲と試す方法を決めます。最初から様式を埋める必要はありません。

> このrepoの作業ガイドで、今の相談に必要なSkillを選んで進めてください。
> 分かる範囲から下書きを返し、確かめる必要があることを私の言葉で伝えてください。
> 根拠・提案・実行・未測定を分け、前の作業の対象と版を引き継いでください。

## 作業を選ぶ

仕事と業務のまとまりから、今必要な作業だけを選びます。この一覧は分類であり、固定の順序ではありません。
個々のSkillは一つの作業の入力・方法・成果・検証を持ちます。選択したSkillと必要な参照だけを読み込みます。

### 現場の仕事を捉える

- [相談の仕事・業務・作業の粒度を揃え、今扱う業務と親子の境界を決める](../../.agents/skills/clarify-work-grain/SKILL.md)
- [最近の一件を担当者とたどり、現状の入力・判断・受渡し・例外を記録する](../../.agents/skills/walkthrough-current-case/SKILL.md)
- [担当者が無意識に使う判断条件を、実例の違いと反例から引き出す](../../.agents/skills/elicit-tacit-decisions/SKILL.md)
- [規定された手順と実際の一件の差を照合し、工夫・例外・統制上の未決を分ける](../../.agents/skills/reconcile-procedure-and-practice/SKILL.md)
- [一件の時間を担当別の人手・機械処理・待ちへ分け、効果比較に使える観測を作る](../../.agents/skills/measure-workload-and-wait/SKILL.md)
- [一連の業務から具体的作業の性質と検証方法を整理する](../../.agents/skills/classify-task-nature/SKILL.md)

### 仕事を組み替えて対話する

- [現行業務を目的から見直し、排除・統合・順序変更・簡素化の選択肢を比較する](../../.agents/skills/redesign-process-options/SKILL.md)
- [変更案を担当者が使う一件の流れへ具体化し、人とagentの役割・例外・成果を設計する](../../.agents/skills/design-future-work/SKILL.md)
- [現行と変更案の差から、必要な情報・役割・許可・実装・検証の変更を特定する](../../.agents/skills/analyze-change-gaps/SKILL.md)
- [理想の業務変更と現実の制約の間で、段階案・残る負担・リスクと期待を関係者へ返す](../../.agents/skills/agree-staged-change/SKILL.md)
- [選んだ業務の成果を子目標と作業へ分け、順序・条件・受渡しを具体化する](../../.agents/skills/decompose-work-goals/SKILL.md)
- [業務の関係と手順を図で返し、担当者の具体例で訂正して反映する](../../.agents/skills/facilitate-process-dialogue/SKILL.md)

### 任せる条件と構成を設計する

- [相手の仕事に沿ってAIへ任せる仕組みを説明する](../../.agents/skills/explain-agent-capability/SKILL.md)
- [作業の期待結果から必要情報と入力の構成を設計する](../../.agents/skills/design-task-input/SKILL.md)
- [人とagentの提案・確定・実行・確認の境界を操作単位で決める](../../.agents/skills/define-delegation-boundary/SKILL.md)
- [業務に合う起動条件を決める](../../.agents/skills/design-trigger-contract/SKILL.md)
- [agentの役割と受渡しを分け、単一手順か複数agentかを比較して実行構成を渡す](../../.agents/skills/partition-agent-roles/SKILL.md)
- [現場で必要な外部接続の情報・操作・権限・変更予定を整理し、方式比較と実装へ渡す](../../.agents/skills/prepare-connection-requirements/SKILL.md)

### 手段・費用・効果を比較する

- [作業ごとの方式・モデル候補を同じ条件で比較し、採用範囲と追加試行を決める](../../.agents/skills/compare-model-options/SKILL.md)
- [件数・処理経路・入出力トークンと単価から推論利用費を見積もる](../../.agents/skills/estimate-inference-cost/SKILL.md)
- [AI導入の初期・情報整備・評価・利用・監視保守・終了費を同じ期間で積み上げる](../../.agents/skills/estimate-total-cost/SKILL.md)
- [業務の変更から余力・品質・利用体験・実際の支出減へつながる条件を見積もる](../../.agents/skills/estimate-benefit-conditions/SKILL.md)
- [投資と次の試行の判断材料を作る](../../.agents/skills/prepare-investment-decision/SKILL.md)

### 確かめ、運用から直す

- [生成物の主張や操作を原資料・期待結果・許可へ照合し、修正と再確認へ返す](../../.agents/skills/verify-output-evidence/SKILL.md)
- [AI導入の対象業務から具体的失敗と影響を洗い出す](../../.agents/skills/identify-adoption-risks/SKILL.md)
- [特定した失敗に対し予防・検知・停止・業務継続・復旧を設計する](../../.agents/skills/design-risk-response/SKILL.md)
- [導入した仕組みの目的・管理者・版・利用・負担・失敗を棚卸し、継続/改善/停止の判断材料を返す](../../.agents/skills/review-operating-inventory/SKILL.md)
- [技術や業務条件の変化を、対象業務の未達・品質・負担・費用へ結び付けて再評価する](../../.agents/skills/reassess-technology-fit/SKILL.md)

### 実装へ渡す

- [設計から実装へ引き渡す](../../.agents/skills/prepare-implementation-handoff/SKILL.md)

### 知識を引き継ぐ

- [経験者の判断を条件・理由・例外がある知識にする](../../.agents/skills/write-conditional-knowledge/SKILL.md)
- [根拠の版・権限・適用範囲を照合する](../../.agents/skills/reconcile-knowledge-sources/SKILL.md)
- [別の担当者・別の一件で知識を使い、誤りを戻す](../../.agents/skills/exercise-knowledge-transfer/SKILL.md)

## 前後をつなぐ

現場の仕事が曖昧なら粒度確認と一件の追跡へ。変更案は現状とは別に作り、図を返して具体例で訂正します。
方式や投資の判断前には対象の失敗・影響と対応案も渡します。未確認は仮説/未決のまま残します。
対象・版・根拠・未決を次の作業へ引き継ぎ、同じ質問を最初から繰り返しません。

導入全体の進行は[一件を試して仕事へ戻す](../../.agents/skills/discovery-facilitation/references/field-delivery-loop.md)、
知識の維持は[Knowledge Stewardship](../../.agents/skills/knowledge-stewardship/SKILL.md)、
試行の評価は[AI Pilot Evaluation](../../.agents/skills/ai-pilot-evaluation/SKILL.md)と組み合わせます。
FDEは設計文書の作成に留まらず、動くagent・接続・コード・テスト・運用を実現する仕事を含みます。
この作業ガイドは、その全ての実装能力が完成したことを示すものではありません。

## まず一件を試す

[基本設計をまとめる例](../../examples/design-preparation/README.md)では、現状の追跡、変更案、図への訂正、試行で見つけた誤りと修正を確認できます。
[経験者の判断を次の設計へ渡す例](../../examples/design-preparation/knowledge-practice.md)では、条件付き知識・根拠照合・別役の適用まで試しています。
成果の型は[templates/field-work](../../templates/field-work/)。空欄を全て埋めることを完了条件にしません。

この作業群はfull cloneで取得できます。既存のconsumer profileは選択した範囲の配布で、この作業群全てを含むものではありません。
架空資料による作業単位の試行と独立レビューを実施しています。全作業を一つの実案件で通した効果は未測定です。
