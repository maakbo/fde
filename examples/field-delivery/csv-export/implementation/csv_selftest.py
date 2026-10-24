"""Implementation HTTP checks. Independent acceptance is performed separately."""
import csv
import io
import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def verify_csv(base):
    checks = 0

    def request(path, method="GET"):
        try:
            response = urlopen(Request(base + path, method=method), timeout=5)
        except HTTPError as error:
            response = error
        with response:
            return response.status, response.headers, response.read()

    query = "?status=NEW&from=2026-10-02&to=2026-10-04"
    status, headers, raw = request("/orders.csv" + query)
    assert status == 200
    assert headers.get("Content-Type") == "text/csv;charset=utf-8"
    assert headers.get("Content-Disposition") == 'attachment; filename="orders.csv"'
    assert headers.get("Cache-Control") == "no-store"
    assert int(headers.get("Content-Length")) == len(raw)
    assert raw.startswith(b"\xef\xbb\xbf")
    assert raw.endswith(b"\r\n")
    rows = list(csv.reader(io.StringIO(raw.decode("utf-8-sig"), newline="")))
    assert rows == [["受注ID", "受注日", "状況"],
                    ["O-105", "2026-10-04", "NEW"],
                    ["O-103", "2026-10-03", "NEW"]]
    checks += 8

    _, _, json_body = request("/orders" + query)
    found = json.loads(json_body)["orders"]
    assert rows[1:] == [[row["id"], row["date"], row["status"]] for row in found]
    checks += 1

    status, headers, raw = request("/orders.csv?status=SHIPPED&from=2026-10-03")
    assert status == 200 and raw == b"\xef\xbb\xbf" + "受注ID,受注日,状況\r\n".encode()
    checks += 1

    for query in ["?status=BAD", "?from=2026-02-30", "?from=2026-10-04&to=2026-10-03",
                  "?unknown=x", "?status=NEW&status=NEW"]:
        status, headers, raw = request("/orders.csv" + query)
        assert status == 400 and headers.get("Content-Disposition") is None
        assert "application/json" in headers.get("Content-Type", "")
        assert json.loads(raw)["error"]
        checks += 1

    status, headers, raw = request("/orders.csv", "POST")
    assert status == 405 and headers.get("Allow") == "GET"
    assert headers.get("Content-Disposition") is None
    checks += 1

    status, _, html = request("/")
    assert status == 200 and b'/orders.csv?' in html
    assert b'type="button" id="csv-download"' in html
    checks += 1
    print(f"PASS CSV HTTP implementation self-test: {checks} checks")
