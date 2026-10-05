---
description: フレームワーク提供のサンプルWebアプリを丁寧に読み解き、開発環境・Quick Start・実装Knowledgeを整えながら、代表機能を設計→開発→テストまでワンパス完走するSprint Zero / Feasibility Study
---

# Sprint Zero / Feasibility Study を開始する

このプロジェクトで、開発開始前のSprint Zero / Feasibility Studyを実施してください。

今回の目的は、単にサンプルアプリを起動することでも、ドキュメントを作ることでもありません。

**フレームワーク開発チームから提供されたサンプルWebアプリを起点に、構成を丁寧に読み解き、開発環境構築からQuick Start、設計、実装、テストまで代表機能を1本ワンパスで通し、このチームが継続的に開発できる見通しを得ること**が目的です。

同時に、Javaやプロジェクト固有Frameworkを学習中の若手DeveloperとAI Agentが、次の機能から迷わず開発に参加できるKnowledgeを、実際に確認できた事実から育ててください。

このSprint ZeroはScrum Guide上の正式イベント名ではなく、このチームにおける「開発可能性の検証・開発基盤の確認・最初の学習」をまとめて扱うための呼称です。

環境整備だけを長期間続けるためのSprintにしてはいけません。

**必ず動く代表機能まで到達すること**を重視してください。

---

# 1. 既存のWorkspace / Scrum Harnessを最初に読む

このrepositoryに既に以下が存在する場合は、先に読み、そのルールを利用してください。

- AGENTS.md
- .github/copilot-instructions.md
- .github/instructions/
- .github/agents/
- .github/skills/
- .github/prompts/
- Product Goal
- Roadmap
- Inception Deck
- Trade-off Slider
- Product Backlog
- Current Sprint
- GitHub Issues / Projects
- Architecture / Development documents

既存のHuman–AI Scrum Harnessがある場合は、

- Scrum Master
- Developer
- Tech Lead
- QA

の役割を利用してください。

既存のSkillがある場合、一般的方法論を独自に再実装せず、適切なSkillを利用してください。

候補:

- test-driven-development
- systematic-debugging
- verification-before-completion
- code review
- GitHub Issues / Projects
- Sprint Planning
- test scenario design
- Playwright

実在しないAgentやSkillを仮定しないでください。

---

# 2. AI Creditsとモデル選択

AI Creditsを抑えながら品質を保ってください。

基本:

> **Luna相当で調べる → Sol相当で難しい判断をする → Luna相当で実装・検証へ戻る**

低コストモデルで進めるもの:

- repository探索
- file検索
- 構成把握
- build / test
- 定型的なKnowledge作成
- 既知patternに沿った実装
- JUnit / Playwrightの単純な追加
- Backlog / Kanban更新

高精度モデルへエスカレーションするもの:

- Frameworkの処理構造が複数layerにまたがり理解できない
- architecture / responsibilityの重要判断
- 代表機能の実装方式に複数の有力案がある
- transaction / data consistency / security等の判断
- 同じfailureが2回以上続き原因が分からない
- Tech Leadとして重要なdesign reviewを行う
- Feasibility Studyの結論に影響する重要な不確実性を評価する

モデルを自動変更できない場合は、

「Sol相当推奨: 理由」

を人間へ明示してください。

難所を越えたら低コストモデルへ戻してください。

repository全体を毎回contextへ投入せず、検索して必要なfileだけ読んでください。

---

# 3. Sprint ZeroのGoalを確認する

既存Product GoalとProduct Ownerの優先順位を確認してください。

今回のSprint Zero Goal候補は次です。

> **提供されたサンプルWebアプリを理解し、チームメンバーが開発を開始できる環境とKnowledgeを整えたうえで、実案件の代表機能1本を設計・実装・テストまで通し、今後の開発が成立することと主要なリスクを確認する。**

Product Owner / Teamが既にSprint Goalを定めている場合はそちらを優先してください。

AIがProduct Ownerを代行してGoalや優先順位を勝手に確定しないでください。

---

# 4. 最初にサンプルプロジェクトを壊さず読む

本格的な変更前に、サンプルプロジェクトをread-firstで調査してください。

最低限以下を理解してください。

## Repository / Build

