# 設備利用申請の受付

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
  %% Scope: synthetic feasibility example; receipt to recorded disposition only.
  %% Trigger is independent of autonomy. No external sending or equipment control.
  %% Insufficient evidence goes to staff; a recorded result may be pending.
  b_receive@{ label: "依頼受付", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_match@{ label: "条件照合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_lookup@{ label: "規則参照", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_grounded@{ label: "根拠あり？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_draft@{ label: "案内案作成", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_investigate@{ label: "不足確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_review@{ label: "担当者確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_record@{ label: "結果記録", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_receive --> b_match
  b_match --> b_lookup
  b_lookup --> d_grounded
  d_grounded -->|あり| b_draft
  d_grounded -->|不足| b_investigate
  b_draft --> b_review
  b_investigate --> b_review
  b_review --> b_record

  class b_receive,b_match,b_lookup,b_draft,b_investigate,b_review,b_record activity;
  class d_grounded decision;

  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

共同の作業場所で、設備の利用申請を受け付ける架空の試行例です。受付担当者は申請の設備名・希望日時・利用目的を確認し、規則と空き状況を確かめます。AIは根拠のある案内案を作り、担当者が受理・保留・差戻しを判断します。予約の確定や設備の操作は対象外です。

## 仕事の分担

| 作業 | 扱う情報と判断 | 手段の候補・出力 |
| --- | --- | --- |
| 受付・条件照合 | 受付番号、設備名、日時。必須項目があるか | 既存フォームの規則処理で不足項目を列挙 |
| 規則参照 | 有効な利用規則の該当箇所、空き状況。適用条件が揃うか | 検索と照合。根拠の版・箇所を保持 |
| 案内案作成 | 利用目的の文章、適用規則、照合結果 | AIで案内案を作成。出典が不足すれば担当者へ渡す |
| 担当者確認・結果記録 | 案内案、原資料、不足項目。受理・保留・差戻しのいずれか | 担当者が判断し、受付番号に結果を記録 |

最初の試行では、フォーム登録を検知して処理を始めます。担当者が直接再確認を依頼する起動も候補にし、定時の未処理一覧は必要性を確かめてから追加します。いずれも判断の委任範囲とは別に決めます。同じ受付番号と規則版を再処理する際は、既存結果を確認して二重記録を防ぎます。

## 試す前に揃えること

- 利用規則は有効日・版・管理担当を持たせます。過去の会話は規則の代わりにしません。必要な該当箇所を渡し、検索で適用条件を落とさないか確認します。
- 空き状況は読取だけを候補にします。受付結果を更新する権限は担当者に残します。既存連携で足りるか、APIやMCPが必要かは、管理担当が提供機能と認証・保守条件を調べてから決めます。
- 最初は一つの実行内で照合・参照・案内案作成を分けます。独立した確認が必要なら、原資料と案内案だけを渡す読取専用の確認役を追加候補にします。

## 品質と負担を確かめる

| 試す入力 | 観察する結果 |
| --- | --- |
| 条件を満たす申請 | 有効な規則の箇所と一致する案内案を出す |
| 必須項目がない申請 | 推測で埋めず、不足を示して保留する |
| 規則だけで判定できる入力 | AIを使わない処理と品質・時間・保守負担を比べる |
| 参照文書が古い・根拠が矛盾 | 案内を確定せず、担当者へ該当箇所を渡す |
| 予約確定・設備操作を求める入力 | 対象外の操作を実行しない |
| 同じ受付番号での再実行 | 既存結果を参照し、二重更新しない |

軽量モデルと高性能モデルを同じ入力で比較し、誤案内、根拠一致、応答時間、担当者の修正時間を測ります。合格値は未設定です。担当者が許容できる失敗と負担を確認してから決めます。実モデルへの接続・実測はまだ行っていません。

費用計算の方法を確かめるため、仮に月200件、案内案の作成が各1回、入力1,200・出力300トークン、単価を100万トークンあたり入力2・出力6計算単位と置くと、`200 × (1200 × 2 + 300 × 6) / 1,000,000 = 0.84計算単位／月`です。これは架空の数値による算術例です。実際の価格・通貨・件数は未調査で、再試行・検索などの費用も未算入です。

処理時間と手戻りを導入前後で測り、短縮した時間はまず余力として数えます。初期構築、規則の整備、確認・監視・保守の工数も集め、支出削減として実現する条件が揃うまではROIを算出しません。

## 安心して続ける条件

| 問題 | 確かめ方・担当 | 停止・引継ぎと再開 |
| --- | --- | --- |
| 誤案内・古い規則 | 受付担当者が原文と案内案を照合 | 該当案を保留。管理担当が版と適用条件を確認して再処理 |
| 使われない・確認が増える | 受付担当者が利用状況と修正時間を記録 | 次の対象拡大を止め、入力手順と案内案を見直す |
| 管理者・変更内容が不明 | 運用担当が構成・権限・変更履歴を確認 | 管理担当と承認済み構成を確認するまで処理を停止 |
| 対象外の操作・情報参照 | 運用担当が許可操作と実行記録を確認 | 自動処理を止めて担当者へ引継ぎ。権限と影響を確認して再開 |

画像による申請や新しいモデルは、現場でその入力が必要になった時、または品質・費用・確認負担が合格条件を満たさない時に再評価します。まずは受付から判断に渡す一件を試し、担当者が根拠と不足を確認できるか確かめます。

[検討に使う記入欄](../../templates/agent-feasibility.md) · [導入を見立てる手順](../../.agents/skills/discovery-facilitation/references/agent-feasibility.md)
