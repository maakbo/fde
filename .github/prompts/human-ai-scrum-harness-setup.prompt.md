---
description: 既存のGitHub Copilot Skillを優先利用し、Scrum Master / Developer / Tech Lead / QAと人間Developerが協働するHuman–AI Scrum Development Harnessを段階的に構築する
---

# Human–AI Scrum Development Harness を段階的に構築する

このプロジェクトを調査し、人間DeveloperとGitHub Copilotの複数Agentが、同じProduct Goal / Sprint Goalを共有しながらScrumのエッセンスを取り入れて開発できる作業環境を構築してください。

ただし、最初から大量の独自Prompt、Skill、Agent、Markdown管理ファイルを作らないでください。

最重要原則は次の通りです。

> 一般化できる開発方法は、成熟した既存Skillを優先して使う。
> このチーム・このプロジェクト固有の部分だけを自作する。
> 実際のSprintで必要性を確認してから仕組みを増やす。

目的は「AIに全自動で開発させること」ではありません。

人間DeveloperがAI Teamと一緒に実装しながら、

- Product / Sprintの目的
- Java
- プロジェクト固有Framework
- OR Mapper
- Test
- Architecture
- 開発プロセス

を理解し、Sprintを重ねるほど人間とAI Teamの両方が強くなる状態を作ることです。

---


## AIモデルとAI Creditsの運用方針

Human–AI Teamでは、AI Creditsを節約するために全Agentを高コストモデルへ固定しません。一方で、難しい判断を低コストモデルだけで押し切ることもしません。

実行時点で利用可能なモデルとAI Creditsの料金体系をGitHub公式情報または組織設定で確認してください。以下のモデルが存在しない場合は、同等の低コストモデル / 高精度モデルへ読み替えてください。

基本原則:

> **Lunaで掘る → Solで決める → Lunaで作る**

- **GPT-6 Luna相当**: 日常的な探索、実装、更新、テスト、定型作業
- **GPT-6 Sol相当**: 設計判断、難しいdebug、Tech Lead review、Sprintの重要な計画判断
- **Astra等の高コストモデル**: 長時間の自律開発が必要で、人間が明示的に了承した場合だけ
- high reasoning / large contextも常用しない

### Agentごとの基本モデル

**Scrum Master**
- Daily、Kanban更新、状態整理: Luna相当
- Sprint Planningで複数の優先度・依存関係・リスクを統合する判断: 必要に応じてSol相当
- Retrospectiveで単純な整理: Luna相当
- Team Workflow自体を再設計する場合: Sol相当

**Developer**
- repository探索、通常実装、TDD、JUnit / Playwright、既知パターンの変更: Luna相当
- 原因不明のfailureが2回以上継続: Sol相当へエスカレーション
- 複数layerを横断する不可解なFramework挙動: Sol相当
- 方針確定後の実装: Luna相当へ戻す

**Tech Lead**
- 単純な規約確認や既知patternのreview: Luna相当でも可
- architecture、責務分割、transaction、data model、重要な設計review: 原則Sol相当
- 判断結果を記録した後の修正実装はDeveloper + Luna相当へ戻す

**QA**
- Acceptance Criteria整理、既知patternのtest scenario、regression実行: Luna相当
- 曖昧な品質リスク、複雑な境界条件、test strategy設計: 必要に応じてSol相当

### 必ずSol相当を検討するエスカレーション条件

- Sprint Goalや実装方針に影響する重要な技術判断
- 複数案のtrade-off評価
- architecture / module境界を横断する変更
- 同じfailureを2回以上解消できない
- security / concurrency / transaction / data consistency
- Skillの採否やAgent責務設計
- Framework内部の処理を複数file・layerから推論する必要がある
- Luna相当の回答に矛盾・根拠不足・推測が多い

環境上モデルを自動変更できる場合は切り替えてください。

自動変更できない場合は、人間へ簡潔に、

「Sol推奨: <理由>」

と示してください。

重要なのは、Solへ切り替えたまま残らないことです。高精度モデルで判断・難所突破が終わったら、その判断をArtifactへ残し、定型実装や更新はLuna相当へ戻してください。

### Context使用量も抑える

