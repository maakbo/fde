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
  %% 全体の参加関係。b_fde を3場面に分け、対象業務選定・業務定義・協働設計・協働検証・現場導入と改善を本文に置く。
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

### 業務定義

対象の業務について、誰が関わり、何を受け取り、何を判断し、誰に何を渡すかを確かめます。前後の仕事との関係も含め、目的、関係者、作業、情報、システム、判断のつながりを業務構造図にまとめます。

熟練者の勘や例外への対応は、具体的な事例をもとに言葉にします。同じ仕事でも判断が異なるときは、その背景を聴き、共通にすることと、それぞれに委ねることを話し合います。

関係者と実装担当者、必要な専門家で、今回変える範囲、必要な機能、品質や速度、利用できる情報、法令や社内ルールなどの条件をそろえます。仕事がどう変わればよいか、何を確かめれば導入に進めるかを合格基準として決めます。

業務構造図、判断基準や例外、期待する変化と合格基準を、協働の設計へ引き継ぎます。

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
  %% AI導入を前提にしない。協働設計・協働検証と、検証後の見直し・中止の判断は直後の本文で扱う。
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

業務変更方針をもとに役割と責任を定め、小さく動く仕組みをつくります。使う人の実感と検証結果から、導入するかを関係者で判断します。

### 協働設計

人、AI、RPA、既存システムの役割と責任を決めます。人の強みをどう活かすか、AIに何を任せるか、誰が結果を確かめるかを、実際の仕事に合わせて考えます。

役割と責任、情報の受け渡しを協働仕様にまとめます。AIを使う部分では、次の事項を具体化します。

- 文脈と入出力：目的、前提、制約、参照情報、判断例。受け取る情報と返す情報、形式と内容の検証方法。
- 起動と接続：人の指示や定時実行などの起動条件。知識、文書、外部システムへの接続先と方法。
- 判断と権限：人が確認・承認・介入する箇所。参照・実行できる範囲と、禁止する操作。
- 検証と安全性：試す場面と評価方法。セキュリティ、法務、倫理上の条件。

JSONなどの出力形式や、RAG・MCP・APIなどの接続方法は、必要に応じて選びます。複雑な判断は抽出、照合、評価などに分け、判断の根拠や人に戻す条件を明確にします。専門的な条件は、必要な専門家と確認します。

[根拠を揃えて調査し、小さく試す実践](../system-development/knowledge-assisted-investigation.md)では、参照知識の更新と、品質・利用・効果を分けた確認を一件でたどれます。

### 協働検証

協働仕様に沿った試作品で動作を確かめ、実際の仕事に近い場面で、業務に使えるかを検証します。試作品（Prototype）、実現性や効果の検証（PoC）、価値を届ける最小限の仕組み（MVP）は、確かめたいことに応じて使い分けます。

本番のデータや権限に影響を与えにくい環境で、次の点を確認します。

- 業務への効果と使い心地：期待した変化があるか。大切にしたいことを守れ、関係者が無理なく納得して使えるか。
- 品質と負担：精度、速度、例外への対応。人が確認する負担や、前後の仕事への影響。
- 安全性と継続性：権限や情報の扱い、再現性、利用料と運用コスト。

評価内容と使う人の実感を協働検証結果にまとめます。合格基準と照らし合わせ、導入へ進む、今回は進めない、対象・設計・手段を変えて再検証する、のいずれかを関係者で決めます。AIを使わない方法も含めて選び、判断の根拠と次に確かめることを残します。

検証で業務の条件や役割分担に不足が分かれば、業務定義や協働設計に戻ります。

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

検証を通った仕組みを限られた範囲で使い、主体者と関係者が運用と改善を担えるようにします。

### 現場導入・改善

担当者や範囲を限定して使い始め、普段の仕事とのずれを直します。処理件数などの実績と、業務や人に起きた変化を分けて確かめます。

時間や品質、顧客に届いた価値に加え、やりたい仕事に時間を使えているか、判断しやすくなったか、負担が誰かに偏っていないかを聴きます。本人たちの実感と業務や事業の成果を照らし合わせ、組織と関係者が目指した状態に近づいているかを振り返ります。短期間で分かる変化と、時間をかけて追う成果は分けて扱います。

現場で得た経験や判断を協働仕様に反映し、実際の仕組みやプロンプトも更新します。判断基準、例外対応、変更手順を業務運用基準として共有します。運用、判断、変更の担当を決め、必要な教育や周知を行い、主体者と関係者が自分たちで改善を続けられるようにします。

同じ仕組みを使う人や範囲を広げることと、処理能力の増強、新機能の追加、別業務への適用は分けて判断します。新たに関わる人の事情や仕事も確かめ、必要なら対象業務選定からやり直します。目指すことや関係者の状況が変わったときも、取り組む対象を見直します。

使える仕組みと判断の根拠を残し、状況や思いの変化に合わせて、自分たちの仕事を育てていきます。
