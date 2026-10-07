---
description: GitHub Copilotをチーム共通のAI開発基盤として、成熟した既製Skillを選定・導入し、Senior Pair Developer / Planner / Reviewerから再利用できる形へ統合する
---

# GitHub Copilot Shared Skills Adoption

このプロジェクトへ、チーム全員がGitHub Copilotから利用できる共通Skillを導入してください。

重要な前提:

- **GitHub Copilotがチーム共通のAI開発基盤**
- Claude Codeを利用できるのは一部メンバーだけ
- Claude Codeがなくても、通常の開発・TDD・Debug・Verification・Reviewが成立すること
- Claude固有のPlugin / Skill / Hookを共有運用の前提にしない
- 一般的な開発手法は成熟した既製Skillを優先する
- Project / Framework固有Knowledgeだけをチーム自身で育てる
- Skillを増やすこと自体を目的にしない

Claude Codeをこのセットアップ作業に利用しても構いませんが、成果物の正本はGitHub Copilot側へ置いてください。

---

# 1. まず現在のCopilot環境を確認する

変更前に以下を調査してください。

- repository structure
- AGENTS.md
- .github/copilot-instructions.md
- .github/instructions/
- .github/agents/
- .github/prompts/
- .github/skills/ または現在のGitHub Copilotが認識するSkill配置
- 既存Skill
- Senior Pair Developer / Mentor
- Planner
- Tech Advisor
- Independent Reviewer / Challenger
- Luna-first Autonomous Development Harness
- build / test / run
- JUnit
- Playwright
- GitHub Copilotを利用するIDE / CLI
- Agent Skillsの現在の公式仕様
- Skillのinstall / repository共有方法
- 組織policy / permission

実行時点のGitHub公式Documentationと、実際に利用中のCopilot環境を正としてください。

未確認のdirectory、frontmatter、install command、tool名を捏造しないでください。

---

# 2. Shared-firstを最優先する

導入するSkillは、原則としてGit repositoryからGitHub Copilot利用者全員が再利用できる形にしてください。

個人home directory、個人IDE設定、Claude Code専用directoryだけに置かないでください。

目標:

> repositoryをcheckoutしたDeveloperがGitHub Copilotを使えば、同じSkillと同じ開発手順を利用できる

状態。

個人環境へ別途installが必要な場合は、

- 何がrepository共有されるか
- 何が個人setupか
- 何を各Developerが実施するか

をQuick Startへ明記してください。

---

# 3. 一般Skillは自作前に既製品を評価する

最初に、現在入手可能なSkillを調査してください。

少なくとも次の責務を評価します。

## Core Engineering

- Test Driven Development
- systematic debugging
- verification before completion
- code review
- review feedback handling

## Planning

- implementation planning
- vertical slicing
- task decomposition

## Defect Investigation

- bug reproduction
- minimal reproduction
- evidence collection

## Testing

- JUnit
- Playwright
- test scenario design
- regression

## Codebase Understanding

- codebase acquisition
- architecture discovery
- project structure discovery

GitHub公式またはGitHub Awesome Copilot等、GitHub Copilotでの利用を意識したsourceを優先してください。

外部community Skillを利用する場合は、少なくとも:

- repository / source
- maintainer
- license
- last update
- responsibility
- permissions / tools
- external communication
- overlap
- opinionatedness
- project fit

を確認してください。

---

# 4. 初期候補として評価するSkill

実際に存在し利用可能であれば、次を優先的に評価してください。

## Adopt候補

### test-driven-development

目的:

- Test first
- Red確認
- minimum implementation
- Green
- Refactor

Senior Pair Developerの通常実装で使用する。

### systematic-debugging

目的:

- 推測修正を減らす
- root cause
- hypothesis
- evidence
- controlled experiment

Frameworkの不可解な挙動、Test failure、integration問題で利用する。

### verification-before-completion

目的:

- EvidenceなしでDoneと言わない
- build / test / runtime resultを確認する

Senior Pair DeveloperがTask Doneを宣言する直前に利用する。

### bug-reproduction-brief

目的:

- Expected / Actual
- environment
- minimum reproduction
- evidence
- reproducibility

Framework自体の不具合が疑われる時、Providerへ問い合わせる前に使用する。

## Trial候補

### writing-plans

PlannerがGoalを小さく検証可能な縦切りTaskへ分解するときに評価する。

ただし、既存のLuna-first Planner設計と競合しないか確認する。

