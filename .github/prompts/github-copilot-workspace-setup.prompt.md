---
description: GitHub Copilot向けに、既存プロジェクトを調査し、安全なInstructions・Skills・Custom Agents・Prompt Files・検査まで含む作業環境を構築する基盤セットアップ指示
---

# GitHub Copilotの作業環境を整えるセットアップ指示

今開いているプロジェクトを調べ、GitHub Copilotで人間とAIが継続的に作業しやすい環境を実際に構築してください。

説明だけで終わらず、必要なファイル作成、既存設定への安全な統合、実行可能な検査、結果報告まで進めてください。

この指示書を `.github/copilot-instructions.md` へ丸ごと保存してはいけません。

目的は「大量のAI設定を作ること」ではありません。

既存プロジェクトの構造とルールを尊重しながら、

- 常時必要な共通Instructions
- 必要な場面だけ適用するInstructions
- 再利用可能なSkills
- 専門的なCustom Agents
- 明示的に呼び出すPrompt Files
- 検証可能な設定と手順
- 人間へ引き継げるContext

を責務ごとに分け、重複なく、小さく、改善可能な状態を作ることです。

---

## 1. 最初に環境を確認する

現在のプロジェクトルート、OS、シェル、IDE、取得できるGitHub Copilot関連バージョンまたは利用形態、Gitの有無と未コミット変更を確認してください。

ホーム全体や無関係なフォルダは走査しないでください。

最低限、以下を確認してください。

- README / CONTRIBUTING
- AGENTS.md / AGENTS.override.md
- .github/copilot-instructions.md
- .github/instructions/
- .github/agents/
- .github/prompts/
- .github/skills/ または現在のCopilotが認識するSkill配置
- その他の既存AI向け指示ファイル
- GitHub Issues / Projects / Actions
- build / test / lint / format
- 既存CI
- 利用中のMCP / Extensions / Toolsがあればその登録状況
- 現在利用可能なGitHub CopilotのAgent / Custom Agent / Skill / Prompt / Instruction機能

秘密を含み得る設定は全文表示せず、必要な構造、登録名、ファイルの存在だけを確認してください。

未知のスクリプト、Hook相当機構、CI、外部通信を伴う処理を無条件に実行してはいけません。

ホーム直下、システム領域、複数案件を含む親フォルダである場合は、書き込まず対象プロジェクトを特定してください。

対象が明確なら、用途を開発・文章制作・調査・事務・混在から判断してください。

不明なものは「未確認」とし、安全な共通部分から進めてください。

---

## 2. GitHub Copilotの仕様を実行時点で確認する

GitHub CopilotのCustomization機能は更新されるため、実行時点のGitHub公式ドキュメントと、現在利用中のIDE / Agent mode / 組織設定を正としてください。

少なくとも次の概念について、現在利用可能か確認してください。

- Repository custom instructions
- Path-specific instructions
- AGENTS.md support
- Prompt files
- Agent Skills
- Custom agents / agent profiles
- Agent mode
- Coding agent
- MCP / external tools
- Permissions / approvals
- Agent hooks または同等の検証拡張機構
- GitHub Issues / Projectsとの連携
- IDEごとの差異

未確認の設定キー、frontmatter、directory、tool名を捏造してはいけません。

通信できない場合は、ローカル環境と既存ファイルから確認できる範囲だけ採用してください。

認証変更、追加課金、外部サービス登録、組織設定変更は行わないでください。

---


## AIモデルとAI Creditsの運用方針

AI Creditsを節約しながら品質を保つため、すべての作業を同じモデルで実行しないでください。

実行時点で利用可能なモデル、価格、AI Creditsの計算方法をGitHub公式情報または現在の組織設定で確認してください。以下のモデル名が利用できない場合は、同等の「低コスト高速モデル」と「高精度推論モデル」に読み替えてください。

基本方針:

- 通常作業は **GPT-6 Luna相当の低コストモデル**
- 設計判断・複雑な分析・難しいレビューは **GPT-6 Sol相当の高精度モデル**
- Astra等の高コスト・長時間自律モデルは、長時間の自律実装が本当に必要で、人間が明示的に了承した場合だけ検討
- high reasoning / large contextも常用せず、必要な時だけ使う
- 高精度モデルで方針が決まったら、その後の定型実装・ファイル編集・検査は低コストモデルへ戻す

