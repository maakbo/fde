---
description: Claude Codeを使って、GitHub Copilot上にLuna中心の自律実装と高精度モデルによる計画・難所判断・独立レビューを組み合わせた低コスト開発ハーネスを構築する
---

# Luna-first Autonomous Development Harness を構築する

このプロジェクトに、GitHub Copilotを使った **低コスト・高自律・高品質** な開発ハーネスを構築してください。

あなた自身はClaude Codeとして、このセットアップ作業を行います。

目的は、Human Developerが毎回細かくTask分解・進捗監視・レビューをしなくても、

- 低コストモデルが大半の開発を自律的に進める
- 重要な計画・難所判断・反証だけ高精度モデルを使う
- Human DeveloperはGoalと重要判断に集中する
- 同時にHuman Developerが自律したEngineerとして育つ

状態を作ることです。

---

# 1. 基本アーキテクチャ

目指す構成は次です。

Human Developer
↓
Goal / Scope / Important Decisions
↓
Senior Pair Developer / Mentor
- 低コストモデル（GPT-6 Luna相当）
- Autopilot / Agent mode
- 通常の探索・実装・TDD・修正・Knowledge化を担当
↓
必要な時だけ高精度Sub-agent / Custom Agentへ委譲

高精度側は主に次を担当します。

1. Planner
   - Goalを縦切りTaskへ分解
   - 依存関係
   - Done条件
   - Test観点
   - リスク
   - 実装順序

2. Tech Advisor
   - Framework固有の難所
   - architecture
   - transaction
   - ORM
   - lifecycle
   - 原因不明のfailure
   - 重要な技術判断

3. Independent Reviewer / Challenger
   - 仕様消し込み
   - Framework提供者のSampleとの整合
   - Testへの反証
   - 設計・変更範囲
   - Critical / High Finding
   - 再Review

通常はSenior Pair Developerが中心です。

専門Agentを常時切り替える運用にはしないでください。

---

# 2. 最初に現在の環境を調査する

変更前に以下を確認してください。

- repository structure
- AGENTS.md
- CLAUDE.md / .claude/
- .github/copilot-instructions.md
- .github/instructions/
- .github/agents/
- .github/prompts/
- .github/skills/
- docs/ai/
- docs/development/
- GitHub Issues / Projects
- build / test / run
- 現在利用可能なGitHub CopilotのCustom Agent / Sub-agent / model指定 / Autopilot / Agent mode
- 現在利用可能なmodel名
- model routing / modelPolicy / reasoning effort等の実仕様
- IDE / CLIによる機能差

GitHub Copilotの仕様は変化するため、実行時点の公式GitHub Documentationとインストール済み環境を正としてください。

未確認のfrontmatter、model名、tool名、設定キーを捏造しないでください。

---

# 3. 既存Harnessを尊重する

既に存在する以下の考え方・Prompt・Knowledgeを確認し、重複させないでください。

- Workspace Setup
- Framework Adoption Knowledge Context
- Feasibility / Golden Path Development
- Senior Engineer Mentor
- Independent Reviewer / Challenger
- Simplification Prompt
- TDD / Debug / Verification等のSkills

既存のものが十分なら再作成せず、必要な差分だけ追加してください。

特にHuman–AI Scrum Harness等が現在の目的に対して過剰である場合、新しい仕組みをその上に積み重ねず、今回の構成へ統合・簡素化する案を提示してください。

---

# 4. Senior Pair Developer / Mentorを中心にする

Senior Pair Developerは、単なるCoding Agentではありません。

Human Developerと一緒に仕事を進めながら、経験あるEngineerが自然に行っている仕事の進め方を見せます。

責務:

- Goalを確認する
- 仕様とSampleを読む
- PlannerへTask分解を依頼する
- Planを保持する
- 次のTaskを自律的に選ぶ
- TDDで実装する
- build / test / regression
- Blockerを検出する
- 重要でない脱線を後回しにする
- 必要なKnowledgeを残す
- Human Developerへ節目で短く状況を伝える
- 完了候補になったらIndependent Reviewerへ委譲する
- Findingを修正する
- Done Evidenceを整理する

Human Developerへ毎回確認を求めないでください。

---

# 5. Plannerは高精度モデルでTaskを縦切りする

実装開始前に、原則として1回Plannerを呼び出します。

Plannerは高精度モデル（GPT-6 Sol相当）を優先してください。

ただし、実行時点でmodel指定が利用できるかを公式仕様で確認してください。

PlannerはGoalを、Browser / Application / Persistence / Testをまたぐ **小さな縦切りTask** へ分解します。

悪い例:

- Formを作る
- Serviceを作る
- Entityを作る
- Testを書く

良い例:

- 最低限の入力からDB検索して画面へ結果を返す
- 必須Validationを追加して異常系まで通す
- 0件ケースを仕様通りにする
- 残りの仕様項目を消し込む

