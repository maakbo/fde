# FDE

組織が目指すことと、そこで働く人たちの思いや背景が、日々の仕事の中でつながっている。自分たちの仕事にしっくりとした手触りがあり、それぞれが自然体で力を発揮できる。そんな心地よい仕事のあり方を、一緒に探り、育てていきます。

組織の使命やビジョンは、さまざまな仕事、業務、作業を通じて実現されます。その一つひとつに関係者がいて、それぞれの事情や積み重ねてきたストーリーがあります。人とAI、業務とシステムの関わりを整え、その人たちが自分たちらしく働き、やりたいことを実現できるようにします。

FDEは、そのための取り組みの一つです。現場に入り、対話を通じて仕事のつながりを捉え、AIエージェントやシステムと一緒に、日々の仕事をつくっていきます。

## FDEを担う人とAI

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
  %% 全体の参加関係。b_fde を以下の3場面と delivery-process.md で具体化する。
  %% FDEは取り組み全体、fdeは伴走する人、fdeAIはその協働を支えるAI。
  %% 主体者も仕事をつくる参加者。左右は指示・従属や判断権の移譲を表さない。
  a_fde@{ label: "fde", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_fde_ai@{ label: "fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_fde@{ label: "業務設計・改善", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_subject@{ label: "主体者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_companions@{ label: "仲間・関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_fde --- b_fde
  a_fde_ai --- b_fde
  b_fde --- a_subject
  b_fde --- a_companions

  class a_fde,a_fde_ai,a_subject,a_companions actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  class b_fde business;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

仕事を変えていく主体者と、前後の仕事を担う仲間や関係者が、思い、経験、困りごとを持ち寄ります。誰にとって何が変わるのかを話し合い、目指すことと大切にしたいことを共有します。

伴走する人を **fde**、その協働を支えるAIを **fdeAI** と呼びます。fdeは現場の話を聴き、仕事や判断のつながりを言葉や図にし、仕組みづくりをともに進めます。fdeAIは情報の整理、設計や実装、検証を支えます。何を変え、どう使うかは、主体者と関係者がfdeとともに確かめ、決めていきます。

## 業務を理解し、変化を決める

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
  %% 関連線は参加・情報の参照や共有。作業順序は delivery-process.md に分ける。
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

使命やビジョンを含む組織方針を確かめ、その仕事が誰に何を届けているかを話し合います。関係者の背景や意向として、思い、得意なこと、困りごと、これまでの経緯を聴き、共有します。目的、関係者、作業、情報、判断のつながりを、業務構造図にまとめます。

続けたいことと変えたいことを話し合い、変更する範囲と理由、期待する変化、守りたい関係や仕事の良さを業務変更方針にまとめます。この方針をもとに、協働の設計を進めます。


## 人とAIの協働をつくり、試す

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
  %% 親: b_fde。人とAIの協働設計から小さな検証まで。
  %% i_change は前の場面の業務変更方針。i_collaboration_spec は人・AI・システムの役割、入出力、権限、介入条件を定める情報。
  %% 協働仕様は動作する試作品そのものではない。仕様に基づく試作・実装を協働設計に含め、実際の動作を検証する。
  %% AI導入を前提にしない。検証後の見直し・中止の判断は本文と delivery-process.md に残す。
  a_participants@{ label: "主体者と関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_support@{ label: "fde・fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_change@{ label: "業務変更方針", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_design@{ label: "協働設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_collaboration_spec@{ label: "協働仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_verify@{ label: "協働検証", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_poc_result@{ label: "協働検証結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  a_participants --- b_design
  a_support --- b_design
  i_change --- b_design
  b_design --- i_collaboration_spec
  i_collaboration_spec --- b_verify
  a_participants --- b_verify
  a_support --- b_verify
  b_verify --- i_poc_result

  class a_participants,a_support actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  class b_design,b_verify business;
  classDef business fill:none,stroke:none,color:#25231F;
  class i_change,i_collaboration_spec,i_poc_result information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

業務変更方針をもとに、人が担うこと、AIやシステムに任せること、互いに確かめることを決めます。役割、入出力、権限、判断の根拠、人に戻す条件を協働仕様にまとめ、その仕様に沿って小さく動く仕組みをつくります。

実際の仕事に近い場面で使い、役に立つか、無理なく使えるか、大切にしたいことを守れているかを確かめます。精度や時間、コスト、使う人の実感を協働検証結果にまとめ、導入、見直し、中止を決めます。AIを使わない方法も含めて選びます。

## 現場で使い、ともに育てる

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
  %% 親: b_fde。限定導入、現場での調整、継続的な改善を扱う。
  %% i_collaboration_spec は前の場面と同じ協働仕様。現場での実際の動作に合わせて更新する。
  %% 業務運用基準は、現場の判断基準、例外対応、変更手順をまとめた情報。情報名は文書形式を指定しない。
  %% 業務運用基準を現場への調整に活用する関係を残す。関連線は時系列や自動実行を表さない。
  %% 主体者は参加者かつ価値の受け手として右に置く。線の順序を変えたら交差を再確認する。
  %% 主体者と関係者が運用・判断・変更を担えることは、目的を育て続けるための条件。
  i_poc_result@{ label: "協働検証結果", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_support@{ label: "fde・fdeAI", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_context_fit@{ label: "現場導入・調整", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_collaboration_spec@{ label: "協働仕様", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  i_knowledge@{ label: "業務運用基準", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/file.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  b_improve@{ label: "業務運用改善", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/ellipse.svg", pos: "b", w: 28, h: 28, constraint: "on" }
  a_participants@{ label: "主体者と関係者", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/maakbo/user.svg", pos: "b", w: 28, h: 28, constraint: "on" }

  b_context_fit --- a_participants
  i_poc_result --- b_context_fit
  a_support --- b_context_fit
  b_context_fit --- i_collaboration_spec
  i_collaboration_spec --- b_improve
  b_improve --- a_participants
  a_support --- b_improve
  i_knowledge --- b_improve
  b_context_fit --- i_knowledge

  class a_participants,a_support actor;
  classDef actor fill:none,stroke:none,color:#25231F;
  class b_context_fit,b_improve business;
  classDef business fill:none,stroke:none,color:#25231F;
  class i_poc_result,i_collaboration_spec,i_knowledge information;
  classDef information fill:none,stroke:none,color:#5F5A52;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

限られた範囲で使い始め、仕事や関係者にどんな変化があったかを確かめます。仕事が進みやすくなったか、やりたいことに時間を使えるか、誰かに負担が偏っていないか。本人たちの実感と、業務や事業の成果を照らし合わせます。

使う中で得た経験をもとに協働仕様を更新し、実際の仕組みやプロンプトにも反映します。現場の判断基準、例外への対応、変更手順を業務運用基準として共有し、運用や変更の担当を決めます。使える仕組みと判断の根拠を残し、主体者と関係者が、状況や思いの変化に合わせて自分たちの仕事を育てていきます。

具体的な手順と各段階の判断条件は、[FDEの進め方](delivery-process.md)で確認できます。
