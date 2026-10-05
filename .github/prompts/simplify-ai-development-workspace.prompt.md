---
description: 実際に使ったAI開発環境を棚卸しし、役割・Prompt・Skill・Instructions・管理Artifactを引き算して、人間とAIが迷わず一緒に開発できる最小構成へ整理する
---

# AI開発環境を引き算する

このプロジェクトで構築したAI開発環境を、実際に使った経験をもとに棚卸しし、**必要最小限で気持ちよく回る構成へ簡素化**してください。

今回の目的は、新しい仕組みを追加することではありません。

> **役に立ったものを残し、重複・儀式・過剰な役割分担を減らし、Human DeveloperとAIが直接仕事を進めやすい状態へ戻す**

ことが目的です。

この作業自体を新しい大きなFrameworkにしないでください。

---

# 1. まず実際に使われたものを確認する

変更前に、現在のAI向け構成を調査してください。

最低限確認するもの:

- AGENTS.md
- .github/copilot-instructions.md
- .github/instructions/
- .github/agents/
- .github/skills/
- .github/prompts/
- docs/ai/
- docs/development/
- tasks/
- GitHub Issues / Projects
- Claude Code向け設定があればその構成
- build / test / run / validation
- Human–AI開発で実際に使ったKnowledge

ファイルが存在するだけで「必要」と判断しないでください。

可能な範囲で、

- 実際に使った
- 役に立った
- 重複した
- 邪魔になった
- 使わなかった
- まだ評価できない

を区別してください。

---

# 2. 今の目的を再確認する

現在もっとも大切なのは、複雑なAI組織を作ることではありません。

中心となる開発ループは次です。

> Sampleを理解する
> → 開発環境を立ち上げる
> → 代表機能を設計する
> → Testを書く
> → 実装する
> → 動かす
> → 理解する
> → 次回に役立つKnowledgeだけ残す

Human DeveloperがJavaとFrameworkを理解しながら、AIと自然に対話して開発を進められることを優先してください。

Scrum、Agent Team、管理Artifact等は、このループを明確に助ける場合だけ残してください。

---

# 3. 引き算の判断基準

各Artifact / Agent / Skill / Prompt / Ruleについて、以下を確認してください。

## Keep

次のいずれかを満たすもの。

- 毎回必要な安定したproject fact
- 人間とAIの双方が実際に参照する
- 同じ調査や失敗を減らした
- 開発の正確性を明確に上げた
- Human Developerの理解を助けた
- 次の機能開発を速くした
- 他の仕組みでは代替しにくい

## Merge

単独では価値があるが、別Artifactと責務が重複しているもの。

## Defer / Archive

将来は使う可能性があるが、現在の開発ループには不要なもの。

## Remove candidate

次のようなもの。

- 同じ内容が複数箇所にある
- 誰も参照しない
- 毎回読むには長すぎる
- AIに儀式的な振る舞いを強制するだけ
- Product開発よりHarness管理を増やす
- Agentを切り替えるためだけに認知負荷が増える
- GitHub Issues等と二重管理になる
- 実務上の効果を説明できない

---

# 4. Scrumを目的化しない

Scrum由来の仕組みは、実際に価値があった部分だけ残してください。

現時点で最低限価値がある可能性が高いもの:

- Goalを1つ明確にする
- 今やっていることを見えるようにする
- Blockerを明らかにする
- 脱線するTaskを後回しにする
- 最後に短く振り返る

これらを実現するために、

- Scrum Master Agent
- Sprint ceremony一式
- 大量のSprint document
- 複雑なKanban
- Scrum用語

が必須とは限りません。

より簡単な仕組みで同じ価値を得られるなら、簡単な方を選んでください。

Human–AI Scrum Harnessは、現在必要でなければ削除候補または将来用Promptとして扱って構いません。

ただし、削除や大きな統合は人間へ提案してから実施してください。

---

# 5. Agentを増やしすぎない

Human DeveloperがAIと直接会話して仕事を進めることを基本にしてください。

役割分担が明確な価値を生まない場合、

- Developer
- Tech Lead
- QA
- Scrum Master
- Reviewer

を常時別Agentとして維持する必要はありません。

例えば、

- 通常は1つのPair Developer
- 難しい設計時だけTech Lead観点
- 完了時だけReviewer / QA観点

のように、**役割をAgentではなく一時的な観点として使う**方が簡単なら、そちらを優先してください。

Agentを残す条件は、

> 「このAgentへ切り替えることで、Human Developerが明確に仕事を進めやすくなるか」

です。

---

# 6. 「正しく動く」と「一緒に仕事したくなる」の両方を残す

AIには2種類の品質が必要です。

## Execution Quality

- Instructionsを守る
- Testする
- 推測を事実扱いしない
- 変更範囲を守る
- build / validationを正しく行う
- Doneを偽らない

## Collaboration Quality

- 今どこまで分かったか自然に伝える
- 次にやることを簡潔に声かけする
- Human Developerが迷っている点を察知する
- Framework固有部分を必要な時に説明する
- 詰まったら相談する
- 人間を置き去りにせずPairで進む

前者だけを残して、無機質で会話しづらい環境にしないでください。

後者だけを重視して、感じは良いが検証が甘い環境にもしてはいけません。

目指すのは、

> **丁寧に伴走するが、検証は厳密**

なAI開発環境です。

---

# 7. Promptの役割を絞る

