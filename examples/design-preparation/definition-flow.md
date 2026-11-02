# レビュー依頼の資料照合

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
  %% 親View: README.md / b_prepare_design。設計をまとめる業務のレビュー依頼受付を展開。
  %% 変更案。根拠: definition-intake.md DEF-IN-v1。担当者の合意/実運用ではない。
  b_receive@{ label: "依頼を受ける", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_check@{ label: "資料を照合", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  d_ready@{ label: "資料は揃った？", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/diamond.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_return@{ label: "修正を頼む", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_handoff@{ label: "照合結果を返す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_receive --> b_check
  b_check --> d_ready
  d_ready -->|はい| b_handoff
  d_ready -->|いいえ| b_return
  b_return --> b_receive

  class b_receive,b_check,b_return,b_handoff activity;
  class d_ready decision;
  classDef activity fill:none,stroke:none,color:#25231F;
  classDef decision fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px,fill:none;
```

設計担当の依頼を受け、資料ID・版・未決欄を照合します。不足や版の矛盾があれば、箇所と理由を設計担当へ返します。訂正して再提出したら同じ照合から確かめ直します。資料が揃えば、照合結果を受付担当が確認できる形で返す変更案です。**揃ったことだけで受付済みにはしません。** 未決の受付可否や権限/担当の不足が残れば、結果は確認待ちとして返します。

| 担当役 | 何を見る/行う | 返すものと限界 |
| --- | --- | --- |
| 設計担当 | 依頼、設計書、要件/参照仕様のID・版・未決。指摘を訂正して再提出 | 依頼と根拠。実人の作業は未実施 |
| 受付担当 | 同じ版の根拠、不足/矛盾、未決の扱いを照合。受付可能か確認 | 照合結果または訂正依頼。未決の可否/権限を確認するまでは受付済みにしない |
| レビュー担当 | 受付結果、根拠版、未決と次の確認事項 | 次の枠調整へ。枠確保/レビュー実施はこの図の外 |

版が分からない、資料が不足/矛盾している時は「いいえ」へ戻します。正本の版を設計担当が確定できなければ、資料管理の決定者へ確認して待ちます。図の戻りは訂正後の再提出を表し、無期限の自動再試行ではありません。

図は資料照合の範囲です。その後、未決を含む依頼の受付可否と、確定/確認する人の権限・時間・アクセスを確かめ、成立した範囲をレビュー枠調整へ渡します。不成立なら該当判断を保留し決定者へ返します。図を行う受付担当そのものが不在なら、AIが代行して完了したことにせず、資料整理までで待ちます。

[親の設計業務](README.md)の一部を展開しています。受付済みは設計承認や開発着手の許可ではありません。人/通常ツール/AIの具体方式は未選択で、図は将来の業務要件案です。根拠は[架空の追加入力](definition-intake.md)、要件と確認条件は[実践結果](definition-result.md)へ。
