# FDE Actor Requirement

## Modeling question

主体者がFDEによって何をできる状態を必要とし、そのためにどのような対策を置くか。

## Reading

左からActor、要求、対策を読む。要求は角丸四角、対策は角のある四角で表す。線は対応関係であり、Business Flowではない。

```mermaid
---
title: FDE Actor Requirement
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: true
    nodeSpacing: 44
    rankSpacing: 84
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
---
flowchart LR
  subgraph actor_lane[" "]
    direction TB
    a_maakbo_fde@{ label: "fde", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
    a_fde_ai@{ label: "fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
    a_subject@{ label: "主体者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/user.svg", pos: "b", w: 38, h: 38, constraint: "on" }
  end
  subgraph requirement_lane[" "]
    direction TB
    r_support(["現場の理解を支える"])
    r_agent_scope(["目的・範囲・必要情報が明確"])
    r_understand(["全体と関係を理解できる"])
    r_consider(["選択肢と影響を考えられる"])
    r_improve(["自分で選び改善できる"])
  end
  subgraph measure_lane[" "]
    direction TB
    m_shape["問いと関係を扱える形にする"]
    m_explicit["役割と制約を明示する"]
    m_visualize["関係を可視化する"]
    m_prepare["判断材料を整える"]
    m_handover["自分で扱える形へ整える"]
  end

  a_maakbo_fde --- r_support
  r_support --- m_shape
  a_fde_ai --- r_agent_scope
  r_agent_scope --- m_explicit
  a_subject --- r_understand
  r_understand --- m_visualize
  a_subject --- r_consider
  r_consider --- m_prepare
  a_subject --- r_improve
  r_improve --- m_handover

  class a_maakbo_fde,a_fde_ai,a_subject actor;
  class r_support,r_agent_scope,r_understand,r_consider,r_improve requirement;
  class m_shape,m_explicit,m_visualize,m_prepare,m_handover measure;

  classDef actor fill:none,stroke:none,color:#25231F;
  classDef requirement fill:#EDF2EA,stroke:#7C8975,color:#25231F,stroke-width:1px;
  classDef measure fill:#FFF7E8,stroke:#B79661,color:#25231F,stroke-width:1px;
  style actor_lane fill:none,stroke:none;
  style requirement_lane fill:none,stroke:none;
  style measure_lane fill:none,stroke:none;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## Boundary

主体者の三つの要求を中心に、FDEを担うActor側の役割上の前提と対策を最小限に置く。個別の実装、業務手順、AIの内部構成は扱わない。
