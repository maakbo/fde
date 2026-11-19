# 調査ノート：普遍原理 × 2026年のAgentic Engineering

調査日: 2026-11-20 JST / 状態: 公開資料の文献調査。**現場への適用効果は未検証**。

## 調査の見方

- **A: 原理・設計思想**＝モデル流行に左右されにくいが、個別効果はまだ測定対象。
- **B: 独立した実証研究**＝対象、手法、期間、信頼区間で解釈。外挿に制限。
- **C: 製品公式仕様**＝提供機能と動作環境の参考。職場導入可否や品質は別途検証。
- **D: 企業の自己事例・技術記事**＝有用な実装知見。ただし一般的な再現性の証拠ではない。
- **E: 本プロジェクトの仮説**＝文献から導出した設計判断であり、先行研究の結論ではない。

AIの「開発生産性」は文脈によってコード補完、タスク完了、PR、受入済み機能、品質、運用安定性が違う。数字を並べて直接比較しない。

## 1. 流行より長く生きる原理

### 1-1. 変わるものを隠し、責務を分ける — Parnas (1972) [A]

David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules* (CACM, Dec 1972)
https://doi.org/10.1145/361598.361623

機能工程ごとのファイル分割だけでは変更容易性は得られない。変化しやすい意思決定と責任の境界を隔離するのが要点。AI開発では、次の責務を混ぜないことに翻訳できる。

- 業務上の意図・QCDの合意と、どのエージェントに委託するか。
- 受入の判定基準と、それを満たす実装手段。
- 検証の実行結果と、検証者が出す解釈。
- 状態の正本と、会話ごとの見せ方。
- プロジェクト知識と、再利用するSkill。

**含意 [E]:** 「Planner.md」「Reviewer.md」ではなく、**独立して変更・検証できる責務**を先に設計する。異なる人格の数は設計の目的ではない。

### 1-2. 価値のループと実装のループは別 — Humans and Agents in Software Engineering Loops [A/D]

Kief Morris, *Humans and Agents in Software Engineering Loops*, Martin Fowler, 2026-03-04
https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html

「Why loop」（求める価値を確かめる）と「How loop」（実現する仕組みを作る）を分け、人がコード行ごとのGatekeeperから、内側のループを設計・改善する立場へ移る考え方。人をHowから完全追放するという主張ではない。

**含意 [E]:** 人は「何を達成し、どんなリスクなら許容できるか」を持ち、AIは下位ループを実行・検証する。人は重要な設計判断や未知・価値の再定義には参加する。

### 1-3. 品質制約と証明可能性が速度を支える [A/D]

Google SRE, *Service Level Objectives* / *Error Budget Policy*
https://sre.google/sre-book/service-level-objectives/
https://sre.google/workbook/error-budget-policy/

サービス信頼性と変更速度のTrade-offを、観測可能なSLO/エラーバジェットで議論する考え方。開発QCDへ**比喩として移植**し、セキュリティ・正確性等を不可譲の制約、残りを調整可能な予算として扱う。SREの本来の運用指標と「開発予算」が同一概念ではないことに注意。

**含意 [E]:** 品質は「最優先」などの曖昧な言葉だけでなく、誰が何をもって合格とするかを表す。Q、C、Dを単一スコアへ安易に加算しない。

### 1-4. 内部品質はAIにも必要 [A/D]

Kief Morris, *Maintainability sensors for coding agents*, 2026-05-27
https://martinfowler.com/articles/sensors-for-coding-agents.html

内部品質が劣化すると、人だけでなくAgent自身が既存構造を把握できず、重複実装や余計な文脈読み込みへ進みやすい。依存・変更量・複雑性のセンサーを「AIの自己修正に使う」観点。

**含意 [E]:** 可読性、凝集性、依存方向、重複、テスト容易性はAI時代に不要になるどころか、将来のAgent作業コストを左右する。

## 2. AIの効果は文脈依存：強い主張を避ける

| 資料 | 分かったこと | 対象と限界 | この構想への含意 |
| --- | --- | --- | --- |
| [B] Cui et al., Management Science 2026 / Microsoft Research | 3組織・4,867人のランダム化実験を統合し、AIコード補完を利用可能な開発者の完了タスクが平均26.08%増（標準誤差10.3%） | コード補完の実験。現代の長時間自律Agent、品質、全工程QCDを証明しない | 成功例を否定しないが、自分の対象で計測する |
| [B] METR 2025-07 | 経験豊富なOSS開発者16人・246タスクの実験ではAI利用が完了時間19%増 | 特定の2025年前半ツール・熟練開発者・既知コードベース。普遍的な遅延を意味しない | 読む・直す・検証する税まで含めて時間を測る |
| [B] METR 2026-02更新 | 後続実験では速くなる兆候を示すが、AIなしで働きたくない参加者の不参加などの選択バイアスで効果の大きさは不確か | 後続結果を「AIで18%速いと実証」と誤読しない | 大きな生産性数値を根拠に現場導入を即決しない |
| [B] DORA 2025 / 2026分析 | AI採用はDelivery Throughputの上昇とInstabilityの増加に**関連**、実装短縮が監査・検証へ再配分されるという観察 | 調査と関連分析が中心で、各案件への因果効果を断定できない | QCD全体と人の負荷を同時に測る |