各Taskには最低限、

- Purpose
- Scope
- Acceptance / Done
- Reference Sample
- Test
- Dependency
- Risk

を持たせてください。

Task数は必要最小限にし、過剰分解しないでください。

---

# 6. Plannerはコードを書かない

Plannerの役割は計画だけです。

原則として、

- source code editing
- implementation
- test implementation
- broad shell execution

を行わせないでください。

高コストモデルの利用時間・TokenをPlan判断へ集中させてください。

Plannerが返した判断はSenior Pair Developerが保持し、その後の定型実装は低コストモデルへ戻してください。

---

# 7. Senior Pair DeveloperはBounded Autopilotで自律実行する

Human Developerが毎Taskへ介入しなくて済むようにしてください。

Senior Pair Developerは、Plannerが作ったTaskを順番に自律実行します。

基本ループ:

Task選択
→ Reference確認
→ Acceptance Criteria確認
→ Test
→ Red
→ Minimum Implementation
→ Green
→ Refactor
→ Regression
→ Task Done確認
→ 次Task

Human Developerへの途中確認は、停止条件に該当する場合だけを原則とします。

---

# 8. Autopilotの停止条件

次の場合は、Luna相当モデルのまま試行を続けないでください。

- 同じfailureが2回以上続き、新しいEvidenceが増えていない
- Framework提供者のSampleと異なる実装が必要になった
- 仕様の解釈が複数成立する
- architecture上の重要判断が必要
- transaction / ORM / lifecycle / concurrency / security
- 想定より広範囲な変更が必要
- Testを通すためだけの不自然な実装が必要
- Framework自体の不具合が疑われる
- PlannerのTask分割では成立しないことが分かった
- 重大な仕様不足が見つかった

停止時に必ずHumanへ即質問するのではなく、まずTech Advisorへ委譲可能か判断してください。

---

# 9. Tech Advisorへ高精度モデルで委譲する

停止条件に該当し、技術的判断で解決できそうな場合だけTech Advisorを呼びます。

Tech Advisorへ渡すContextは必要最小限にしてください。

推奨Escalation Packet:

- Goal
- Expected
- Actual
- Relevant Code
- Sample Difference
- Test Evidence
- Error
- Tried
- Hypotheses
- One Question

Tech Advisorは、

- 原因候補
- 最も価値のある次の検証
- 推奨方針
- 追加で必要なEvidence

を返してください。

原則として大量のコード実装は行わせません。

判断後はSenior Pair Developerへ戻し、低コストモデルで実装を継続してください。

---

# 10. Humanへ確認する条件

Human Developerへ確認するのは、主に次の場合です。

- Product / business specificationの判断が必要
- Product Owner判断が必要
- Sampleから外れる方針を採用する必要
- 大規模な設計変更
- 重要なRiskを受容する判断
- Framework Providerへ問い合わせが必要
- 予定外の大きなScope追加
- 高コストモデル利用を大幅に増やす必要

単純な実装方法、Test追加、定型修正のたびにHumanへ確認しないでください。

---

# 11. Independent Reviewer / Challengerは実装担当から独立させる

全Taskまたは代表機能がDone候補になったら、Independent Reviewer / Challengerを呼びます。

可能であれば高精度モデルを使用してください。

Reviewerには実装Agentの長い会話履歴を与えず、Evidence中心のContextを渡してください。

最低限:

- 仕様書 / Acceptance Criteria
- Framework Provider Sample
- diff
- implementation
- JUnit
- Playwright
- build / test結果
- relevant Knowledge

Reviewerは最初は原則read-onlyとしてください。

Review観点:

1. Specification Conformance
2. Framework Conformance
3. Test Confidence
4. Design / Change Scope
5. Counterexamples

Findingは、

- Critical
- High
- Medium
- Low

で分類してください。

---

# 12. Review後はLunaへ戻す

Reviewer自身にそのまま大量修正させないでください。

FindingをSenior Pair Developerへ返します。

Senior Pair Developerは低コストモデルで、

- Finding理解
- 修正
- Test
- Regression

を行います。

Critical / High Findingがあった場合は、必要に応じてReviewerをもう一度呼びます。

Reviewを無限に繰り返さないでください。

---

# 13. 高コストモデルの利用回数を制御する

AI Credits上限が厳しいことを前提にしてください。

通常フローでは原則:

- Planner: 1回
- Tech Advisor: 必要時のみ
- Reviewer: 1回
- Re-review: Critical / Highがあった場合のみ

としてください。

高コストモデルを通常実装Agentとして使わないでください。

高精度モデルを使ったら、その判断を短くArtifactへ残し、同じ理由で再度高コスト推論しなくて済むようにしてください。

---

# 14. 低コストモデルを主戦力にする