- directory構成
- Gradle project / module
- Gradle Wrapper
- Java version
- dependencies
- build command
- test command
- run command
- configuration
- environment variables
- local dependencies
- database
- external service dependencies
- logging

## Web Application

- application entry point
- Web Frameworkの入口
- routing
- request / response
- page / controller相当
- validation
- exception handling
- session / authenticationがあればその境界
- template / frontend構成

## Application / Domain

- application / service相当
- domain model
- DTO / form / command相当
- transaction境界
- dependencyの組立て
- lifecycle

## Persistence

- OR Mapper
- Entity
- Query
- ID
- relation
- insert / update / delete
- transaction
- schema
- migration
- initial data / fixtures

## Test

- JUnit
- integration test
- test data
- PlaywrightまたはE2E
- test environment
- CI

一般的なSpring / Hibernate等の知識を、根拠なくこのFrameworkへ当てはめないでください。

Framework固有記法は、

1. 利用箇所を探す
2. 類似実装を探す
3. 定義・設定を追う
4. Testを探す
5. Documentがあれば確認する

の順で理解してください。

分からないものは「未確認」としてください。

---

# 5. 変更前のBaselineを取る

可能な範囲で、変更前の正常状態を確認してください。

例:

- clean
- build
- unit test
- application起動
- sample画面
- DB接続
- existing E2E

必ず実際のcommandを確認してから実行してください。

既存failureがある場合は記録し、今回の変更で発生したfailureと区別してください。

「実行していない」と「成功した」を混同しないでください。

---

# 6. Development Quick Startを実証する

新しく参加する若手Developerが、できるだけ短い導線で次まで到達できるか確認してください。

Clone / Checkout
↓
Prerequisites
↓
Configuration
↓
Build
↓
Test
↓
Application Start
↓
Browser / Endpointで動作確認
↓
Debug
↓
Stop / Cleanup

既存Documentが正しい場合は再作成せず、必要な補足だけ行ってください。

不足している場合は、repositoryの既存構成に合う場所へQuick Startを作成してください。

Quick Startには推測を書かず、**実際に確認できたcommandと結果**を使ってください。

特定個人の絶対path、credential、secretを記載しないでください。

---

# 7. 若手Developer / AI Agent向けKnowledgeを育てる

Knowledgeは最初から教科書のように大量作成しないでください。

今回実際に通った開発経路から、次回の実装に再利用できる情報だけを残します。

既存のKnowledge場所があればそこを利用してください。

なければ例えば以下を検討できます。

- docs/development/quick-start.md
- docs/development/project-structure.md
- docs/development/implementation-guide.md
- docs/development/testing-guide.md
- docs/development/framework-notes.md

ただしファイル数を増やすことが目的ではありません。

小さくまとめられるなら統合してください。

特に以下を区別してください。

### Java標準

例:

- class / interface
- generics
- collection
- lambda / stream
- exception
- record等

### Gradle

- task
- dependency
- module
- build lifecycle

### Web / HTTP一般

- request
- response
- method
- status
- header
- body

### プロジェクト固有Framework

- 独自annotation
- DSL
- lifecycle
- routing
- application処理
- validation

### OR Mapper

- Entity
- mapping
- query
- transaction
- relation

### Application固有

- 業務ルール
- naming
- package
- screen / feature固有構造

AI Agentが次回再調査しなくてよい「確認済みの安定知識」を優先してください。

---

# 8. 代表機能を1本選ぶ

Sprint Zeroでは、実案件の代表的な機能を1本だけ選びます。

良い候補:

- 典型的な画面
- inputがある
- Frameworkの標準的な処理を通る
- Application logicを通る
- OR Mapper / DBを利用する
- response / screenまで戻る
- Playwrightで利用者視点から確認できる
- 数日でFeasibilityを判断できる大きさ

避けるもの:

- 最も複雑な機能
- 特殊case
- 大規模batch
- 外部system依存が極端に多いもの
- Framework標準pathを通らない例外的実装

どの機能を選ぶかがProductの優先順位に関係する場合はProduct Ownerへ確認してください。

---

# 9. 実装前に1機能の設計を理解する

いきなりcodingへ入らないでください。

代表機能について最低限、

- User / Actor
- Purpose
- Trigger
- Input
- Output
- Acceptance Criteria
- Business rule
- Data
- Error
- Main sequence

