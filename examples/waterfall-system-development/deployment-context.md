# 本番変更を安全に業務へ渡す — Business Use Case Context

導入を、単なる本番配備ではなく、Go / No-Go 判断から切替、確認、必要時の復旧、運用責任移管までを含む scene として捉えます。

親 View: `business-map.md` / expanded node: `b_deployment`

```mermaid
---
title: 本番変更を安全に業務へ渡す
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

  b_decide_release@{ label: "実施を判断", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_apply_production@{ label: "本番へ反映", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_verify_production@{ label: "本番を確かめる", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_recover_safe_state@{ label: "安全状態へ戻す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_transfer_operation@{ label: "運用へ渡す", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

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

## 読み方

リリース責任者と運用担当が、対象範囲・計画・既知問題から実施可否を判断し、本番反映後は監視と重要業務確認によって継続可否を判断します。異常時は安全な状態へ戻し、正常に利用可能と確認できた変更だけを運用責任へ移します。

## Master references

- Actors: `a_release_manager`, `a_ops`
- Information: `i_release_scope`, `i_release_plan`, `i_known_issue`, `i_business_validation_result`, `i_runbook`
- External Systems: `x_cicd`, `x_production_env`, `x_monitoring`

## 次の問い

導入の完了点は「業務確認成功」か「運用責任移管」か、それとも初期流動監視の終了まで含めるべきか？