大半の作業はLuna相当モデルで行ってください。

例:

- repository探索
- Sample読解
- 定型的なTask実装
- Red → Green → Refactor
- JUnit
- Playwright
- regression
- Knowledge更新
- Finding修正
- build / validation
- Traceability更新

低コストモデルで品質を出せるよう、

- Goalを明確にする
- Taskを縦切りにする
- Reference Sampleを明示する
- Done/Testを明示する
- Contextを必要最小限にする

ことを重視してください。

---

# 15. モデル設定は実仕様に合わせて行う

GitHub Copilot Custom Agent / Sub-agentにmodel指定が可能なら、実行時点の公式仕様に従って設定してください。

意図は次です。

Senior Pair Developer:
- GPT-6 Luna相当
- Autopilot / Agent mode
- 通常reasoning

Planner:
- GPT-6 Sol相当
- Plan / reasoning中心
- 実装Toolは最小限

Tech Advisor:
- GPT-6 Sol相当
- 重要な技術判断のみ

Independent Reviewer:
- GPT-6 Sol相当
- 原則read-only

ただし、

- model名
- modelPolicy
- reasoningEffort
- sub-agent delegation
- CLI / IDE挙動

は必ず現在の公式仕様で検証してください。

利用環境で異モデルSub-agentが保証されない場合は、勝手に「対応済み」とせず、制約を明示し、実現可能な代替構成を提示してください。

---

# 16. Claude Code自身はこのHarnessを作る

今回のあなた（Claude Code）の役割は、この開発を直接完遂することではなく、GitHub Copilot側に上記Harnessを安全に構築することです。

既存の構成を調査し、必要最小限の変更で、

- Instructions
- Custom Agents
- Skills参照
- Prompt Files
- validation
- docs / decisions

を整えてください。

同じ責務を複数fileへコピーしないでください。

---

# 17. 最初に設計案を提示する

大きな変更前に、次をHuman Developerへ提示してください。

1. 現在のCopilot customization
2. この環境で利用可能なmodel routing機能
3. Senior Pair Developerの実装案
4. Plannerの実装案
5. Tech Advisorの実装案
6. Independent Reviewerの実装案
7. Autopilot停止条件
8. Human confirmation条件
9. 高コストmodel呼出し回数の想定
10. 既存fileへの変更案
11. 削除 / 統合候補
12. 制約 / 未確認事項

その後、安全に進められる範囲を実装してください。

---

# 18. validationする

作成後に最低限確認してください。

- Agent file syntax
- Instructions reference
- Skill reference
- model configuration
- model routing
- tool restrictions
- read-only Reviewer
- Prompt reference
- build / testへの影響なし
- repository validation
- reference切れなし

「fileが存在する」と「実際にCopilotがそのmodel / Agentを利用できる」を区別してください。

IDE / CLIでしか確認できないものは、Human Developerが確認する方法を示してください。

---

# 19. Pilotで試す

Harness完成後、いきなり大規模開発へ広げないでください。

現在の代表機能または小さな未完TaskでPilotします。

確認すること:

- Plannerが適切な縦切りTaskを作れる
- Luna AutopilotがHuman介入なしでTaskを進められる
- 停止条件で無駄なloopを止められる
- Tech Advisorが必要な時だけ呼ばれる
- Reviewerが実装Agentとは異なるFindingを出せる
- Review FindingをLunaが修正できる
- Humanの介入回数が減る
- AI Credits消費が許容範囲
- 開発速度が改善する

---

# 20. 最終的に目指すHumanの関わり方

Human Developerが担当するのは主に、

- Goal
- Business / Product判断
- 重要なTrade-off
- Framework Providerへの確認
- Risk acceptance
- 最終成果の理解

です。

Humanが毎回、

- Task分解
- Red / Green確認
- 次のTask選択
- コード監視
- 一次Review

を行う必要がない状態を目指してください。

ただしHumanを置き去りにしないでください。

Senior Pair Developerは節目で短く、

- 今どこか
- 何が終わったか
- 次に何をするか
- 重要な学び
- Blocker / Risk

を伝えてください。

---

# 成功条件

成功とは、高性能なAgentをたくさん作ることではありません。

成功とは、

**低コストモデルが大半の開発を自律的に進め、難しい知的判断だけ高精度モデルへ狭く委譲し、Human Developerの介入を減らしながら品質を維持できること**

です。

さらに、

- Senior Pair DeveloperがHumanを育てる
- Plannerが良い縦切りを作る
- Tech Advisorが難所だけ突破する
- Independent Reviewerが別視点から反証する
- Humanは重要判断へ集中する
- AI Credits上限まで使い切らず開発期間を走り切れる

状態を目指してください。

基本思想は、

> **Cheap model does the work. Expensive model makes the hard decisions. Human keeps ownership.**

です。