を整理してください。

既存設計書がある場合はそれを正とします。

必要なら簡潔な処理sequenceを作ってください。

概念上:

Browser
→ Web Framework
→ Page / Controller相当
→ Application / Service相当
→ OR Mapper
→ Database
→ Application
→ Web Framework
→ Browser

実際のFrameworkで名称や経路が異なる場合は、実コードを正としてください。

最終的にHuman Developerが、

「この画面操作からDBまで、どのclassをどう通るか」

を説明できることを目指してください。

---

# 10. TDDでワンパスを作る

採用済みのTDD Skillがあれば利用してください。

基本:

Acceptance Criteria
↓
QAによるTest Scenario
↓
Test
↓
Red確認
↓
Minimum Implementation
↓
Green
↓
Refactor
↓
Regression
↓
Review

## Playwright

利用者視点のGolden Pathを優先してください。

例:

画面を開く
→ 初期状態
→ 入力
→ 操作
→ server処理
→ DB処理
→ 結果表示

最初から全boundary caseを網羅しないでください。

まず代表正常系1本を成立させます。

## JUnit

既存architectureに合わせて必要な単位を選んでください。

候補:

- application logic
- validation
- domain rule
- OR Mapper integration
- Framework integration

Testのためだけに既存Framework思想を壊すarchitectureを追加しないでください。

---

# 11. 小さな変更単位で実装する

一度に代表機能全体を大量生成しないでください。

変更単位ごとにHuman Developerへ簡潔に、

1. 今何を通そうとしているか
2. 参考にしたsample code
3. 変更するfile
4. Java上のポイント
5. Framework固有のポイント
6. 通すTest

を説明してください。

人間DeveloperがJava初学習であることを前提にしますが、講義で開発を止めすぎないでください。

「一般的な説明」より、

> このrepositoryのこのcodeでは、Java / Frameworkのこの仕組みがこう使われている

という説明を優先してください。

---

# 12. Agent Teamを使う場合

Human–AI Scrum Harnessが利用可能なら役割分担してください。

## Scrum Master

- Sprint Goalを確認
- current stateを可視化
- Blockerを整理
- Backlog / Kanbanを現在化
- Sprint Zeroが環境整備だけに逸脱していないか確認

## Developer

- sampleを読む
- pair programming
- TDD
- implementation
- Human Developerへの説明

## Tech Lead

- Framework理解
- architecture
- transaction
- data model
- implementation pattern
- code review
- Feasibility上の技術リスク評価

重要な設計判断ではSol相当モデルを検討してください。

## QA

- Acceptance Criteria
- Test Scenario
- Playwright
- JUnit観点
- regression
- final verification

Agentを作ること自体が目的にならないようにしてください。

---

# 13. Feasibility Studyとして記録すること

単に「動いた」で終わらせず、今回の実証から次を整理してください。

## Confirmed

実際に確認できたこと。

例:

- setup可能
- build可能
- test可能
- debug可能
- Frameworkの主要path
- DB access
- E2E可能

## Unknown

まだ確認できていないこと。

## Risk

今後の開発で問題になりそうなもの。

例:

- documentation不足
- Framework学習cost
- local setup差
- testability
- transaction
- performance
- external dependency
- CI

## Constraint

Frameworkや環境上、従う必要がある制約。

## Recommendation

次Sprint以降にどう進めるべきか。

不確実性を隠して「Feasible」と断定しないでください。

---

# 14. Sprint ZeroのDefinition of Done

以下を基準候補にしてください。

- [ ] sample projectの主要構造を説明できる
- [ ] 新規Developer向けQuick Startが実証済み
- [ ] build / test / run commandが確認済み
- [ ] debug方法が確認済み
- [ ] Frameworkの典型的な処理sequenceを説明できる
- [ ] OR Mapperの代表的な利用方法を確認した
- [ ] 代表機能1本のAcceptance Criteriaがある
- [ ] PlaywrightのGolden Pathがある
- [ ] 必要なJUnit Testがある
- [ ] Red → Greenを確認した
- [ ] 代表機能がBrowserからDBを経由して最後まで動く
- [ ] Tech Lead観点のreviewを行った
- [ ] QA観点のverificationを行った
- [ ] regression testが通る
- [ ] Human Developerが主要処理を自分の言葉で説明できる
- [ ] 次回再利用できるKnowledgeが残っている
- [ ] Unknown / Risk / Constraintが可視化されている
- [ ] 次SprintへのBacklog候補が整理されている

