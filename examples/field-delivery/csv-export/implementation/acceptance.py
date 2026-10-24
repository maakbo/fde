"""Independent HTTP acceptance from R1-R6; not browser or business-effect evidence."""
import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def require(condition, details):
    if not condition:
        raise AssertionError(details)


def verify(base):
    def request(path, method="GET"):
        try:
            response = urlopen(Request(base + path, method=method), timeout=5)
        except HTTPError as error:
            response = error
        with response:
            return response.status, response.headers, response.read().decode("utf-8")

    def orders(query, expected):
        status, headers, body = request("/orders" + query)
        require(status == 200, (query, status, body))
        require("application/json" in headers.get("Content-Type", ""), headers)
        data = json.loads(body)
        require(data["count"] == len(expected), (query, data))
        require([row["id"] for row in data["orders"]] == expected, (query, data))
        return data

    all_ids = ["O-105", "O-103", "O-104", "O-102", "O-101"]
    before = orders("", all_ids)
    orders("?status=&from=&to=", all_ids)
    orders("?status=NEW", ["O-105", "O-103", "O-101"])
    orders("?status=CANCELLED", ["O-104"])
    orders("?from=2026-10-03&to=2026-10-03", ["O-103", "O-104"])
    orders("?from=2026-10-03", ["O-105", "O-103", "O-104"])
    orders("?to=2026-10-02", ["O-102", "O-101"])
    orders("?status=NEW&from=2026-10-02&to=2026-10-04", ["O-105", "O-103"])
    orders("?status=SHIPPED&from=2026-10-03", [])
    print("PASS HTTP acceptance: 9 search cases (R1-R5)")

    for query in ["?status=OTHER", "?from=2026-02-30", "?to=2026-1-01",
                  "?from=2026-10-04&to=2026-10-01"]:
        status, _, body = request("/orders" + query)
        require(status == 400 and json.loads(body).get("error"), (query, status, body))
    require(orders("", all_ids) == before, "search/error handling changed source orders")
    require(request("/orders", "POST")[0] == 405, "POST must be rejected")
    status, _, html = request("/")
    require(status == 200 and '<form' in html and 'type="date"' in html, "search form delivery")
    require(all(label in html for label in ["未出荷", "出荷済み", "取消済み", "該当する受注はありません"]),
            "search choices and empty-result message")
    print("PASS HTTP acceptance: 4 invalid cases, unchanged data, read-only method and HTML delivery (R6)")
    print("NOTE: HTML delivery checked; real browser interaction and field acceptance unmeasured")