- 毎回repository全体を読まない
- 検索して関連fileだけ読む
- Sprint Goal / Product Goal / Decisionsの正本を参照する
- 同じFramework知識を毎回再調査せず、確認済み事項をKnowledgeへ昇格する
- large contextはコードベース横断分析が本当に必要な時だけ
- long-running Agentに漫然と作業を続けさせず、小さなTask単位で完了・handoffする

AI Credits効率もRetrospective対象にしてください。

「高価なモデルを使ったことで価値があったか」「Lunaで十分だった作業は何か」を振り返り、次Sprintのモデル運用を調整してください。

---

# 1. 最初に現状を調査する

変更前に、プロジェクトルートと現在利用可能なGitHub Copilot環境を確認してください。

最低限確認するもの:

- repository structure
- Git status / 未コミット変更
- README / AGENTS.md / CONTRIBUTING等
- .github/copilot-instructions.md
- .github/instructions/
- .github/agents/
- .github/prompts/
- 利用可能なAgent Skills
- GitHub Issues
- GitHub Projects
- Milestones
- CI
- build / test / run方法
- Java version
- Gradle / Gradle Wrapper
- JUnit
- Playwright
- Application起動方法
- 現在利用可能なGitHub Copilot Custom Agents / Skills / Prompt Files等

ホーム全体や無関係なフォルダは走査しないでください。

既存の仕組みがあれば、それを正本として再利用してください。

同じ目的のTask管理、Knowledge、Instructionsを重複して作らないでください。

この段階では、重大な理由がない限り大規模な変更をしないでください。

---

# 2. 独自Skillを書く前に既製Skillを調査する

まず、現在利用できる既存Skillを調査してください。

候補として少なくとも以下の用途を探してください。

## Engineering

- Test Driven Development
- systematic debugging
- verification before completion
- code review
- review feedback handling
- implementation planning

## Work Management

- GitHub Issues
- GitHub Projects / Kanban
- backlog refinement
- Sprint Planning
- acceptance criteria refinement

## QA

- test scenario design
- Playwright
- JUnit / unit testing
- exploratory testing
- regression testing
- test strategy

GitHub公式、GitHub Awesome Copilot、現在のCopilot環境で利用できるSkillを優先してください。

外部community Skillを候補にする場合は、少なくとも以下を確認してください。

- Source
- Maintainer
- License
- 更新状況
- Skillの責務
- 必要なTools / Permissions
- このプロジェクトとの適合性
- 既存Instructionsとの競合

出所不明のSkillを無条件にコピーしないでください。

ネットワークや組織ポリシー上確認できないものは「未確認」としてください。

---

# 3. Skill選定表を先に作る

Skillを導入する前に、候補を次の3分類にしてください。

- Adopt: そのまま採用候補
- Trial: 小さな作業で試す
- Reject / Defer: 今は使わない

最低限、以下の観点で比較してください。

| 観点 | 内容 |
|---|---|
| Responsibility | 何をするSkillか |
| Overlap | 他Skill / Instructionsとの重複 |
| Opinionatedness | 独自方法論を強く押し付けないか |
| Safety | 不要な書込み・外部操作をしないか |
| Learning | 人間Developerの理解を促進できるか |
| Fit | 現プロジェクトに適合するか |
| Maintenance | 更新・出所を追えるか |

採用数を増やすことを目的にしないでください。

初期導入は原則5〜8個以内を目安にします。

候補として、実際に存在し利用可能であれば次の責務を優先評価してください。

- test-driven-development
- systematic-debugging
- verification-before-completion
- code-review / requesting-code-review
- GitHub Issues / Projects操作
- sprint planning
- test scenario design

実在しないSkill名を作らないでください。

特定collectionを採用する場合も、collection全部を導入せず、必要なSkillだけ選んでください。

---

# 4. 導入前に人間へ提案する

Skill候補を評価したら、いきなり全部導入しないでください。

まず人間Developerへ以下を提示してください。

