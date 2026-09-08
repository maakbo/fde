# システム開発 アクターマスタ

ウォーターフォール型システム開発に登場しうる Actor の初期候補です。肩書きの一覧を完成形とはせず、各 Context で「その Business に直接参加しているか」を確認して採用します。

## この評価で使う Actor

Contextで選択した候補だけを、reader-facingな短いlabelで並べています。詳しい責任範囲と境界の候補は下の辞書で確認します。関係がまだ確定していないため、線は引いていません。

```mermaid
---
title: この評価で使う Actor
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 64
    rankSpacing: 80
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#8A847A"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  a_business_user@{ label: "業務担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_ba@{ label: "要件担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_business_owner@{ label: "業務責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_developer@{ label: "開発者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_dev_lead@{ label: "開発PL", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_tester@{ label: "テスター", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_external_system_owner@{ label: "外部担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_release_manager@{ label: "リリース責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_ops@{ label: "運用担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }

  class a_business_user,a_ba,a_business_owner,a_developer,a_dev_lead,a_tester,a_external_system_owner,a_release_manager,a_ops actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

この短いlabelはこの評価での表示名です。辞書の役割説明を置き換えず、Contextでは同じIDで再利用します。

## Actor dictionary

| ID | Actor | 主な価値 / 責任 | 境界上の注意 |
| --- | --- | --- | --- |
| `a_customer_owner` | 顧客 / 発注責任者 | 投資・契約・最終判断を担う | 業務主管と同一人物の場合がある |
| `a_system_planning` | システム企画 | システム化構想、投資判断、全体方針を担う | 要件担当より上流の企画責任を持つことが多い |
| `a_business_owner` | 業務主管 / 業務責任者 | 業務成果、業務ルール、受入判断を担う | ユーザー代表と分離するか要確認 |
| `a_business_user` | ユーザー / 業務担当者 | 実業務を実行し、業務適合性を評価する | UATでは中心 Actor になりうる |
| `a_pm` | PM | 全体計画、進捗、費用、品質、意思決定を統合する | 発注側PMと開発側PMを分ける場合がある |
| `a_pmo` | PMO | 計画・実績・課題・会議体の統制を支援する | PMの責任そのものとは分ける |
| `a_dev_lead` | 開発PL | 開発チームの設計・実装・試験を統率する | アーキテクトとの責任境界を要確認 |
| `a_ba` | BA / 要件担当 | 要求を業務・システム要件へ構造化する | システム企画、業務主管との協働が中心 |
| `a_architect` | アーキテクト | 構造・非機能・技術方式・横断整合を担う | 基本設計だけでなく要件〜導入を横断する |
| `a_ux` | UI/UX担当 | 利用者行動を画面・操作設計へ変換する | 必須 Actor ではない |
| `a_developer` | 開発者 | 詳細設計をコードと単体検証へ変換する | 設計者と同一の場合がある |
| `a_test_lead` | テストリーダ | テスト戦略、計画、品質判断を統率する | QAとの責任を分ける |
| `a_tester` | テスター | 仕様に基づき検証し結果を記録する | 開発者が兼任する場合がある |
| `a_infra` | インフラ / クラウド担当 | 環境・ネットワーク・基盤構成を提供する | 対象システム開発チーム内外を確認する |
| `a_dba` | DBA / データ基盤担当 | DB構成、性能、保全を支援する | 専任不在ならアーキ / 開発へ統合しうる |
| `a_security` | セキュリティ担当 | セキュリティ要求・設計・試験・承認を支援する | 組織の審査部門の場合もある |
| `a_qa` | 品質保証 | 品質計画・レビュー・工程移行判断を独立視点で確認する | テスト実行主体とは限らない |
| `a_ops` | 運用 / 保守担当 | 運用可能性を確認し本番運用責任を引き受ける | 要件・設計段階から参加することが重要 |
| `a_release_manager` | リリース責任者 | 本番変更の調整、Go/No-Go、切替統制を担う | PM / 運用が兼任する場合がある |
| `a_external_system_owner` | 外部システム担当 | 接続先システムの仕様・試験・変更を担う | 外部結合では対等な協働相手になる |
| `a_external_vendor` | 外部ベンダ | 外部製品・サービス・委託範囲を担当する | 外部システム担当と同義にしない |
| `a_service_desk` | サービスデスク | 本番問い合わせ・一次受付を担う | 導入 / 運用移管で関係が強い |
| `a_change_authority` | 変更承認者 / CAB | 本番変更や重要変更の承認を担う | 組織により存在しない |

## Actor groups / same-type relations の初期仮説

これは組織図ではなく、モデル上の整理候補です。実際の組織構造として確定するまでは関係を固定しません。

### 事業・発注側候補
- 顧客 / 発注責任者
- システム企画
- 業務主管 / 業務責任者
- ユーザー / 業務担当者

### プロジェクト統制候補
- PM
- PMO
- 品質保証
- 変更承認者 / CAB

### 開発実行候補
- 開発PL
- BA / 要件担当
- アーキテクト
- UI/UX担当
- 開発者
- テストリーダ
- テスター
- インフラ / クラウド担当
- DBA
- セキュリティ担当

### 運用・リリース候補
- 運用 / 保守担当
- リリース責任者
- サービスデスク

### 外部協働候補
- 外部システム担当
- 外部ベンダ

## Context で必ず確認すること

1. 誰が Business を実行するか。
2. 誰が入力情報を提供するか。
3. 誰が判断・承認するか。
4. 誰が結果の価値を受け取るか。
5. 「レビュー参加者」と「Business の責任主体」を混同していないか。
6. 同じ肩書きでも発注側 / 開発側 / 運用側で責任が異ならないか。
7. 一人が複数ロールを兼務する場合、Actor を人ではなく責任として扱えているか。

## 特にレビューしたい Actor 境界

- システム企画と業務主管はどこで責任が分かれるか。
- PMと開発PLの「品質判断」「工程移行判断」はどちらの責任か。
- BAとアーキテクトの境界は要件 / 方式で明確に切れるか、それとも共同 Business が多いか。
- テストリーダと品質保証を別 Actor とする意味はあるか。
- 運用担当は導入時だけでなく、要件定義・基本設計から直接参加する Actor とすべきか。
