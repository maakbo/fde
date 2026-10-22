# リリース・運用保守

検証した版を本番へ反映し、利用できる状態を維持する仕事です。

## 本番へ届け、稼働を支える

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
  %% parent: ../README.md / b_operate
  a_team@{ label: "開発チーム", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_ops@{ label: "運用担当者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_results@{ label: "テスト結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_prepare@{ label: "リリース準備", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_operation@{ label: "運用手順書", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_release@{ label: "本番リリース", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  x_prod@{ label: "本番環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/server.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_maintain@{ label: "運用保守", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_incident@{ label: "障害・変更依頼", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_team --- b_prepare
  a_team --- b_release
  a_team --- b_maintain
  a_ops --- b_prepare
  a_ops --- b_release
  a_ops --- b_maintain
  i_results --- b_prepare
  b_prepare --- i_operation
  i_operation --- b_release
  i_operation --- b_maintain
  b_release --- x_prod
  x_prod --- b_maintain
  b_maintain --- i_incident

  class a_team,a_ops actor;
  class i_results,i_operation,i_incident information;
  class b_prepare,b_release,b_maintain business;
  class x_prod external;
  classDef actor fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

開発チームが移行と切戻しを準備し、運用担当者が監視・問い合わせ・障害対応を引き継ぎます。

## 本番へ反映する前後の仕事

リリース準備では、反映する版、テスト結果、移行データと手順、作業時間、切戻し条件、利用者への案内を揃えます。関係者が実施可否を判断できる状態にし、確認してから本番へ反映します。反映後は、注文登録や照会などの主要操作、監視、データの整合を確認します。

運用手順書には監視項目、問い合わせ先、一次対応、復旧・切戻しの方法を残します。障害が起きたら、症状、影響、対象版、直前の変更を確認し、復旧と原因調査を進めます。対応で分かった問題は、障害・変更依頼として次の要件や実装へ戻します。

## AIエージェントの導入候補

リリース対象の差分とテスト結果から確認漏れを挙げ、運用では許可されたログ・手順・変更履歴から原因候補を調べてもらえます。本番操作と復旧方針は権限を持つ担当者が決めます。初動時間だけでなく、誤った原因候補や復旧の負担も観測します。

[システム開発の全体](../) / [次の要求を整理する](../requirements/)

<!--
## Master references

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| `../people.md` | `a_team` | 開発チーム | 本文に示す担当・入出力・利用先 |
| `../people.md` | `a_ops` | 運用担当者 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_results` | テスト結果 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_operation` | 運用手順書 | 本文に示す担当・入出力・利用先 |
| `../environments.md` | `x_prod` | 本番環境 | 本文に示す担当・入出力・利用先 |
| `../deliverables.md` | `i_incident` | 障害・変更依頼 | 本文に示す担当・入出力・利用先 |
-->
