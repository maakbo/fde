---
description: 既存のJava/Gradle Webアプリを読み解き、Playwright/JUnitのTDDで代表画面をワンパス実装しながら、人間とCopilotが継続開発できるハーネスを育てる
---

# Java Webアプリ開発ハーネスを構築し、代表画面をワンパス実装する

あなたには、このリポジトリにおける開発パートナーとして、既存コードを理解しながら、今後人間とAIが継続的に開発を進められる「開発ハーネス」を構築してほしいです。

今回の目的は、単にコードを生成して1機能を完成させることではありません。

提供済みのWebアプリのサンプルプロジェクトを出発点として、次を一連の仕事として扱ってください。

- リポジトリを読み解く
- 開発・実行・テスト方法を明らかにする
- 実案件の代表的な画面を1本模倣する
- Playwright / JUnitによるテストを先に定義する
- テストが通るように実装する
- Web → アプリケーション処理 → OR Mapper → DB → 応答まで、代表的な処理シーケンスをワンパス通す
- そこで得られた知識をリポジトリへ蓄積する
- 次の機能開発や、別の開発メンバーの参加が楽になる状態を作る

## 前提

想定する技術構成は以下です。実際のプロジェクト構成を一次情報として扱い、異なる場合はそちらを優先してください。

- Java 21
- Gradle
- 組織固有のWebアプリケーションフレームワーク
- 組織固有のOR Mapper
- 一般的なWebサーバー / HTTPランタイム
- Spring / Spring BootやHibernate等の一般的なフレームワークを直接利用しているとは限らない
- OR Mapperは一般的なORMと近い概念を持つ可能性がある

一般論を推測で当てはめず、このリポジトリのコード、設定、サンプル、ドキュメント、テストを一次情報として扱ってください。

分からない独自記法が出た場合は、まずリポジトリ内を探索し、類似実装・定義元・呼び出し関係・設定・テストをたどって意味を確認してください。根拠のないAPI、annotation、設定値、フレームワーク仕様を創作しないでください。

## 1. 最初にリポジトリを理解する

コード変更を急がず、最初に以下を把握してください。

- ディレクトリ構成
- Gradleのproject / module構成
- Javaのpackage構成
- build / test / application起動方法
- Webアプリの入口
- routing / controller相当
- request / response
- 画面描画
- application / service相当
- entity / domain model
- OR Mapper
- transaction境界
- DB接続・初期化
- schema / migration / test data
- JUnit
- Playwright
- configuration / logging / exception handling / validation
- dependency injectionまたはオブジェクト生成
- フレームワーク固有annotation / DSL / configuration
- 推奨されていそうな典型実装

特に「1リクエストがどこから入り、どのコードを通り、DBへ到達し、どのようにレスポンスになるか」を追跡してください。

調査結果はChatだけに保持せず、後述する永続的なプロジェクトコンテキストへ残してください。

## 2. 変更前のベースラインを確認する

現在のサンプルアプリについて可能な範囲で以下を実行してください。

- clean
- build
- unit test
- application起動
- 既存画面またはendpointの動作確認

Gradle Wrapperがあればそれを優先してください。

既存状態のfailureは今回の変更によるfailureと混同しないよう記録してください。コードを理解する前に大規模なrename、refactoring、package再編、dependency更新を行わないでください。

## 3. 代表画面の仕様をテストとして先に表現する

私から与える画面仕様を整理し、「利用者から見てどう動けば完成か」をAcceptance Criteriaとして明文化してください。

実装より先にテストを設計します。

### Playwright

利用者視点の主要シナリオを表現してください。

例:

画面を開く
→ 初期表示
→ 値を入力
→ 操作
→ サーバーへリクエスト
→ DBを利用した処理
→ 結果が画面へ反映

まず「代表的な正常系1本」をGolden Pathとします。validation、error、0件、複数件、更新などは必要に応じて後から追加します。最初からケースを増やしすぎず、まずワンパスを成立させてください。

### JUnit

Playwrightより下位の責務をテストしてください。

既存アーキテクチャに合わせ、application/service相当、domain logic、validation、OR Mapperを利用したrepository相当、framework integrationなどから必要なテスト境界を判断してください。

テストしやすくするためだけに既存フレームワーク思想とかけ離れたarchitectureを持ち込まないでください。

## 4. Red → Green → Refactor

基本サイクル:

1. 小さな仕様を決める
2. テストを書く
3. 意図した理由で失敗することを確認する
4. 最小限の実装をする
5. テストを通す
6. 必要な範囲だけrefactorする
7. 全テストを再実行する
8. 学んだことを記録する
9. 次の小さな仕様へ進む

一度に大量のコードを生成せず、「今どのテストを通そうとしているのか」が分かる単位で変更してください。

## 5. 1画面を通して処理シーケンスを明らかにする

代表画面を実装しながら、概念上の次の流れが実際にはどう表現されているかを明らかにしてください。

Browser
→ HTTP Request
→ Web Framework
→ 画面 / Controller相当
→ Application / Service相当
→ OR Mapper
→ Database
→ Entity / Result
→ Application
→ Web Framework
→ HTTP Response
→ Browser