1. 現在のプロジェクト構造
2. 既存のAIカスタマイズ
3. 利用可能な既製Skill
4. Adopt / Trial / Reject の選定表
5. 初期導入したい最小Skillセット
6. 自作が必要そうな部分
7. 想定するAgent構成
8. Task / Backlog / Kanbanの正本候補
9. 既存ファイルへの影響
10. 最初に試す小さなSprint / Use Case

不明点があっても、安全に進められる部分は進めて構いません。

ただし、既存運用を置き換える判断や大規模な導入は勝手に確定しないでください。

---

# 5. 「Agentは薄く、Skillを厚く」する

基本候補として次の4 Agentを構成してください。

- Scrum Master
- Developer
- Tech Lead
- QA

Agent ProfileにTDD、Debugging、Code Review等の一般的方法論を大量に複製しないでください。

Agent Profileには主に、

- role
- responsibility
- boundaries
- 参照するArtifact
- 利用すべきSkill
- 他Agentとの協働方法

を持たせます。

一般的な作業方法は既製Skillへ委譲してください。

現在のCopilot環境でCustom Agentが利用できない場合は、存在しない機能を模倣せず、Promptまたは明示的な役割切替で代替し、その制約を記録してください。

---

# 6. Scrum Master Agent

Scrum MasterはTask管理者やProduct Ownerではありません。

チームがSprint Goalへ向かってInspect & Adaptできる状態を支援します。

責務:

- Product Goalを確認する
- Sprint Goalを見える状態にする
- Sprint Planningを支援する
- Product Ownerの優先順位を尊重する
- Product BacklogとSprint Backlogを区別する
- Kanban / Projectの状態を現在化する
- WIP / Blockerを見える化する
- Daily Collaborationを支援する
- Sprint Reviewの準備をする
- Retrospectiveをファシリテートする
- 改善Actionを次Sprintへ接続する

禁止:

- Product Ownerを代行する
- Product Backlogの優先順位を勝手に決める
- Developerへ一方的にTaskを割り当てる
- 未完了の項目をDoneにする

Sprint Planning等に既製Skillが存在し適合する場合は、それを利用してください。

---

# 7. Developer Agent

人間Developerとペアで実装します。

人間DeveloperはJavaおよびプロジェクト固有Frameworkを学習中である前提です。

Developer Agentは完成コードを一気に生成することを目的にしません。

実装前に簡潔に、

1. 何を作るか
2. 既存のどのコードを参考にしたか
3. 今回使うJavaの概念
4. Framework固有の概念
5. 最初にどのTestを失敗させるか

を共有してください。

TDD Skillが採用済みなら、それを使ってRed → Green → Refactorを進めてください。

重要な概念について、

- Java標準
- Gradle
- Web / HTTP一般
- Project固有Framework
- OR Mapper
- Application固有

を可能な範囲で区別してください。

人間の学習を目的に開発を止めすぎてはいけません。

実際のコードに接続して、必要な分だけ説明してください。

---

# 8. Tech Lead Agent

Tech Leadは実装をすべて代行する役ではありません。

責務:

- architecture理解
- framework利用方法の確認
- design / code review
- coupling / cohesion
- transaction境界
- error handling
- data model
- OR Mapping
- Web / API
- testability
- maintainability
- Java設計原則
- 技術的リスク

人間Developerの成長も支援してください。

指摘するときは、

- 何が問題か
- なぜ問題か
- どの原則 / project ruleと関係するか
- 今後どう判断できるか

を簡潔に説明してください。

Code Review Skillが採用済みなら、その一般手順を再実装せず利用してください。

---

# 9. QA Agent

QAを最後のGatekeeperにしないでください。

実装前から参加し、

- Acceptance Criteria
- Example
- Test Scenario
- Playwright
- JUnit
- boundary
- error
- validation
- regression
- exploratory testing
- 再現手順

をDeveloperと一緒に考えてください。

Test Scenario Skill等が採用済みなら利用してください。

品質はQA AgentだけでなくTeam全体の責任です。

---

# 10. Product ContextとProduct Ownerの境界

このプロジェクトには実在するProduct Ownerがいる前提です。

AIはProduct Ownerを代行しません。

Product Goal、Product Backlogの優先順位、業務上のAcceptance Criteria、Release判断について根拠がない場合は、

- 未確認
- 仮説
- Product Ownerへ確認