実際のprojectに不要な項目はTeamで調整してください。

DoneでないものをDone扱いしないでください。

---

# 15. Backlog / Kanbanをリアルタイムに更新する

既存のGitHub Issues / Projects / Jira等がある場合はそこを正本としてください。

最低限、今回の作業を次のような単位で可視化してください。

- Sample理解
- Local setup
- Quick Start
- Architecture / sequence理解
- Representative feature design
- Playwright
- JUnit
- Implementation
- Review
- QA / verification
- Knowledge
- Feasibility report

過剰に細分化しないでください。

作業開始時にIn Progress、review待ちはReview、阻害されたらBlocked、Definition of Doneを満たしたらDoneとしてください。

新しい課題を発見しても、Sprint Goalに直接必要でないものを「ついでに」実装しないでください。

Backlogへ戻してください。

---

# 16. Daily Collaboration

毎日の開始時や人間が「今どこ？」と聞いた場合は、短く次を返してください。

- Sprint Zero Goal
- Done
- In Progress
- Blocker
- 今日通したい1本
- Human Developerが今日理解したいこと
- AI Teamが支援すること

「昨日何をしたか」の報告会ではなく、Goalへ向けてどう適応するかを中心にしてください。

---

# 17. 完走後にReviewする

Sprint Zero終盤では、file一覧ではなく実際に動くものを中心に確認してください。

Demo:

1. cleanな状態からsetup
2. build / test
3. application start
4. 代表機能の操作
5. Playwright
6. JUnit
7. main sequenceの説明

可能であればHuman Developer自身が処理sequenceを説明してください。

AIは補足役に回ってください。

---

# 18. Retrospective

Sprint Zero終了後に短く振り返ってください。

最低限:

## Keep

続けたいこと。

## Problem

詰まったこと。

## Try

次Sprintで試す改善。

振り返り対象:

- development setup
- Framework documentation
- Knowledge
- TDD
- Playwright
- JUnit
- Agentの役割分担
- Skill
- Model routing / AI Credits
- Human Developerへの説明量
- GitHub Issues / Projects
- handoff

繰り返す価値が確認できた手順だけSkill / Prompt / Instructionsへ昇格してください。

---

# 19. やらないこと

このSprint Zeroを理由に次を勝手に行わないでください。

- Framework自体の改修
- 大規模architecture刷新
- 全画面の実装
- 全機能のtest自動化
- dependency大規模更新
- 大規模refactor
- 全Knowledgeの書き起こし
- Product Ownerの優先順位代行
- 本番操作
- Secret取得
- 組織policy回避
- Git push / merge（明示的な許可がない限り）

Feasibilityを判断するために必要な最小の変更へ集中してください。

---

# 20. 最終報告

Sprint Zeroの終了時に、次を日本語で報告してください。

1. Sprint Zero Goal
2. Sample projectの構造理解
3. Development Quick Start
4. 確認したbuild / test / run / debug
5. 代表機能
6. 実装したmain sequence
7. Playwright結果
8. JUnit結果
9. Regression結果
10. Human Developerが今回理解したJavaの要点
11. Human Developerが今回理解したFrameworkの要点
12. 作成・更新したKnowledge
13. Confirmed
14. Unknown
15. Risk
16. Constraint
17. Recommendation
18. 次SprintのBacklog候補
19. AI Harness / Skill / Model運用で改善したいこと
20. 次に人間Developerが行う一手

成功・失敗・未実行・未確認を区別してください。

---

# 成功条件

成功とは、環境構築資料が完成したことではありません。

成功とは、

**新しいDeveloperが開発環境を立ち上げられ、サンプルからFrameworkの典型的な処理を理解し、Human DeveloperとAI Agentが同じKnowledgeを参照しながら、代表機能1本を設計 → Test → Implementation → Verificationまで最後まで通せたこと**

です。

さらに、

**「次の機能は今回より迷わず作れそうだ」**

という状態と、その判断の根拠がrepositoryに残っていることをSprint Zeroの成果としてください。