現在のPrompt Filesを確認し、それぞれの役割が重複していないか確認してください。

現時点の中心候補は次です。

## Workspace Setup

AIが安全にprojectを理解して働ける下地を作る。

## Framework Adoption Knowledge Context

この活動の目的をAIへ伝える。

- Human Developerが学ぶ
- FrictionをKnowledgeへ変える
- 次のDeveloperを助ける
- Framework ProviderへFeedbackする

## Sprint Zero / Feasibility Study

代表機能を1本、設計 → 開発 → Testまで通す実践。

名称にSprint Zeroを使い続ける必要があるかも再評価してください。
実態が「Feasibility / Golden Path Development」であれば、より分かりやすい名前へ変更候補を提示してください。

## Senior Engineer Mentor Lesson

完走後、実コードを教材にHuman Developerの理解へ変える。

これら以外のPromptは、

- 今使うもの
- 将来用
- 重複
- 不要

に分類してください。

---

# 8. Instructionsをさらに短くする

常時読み込むInstructionsには、毎回必要な安定事項だけを残してください。

残す候補:

- project purpose
- build / test / run
- important architecture facts
- Frameworkで確認済みのrule
- change boundaries
- verification requirement
- Human Developerを置き去りにしない方針
- Knowledgeの参照先

削る候補:

- 長い背景説明
- 現在のTask
- 過去の経緯
- ceremony
- Promptで十分な手順
- Skillと重複する一般論

常時Contextを小さくすることは、AI Credits削減にもつながります。

---

# 9. Skillも実績ベースで減らす

既製Skillを含め、導入済みSkillを確認してください。

Skillは「良さそうだから」ではなく、

> 実際に呼ばれ、期待する品質向上があったか

で評価してください。

特に、

- TDD
- systematic debugging
- verification
- code review

のように開発品質へ直接効いたものは優先して残します。

反対に、ほとんど使わないSkillや、Agent Prompt内の短い指示で十分なものは削減候補です。

---

# 10. Task / Knowledgeの二重管理をなくす

同じ情報が、

- GitHub Issues
- GitHub Projects
- tasks/*.md
- Sprint document
- Prompt
- Instructions

へ複製されていないか確認してください。

正本を1つ決めてください。

Knowledgeについても、

- Quick Start
- Implementation Guide
- Framework Notes
- Testing Guide

を細分化しすぎず、読みやすい単位へ統合してください。

新しいfileを増やすより、見つけやすさを優先してください。

---

# 11. Model routingも簡潔にする

AI Credits節約の基本ルールは維持します。

> Luna相当で調査・通常作業
> → 難しい判断だけSol相当
> → 方針確定後Luna相当へ戻る

ただし、各Promptに同じ長いmodel policyを重複させる必要があるか確認してください。

安定した共通Ruleとして1箇所に置けるなら統合を提案してください。

モデル設定そのものが複雑な運用負荷にならないようにしてください。

---

# 12. まず削除案を提示する

破壊的変更の前に、次の表を人間へ提示してください。

| 対象 | 現在の役割 | 実利用 | 判断 | 理由 | 変更案 |
|---|---|---|---|---|---|
| ... | ... | Used / Unused / Unknown | Keep / Merge / Defer / Remove | ... | ... |

その後、

## Minimal Target

として、

「このprojectでAIと開発するために最低限これだけあればよい」

という最小構成を提示してください。

目標は可能であれば、

- 共通Instructions: 1つ
- project context / Knowledge入口: 1つ
- 毎日使う主要Prompt: 少数
- Skill: 実績のあるものだけ
- Agent: 本当に役割分離が必要なものだけ
- Taskの正本: 1つ

程度の分かりやすさです。

数字を達成するために無理に削らないでください。

---

# 13. 人間の承認後に整理する

削除・統合・rename等の大きな変更は、Minimal Targetを人間が確認してから実施してください。

実施時は、

- 既存Knowledgeを失わない
- 有用なruleを落とさない
- reference切れを直す
- validationを行う
- Git diffを確認する

ようにしてください。

「削除したからシンプルになった」ではなく、実際の利用導線が簡単になったことを確認してください。

---

# 14. 最後に1つの利用導線を示す

整理後、人間Developerが迷わないように、

> **明日からどう使うか**

を非常に短く示してください。

理想的には例えば、

1. AIと普通に開発を始める
2. 代表機能を通す時だけFeasibility Promptを使う
3. 困ったらDebug / TDD Skillを使う
4. 完走したらMentor Promptで振り返る
5. 再利用価値がある知識だけ残す

程度です。

「どのAgentを選ぶか」「どのPromptを毎回呼ぶか」をHuman Developerが常に考え続ける環境にしないでください。

---

# 15. 成功条件

成功とは、AI開発環境の設計が美しくなったことではありません。

成功とはHuman Developerが、

> **何も気にしすぎずAIと開発を始められる**

状態になることです。

具体的には、

- AIとの対話が自然
- 何を使うか迷わない
- Contextが重すぎない
- Task管理が重複しない
- Knowledgeが見つかる
- Test / verificationは弱くならない
- Java / Frameworkの理解を促してくれる
- 次の機能へすぐ進める
- AI Creditsを無駄に消費しない

状態です。

最終判断基準は、

> **これは開発を助けているか。それとも、AI開発環境を管理する仕事を増やしているか。**

です。

後者なら、引き算してください。