推奨パターン:

> Lunaで調べる → Solで決める → Lunaで作る・検査する

### Luna相当で進める作業

- repository構造の調査
- 既存Instructions / Agents / Skills / Promptsの棚卸し
- file検索
- GitHub Issues / Projectsの状態取得
- 定型的なfile作成・編集
- 既に決まった設計に沿った実装
- 単純なJUnit / Playwright追加
- README / Context / Report更新
- build / test実行
- 機械的なvalidation

### Sol相当へエスカレーションする条件

次のいずれかに該当したら、Lunaのまま押し切らないでください。

- 複数の設計案から重要な選択を行う
- Agent / Skill / Instructionsの責務境界を決める
- architectureやmodule境界を横断する変更
- 既存仕様が曖昧で、複数file・複数layerを横断して推論する必要がある
- 同じfailureが2回以上続き、原因が特定できない
- transaction、concurrency、security、data consistency等の高リスク判断
- code reviewで設計上の妥当性を評価する
- Skillの採否やScrum Harness全体の構造を決定する
- 低コストモデルの回答に矛盾、根拠不足、過剰な推測が見られる

エスカレーション時は、可能ならモデルを切り替えてください。環境上自動切替できない場合は、

「ここからはSol相当を推奨: <理由>」

と明示してください。

高精度モデルを使った後は、判断結果を短くArtifactへ残し、その判断に従う作業はLuna相当へ戻してください。

### Credits最適化のためのContext管理

- repository全体を毎回Contextへ投入しない
- まず検索し、必要なfileだけ読む
- 安定した事実はInstructions / Contextへ残し、毎回再推論しない
- 長いChat履歴よりrepositoryの正本を優先する
- 同じ調査を繰り返さない
- 大context / high reasoningの利用理由を説明できる場合だけ有効化する

モデル選択も今回構築するWorkspaceの一部です。Custom Agentがモデル指定をサポートする場合は、役割と作業特性に合わせて適切なモデルを設定してください。未対応なら、各Agent / Promptにエスカレーション基準を記載してください。

---

## 3. 変更の境界を決める

最初に短い作業計画を示したら、対象プロジェクト内の可逆的な設定作業を進めてください。

既存ファイル、未コミット変更、既存の意味を維持し、必要箇所だけ変更します。

この依頼だけでは次を行わないでください。

- ファイル移動・削除
- 大規模なrepository再編
- グローバル設定変更
- package追加
- 外部送信・公開
- Git commit / push / merge
- 本番操作
- Secret閲覧
- 権限拡大
- 組織設定変更
- GitHub App / MCPの追加

必要な場合は提案に留めてください。

既存JSON / YAML / Markdownを更新する場合、未知のキーや既存項目を消さず、配列や設定全体を丸ごと置換しないでください。

外部を指すsymlinkへ書き込まないでください。

変更前の状態はローカルで復元可能にしてください。

復元対象は今回の差分だけとし、`git reset --hard` や `git clean` は禁止です。

---

## 4. Instructionsを短く責務分離する

常時読み込ませる情報を肥大化させないでください。

既存構成がなければ、責務を次のように分離することを検討してください。

### AGENTS.md

ツール非依存の共通方針を置きます。

目安は短く保ち、

- project purpose
- 重要な参照先
- build / test
- 変更境界
- 完了条件
- 安全ルール

など、どのAgentにも必要な安定情報だけを書きます。

既存AGENTS.mdがある場合は重要なルールを保持してください。

GitHub Copilot専用の機能や構文をAGENTS.mdへ過度に埋め込まないでください。

### .github/copilot-instructions.md

GitHub Copilotがrepository全体で常に知る必要がある、安定した補足だけを書いてください。

例えば:

- AGENTS.mdを先に読む
- project固有の重要ルール
- build / testの入口
- 変更時の禁止事項
- Instructions / Skills / Agentsの参照方針