参照:
- https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/
- https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- https://metr.org/blog/2026-02-24-uplift-update/
- https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/
- https://dora.dev/insights/balancing-ai-tensions/

## 3. 2026年に検証できる実装可能性と知見

### 3-1. AWS Labs AI-DLC Workflows [C] — 工程・状態・承認の候補

公式:
- https://github.com/awslabs/aidlc-workflows
- https://awslabs.github.io/aidlc-workflows/guide/00-introduction/
- https://awslabs.github.io/aidlc-workflows/guide/04-phases-and-stages/
- https://awslabs.github.io/aidlc-workflows/guide/workflow-profiles/
- https://awslabs.github.io/aidlc-workflows/guide/harnesses/copilot/

2026-11-20時点の公開ドキュメント上、ライフサイクルは **Initialization → Ideation → Inception → Construction → Operation**。Stage/Scope/承認Gate/成果物/状態管理の仕組みがある。企業向け以外にもpoc・bugfix・refactor・feature等のプロファイルがある。

**重要な更新:** GitHub Copilot CLIおよびVS Codeへの対応が明記され、表示されている前提は Copilot CLI >= 1.0.74 / VS Code >= 1.130、設定入口は aidlc config --harness copilot。したがって「Copilot非対応だから使えない」という前提は誤り。ただし職場PCの実バージョン・組織ポリシー・XDR・コマンド実行承認・外部ツール導入可否は**未確認**。Windowsではコマンドの都度確認が残る操作もある。

公式実装にはArtifact、承認、Code Generation/Build/Test、単位依存関係、条件付きの協働者、特定条件でのswarm実行が記されている。**その記述は既存のブランチ/worktree隔離や独立した評価Oracleが自動で正しく設計される保証ではない**。実装できること／運用に合うこと／成果が出ることは別。

**示唆 [E]:** 既存のScrum、TDD、設計消し込み、品質GateをAI-DLCに「置き換える」のではなく、工程制御・文脈再開・承認の重複箇所を候補として試す。Enterprise profileは高品質要求に親和的でも、最小PoCでは儀式の多さが逆効果になりうるためpoc等との比較が必要。

### 3-2. ハーネス設計そのものがエンジニアリング [D]

OpenAI, *Harness engineering: leveraging Codex in an agent-first world*, 2026-02-11
https://openai.com/index/harness-engineering/

公開実践報告は、Agentが読み取れるRepository、明確な境界、不変条件のLinter/Structural Test、アプリを実際に動かすBrowser/DOM/Screenshotのフィードバックを重視。これは企業内の事例報告であり、どの組織でも同じ生産性となる証拠ではない。

**示唆 [E]:** Promptを肥大化させて禁止事項を増やすより、検証できる不変条件を自動テストへ移す。アーキテクチャの責務は「コーディング判断の大半をどの環境で安全に自動化できるか」の設計へ移る。

Anthropic, *Building effective agents*, 2024-12-19
https://www.anthropic.com/research/building-effective-agents

単一の呼出し・決まったWorkflowで足りるところにAgent/多段構成を追加しない原則。オーケストレーションは単純な方法では測定目標を満たせない場合に導入。

Anthropic, *How we built our multi-agent research system*, 2025-06-13
https://www.anthropic.com/research/multi-agent-research-system

独立探索が多い研究において並列Agentは有効。ただし同記事は、研究型multi-agentが通常の会話に比べ約15倍のTokenを消費し、依存関係が多いコーディングは研究ほど並列化しにくいと説明。これを「多Agentならコーディング品質も必ず上がる」として扱わない。

### 3-3. 長期作業に必要なのは評価の独立性と記憶設計 [D]

Anthropic, *Harness design for long-running application development*, 2026-03-24
https://www.anthropic.com/research/harness-design-long-running-apps

計画と生成、ブラウザ実操作、Bug報告、評価の反復を比較し、自己評価の限界、実際の機能が見た目だけになる問題、ベースラインの改善を報告。**実験的な事例**であり、あるプロンプトが万人に効く証明ではない。

Anthropic, *Demystifying evals for AI agents*, 2026-01-09
https://www.anthropic.com/research/demystifying-evals-for-ai-agents

**Transcript/Trajectory（何をしたか）とOutcome（現実に何が起きたか）は違う。** 静的解析、ブラウザ評価、人による校正、回帰用のケースセットがAgentハーネス改善に必要。単独のLLMによる「合格」評価には限界。

Anthropic, *Effective context engineering for AI agents*, 2025-09-29
https://www.anthropic.com/research/effective-context-engineering-for-ai-agents

無制限な文脈は有害。最小で信号密度の高い情報、明確な道具の境界、必要時の検索が重要。

