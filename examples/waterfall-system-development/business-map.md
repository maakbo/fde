# システム開発

ウォーターフォール型システム開発を、13の大きな業務で俯瞰します。

このページを認識合わせの入口にします。図の業務を選ぶと、その業務の詳細へ進めます。図の直下には、各業務が何を整えるのかを日本語で並べています。

## モデル

```mermaid
---
title: システム開発
config:
  layout: elk
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
    lineColor: "#9E988E"
    fontFamily: "Inter, Hiragino Sans, sans-serif"
    fontSize: "14px"
  themeCSS: ".image-shape p { padding: 0 !important; background-color:#FFFFFF !important; } .image-shape foreignObject { overflow: visible; } .image-shape .labelBkg { background-color:#FFFFFF !important; } .image-shape .label rect { fill:#FFFFFF !important; opacity:1 !important; } .image-shape[id*='-flowchart-b_'] .label p { margin-top: -6px !important; } .image-shape g:first-child path { stroke:#FFFFFF !important; stroke-width:6px !important; }"
---
flowchart TB
  b_system_development@{ label: "システム開発", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_estimation@{ label: "見積", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_requirements@{ label: "要件定義", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_basic_design@{ label: "基本設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_detailed_design@{ label: "詳細設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_implementation_unit@{ label: "実装・単体", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_internal_test_design@{ label: "内結設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_internal_test@{ label: "内結試験", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_external_test_design@{ label: "外結設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_external_test@{ label: "外結試験", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_system_test_design@{ label: "ST設計", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_system_test@{ label: "ST", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_uat@{ label: "UAT", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }
  b_deployment@{ label: "導入", img: "https://raw.githubusercontent.com/maakbo/fde/main/assets/icons/lucide-thin/ellipse.svg", pos: "b", w: 30, h: 30, constraint: "on" }

  b_system_development --- b_estimation
  b_system_development --- b_requirements
  b_system_development --- b_basic_design
  b_system_development --- b_detailed_design
  b_system_development --- b_implementation_unit
  b_system_development --- b_internal_test_design
  b_system_development --- b_internal_test
  b_system_development --- b_external_test_design
  b_system_development --- b_external_test
  b_system_development --- b_system_test_design
  b_system_development --- b_system_test
  b_system_development --- b_uat
  b_system_development --- b_deployment

  click b_estimation href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#1-%E8%A6%8B%E7%A9%8D" "見積の分解を見る"
  click b_requirements href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/requirements-context.md" "要件定義を詳しく見る"
  click b_basic_design href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#3-%E5%9F%BA%E6%9C%AC%E8%A8%AD%E8%A8%88" "基本設計の分解を見る"
  click b_detailed_design href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#4-%E8%A9%B3%E7%B4%B0%E8%A8%AD%E8%A8%88" "詳細設計の分解を見る"
  click b_implementation_unit href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/implementation-unit-context.md" "実装・単体を詳しく見る"
  click b_internal_test_design href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#6-%E5%86%85%E9%83%A8%E7%B5%90%E5%90%88%E3%83%86%E3%82%B9%E3%83%88%E8%A8%AD%E8%A8%88" "内部結合テスト設計の分解を見る"
  click b_internal_test href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#7-%E5%86%85%E9%83%A8%E7%B5%90%E5%90%88%E3%83%86%E3%82%B9%E3%83%88" "内部結合テストの分解を見る"
  click b_external_test_design href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#8-%E5%A4%96%E9%83%A8%E7%B5%90%E5%90%88%E3%83%86%E3%82%B9%E3%83%88%E8%A8%AD%E8%A8%88" "外部結合テスト設計の分解を見る"
  click b_external_test href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/external-integration-context.md" "外部結合テストを詳しく見る"
  click b_system_test_design href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#10-%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%83%86%E3%82%B9%E3%83%88%E8%A8%AD%E8%A8%88" "システムテスト設計の分解を見る"
  click b_system_test href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#11-%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%83%86%E3%82%B9%E3%83%88" "システムテストの分解を見る"
  click b_uat href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/decomposition-catalog.md#12-%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E5%8F%97%E5%85%A5%E3%83%86%E3%82%B9%E3%83%88" "UATの分解を見る"
  click b_deployment href "https://github.com/maakbo/fde/blob/main/examples/waterfall-system-development/deployment-context.md" "導入を詳しく見る"

  class b_system_development,b_estimation,b_requirements,b_basic_design,b_detailed_design,b_implementation_unit,b_internal_test_design,b_internal_test,b_external_test_design,b_external_test,b_system_test_design,b_system_test,b_uat,b_deployment business;
  classDef business fill:none,stroke:none,color:#25231F;
  linkStyle default stroke:#9E988E,stroke-width:0.75px;
```

## 図の業務

| 業務 | 何を整えるか |
| --- | --- |
| [見積](decomposition-catalog.md#1-見積) | 開発範囲と不確実性を見極め、費用・期間・体制を判断できる形にする。 |
| [要件定義](requirements-context.md) | 業務の期待を、人とシステムの責務が分かる要件へ整える。 |
| [基本設計](decomposition-catalog.md#3-基本設計) | 要件を、利用者や外部システムから見える仕様へ変える。 |
| [詳細設計](decomposition-catalog.md#4-詳細設計) | 外部仕様を、実装できる内部構造と処理へ落とす。 |
| [実装・単体](implementation-unit-context.md) | 内部仕様をコードへ変え、単体で成立する変更として確かめる。 |
| [内結設計](decomposition-catalog.md#6-内部結合テスト設計) | 内部の責務境界を、結合で検証できる条件とシナリオへ変える。 |
| [内結試験](decomposition-catalog.md#7-内部結合テスト) | コンポーネントを組み合わせ、内部連携の成立と不具合を確かめる。 |
| [外結設計](decomposition-catalog.md#8-外部結合テスト設計) | 外部との契約や異常条件を、双方で試せるシナリオへ整える。 |
| [外結試験](external-integration-context.md) | 外部との接続・契約・異常時の責任境界が成立するか確かめる。 |
| [ST設計](decomposition-catalog.md#10-システムテスト設計) | システム全体として証明すべき業務品質・非機能品質を試験へ変える。 |
| [ST](decomposition-catalog.md#11-システムテスト) | 本番相当でE2Eと非機能を確かめ、UATへ渡せる品質を判断する。 |
| [UAT](decomposition-catalog.md#12-ユーザー受入テスト) | 実業務の観点から使えるかを確かめ、受入可否を決める。 |
| [導入](deployment-context.md) | 本番へ安全に切り替え、業務利用を確認して運用へ責任を渡す。 |

この一覧は [業務分解カタログ](decomposition-catalog.md) の要約です。詳しい分解は必要になった業務だけ掘ります。

## この図が表していること

13工程は、システム開発を話すための最初の共通言語です。工程間の厳密な順番を示す図ではありません。実務にある変更、差戻し、再試験、再合意は、各業務の Context / Flow で見ます。

## 支えるモデル

必要なときだけ参照します。

- [Actor](master-actor-map.md) — 誰がどの責任で参加するか
- [Information](master-information-model.md) — 何を判断・更新・引き渡すか
- [External System](master-system-map.md) — どのツール・環境・外部システムと関わるか