進捗、現在のSprint、詳細な作業履歴など一時的な情報を入れないでください。

### .github/instructions/

現在の仕様でpath-specific instructionsが利用できる場合だけ使ってください。

例えば:

- Java source
- tests
- docs
- infrastructure

など、対象pathでのみ必要なルールへ限定します。

repository-wide ruleをコピーして増殖させないでください。

---

## 5. プロジェクトContextと作業情報をInstructionsから分離する

同等の既存構成がある場合はそれを優先してください。

なければ必要に応じて次のような場所を検討してください。

- docs/ai/context.md
- docs/ai/checks.md
- docs/ai/setup-report.md
- docs/ai/decisions.md
- tasks/active.md
- tasks/handoff.md
- outputs/

ただし、GitHub Issues / Projects等がTask管理の正本として存在する場合、`tasks/active.md` 等を二重管理のために新設しないでください。

### context.md

- project purpose
- 利用者
- architecture概要
- 参照すべき資料
- 確定事項
- 未確認事項

### checks.md

- 作業別の合格条件
- 実在する検査command
- 手動確認事項
- 実行時の副作用

### setup-report.md

- 今回変更したもの
- 検査結果
- 未適用項目
- 制約
- 復元方法

### decisions.md

AI環境に関する重要な選択だけを残します。

長い作業日記にはしないでください。

---

## 6. 既製Skillを優先し、独自Skillを増やしすぎない

一般的な方法論について独自Skillを書く前に、利用可能な既製Skillを調査してください。

例:

- Test Driven Development
- systematic debugging
- verification before completion
- code review
- implementation planning
- GitHub Issues / Projects
- Sprint Planning
- test scenario design
- Playwright
- documentation

候補Skillについて、

- Source
- Maintainer
- License
- Responsibility
- Permissions / Tools
- 更新状況
- 既存Skillとの重複
- projectへの適合性

を確認してください。

初回からSkill collection全体を導入しないでください。

必要なSkillだけ選択します。

独自Skillは、

- project固有である
- 何度も繰り返す
- 手順が安定した
- Instructionsでは長すぎる

場合に作成してください。

実際のSprint / 作業で繰り返す価値が確認される前に、大量のSkillを作らないでください。

---

## 7. 毎回使う作業手順をSkillにする場合

現在のGitHub CopilotがAgent Skillsをサポートしている場合、公式仕様に従った配置と形式を使用してください。

Skillは具体的な責務を1つ持たせます。

例えばproject固有に必要であれば、

- project-work
- project-check

のようなSkillを検討できます。

### project-work

「資料確認 → 必要な計画 → 小さく実行 → 検査 → 修正 → 引き継ぎ」

を担当します。

軽微な変更では過剰な儀式を省略してください。

同じ失敗が2回続く、または修正が3巡しても解消しない場合は、原因と不足情報を記録して人間へ相談してください。

これはproject上の運用ルールであり、GitHub Copilot製品の固定仕様ではありません。

### project-check

成果物と差分を、定義済みの合格条件に対して検査します。

- 検査結果
- 証拠
- 未確認事項

を区別してください。

Skillから権限承認を迂回しないでください。

公開・送信・merge・production操作などは含めないでください。

---

## 8. 専門的な役割だけCustom Agentにする

現在のGitHub CopilotがCustom Agent / Agent Profileをサポートする場合だけ利用してください。

Agent Profileは一般的な開発方法論を大量に複製せず、

- Role
- Responsibility
- Boundaries
- 利用するSkill
- 参照するArtifact
- 他Agentとのhandoff

を中心にしてください。

例:

- Developer
- Tech Lead
- QA
- Reviewer
- Scrum Master

ただし、projectに本当に必要なAgentだけ作成してください。

Custom Agentが利用できない環境では、存在しない機能を模倣せず、Prompt Filesまたは通常のAgent modeで役割を明示する方法へ切り替えてください。

---

## 9. 作成役とは別の確認役を用意する

変更を作る役と、変更を確認する役を論理的に分離してください。

Custom Agentが利用可能なら、読み取り中心のReviewer Agentを検討してください。

