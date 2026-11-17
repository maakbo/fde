# システム開発

**システム開発という仕事の全体像（構成案）**。開発対象となる個別製品のアーキテクチャではなく、事業の意図と利用者のニーズを受け、関係者が協力して価値を生む仕事を捉えています。

## システムコンテキスト

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
  %% 全体の仕事のコンテキスト。左=価値を提供する役割、中央=仕事、右=価値を受ける役割。
  %% 目的は中央業務の右上に置く意図で、右側の要素のうち最初に定義・接続する。
  %% 方向は配置で伝える。実線は参加関係、点線は目的。時系列と情報の受渡しは次のView。
  a_business_owner@{ label: "事業責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_business_staff@{ label: "業務担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_pm@{ label: "PM", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_developer@{ label: "開発者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_system_development@{ label: "システム開発", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  p_purpose("事業の目指す姿や利用者のニーズを捉え、\n関係者とともに、価値を生むシステムを開発する。")
  a_user@{ label: "利用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_operator@{ label: "運用者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_business_owner --- b_system_development
  a_business_staff --- b_system_development
  a_pm --- b_system_development
  a_developer --- b_system_development

  b_system_development -.- p_purpose
  b_system_development --- a_user
  b_system_development --- a_operator

  class a_business_owner,a_business_staff,a_pm,a_developer,a_user,a_operator actor;
  class b_system_development business;
  class p_purpose purpose;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef purpose fill:#FFFFFF,stroke:#9E988E,color:#25231F,stroke-width:0.75px;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

事業責任者・業務担当者・PM・開発者が目的や知見、力を持ち寄り、利用者と運用者へ価値を届けます。運用者は受け取るだけでなく、継続的な価値提供と改善にも関わります。関係線は**参加・関与**を示し、工程順や一方向の受渡しを意味しません。役割の位置はこの場面の主要な価値関係であり、固定した組織境界を表しません。

**この一枚には情報・工程・具体的な外部システムを置きません**。外部システムが不要という意味ではなく、特定の接続先や開発方式を前提にしないためです。業務や情報の関係は下位のビューで整理します。引き渡して終わりではなく、運用・保守・改善による継続的な価値提供も視野に入れます。

> **下記は以前の題材による旧試作で、現在の合意に未対応です。** 申請・承認Webシステムと会計連携を含む具体的な設定、既存の10工程の整理は今回のシステム開発モデルの決定事項ではありません。後続図はこれから再検討します。

## ビジネスコンテキスト — 業務、関係者、情報のつながり

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
  a_user@{ label: "利用部門", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_it@{ label: "顧客IT担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_dev@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_test@{ label: "テスト担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_ops@{ label: "運用保守担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  x_accounting@{ label: "既存会計システム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_request@{ label: "開発要求", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirements@{ label: "合意済み要件", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "設計仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_results@{ label: "検証結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_handover@{ label: "運用引継ぎ", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_change@{ label: "変更要求", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_requirements@{ label: "要件を合意する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_design@{ label: "仕様を具体化する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_build@{ label: "実装する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_verify@{ label: "品質を検証する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_release@{ label: "受入・導入する", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_operate@{ label: "利用を支える", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_user --- b_requirements
  a_user --- b_release
  a_it --- b_requirements
  a_it --- b_design
  a_dev --- b_design
  a_dev --- b_build
  a_test --- b_verify
  a_ops --- b_release
  a_ops --- b_operate
  x_accounting ---|"連携先・結合試験"| b_verify

  i_request --- b_requirements
  i_requirements --- b_requirements
  i_requirements --- b_design
  i_design --- b_design
  i_design --- b_build
  i_design --- b_verify
  i_results --- b_verify
  i_results --- b_release
  i_handover --- b_release
  i_handover --- b_operate
  i_change --- b_operate
  i_change --- b_requirements

  b_requirements --- b_design
  b_design --- b_build
  b_build --- b_verify
  b_verify --- b_release
  b_release --- b_operate
  class a_user,a_it,a_dev,a_test,a_ops actor;
  class x_accounting external;
  class i_request,i_requirements,i_design,i_results,i_handover,i_change information;
  class b_requirements,b_design,b_build,b_verify,b_release,b_operate business;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef external fill:none,stroke:none,color:#5F5A52;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

業務名は、工程名の言い換えではなく**何を何に変えるか**で仮置きしています。線は、参加・情報の参照や作成・成果の受渡しの**関係**です。細かい時系列や分岐をこの図へ押し込まず、選んだ業務の[ビジネスユースケース](basic-design/README.md)と[業務フロー](basic-design/review-flow.md)で表現します。

この図の主要情報は、独立した[情報モデル](information-model.md)でも同じ意味・IDで扱います。下位モデルで情報や責任が変わったら、この図へ戻して更新します。

## フェーズ — 業務を探すための入口

フェーズは開発の進行を眺める**索引**です。意味上の分解は「仕事 → 業務 → 子業務 → 作業」。一つの業務は複数フェーズにまたがる場合があります。

| フェーズ | 関係する業務（上図） | 掘り下げ先 |
| --- | --- | --- |
| 要件定義 | 要件を合意する | [既存As-Is](../requirements/) |
| 基本設計 | 仕様を具体化する | **[ビジネスユースケースを展開](basic-design/README.md)** |
| 詳細設計 | 仕様を具体化する | [既存As-Is](../detailed-design/) |
| 実装・単体テスト | 実装する・品質を検証する | [既存As-Is](../implementation/) |
| 内部結合テスト | 品質を検証する | [既存As-Is](../internal-integration/) |
| 外部結合テスト | 品質を検証する（既存会計との連携） | [既存As-Is](../external-integration/) |
| システムテスト | 品質を検証する | [既存As-Is](../system-test/) |
| ユーザー受入テスト | 受入・導入する | [既存As-Is](../user-acceptance/) |
| 導入 | 受入・導入する・利用を支える | [既存As-Is](../deployment/) |
| 運用・保守 | 利用を支える・変更を要件へ返す | [既存As-Is](../operations/) |

## 次に見る

**[基本設計のビジネスユースケース](basic-design/README.md)** → **[設計レビューの業務フロー（担当者別スイムレーン）](basic-design/review-flow.md)** ／ **[情報モデル](information-model.md)**

自分の業務に使う場合は、**[実案件への転用手順](USE.md)** から、AIエージェントと対話して仮モデルを作成・修正します。実業務の資料をこの公開リポジトリへ載せることは前提としません。

[従来のAs-Isへ戻る](../README.md)
