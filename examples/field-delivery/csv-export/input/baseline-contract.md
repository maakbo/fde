# 既存検索の公開架空仕様

これは既存機能のbaselineであり、新CSVの仕様決定ではない。コードはbaseline/にある。
Java16+標準ライブラリ・plain class、Python3。localhost固定の小さいデモ。
GET / は検索画面。GET /orders はcountとordersのJSON、正常200、不正400。
検索条件はstatus(NEW/SHIPPED/CANCELLED)、from/to(YYYY-MM-DD任意・両端含む)、AND。
空値は未指定。開始が終了より後、不正な状況/日付、未知queryや重複queryは400。
順序は受注日の降順、同日はID昇順。0件は正常。検索は元データを変更しない。
GET以外は405、未知pathは404。既存の機能はCSV追加後も維持する。

fixture: O-101/2026-10-01/NEW、O-102/2026-10-02/SHIPPED、
O-103/2026-10-03/NEW、O-104/2026-10-03/CANCELLED、O-105/2026-10-04/NEW。
実DB、auth、権限、paging、実データ、実Excel、性能は対象外・未検証。
上の2xx/4xxはこの架空baselineの既存振る舞いで、全案件の標準ではない。