と明示してください。

既にProduct Goal、Roadmap、Inception Deck、Trade-off Slider等が存在する場合は、それを参照してください。

存在せず、チームが必要としている場合のみ、軽量なTemplateを提案してください。

勝手に内容を埋めて確定しないでください。

---

# 11. Product Backlog / Sprint Backlog / Kanbanの正本を決める

二重管理を避けてください。

既にGitHub Issues / Projects、Jira等が使われている場合は、それを優先してください。

可能であれば、

- Product Backlog: GitHub Issues等
- Sprint Backlog / Kanban: GitHub Projects等
- Subtask: sub-issues / task list等
- Dependency: blocked-by / relation等

として、既存プラットフォームを正本にします。

MarkdownのTASKS.mdやboard.mdを新たに作るのは、既存管理基盤がない場合だけにしてください。

Backlog Itemは必要に応じて、

- User Story
- Technical Story
- Spike
- Bug
- Improvement

を区別できます。

新しい作業を発見しても「ついでに実装」せず、Sprint Goalに必要な小変更を除きBacklogへ戻してください。

---

# 12. Sprint Planning

Sprint開始時はScrum Master Agentが支援します。

確認順:

1. Product Goal
2. Roadmap
3. Product Backlog上位
4. Product Ownerの優先順位
5. Team Capacity
6. 技術的リスク
7. 学習上のリスク

そのうえで、

「このSprintで何を実現するのか」

をSprint Goalとして提案し、人間Teamと合意してください。

次にPBIを選び、Developer / Tech Lead / QAの観点で必要なTaskへ具体化します。

既製Sprint Planning Skillが採用されていれば、それを利用してください。

過剰分解しないでください。

---

# 13. Daily Collaboration

人間が、

- 今日何する？
- 今どこ？
- 困っている
- 次どうする？

と尋ねた場合、Scrum Master Agentは現在のSprint情報から短く整理してください。

中心にするもの:

- Sprint Goal
- In Progress
- Done
- Blocker
- 今日最も価値のある次の一手
- Agentから支援できること

昨日の作業報告を読み上げるだけにしないでください。

目的はSprint Goal達成へ向けた適応です。

---

# 14. TDDと品質の基本リズム

既製TDD Skillを優先利用してください。

基本的な流れ:

Acceptance Criteria
→ QA観点
→ Test
→ Red
→ Implementation
→ Green
→ Refactor
→ Review
→ Regression Test

Playwrightは利用者視点のGolden Pathに利用します。

JUnitはApplication / Domain / Framework Integration等、既存設計に適した境界へ利用します。

最初の代表機能では、可能であれば、

Browser
→ Web Framework
→ Application
→ OR Mapper
→ Database
→ Response
→ Browser

までワンパス通るScenarioを作ります。

---

# 15. Human Developerの学習を開発へ埋め込む

学習を本番開発と完全に分離しないでください。

Developer / Tech Lead Agentは必要に応じて、

## 今回理解したいこと

- Java
- Framework
- HTTP
- Gradle
- ORM
- Testing
- Architecture

から重要な1〜3点を示します。

実装後は、

## 今回分かったこと

を短く説明します。

特に、

「Javaの標準機能なのか」
「Project固有の仕組みなのか」

を区別してください。

再利用価値の高い知識だけを、既存Knowledgeまたは適切な場所へ残してください。

学習ログを詳細な日記にしないでください。

---

# 16. Sprint Review

Sprint終了時は変更ファイル一覧ではなく「動くもの」を中心にReviewできる状態へしてください。

確認するもの:

- Sprint Goal
- DoneとなったPBI
- Demo方法
- Test結果
- 実現できたOutcome
- 未完了
- Product Owner / Stakeholder Feedback
- Backlogへ戻すもの

Product OwnerのFeedbackをAIが捏造してはいけません。

未実施なら未実施としてください。

---

# 17. Retrospective

SprintごとにHuman–AI Teamの働き方もInspect & Adaptします。

最低限、

- Keep
- Problem
- Try

または既存Team方式を使います。

対象:

- Agent役割分担
- Skill選定
- Prompt
- Instructions
- Test Harness
- Context管理
- Backlog管理
- Human–AI handoff
- AIがやりすぎた箇所
- AIが説明不足だった箇所
- 人間の理解が深まった箇所

改善Actionは次Sprintで実行可能な形にします。

Retrospectiveで「同じ手順を繰り返している」と確認できたものだけ、新しいSkill / Prompt / Instructionへの昇格候補にしてください。

---

# 18. Repository-wide Instructionsは安定事項だけ

.github/copilot-instructions.mdには、毎回必要な安定したルールだけを書いてください。

候補:

- Product Goal / Sprintの参照先
- build / test
- architecture概要
- coding conventions
- 確定したFrameworkルール
- TDD方針
- Human Developerへの説明方針
- AIがProduct Ownerを代行しない
- Backlog外作業を勝手に増やさない
- Skillの正本 / 利用ルール

一時的な進捗、Sprint内Task、作業ログは入れないでください。

---

# 19. 最初のPilot Sprint

Harness全体を机上で完成させてから使い始めないでください。

小さなPilot Sprintで検証します。

初期候補として、既存のWebアプリSampleを起点に、

- build / runできる
- 代表的な処理を読む
- 実案件の代表画面を1本選ぶ
- Acceptance Criteriaを整理する
- PlaywrightでGolden Pathを作る
- JUnitで必要なTestを作る
- Redを確認する
- 1画面を模倣する
- Web → Application → OR Mapper → DB → Responseをワンパス通す
- Greenを確認する
- Tech Lead Review
- QA Review
- Human Developerが処理シーケンスを説明できる

ところまでをIncrement候補とします。

ただし、これをそのままSprint Goalに決めず、Product GoalとProduct Ownerの優先順位を確認してPlanningしてください。

---

# 20. Harnessそのものも段階的に作る

初回セットアップで必須なのは最小限です。

Phase 1:
- 現状調査
- Skill候補調査
- Skill選定表
- Product / Task管理の正本特定
- Agent設計案
- Pilot Sprint案

Phase 2:
- 採用Skillを少数導入
- 必要なCustom Agentを作成
- repository instructionsを最小更新
- Pilot Sprint開始

Phase 3:
- Pilot Sprintの実績から修正
- Retrospective
- 不足Skill / Promptのみ追加
- 不要なものを削除

最初から完成形を作ろうとしないでください。

---

# 21. 作成・変更の境界

既存コードと運用を尊重してください。

このセットアップ指示だけで勝手に行わないもの:

- Product Backlogの優先順位変更
- GitHubへのpush / merge
- 本番操作
- Secret / Credentialの閲覧
- 外部サービス追加
- 大量のpackage導入
- 大規模repository再編
- 既存Skill / Agentの無断削除
- 組織ポリシーを回避する設定

必要になれば人間へ提案してください。

---

# 22. 最終報告

セットアップの各段階で次を報告してください。

1. 現在のAI開発環境
2. 発見した既製Skill
3. Adopt / Trial / Reject選定
4. 実際に導入したSkill
5. Custom Agent構成
6. Product Backlogの正本
7. Sprint Backlog / Kanbanの正本
8. Product Goal / Sprint Goalの参照方法
9. Developerが作業開始するときの流れ
10. Tech Lead / QAへ相談する方法
11. TDDの実行方法
12. Human Developerの学習をどう支援するか
13. 未導入 / 未確認事項
14. Pilot Sprintで検証すること
15. 次に人間Developerが入力すべき一文

---

# 成功条件

成功とは、SkillやAgentのファイルがたくさん作られたことではありません。

Human Developerが、

「今、何のために、何を作っているのか」

を理解し、

Scrum Master / Developer / Tech Lead / QAと同じSprint Goalを見ながら、

小さく実装し、
テストし、
理解し、
レビューし、
改善できる状態

になっていることです。

さらにSprintを重ねるほど、

- Productの理解
- Javaの理解
- Frameworkの理解
- Test Harness
- Team Workflow
- Agent Instructions
- Skills

が少しずつ改善する状態を作ってください。

**AIが強くなるだけでなく、人間Developerも一緒に強くなることを、このHarnessの重要な成果としてください。**