Reviewerには可能な限り、

- source
- tests
- diff
- acceptance criteria

を読み取る能力だけを与え、不要な編集、shell、外部送信権限を与えないでください。

確認観点:

- 具体的な誤り
- Acceptance Criteria未達
- 根拠不足
- regression risk
- 依頼外変更
- security / privacy
- test不足

問題を無理に作らないでください。

独立Reviewerを起動できない場合は、主担当が観点を切り替えて確認し、「独立レビュー未実施」と記録してください。

---

## 10. Prompt Filesは「明示的に開始したい作業」に使う

Prompt Filesが現在利用可能なら、常時Instructionsへ入れる必要がない反復作業を置いてください。

候補:

- workspace setup
- Sprint Planning
- Daily
- code review
- test planning
- Sprint Review
- Retrospective
- architecture investigation

Promptは長期的なproject factを持つ場所ではありません。

Product Goalやarchitectureの正本をPromptへコピーせず、実在する参照先を読むよう指示してください。

同じ内容をInstructions / Skill / Agent / Promptへ重複させないでください。

---

## 11. Task管理の正本を二重化しない

既にGitHub Issues / Projects / Milestonesが使われている場合は、可能な限りそれを利用してください。

Markdownによる独自BacklogやKanbanを安易に追加しないでください。

利用可能なCopilot Skill / ToolがGitHub Issues / Projectsを安全に操作できる場合、

- Product Backlog
- Sprint Backlog
- Kanban
- Subtask
- Dependency
- Status

を既存GitHub機能へ寄せることを検討してください。

更新権限や組織policyが不明なら、自動変更せず提案に留めてください。

---

## 12. 権限を緩めない

GitHub Copilot Agent mode、Coding Agent、MCP、Custom Agent等の権限モデルを現在の公式仕様で確認してください。

承認なしに権限を広げないでください。

特に、

- unrestricted shell
- production access
- Secret read
- external write
- GitHub push / merge
- organization administration
- package publication
- cloud resource mutation

を自動許可しないでください。

既存の過剰権限が見つかった場合は、勝手に変更せず報告してください。

`.gitignore` やInstructionsだけで機密アクセスを完全に防げると説明してはいけません。

MCPは自動追加せず、

- 用途
- 接続先
- 必要権限
- 送信データ
- organization policy

が分かってから提案してください。

---

## 13. 実行できる軽量検査を作る

追加依存なしで可能なら、Python / Node / shell等を使って、今回管理するAI設定の構造を検査する軽量scriptを作成してください。

対象例:

- 必須ファイルの存在
- Markdown参照先
- JSON / YAML syntax
- Instructionsの重複
- 存在しないSkill参照
- Agentが参照するSkill / file
- Promptから参照するfile
- 循環参照
- 禁止された秘密pathの記載

巨大directoryやsecretを再帰走査しないでください。

正式なparserがない形式を完全検証したと主張しないでください。

検査できない項目は「未検証」としてください。

---

## 14. 自動検査との接続は現在のCopilot仕様に合わせる

GitHub Copilot側に現在利用可能なHook / Agent Hook / validation extension等が存在し、このproject環境でも安全に利用できることを確認できた場合だけ、自動検査への接続を検討してください。

存在しないHook機構をClaude CodeのHookになぞらえて作らないでください。

代替として既存CI / GitHub Actionsを利用できる場合もありますが、このセットアップだけを理由に勝手にCIを追加・変更しないでください。

自動接続する場合は、

- network不要
- file変更なし
- package導入なし
- 対象path固定
- timeoutあり
- failure理由が明確
- 無限loopしない

ことを確認してください。

適切な仕組みがなければmanual checkで十分です。

---

## 15. project固有の情報と汎用方法論を分ける

次を混同しないでください。

### Project fact

例:

- Java version
- build command
- Framework固有記法
- directory構造
- coding convention
- Product Goal
- Definition of Done

これはInstructions / Context / project docs等へ。

### General practice

例:

- TDD
- debugging
- code review
- Sprint Planning

これは既製Skillを優先。

### Role

例:

