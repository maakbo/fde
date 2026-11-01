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


## FDEの業務

顧客とFDEは、現場の仕事を理解し、変える対象と条件を決め、仕組みを設計・実装し、効果を確かめて運用へつなぎます。調査や試行で前提が変われば、対象や要件、設計へ戻ります。

| 業務 | 顧客とFDEが一緒に決めること | 次の業務へ渡す成果 |
| --- | --- | --- |
| [業務理解・対象選定](discovery/README.md) | どんな仕事を、なぜ変えるか | 現行業務、課題、改善対象と選定理由 |
| [業務要件定義](planning/README.md) | どこまで変え、何ができればよいか | 対象範囲、合格条件、責任と制約 |
| [協働設計](design/README.md) | 人・AI・システムでどう実現するか | 役割、情報、接続、処理と例外の設計 |
| [実装・テスト](implementation/README.md) | 設計をどう動く仕組みにするか | コード・設定、テスト結果、残件 |
| [PoC・導入評価](evaluation/README.md) | 現場で使えるか、何を直すか | 品質・利用・効果の評価と次の判断 |
| [導入・運用改善](operations/README.md) | 誰が使い、支え、改善し続けるか | 運用体制、利用手順、監視と改善の記録 |

対象選定時から費用・リスク・関係者の協力を確認し、合格条件は試行の前に決めます。運用担当者も設計や試行に参加します。六つの業務を毎回一律に最初から実施するのではなく、確認済みの成果を引き継ぎ、不足する作業を行います。

## 最初の相談

「どの業務にAIを使えばよいか」から相談できます。最近進めた仕事について、依頼を受けてから成果を渡すまでを、[業務理解・対象選定](discovery/workflow.md)で一緒にたどります。

例えば「設計レビューで、要件の確認漏れによる差戻しが多い」という相談なら、FDEは最近の設計を確認し、誰が何を見落とし、どこで分かったかを整理して返します。顧客がその理解を訂正し、AIによる要件照合などを候補として比較します。AIを使うことを最初の結論にはしません。

既に対象と要件が決まっている場合は、対応する業務から始められます。顧客がSkill名や帳票を選ぶ必要はありません。

[案件の実践例](../examples/README.md) / [成果物のフォーマット](../templates/README.md) / [リポジトリの入口](../README.md)