一般的な名称と実際の名称が異なる場合は、実際の名称を優先してください。

最終的には代表画面について、主要class / file / annotation / configurationを紐付けた処理シーケンスを説明できる状態にしてください。

## 6. 仕組みの出所を区別する

重要な仕組みについて以下を区別してください。

- Java 21標準
- Gradle
- 一般的なWeb / HTTP
- Webサーバー / HTTPランタイム由来
- プロジェクト固有Webフレームワーク
- プロジェクト固有OR Mapper
- 一般的なORM概念
- サンプルアプリ固有

特に独自記法は「この書き方は何者なのか」が分かるようにしてください。

## 7. リポジトリを人間とAIが継続開発しやすい状態へ育てる

今回限りのChat履歴に知識を閉じ込めないでください。

既存ルールを確認し、同じ目的のファイルを重複させず、必要に応じて以下を整備・更新してください。

### Repository Instructions

GitHub Copilotが常に知るべき情報はrepository-level instructionsへ。

候補: `.github/copilot-instructions.md`

内容例:

- システム目的
- 技術スタック
- project structure
- build / test / run
- coding conventions
- framework固有事項
- テスト方針
- 変更時のガードレール
- 参照すべきドキュメント

推測で埋めず、確認できた事実だけを書いてください。

### CONTEXT

目的、現在地、システム構造、重要な前提。

### TASKS

TODO / IN PROGRESS / DONEなどで現在地が分かる状態にし、完了事項を永遠にTODOとして残さないでください。

### DECISIONS

- 何を決めたか
- なぜそうしたか
- 他に何を検討したか
- 再検討条件

### LEARNINGS

独自annotation、routing、transaction、OR Mapper、典型パターン、ハマりどころなど、実作業で確認できた知識。

### WORKLOG

重要な作業について、実施内容、変更ファイル、主要command、test結果、判明事項、次の一手を、後で役立つ粒度で記録してください。

## 8. 再利用可能なPrompt / Skillへ昇格させる

繰り返す価値がある手順は、その場限りのChat指示で終わらせないでください。

候補例:

- 新しい画面を1本追加する
- フレームワークの処理シーケンスを解析する
- OR Mapperを使ったEntity追加
- Playwright E2E追加
- JUnit追加
- 新規メンバー向け環境確認
- build failure解析

利用可能なrepository customization機構を確認し、必要に応じてreusable prompt、path-specific instruction、custom agent、Skill等へ整理してください。

ただし最初から大量に作らず、一度実作業で繰り返す価値を確認したものから昇格させます。Prompt / Skill自体も実作業から継続的に改善してください。

## 9. 新規メンバーが参加できる状態を作る

少なくとも次の導線を明確にしてください。

新規clone
→ 前提確認
→ build
→ test
→ application起動
→ 代表画面確認
→ Playwright
→ JUnit

既存方式を尊重し、勝手なDocker化や大規模な環境刷新は行わないでください。

## 10. 私との協働ループ

今後、私が自然言語で仕様や変更内容を伝えます。その都度:

1. 現在のコードと永続コンテキストを確認
2. 要求を既存architectureへ当てはめる
3. 影響範囲を調査
4. 必要なテストを先に定義
5. 小さく実装
6. test
7. 必要なrefactor
8. CONTEXT / TASKS / DECISIONS / LEARNINGS等を更新

過去に決めたことを毎回ゼロから再考しないでください。ただし、新しい知識と矛盾した判断は根拠を示して更新してください。

## 11. 実装原則

- 既存フレームワークの思想・規約を最優先
- サンプルコードの典型パターンを尊重
- 根拠なく一般フレームワーク流を持ち込まない
- 独自APIを推測で作らない
- 不明点はまずコードベースを検索
- 小さな変更単位を維持
- テスト可能な状態を維持
- unrelatedなrefactorを混ぜない
- 変更理由を説明可能にする
- build / test failureを放置しない
- workaroundは理由を記録
- 仮定を事実として永続化しない
- public repositoryへ顧客情報、認証情報、組織固有の秘密情報を持ち込まない

## 最初に実施してほしいこと

まずリポジトリを調査し、本格実装前に以下を提示してください。

1. リポジトリ構造の理解
2. 起動・build・test方法
3. Webリクエストの大まかな処理シーケンス
4. プロジェクト固有フレームワークの主要な仕組み
5. OR Mapper利用箇所と基本的な使い方
6. 現在のテスト
7. Playwright導入状況
8. 代表画面1本を追加する場合の想定変更箇所
9. 開発ハーネスとして追加・改善したいrepository-levelの仕組み
10. 最初のTDDサイクルとして着手する最小単位

その後、重大な不明点がなければ、環境整備と最初のGolden Path実装まで継続してください。

途中で得た知識はその場限りにせず、リポジトリへ還元してください。

成功条件は「画面が1本動いた」だけではありません。

**この1本を通じて、このフレームワークで次の1本をより速く、安全に、人間とCopilotが協働して開発できる状態になったこと**を成功とします。
