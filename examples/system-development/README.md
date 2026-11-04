# BtoB Web業務システムの開発と運用

```mermaid
---
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
flowchart LR
  %% Overall context: 人が担う開発・運用の参加関係。工程の順序・成果物は下の各工程へ。
  a_business@{ label: "利用部門", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_customer_it@{ label: "顧客IT担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_pm@{ label: "PM", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_development@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_system_development@{ label: "開発・運用", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_test@{ label: "テスト担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_partner@{ label: "外部連携担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_operations@{ label: "運用保守担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_business --- b_system_development
  a_customer_it --- b_system_development
  a_pm --- b_system_development
  a_development --- b_system_development
  b_system_development --- a_test
  b_system_development --- a_partner
  b_system_development --- a_operations
  class a_business,a_customer_it,a_pm,a_development,a_test,a_partner,a_operations actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  class b_system_development business;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

法人顧客の利用部門が、申請・承認と会計への受渡しを日々の業務で使えるように、開発チームがWeb業務システムを作り、運用保守担当へ引き継ぎます。開発の仕事は、業務要求を合意し、設計・実装・検証を経て利用を開始し、その後も業務を継続できるよう支えることです。

**架空のAs-is（初版）**です。人手によるウォーターフォール型開発の一例として置いた前提であり、実在する現場の観察結果や全社共通の標準ではありません。AI導入対象や改善効果はまだ決めていません。

## 開発の前提

- 法人顧客から受託する新規開発。社員がブラウザから申請・承認し、既存の会計システムへ連携します。製品利用者の申請業務と、それを作る開発チームの仕事は別です。
- 要件定義から運用・保守までを対象とします。営業・契約締結は対象外、契約上の範囲・予算・納期は入力条件とします。技術製品、人数、工数、件数、期間は未設定です。
- 聞取り、文書作成、設計、コーディング、テスト項目作成・操作・判定、レビュー、承認、配置・移行、運用判断はすべて人が行います。生成AI、エージェント、自動テスト、自動デプロイは使いません。
- 文書・表計算、メール・会議、共有フォルダ、IDE・コンパイラ、Git、ブラウザ・DB操作ツールは人が操作する道具として使います。システム自体のプログラム処理まで手作業にする意味ではありません。
- 工程ごとの成果物をレビュー・承認して次工程へ渡します。テスト観点、環境、移行・運用の準備は前工程から始めます。指摘や変更が出れば、その原因の工程へ戻ります。

利用部門の業務責任者は業務要件と受入を判断し、業務担当者は具体例の提供と受入操作を行います。顧客IT担当は技術・運用制約と本番変更を管理し、PMは計画・進捗・課題・工程移行を調整します。開発チーム内の要件・設計・実装担当、テスト責任者、運用責任者は各工程で役割を分けます。同じ人が兼務するかは未設定です。外部連携担当は会計システム側の担当者と調整します。

## 要件から実装へ

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  %% parent: README.md / b_system_development ; 承認後の主経路。工程間の差戻し・変更・待ちはhandoffs.md。連続する区間は端の工程を共有する。
  b_requirements@{ label: "要件定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_basic_design@{ label: "基本設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_detailed_design@{ label: "詳細設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_implementation@{ label: "実装・単体テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_requirements --> b_basic_design
  b_basic_design --> b_detailed_design
  b_detailed_design --> b_implementation
  click b_requirements "https://github.com/maakbo/fde/blob/main/examples/system-development/requirements/README.md"
  click b_basic_design "https://github.com/maakbo/fde/blob/main/examples/system-development/basic-design/README.md"
  click b_detailed_design "https://github.com/maakbo/fde/blob/main/examples/system-development/detailed-design/README.md"
  click b_implementation "https://github.com/maakbo/fde/blob/main/examples/system-development/implementation/README.md"
  class b_requirements,b_basic_design,b_detailed_design,b_implementation activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

利用部門の要求を要件にまとめ、基本設計で外から見える振る舞い、詳細設計で内部処理を決めます。実装担当は承認された設計からコードを作り、単体で確認します。

[要件定義](requirements/) / [基本設計](basic-design/) / [詳細設計](detailed-design/) / [実装・単体テスト](implementation/)

## 結合から受入へ

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  %% parent: README.md / b_system_development ; 承認後の主経路。工程間の差戻し・変更・待ちはhandoffs.md。連続する区間は端の工程を共有する。
  b_implementation@{ label: "実装・単体テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_internal_integration@{ label: "内部結合テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_external_integration@{ label: "外部結合テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_system_test@{ label: "システムテスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_user_acceptance@{ label: "ユーザー受入テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_implementation --> b_internal_integration
  b_internal_integration --> b_external_integration
  b_external_integration --> b_system_test
  b_system_test --> b_user_acceptance
  click b_implementation "https://github.com/maakbo/fde/blob/main/examples/system-development/implementation/README.md"
  click b_internal_integration "https://github.com/maakbo/fde/blob/main/examples/system-development/internal-integration/README.md"
  click b_external_integration "https://github.com/maakbo/fde/blob/main/examples/system-development/external-integration/README.md"
  click b_system_test "https://github.com/maakbo/fde/blob/main/examples/system-development/system-test/README.md"
  click b_user_acceptance "https://github.com/maakbo/fde/blob/main/examples/system-development/user-acceptance/README.md"
  class b_implementation,b_internal_integration,b_external_integration,b_system_test,b_user_acceptance activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

単体確認済みの部品を内部で結合し、次に会計システムとの接続を確かめます。システム全体の要件を検証した後、利用部門が業務として受け入れられるか判断します。

[実装・単体テスト](implementation/) / [内部結合テスト](internal-integration/) / [外部結合テスト](external-integration/) / [システムテスト](system-test/) / [ユーザー受入テスト](user-acceptance/)

## 導入から運用へ

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: false
    nodeSpacing: 52
    rankSpacing: 52
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    primaryTextColor: "#25231F"
    edgeLabelBackground: "#FFFFFF"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  %% parent: README.md / b_system_development ; 承認後の主経路。工程間の差戻し・変更・待ちはhandoffs.md。連続する区間は端の工程を共有する。
  b_user_acceptance@{ label: "ユーザー受入テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_deployment@{ label: "導入", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_operations@{ label: "運用・保守", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_user_acceptance --> b_deployment
  b_deployment --> b_operations
  click b_user_acceptance "https://github.com/maakbo/fde/blob/main/examples/system-development/user-acceptance/README.md"
  click b_deployment "https://github.com/maakbo/fde/blob/main/examples/system-development/deployment/README.md"
  click b_operations "https://github.com/maakbo/fde/blob/main/examples/system-development/operations/README.md"
  class b_user_acceptance,b_deployment,b_operations activity;
  classDef activity fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

受入判定と本番作業の許可を得て導入します。運用保守担当が手順・構成・残件を受け取り、日々の確認と問合せ・障害・変更への対応を継続します。

[ユーザー受入テスト](user-acceptance/) / [導入](deployment/) / [運用・保守](operations/)

## 工程で変わる成果と受取者

| 工程 | 受け取るもの | 人が行う仕事 | 次へ渡すもの・受取者 |
| --- | --- | --- | --- |
| [要件定義](requirements/) | 開発依頼 | 顧客の業務と制約を、開発・受入で確認できる要求へまとめる。 | 承認済み要件、受渡し記録 → 基本設計担当 |
| [基本設計](basic-design/) | 承認済み要件 | 承認済み要件を、利用者と外部システムから見える振る舞いと構成へ変える。 | 承認済み基本設計、確認事項 → 詳細設計担当・テスト担当・運用担当 |
| [詳細設計](detailed-design/) | 承認済み基本設計 | 基本設計を、実装者が処理とデータ更新を判断できる具体的な設計へ変える。 | 承認済み詳細設計、実装対象一覧 → 実装担当・内部結合テスト担当 |
| [実装・単体テスト](implementation/) | 承認済み詳細設計 | 詳細設計どおりにコードを作成し、処理単位の振る舞いを確認する。 | 単体確認済みコード一式、版一覧 → 内部結合テスト担当 |
| [内部結合テスト](internal-integration/) | 単体確認済みコード | 開発対象のWeb・AP・DB・バッチを組み合わせ、内部の受渡しを確認する。 | 内部結合済みビルド、結果一式 → 外部結合テスト担当 |
| [外部結合テスト](external-integration/) | 内部結合済み版 | 境界の外にある会計システムと、合意したデータを正しく受け渡せるか確認する。 | 外部結合済み版、連携結果一式 → システムテスト担当 |
| [システムテスト](system-test/) | 外部結合済み版 | 完成したシステム全体が、機能・品質・運用の要件を満たすか確認する。 | 受入対象版、操作手順、試験結果 → 利用部門の受入担当・業務責任者 |
| [ユーザー受入テスト](user-acceptance/) | 受入対象版 | 利用部門が、自分たちの業務をシステムで遂行できるか確認し、受入可否を決める。 | 受入記録、利用開始条件 → 導入担当・運用担当 |
| [導入](deployment/) | 受入記録 | 受入済みのシステムとデータを本番へ移し、利用と運用を開始できる状態にする。 | 本番構成記録、運用引継ぎ記録 → 利用部門・運用保守担当 |
| [運用・保守](operations/) | 本番構成・引継ぎ記録 | 稼働状況を確認し、問合せ・障害・変更へ対応して業務利用を維持する。 | 完了または継続の記録、更新した手順 → 利用部門・次の運用当番・保守担当 |

工程の開始は、前工程の承認版と必要な環境・担当が揃った時です。成果物を送っただけでは受渡し完了にせず、受取側が版・対象・残件を確認します。承認待ち、外部環境待ち、指摘の修正、要件変更は[工程をまたぐ受渡しと変更](handoffs.md)で扱います。

## 現状を確かめる入口

各工程の作業と受渡しをたどり、実際の案件と違う担当・成果物・承認・戻り先を確かめます。頻度、作業時間、待ち時間、差戻し件数、困りごと、その理由はまだ観察していません。手作業があることだけで非効率やAI適合性を判断しません。

次の[業務理解・対象選定](../../work/discovery/workflow.md)では、このAs-isを基に一件の仕事を追い、課題の根拠を集めて改善候補を比較します。最初に確かめる問いは「一件の開発案件で、要件定義から運用・保守まで、各担当は実際に何を受け取り、何をして、どの判断を経て次へ進めていますか」です。
