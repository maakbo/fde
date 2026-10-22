# システム開発の仕事を、要件定義から運用保守までたどる

システム開発は、業務上の要求を、使い続けられるソフトウェアにする仕事です。

## 開発を進める人と成果物

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
  a_user@{ label: "業務担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_team@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_request@{ label: "開発要求", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_requirements@{ label: "要件定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_design@{ label: "基本設計・詳細設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_build@{ label: "実装・単体テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_test@{ label: "結合・総合・受入テスト", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_operate@{ label: "リリース・運用保守", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_requirements@{ label: "要件定義書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_design@{ label: "設計書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_code@{ label: "ソースコード", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_results@{ label: "テスト結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_ops@{ label: "運用担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_user --- b_requirements
  a_user --- b_test
  a_user --- b_operate
  a_team --- b_requirements
  a_team --- b_design
  a_team --- b_build
  a_team --- b_test
  a_team --- b_operate
  i_request --- b_requirements
  b_requirements --- b_design
  b_design --- b_build
  b_build --- b_test
  b_test --- b_operate
  b_requirements --- i_requirements
  b_design --- i_requirements
  b_test --- i_requirements
  b_design --- i_design
  b_build --- i_design
  b_test --- i_design
  b_build --- i_code
  b_test --- i_code
  b_test --- i_results
  b_operate --- i_results
  b_design --- a_ops
  b_operate --- a_ops
  click b_requirements href "https://github.com/maakbo/fde/blob/main/examples/system-development/requirements/README.md" "requirements"
  click b_design href "https://github.com/maakbo/fde/blob/main/examples/system-development/design/README.md" "design"
  click b_build href "https://github.com/maakbo/fde/blob/main/examples/system-development/implementation/README.md" "implementation"
  click b_test href "https://github.com/maakbo/fde/blob/main/examples/system-development/testing/README.md" "testing"
  click b_operate href "https://github.com/maakbo/fde/blob/main/examples/system-development/release-and-operations/README.md" "release-and-operations"
  class a_user,a_team,a_ops actor;
  class i_request,i_requirements,i_design,i_code,i_results information;
  class b_requirements,b_design,b_build,b_test,b_operate business;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

業務担当者、開発チーム、運用担当者が、何を決め、どんな成果を受け渡しているのかを見ていきます。

## システム開発で、何を決めていくのか

開発を始める時点では、利用者の要望がそのまま実装できる形になっているとは限りません。「入力の手間を減らしたい」という話から、誰が何を入力し、どこで確認し、何をもって完了するかを確かめます。要件定義で決めたことを設計へ、設計をコードとテストへつなぎ、業務で使えることを確かめて本番へ届けます。

ここでは架空の受注管理システムを例にします。営業担当者が注文を登録し、進捗を確認できる仕組みを開発します。要件定義から運用までを見渡しますが、各段階を一度ずつ終える進め方に限定しません。テストや利用者との確認で分かったことは、要件や設計へ戻します。開発チームには要件・設計・実装・テストを担う人を含み、役割の分担や兼任はチームで変わります。

| 業務 | 主に決めること・行うこと | 次へ渡す成果 |
| --- | --- | --- |
| [要件定義](requirements/) | 業務の課題、利用者、対象範囲、必要な機能と品質を合意する | 要件定義書、受入条件 |
| [基本設計・詳細設計](design/) | 画面・API・データと、内部の処理・例外を具体化する | 設計書、実装・テストの判断材料 |
| [実装・単体テスト](implementation/) | 設計をコードにし、処理単位の動作を確かめる | ソースコード、単体テスト、レビュー結果 |
| [結合・総合・受入テスト](testing/) | 接続、システム全体、利用者の業務を確かめる | テスト結果、不具合と対応判断 |
| [リリース・運用保守](release-and-operations/) | 本番への反映、監視、障害対応、改善を続ける | 稼働するシステム、運用手順、次の変更依頼 |

## 要件定義から運用保守まで

### 要件定義

「何を作るか」を、業務担当者と開発チームで合意する仕事です。受注管理なら、注文の登録・変更・照会を誰が行い、どの情報を必要とするかを確かめます。画面の要望だけでなく、現在の二重入力や確認漏れがどこで起きるかを聞きます。

機能要件には注文登録や検索などを、非機能要件には応答性能、権限、可用性、運用上の条件などを整理します。要求の理由、対象外、まだ決められていないことも残します。詳しくは[要件定義](requirements/)へ。

### 基本設計・詳細設計

基本設計では、利用者や他システムから見た振る舞いを決めます。注文登録画面の項目やエラー表示、APIの入出力、データの関係などです。詳細設計では、それを実現する内部の責務、処理順序、トランザクション、例外処理などを具体化します。

設計書の名前や分け方は現場によって異なります。大切なのは、実装する人とテストする人が、同じ振る舞いを思い描けることです。[設計の具体例](design/)では、注文登録を通して境界を確かめます。

### 実装・単体テスト

開発者は設計と既存コードを確認し、変更する箇所を決めます。コードを書き、正常時だけでなく入力不足や失敗時も単体テストで確かめ、レビューで変更理由と検証結果を共有します。設計の不足に気づいたら、推測で埋めず確認して戻します。

[実装・単体テスト](implementation/)では、作業の受取りから修正・再実行までを一件たどれます。

### 結合・総合・受入テスト

結合テストでは、画面とAPI、APIとDBなどの接続を確かめます。総合テストでは、注文登録から検索・表示までをシステムとして動かし、非機能の条件も確認します。受入テストでは、業務担当者が実際に使う手順で目的を満たせるかを判断します。

見つかった問題は、実装の不具合、設計の不足、要件の認識違いで戻り先が異なります。[テストの進め方](testing/)で、根拠と結果のつなぎ方を見ます。

### リリース・運用保守

テストが通っただけで開発は終わりません。反映する版、データ移行、切戻し、利用者への案内、監視と問い合わせ先を揃え、本番へ反映します。稼働後は障害や利用状況を確認し、修正・改善を次の開発要求へつなげます。[リリース・運用保守](release-and-operations/)へ。

## AIエージェントを入れるなら

開発チームが時間を使っている仕事と、その理由から導入箇所を選びます。次はこの架空例で検討する候補であり、効果の実測結果ではありません。

| 課題 | エージェントが進める仕事 | 人が判断すること・確かめる効果 |
| --- | --- | --- |
| 影響調査に時間がかかる | 要件、設計書、コード、テストを検索し、変更箇所と影響候補を根拠付きでまとめる | 対象範囲と未確定仕様を判断。調査時間だけでなく見落とし・確認負担も見る |
| 実装とテストの往復が重い | 合意した条件からテストとコードを作り、実行し、失敗を調べて修正する | 設計の採否と差分をレビュー。[一件を任せる例](implementation/agent-assisted-flow.md)で進め方を見る |
| レビュー前の確認がばらつく | 差分と仕様を照合し、テスト不足や矛盾を挙げ、指摘への修正と再検証を進める | 指摘の妥当性と合格を判断。レビュー負担と流出不具合を観測する |
| 障害調査が担当者に依存する | 許可されたログ・手順・変更履歴を調べ、原因候補と確認手順をまとめる | 対応方針と本番操作を判断。初動、誤判断、復旧の負担を確かめる |

[関係者](people.md)・[成果物](deliverables.md)・[開発環境](environments.md)の用語は、各業務で共通に使います。

<!--
## Master references

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| `people.md` | `a_user` | 業務担当者 | 本文に示す担当・入出力・利用先 |
| `people.md` | `a_team` | 開発チーム | 本文に示す担当・入出力・利用先 |
| `deliverables.md` | `i_request` | 開発要求 | 本文に示す担当・入出力・利用先 |
| `deliverables.md` | `i_requirements` | 要件定義書 | 本文に示す担当・入出力・利用先 |
| `deliverables.md` | `i_design` | 設計書 | 本文に示す担当・入出力・利用先 |
| `deliverables.md` | `i_code` | ソースコード | 本文に示す担当・入出力・利用先 |
| `deliverables.md` | `i_results` | テスト結果 | 本文に示す担当・入出力・利用先 |
| `people.md` | `a_ops` | 運用担当者 | 本文に示す担当・入出力・利用先 |
-->

[受注一覧の機能追加を進めた架空例](../field-delivery/order-search/README.md)では、要件定義から設計・実装・テスト・レビュー・リリース準備へ、AIと成果を引き継いだ結果を確認できます。
