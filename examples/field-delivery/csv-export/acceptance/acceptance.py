#!/usr/bin/env python3
"""Independent localhost HTTP acceptance checks for the fictional orders CSV."""

import argparse
import csv
import io
import json
import sys
import urllib.error
import urllib.parse
import urllib.request


HEADER = ["受注ID", "受注日", "状況"]
ALL = [
    ("O-105", "2026-10-04", "NEW"),
    ("O-103", "2026-10-03", "NEW"),
    ("O-104", "2026-10-03", "CANCELLED"),
    ("O-102", "2026-10-02", "SHIPPED"),
    ("O-101", "2026-10-01", "NEW"),
]
NEW = [ALL[0], ALL[1], ALL[4]]
COMPOUND = [ALL[1], ALL[4]]
SAME_DAY = [ALL[1], ALL[2]]
CASES = [
    ("all", "", ALL),
    ("new", "status=NEW", NEW),
    ("compound", "status=NEW&from=2026-10-01&to=2026-10-03", COMPOUND),
    ("same-day", "from=2026-10-03&to=2026-10-03", SAME_DAY),
    ("empty", "status=SHIPPED&from=2026-10-03", []),
    ("blank", "status=&from=&to=", ALL),
]
BAD = [
    ("bad-status", "status=INVALID"),
    ("bad-from", "from=2026-02-30"),
    ("bad-to", "to=bad"),
    ("reversed", "from=2026-10-04&to=2026-10-03"),
    ("unknown-query", "unknown=1"),
    ("duplicate-query", "status=NEW&status=NEW"),
]


class Checks:
    def __init__(self):
        self.failures = []
        self.passed = 0

    def check(self, condition, label, detail=""):
        if condition:
            self.passed += 1
        else:
            self.failures.append(f"{label}: {detail}")


def request(url, method="GET"):
    req = urllib.request.Request(url, method=method)
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status, response.headers, response.read()
    except urllib.error.HTTPError as error:
        return error.code, error.headers, error.read()


def url_for(base, path, query=""):
    url = base.rstrip("/") + path
    return url + ("?" + query if query else "")


def json_rows(body, checks, label):
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        checks.check(False, label, f"JSON decode: {error}")
        return None
    if not isinstance(payload, dict) or not isinstance(payload.get("orders"), list):
        checks.check(False, label, "expected object with orders array")
        return None
    raw_rows = payload["orders"]
    rows = []
    for index, row in enumerate(raw_rows):
        if not isinstance(row, dict):
            checks.check(False, label, f"orders[{index}] is not an object")
            return None
        if "date" not in row:
            checks.check(False, label, f"orders[{index}] missing date: {row!r}")
            return None
        rows.append((row.get("id"), row["date"], row.get("status")))
    checks.check(payload.get("count") == len(raw_rows), label + " count", repr(payload.get("count")))
    return rows


def record_ends_are_crlf(data):
    """Check record terminators outside quoted fields without rejecting embedded CR/LF."""
    quoted = False
    index = 0
    ends = 0
    while index < len(data):
        byte = data[index]
        if byte == 34:
            if quoted and index + 1 < len(data) and data[index + 1] == 34:
                index += 2
                continue
            quoted = not quoted
        elif not quoted and byte in (10, 13):
            if data[index:index + 2] != b"\r\n":
                return False
            ends += 1
            index += 2
            continue
        index += 1
    return not quoted and ends > 0 and data.endswith(b"\r\n")


def csv_rows(body, headers, checks, label):
    checks.check(headers.get_content_type() == "text/csv", label + " content type", str(headers.get("Content-Type")))
    checks.check(headers.get_param("charset") == "utf-8", label + " charset", str(headers.get("Content-Type")))
    disposition = headers.get("Content-Disposition", "")
    checks.check(disposition.lower().startswith("attachment"), label + " attachment", disposition)
    checks.check("filename=orders.csv" in disposition or 'filename="orders.csv"' in disposition,
                 label + " filename", disposition)
    return csv_body_rows(body, checks, label)


def csv_body_rows(body, checks, label):
    checks.check(body.startswith(b"\xef\xbb\xbf") and not body[3:].startswith(b"\xef\xbb\xbf"),
                 label + " one BOM", repr(body[:8]))
    if not body.startswith(b"\xef\xbb\xbf"):
        return None
    data = body[3:]
    checks.check(record_ends_are_crlf(data), label + " CRLF record endings")
    try:
        reader = csv.reader(io.StringIO(data.decode("utf-8"), newline=""), strict=True)
        rows = list(reader)
    except (UnicodeDecodeError, csv.Error) as error:
        checks.check(False, label + " CSV parser", str(error))
        return None
    checks.check(bool(rows) and rows[0] == HEADER, label + " header", repr(rows[:1]))
    checks.check(all(len(row) == 3 for row in rows), label + " three columns", repr(rows))
    return [tuple(row) for row in rows[1:]] if rows else None


