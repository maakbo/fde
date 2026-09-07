# 導入

本番へ安全に切り替え、業務利用を確認して運用へ責任を渡す場面です。

← [システム開発](business-map.md)

## モデル

```mermaid
---
title: 導入
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
  a_release_manager@{ label: "リリース責任者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  a_ops@{ label: "運用担当", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  i_release_scope@{ label: "リリース範囲", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_release_plan@{ label: "リリース計画", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_known_issue@{ label: "既知問題", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  b_decide_release@{ label: "実施判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_apply_production@{ label: "本番反映", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_verify_production@{ label: "本番確認", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_recover_safe_state@{ label: "切戻し", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_transfer_operation@{ label: "運用移管", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  x_cicd@{ label: "CI/CD", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_production_env@{ label: "本番環境", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  x_monitoring@{ label: "監視基盤", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/server.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_business_validation_result@{ label: "業務確認結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }
  i_runbook@{ label: "運用手順", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/file.svg", pos: "b", w: 32, h: 32, constraint: "on" }

  a_release_manager --- b_decide_release
  a_ops --- b_decide_release
  i_release_scope --- b_decide_release
  i_release_plan --- b_decide_release
  i_known_issue --- b_decide_release
  b_decide_release --- b_apply_production
  x_cicd --- b_apply_production
  x_production_env --- b_apply_production
  b_apply_production --- b_verify_production
  x_monitoring --- b_verify_production
  a_ops --- b_verify_production
  b_verify_production --- i_business_validation_result
  b_verify_production --- b_recover_safe_state
  i_business_validation_result --- b_transfer_operation
  i_runbook --- b_transfer_operation
  a_ops --- b_transfer_operation
  b_recover_safe_state --- a_release_manager
  b_transfer_operation --- a_ops

  click b_verify_production href "https://github.com/maakbo/fde/blob/eval/waterfall-system-development-modeling/examples/waterfall-system-development/deployment-flow.md" "本番確認の流れを見る"

  class a_release_manager,a_ops actor;
  class b_decide_release,b_apply_production,b_verify_production,b_recover_safe_state,b_transfer_operation business;
  class i_release_scope,i_release_plan,i_known_issue,i_business_validation_result,i_runbook information;
  class x_cicd,x_production_env,x_monitoring external;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef business fill:none,stroke:none,color:#25231F;
  classDef information fill:none,stroke:none,color:#5F5A52;
  classDef external fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 図の業務

| 業務 | 何をしているか |
| --- | --- |
| **実施判断** | 対象範囲・計画・既知問題を見て、本番変更を始めてよいか判断する。 |
| **本番反映** | 合意した版・設定・移行内容を本番環境へ反映する。 |
| [**本番確認**](deployment-flow.md) | 技術疎通と重要業務を確かめ、切替を継続できるか判断する。 |
| **切戻し** | 継続できないとき、旧状態へ戻して安全性とデータ整合を回復する。 |
| **運用移管** | 利用可能と確認した変更を、既知問題と運用手順ごと運用へ渡す。 |

## この図が表していること

導入は「デプロイが成功したら終わり」ではありません。実施判断、本番反映、業務利用確認、必要なら切戻し、最後に運用責任を移すところまでを一つの場面として見ています。

## 関連

- [本番確認の流れ](deployment-flow.md) →
- [Actor](master-actor-map.md)
- [Information](master-information-model.md)
- [External System](master-system-map.md)