### requesting-code-review / code-review

Independent Reviewerへ、

- requirement
- diff
- evidence

を渡す手順として再利用価値を確認する。

既存のIndependent Reviewer / Challengerの責務を置き換えず、重複を避ける。

### acquire-codebase-knowledge

Framework ProviderのSample Projectを初めて読む時にTrialする。

ただし大量Document生成が現在のSimplification方針に反する場合は、解析methodだけ参考にし、出力構造は採用しない。

---

# 5. Skill Collectionを丸ごと入れない

Superpowers等のcollectionを利用する場合も、collection全体を標準workflowへ組み込まないでください。

初期導入は原則:

- TDD
- Debug
- Verification
- Bug Reproduction
- 必要ならPlanning

程度に絞ってください。

未使用Skillが大量に存在すると、

- Agentの選択迷い
- Context増加
- workflow複雑化
- maintenance増加

につながります。

**必要になった時に増やす**ことを優先してください。

---

# 6. Senior Pair DeveloperからSkillを使う

通常のHuman–AI開発の入口は、Senior Pair Developer / Mentorを維持してください。

Human DeveloperがSkill名を毎回覚えて直接選択しなくてもよい構成を目指します。

例:

Senior Pair Developer
→ Task開始
→ TDD Skill
→ failure
→ systematic-debugging
→ 実装
→ verification-before-completion
→ Done候補
→ Independent Reviewer

Framework bug疑い
→ bug-reproduction-brief
→ Evidence package
→ Provider確認候補

Human Developerが、

> 今どのSkillを使うべき？

を毎回判断する必要を減らしてください。

---

# 7. Plannerとの統合

Planner / 高精度modelは、縦切りTaskの設計に集中します。

writing-plans等の既製Skillを利用する場合は、

- layer別Taskではなくvertical sliceになるか
- Task単体でTest cycleを持てるか
- Doneが明確か
- PlannerのToken消費を増やしすぎないか

をPilotで確認してください。

良いTask:

> 最低限の検索条件からDB取得し、画面へ結果を返す。

悪いTask:

> Controller作成
> Service作成
> Entity作成

Skillの思想が既存Harnessより重い場合は、全面採用せず良い部分だけ利用してください。

---

# 8. Independent Reviewerとの統合

Independent Reviewer / Challengerは独立したまま維持してください。

既製Code Review Skillを導入しても、

> 作るAgentと疑うAgentを分ける

設計は崩さないでください。

Reviewerへ渡すもの:

- Goal
- Specification / Acceptance Criteria
- Framework Provider Sample
- diff
- implementation
- tests
- build / test result

原則として渡さないもの:

- 実装Agentの長いconversation
- 実装Agentの自己評価
- 不要なrepository全体

Review SkillはReviewerの一般手順を補助するものとして使い、仕様適合・Framework整合・Test反証というproject固有責務は既存Reviewer側に残してください。

---

# 9. Framework ProviderのSampleを最重要Referenceとして扱う

今回のprojectでは、Framework開発者のSample Projectが重要なReference Implementationです。

Skillが一般的なJava / Spring / Hibernate等のpatternを推奨しても、SampleとProject固有Frameworkの事実を優先してください。

Agentは、

- Java standard
- Gradle
- Web / HTTP
- Project Framework
- OR Mapper
- Application-specific

を区別してください。

Skillが一般論をProject固有仕様へ上書きしないようにしてください。

---

# 10. Project固有Skillは急いで作らない

Framework固有Knowledgeが増えても、すぐ独自Skill化しないでください。

まず:

実装
→ 再利用
→ 同じ手順を再度利用
→ 安定したことを確認
→ Skill化検討

としてください。

単なるKnowledgeなら、

- Quick Start
- Implementation Guide
- Framework Notes
- Testing Guide

等の既存Knowledgeへ残してください。

Skillは「繰り返し実行するprocedure」に限定してください。

---

# 11. Claude Code依存を作らない

Claude Codeは、

- Skill比較
- Setup支援
- Harness改善
- Experiment

に利用して構いません。

しかし共有成果物について、

- CLAUDE.mdだけに重要ruleがある
- .claude/skillsだけに必須Skillがある
- Claude Pluginを入れないと通常開発できない
- Claude固有Hookが品質Gateになっている

状態を作らないでください。

Claude Codeを利用しないDeveloperでも、

> GitHub Copilot + repository

だけで通常開発できることが必須です。

