# 業務理解・対象選定

```mermaid
---
config:
  layout: dagre
  theme: neutral
  flowchart:
    curve: basis
    diagramPadding: 40
    htmlLabels: true
    nodeSpacing: 64
    rankSpacing: 80
    padding: 8
  themeVariables:
    background: "#FFFFFF"
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart LR
  %% 親: b_fde。対象の見極めと業務の定義を、一つの話し合いの場面としてまとめる。
  %% a_participants は主体者と仲間・関係者、a_support は fde と fdeAI の集約。各場面で同じ意味。
  %% 関連線は参加・情報の参照や共有。対象業務選定と業務定義の進め方・判断条件は直後の本文で扱う。
  %% 主体者は業務理解と方針策定の参加者であり、その成果を使う受け手として右に置く。
  %% 組織方針と関係者背景・意向は別の情報。両者の一致を前提にせず、各人の事情や経緯も残す。
  %% 業務構造図は目的、関係者、作業、情報、判断を扱う。業務変更方針は変更範囲・理由・期待する変化を含む。
  i_organization_policy@{ label: "組織方針", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_participant_context@{ label: "関係者背景・意向", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_support@{ label: "fde・fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_understand@{ label: "現行業務理解", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_business_model@{ label: "業務構造図", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_select@{ label: "業務変更方針策定", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_change@{ label: "業務変更方針", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_participants@{ label: "主体者と関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_understand --- a_participants
  b_select --- a_participants
  i_organization_policy --- b_understand
  i_participant_context --- b_understand
  a_support --- b_understand
  a_support --- b_select
  b_understand --- i_business_model
  i_business_model --- b_select
  b_select --- i_change

  class a_participants,a_support actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  class b_understand,b_select business;
  classDef business fill:none,stroke:none,color:#25231F;
  class i_organization_policy,i_participant_context,i_business_model,i_change information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

組織方針と関係者の背景をもとに、取り組む対象を選び、業務の範囲と判断条件を定めます。

### 対象業務選定

使命やビジョンを含む組織方針と、その仕事が顧客や仲間に届けている価値を確かめます。関係者の背景や意向として、思い、事情、得意なこと、困りごと、これまでの経緯を聴き、続けたいことと変えたいことを話し合います。

実際の仕事をたどり、待ちや手戻り、繰り返し、特定の人に集中する作業や判断を確認します。なくす、まとめる、順番を変えるなどの方法を考え、人が担うか、ルールやRPA、AIを使うかを比較します。

最初に取り組む対象は、次の点から選びます。

- 目指す変化：組織の目指すことや、関係者が実現したいことにつながるか。守りたい仕事の良さや関係は何か。
- 効果：工数、品質、速度、顧客への価値がどう変わるか。関係者の負担や役割にどんな影響があるか。
- 実現可能性：必要な情報や知識、技術、協力が得られるか。
- リスクと適性：正確性、情報の扱い、法令、業務への影響を踏まえ、その手段に任せられるか。

共感そのものに価値がある仕事や、AIに渡せない情報を扱う仕事などは、人が担う範囲を確かめます。対象と選んだ理由、期待する変化、守りたいことを業務変更方針として共有します。


顧客の業務責任者・担当者とFDEが、現行の仕事と課題を照合し、最初に取り組む対象を選びます。業務の詳しい条件は、選定した根拠とともに業務要件定義へ渡します。

[顧客と進める手順](workflow.md) / [次：業務要件定義](../planning/README.md) / [FDEの仕事全体](../README.md)