def check_error_json(checks, label, status, headers, body):
    checks.check(status == 400, label + " status", str(status))
    checks.check(headers.get_content_type() == "application/json", label + " JSON type", str(headers.get("Content-Type")))
    checks.check(not headers.get("Content-Disposition", "").lower().startswith("attachment"),
                 label + " no attachment", str(headers.get("Content-Disposition")))
    try:
        json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        checks.check(False, label + " JSON body", str(error))


def run(args):
    checks = Checks()
    base = args.base_url.rstrip("/")
    path = args.csv_path
    checks.check(path.startswith("/") and path not in ("/", "/orders"), "CSV path", path)
    if checks.failures:
        return checks
    baseline_before = None
    for name, query, expected in CASES:
        json_status, _, json_body = request(url_for(base, "/orders", query))
        checks.check(json_status == 200, "JSON " + name + " status", str(json_status))
        actual_json = json_rows(json_body, checks, "JSON " + name) if json_status == 200 else None
        if actual_json is not None:
            checks.check(actual_json == expected, "JSON " + name + " rows", f"got {actual_json!r}, expected {expected!r}")
            if name == "all":
                baseline_before = actual_json
        csv_status, headers, body = request(url_for(base, path, query))
        checks.check(csv_status == 200, "CSV " + name + " status", str(csv_status))
        if csv_status == 200:
            actual_csv = csv_rows(body, headers, checks, "CSV " + name)
            if actual_csv is not None:
                checks.check(actual_csv == expected, "CSV " + name + " rows", f"got {actual_csv!r}, expected {expected!r}")
                if actual_json is not None:
                    checks.check(actual_csv == actual_json, "JSON/CSV " + name + " equality")
    for name, query in BAD:
        for target in ("/orders", path):
            status, headers, body = request(url_for(base, target, query))
            check_error_json(checks, name + " " + target, status, headers, body)
    for target in ("/orders", path):
        status, _, _ = request(url_for(base, target), method="POST")
        checks.check(status == 405, "POST " + target, str(status))
    status, _, _ = request(url_for(base, "/__acceptance_unknown_path__"))
    checks.check(status == 404, "unknown path", str(status))
    status, _, _ = request(url_for(base, "/"))
    checks.check(status == 200, "existing page", str(status))
    status, _, body = request(url_for(base, "/orders"))
    after = json_rows(body, checks, "JSON after mutation checks") if status == 200 else None
    checks.check(status == 200 and baseline_before == after, "source unchanged", f"before={baseline_before!r}, after={after!r}")

    if args.special_csv_url:
        special_status, headers, body = request(args.special_csv_url)
        checks.check(special_status == 200, "special fixture status", str(special_status))
        if special_status == 200:
            actual = csv_rows(body, headers, checks, "special fixture")
            expected = [(args.special_id, args.special_date, args.special_status)]
            checks.check(actual == expected, "special fixture preserved", f"got {actual!r}, expected {expected!r}")
    elif args.special_csv_file:
        with open(args.special_csv_file, "rb") as source:
            actual = csv_body_rows(source.read(), checks, "special formatter fixture")
        expected = [(args.special_id, args.special_date, args.special_status)]
        checks.check(actual == expected, "special formatter fixture preserved",
                     f"got {actual!r}, expected {expected!r}")
    else:
        print("UNVERIFIED: special formatter fixture, browser button behavior, actual Excel", file=sys.stderr)
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True, help="running localhost server base URL")
    parser.add_argument("--csv-path", required=True, help="CSV path selected in Design, beginning with /")
    parser.add_argument("--special-csv-url", help="full HTTP URL for Design-provided isolated special fixture")
    parser.add_argument("--special-csv-file", help="raw stdout bytes from SpecialCsvHarness")
    parser.add_argument("--special-id", default='和文,"引用",末尾\r\n次行')
    parser.add_argument("--special-date", default="2026-10-05")
    parser.add_argument("--special-status", default="NEW")
    args = parser.parse_args()
    if args.special_csv_url and args.special_csv_file:
        parser.error("choose one special fixture source")
    parsed = urllib.parse.urlsplit(args.base_url)
    if parsed.scheme != "http" or parsed.hostname not in ("localhost", "127.0.0.1", "::1"):
        parser.error("--base-url must be local HTTP")
    if args.special_csv_url:
        special = urllib.parse.urlsplit(args.special_csv_url)
        if special.scheme != "http" or special.hostname not in ("localhost", "127.0.0.1", "::1"):
            parser.error("--special-csv-url must be local HTTP")
    try:
        checks = run(args)
    except (OSError, urllib.error.URLError) as error:
        print(f"FAIL: HTTP execution: {error}", file=sys.stderr)
        return 1
    for failure in checks.failures:
        print("FAIL: " + failure, file=sys.stderr)
    print(f"{checks.passed} checks passed; {len(checks.failures)} failed")
    return 1 if checks.failures else 0


if __name__ == "__main__":
    sys.exit(main())