Claude側で有効だった方法を採用する場合は、GitHub Copilot側の正式な仕組みへ移植してください。

---

# 12. Skillの正本と由来を残す

外部Skillをrepositoryへ取り込む場合、由来が分からなくならないようにしてください。

少なくとも必要に応じて、

- source URL / repository
- upstream Skill名
- version / commit / retrieval date
- license
- local modifications

を確認できる形にしてください。

ただし全Skillへ長大な説明fileを追加しないでください。

upstream更新のたびに自動追従する仕組みも、必要性が確認されるまで作らないでください。

---

# 13. Security / Permission

外部Skillの内容を信頼しすぎないでください。

導入前に、

- shell
- network
- file write
- package install
- secret access
- external service
- Git operation

を確認してください。

Skillから、

- permission bypass
- unrestricted shell
- arbitrary external upload
- credential read
- production mutation

を要求する場合は、導入を保留してください。

組織policyを最優先してください。

---

# 14. 初期選定表をHumanへ出す

導入前に次を提示してください。

| Skill | Source | Responsibility | Agent | Decision | Reason |
|---|---|---|---|---|---|
| ... | ... | ... | Senior Pair Developer / Planner / Reviewer | Adopt / Trial / Reject | ... |

さらに、

## Initial Minimal Set

として初期導入Skillを5個前後以内で提案してください。

現時点の有力候補:

1. test-driven-development
2. systematic-debugging
3. verification-before-completion
4. bug-reproduction-brief
5. writing-plans（Trial）

Code Review SkillはIndependent Reviewerとの重複を確認してから判断してください。

---

# 15. Pilotで効果を検証する

Skillを導入したら、小さな実Taskで確認してください。

最低限:

## TDD

- Redを本当に確認したか
- Greenまで自律的に進められたか
- 過剰実装を減らせたか

## Debug

- 推測修正が減ったか
- root causeへ近づいたか
- 同じ試行loopを減らせたか

## Verification

- Done宣言前にEvidenceが得られたか
- false completionを防げたか

## Bug Reproduction

- Framework Providerへ渡せる再現情報になったか

## Planning

- 縦切りになったか
- HumanによるTask分解が減ったか

「Skillを呼べた」ではなく「開発体験または品質が改善した」で評価してください。

---

# 16. Skillを減らせる状態も成功

TrialしたSkillが、

- 役に立たない
- 重い
- 既存Agent指示で十分
- Contextを増やすだけ
- 開発速度を落とす

なら削除・Deferしてください。

導入したものを残すことに執着しないでください。

---

# 17. 最終的な共有Developer Experience

チームのDeveloperがrepositoryを開いた時、理想的には次だけ意識すればよい状態にしてください。

1. Senior Pair DeveloperへGoalを伝える
2. Agentが必要なSkillを選ぶ
3. Luna中心で自律実装する
4. 難所だけ高精度Agentへ委譲する
5. Independent ReviewerがDone候補を反証する
6. Humanは重要判断と理解に集中する

SkillやAgentの内部構成を、全Developerが暗記する必要はありません。

---

# 18. 最終報告

最後に日本語で以下を報告してください。

1. 現在のGitHub Copilot Skill対応状況
2. 調査した外部Skill
3. Adopt / Trial / Reject
4. 実際に導入したSkill
5. 各SkillのSource
6. Senior Pair Developerとの接続
7. Plannerとの接続
8. Independent Reviewerとの接続
9. Claude Codeに依存していないこと
10. 個人setupが必要な項目
11. Pilot結果
12. AI Credits / Contextへの影響
13. 不要と判断したSkill
14. 次に試す1つ
15. Team Memberが最初に行うこと

---

# 成功条件

成功とは、多数のSkillをinstallしたことではありません。

成功とは、

- GitHub Copilotがチーム共通のAI開発基盤になっている
- Claude Codeを持たないDeveloperも同じworkflowを利用できる
- Senior Pair Developerが適切なSkillを自律的に使える
- TDD / Debug / Verificationが一般Skillとして再利用される
- Framework固有Knowledgeはprojectの正本に残る
- Task分解・Debug・ReviewのHuman負荷が減る
- 品質が落ちない
- AI Creditsを無駄に増やさない
- 不要なSkillを増やさない

状態です。

基本思想は、

> **Shared tooling lives in GitHub Copilot. Claude Code may help build it, but the team must not depend on Claude Code.**

です。