Anthropic, *The components of agent memory*, 2026-11-06
https://www.anthropic.com/research/components-of-agent-memory

Agent Memoryを、transcript / notes / knowledge representations / preloaded context 等の層として考え、何を将来のために残すかを評価。記事で示されるDreamingやメモリの実装は製品特有であり、GitHub+Markdownに同等機能がすでに存在する意味ではない。

**示唆 [E]:** 現在地のコンパクトなStateを少量注入し、根拠は索引から遡る。記憶の正しさを保つために更新源・期限・矛盾・失効を扱う。長い履歴を丸ごとContextへ載せることをやめる。

### 3-4. テストを「AIが自分で変えられる言い訳」にしない [D]

Giorgio Giammaria et al., *Tests as data*, Martin Fowler, 2026-11-11
https://martinfowler.com/articles/tests-as-data.html

顧客の言葉による受入シナリオと、実装コード・テストランナーを分離し、テストデータを変更に強い独立資産として扱う実践提案。黒箱テスト、Mutation Testing、Property-based Test、Linter、Human Exploratory Testingも組み合わせる。特定の実践者の見解であり、厳密な比較実験ではない。

**示唆 [E]:** TDDは必要だが十分ではない。AIが書いたテストとコードが**同じ仕様誤解を共有していれば、全部Greenでも間違い**。受入Oracleは、実装に先立ち人が承認した振る舞い・設計入力から独立して保護する。UIはDOM/操作だけでなく、適切な環境でScreenshotを使った人の受入も残す。

### 3-5. CI上のAgentic Workflowは選択肢だが主役ではない [C]

GitHub, *GitHub Agentic Workflows generally available*, 2026-10-28
https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/

MarkdownからActions workflowを作り、issue triageやCI分析等を実行する仕組み。隔離・権限・Firewallが公式に説明されている。**組織のGitHub Actions利用可否、秘密情報、実行権限、ポリシーを確認するまでは導入候補止まり**。VS Codeでの受入ブラウザ操作やAI-DLCとは別の問題を解く仕組み。

### 3-6. ベンチマークの高さを実案件の品質保証と取り違えない [B/C]

Deng et al., *SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?*, ICML 2026
https://proceedings.mlr.press/v306/deng26f.html

Scale Labs, *SWE-Bench Pro V2*, 2026-10
https://labs.scale.com/leaderboard/swe_bench_pro_public_v2

OpenAI, *Separating signal from noise in coding evaluations*, 2026-07-08
https://openai.com/index/separating-signal-from-noise-coding-evaluations/

長い実務的なソフトウェア変更の評価は難しく、問題選択・正解テスト・混入/漏洩などでスコアの意味が変わる。GitHub上の公開ベンチマークで高得点でも、未整理な設計入力・実行権限・UI評価・職場固有の規約に適合することの証明にはならない。

## 4. 先行知見から導く設計論点（ここからは仮説）

| 研究が示す問題 | そのままの解決では不足 | 今回の仮説 |
| --- | --- | --- |
| QCD全体の実測は混合 | Agentの生成速度だけ見る | QCD Contract + Outcome Scorecard |
| 監査・検証税 | Reviewerを追加するだけ | Decision Surface + Evidence on demand |
| Agent自身の誤検証 | 同じAgentのテスト通過を信じる | 承認済みAcceptance Oracle + 独立反証 |
| 記憶の氾濫 | Markdownを増やす | Current State / Evidence Ledger / Skill Memoryの3層 |
| Workflowの過剰複雑化 | 高機能フレームワークに全面移行 | AI-DLCの既製機能を先に試し、重複を減らす |
| 人がWhy、AIがHowに固定される | 人は最後の承認ボタンのみ | AIもWhyの問い直し・新しい可能性を**提案**できる |
| 複利エンジニアリングの効果不明 | Skillを増やす | Failure Case → Replay Eval → Verified Learning |

## 5. 検証しない限り断定しないこと

1. AI-DLCが既存ハーネスより速い、軽い、高品質であるか。
2. Copilot/VS Code環境で対象Version・組織ポリシー・追加実行コマンドが許可されるか。
3. 同じモデルを複数Agentへ割り当てることで「独立した」批判がどの程度得られるか。
4. UIの自動スクリーンショット比較でUX・視認性まで保障できるか。
5. Skillの自己改善で実案件の横展開が良くなるか。
6. 人が面白いと感じる「驚き」を定量指標だけで捉えられるか。
7. 規格・調査・ベンチマークから個別組織のQCD改善効果を推定できるか。

これらを [HYPOTHESES.md](HYPOTHESES.md) で反証可能な形へ落とす。

## 6. 文献の選定・限界

ここでは古典原理、独立した開発者実験、企業・プロジェクトの公式実装、AI Agentの運用事例、テスト/品質の実務的議論を組み合わせた。2026-11-20までに確認できた公開資料に限定。体系的な全論文サーベイではなく、ベンダー事例が多いこと、職場の実Repositoryを読んでいないこと、実物を実行したわけではないことを明示する。将来のVersionで仕様は変わりうる。