- Developer
- Tech Lead
- QA
- Scrum Master

これは必要ならCustom Agentへ。

### One-off / explicitly invoked workflow

例:

- workspace setup
- retrospective
- architecture investigation

これはPrompt File候補。

この分離を維持してください。

---

## 16. AIが人間の理解を置き去りにしない

開発projectでは、AIが短時間で大量のコードを生成することだけを成功としないでください。

人間Developerが学習中の場合は、変更前後に必要な範囲で、

- 何を変更するか
- なぜその変更が必要か
- 既存コードの何を参考にしたか
- 標準技術かproject固有技術か
- どの検査で正しさを見るか

を説明してください。

ただし、簡単な変更で長い講義を行わないでください。

説明量はtaskの難易度と人間の理解度に合わせます。

---

## 17. セットアップは段階的に行う

初回から完成形を作らないでください。

### Phase 1: Inspect

- current repository
- current Copilot customization
- project task management
- build / test
- available Skills / Agents / Prompts
- permissions

を調査します。

### Phase 2: Propose

作成前に、

- 維持する既存構成
- 追加したい最小Instructions
- 採用したい既製Skill
- 自作が必要なSkill
- 必要なCustom Agent
- 必要なPrompt
- Task管理の正本
- Validation方法

を短く提示します。

### Phase 3: Build minimum setup

合意または安全に進められる範囲で最小構成を実装します。

### Phase 4: Validate

設定構造と参照を検査します。

### Phase 5: Trial

実際の小さなTaskで利用し、使いにくい部分を確認します。

### Phase 6: Adapt

不要なものは増やさず、繰り返し必要なものだけ改善します。

---

## 18. 同じセットアップを再実行しても増殖させない

この指示を再実行したとき、

- 同じAgent
- 同じSkill
- 同じPrompt
- 同じInstructions
- 同じdirectory
- 同じvalidation

を重複して作らないでください。

既存のものを読み、必要な差分だけ更新してください。

既に適切なものが存在する場合は「変更不要」と判断してください。

---

## 19. 本当に使えるか確認する

作成後にすべて読み直し、

- Instructionsの参照
- path-specific instructionの適用範囲
- Skillの形式
- Custom Agentの形式
- Prompt Fileの形式
- 各Artifact間の参照先
- validation script
- task管理の正本
- 依頼外変更の有無

を確認してください。

既存のbuild / test / lint等は、定義と副作用を確認したうえで必要分だけ実行してください。

安全に実行できない場合は「未実行」とし、成功扱いしないでください。

「ファイルが存在すること」と「GitHub Copilotが実際に読み込んだこと」を区別してください。

IDE上でのみ確認可能な項目は、利用者が新しいCopilotセッションで確認する具体的な方法を案内してください。

自分で確認できないUI操作を「確認済み」と書かないでください。

---

## 20. 最後に報告する

最後に日本語で次を報告してください。

1. 調査したGitHub Copilot環境
2. 既存で利用した仕組み
3. 作成・変更したファイル
4. Instructionsの構成
5. 導入したSkill
6. 作成したCustom Agent
7. 作成したPrompt File
8. Task管理の正本
9. 実行した検査と結果
10. 実際には確認できていない項目
11. 保留した機能と理由
12. 今回だけの復元方法
13. 次の新規Copilotセッションで確認すること
14. 最初に送る依頼例

成功・失敗・未実行・未確認を区別してください。

---

# 成功条件

成功とは、`.github` 配下に大量のファイルが作られたことではありません。

成功とは、

- 人間とCopilotが同じproject factsを参照できる
- 一般的方法論は再利用可能なSkillへ委譲されている
- Agentごとの責務が混ざっていない
- 一時的なTaskと安定したInstructionsが分離されている
- 変更と検査が再現可能である
- 不要な権限を増やしていない
- 既存repositoryの構造を壊していない
- 同じセットアップを再実行しても設定が増殖しない
- 実際のTaskを通じて改善できる

状態です。

**GitHub Copilotを強く設定することではなく、人間とCopilotが安全に、理解可能に、継続して一緒に働ける作業環境を作ってください。**
