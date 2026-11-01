"""Exercise-only local release checks; no real index, cache, service, or auth."""

import json
from datetime import date
from pathlib import Path

docs = json.loads((Path(__file__).parent / "fixture.json").read_text())["documents"]


def applicable(asof, *, revoked=frozenset(), history_allowed=False):
    t = date.fromisoformat(asof)
    if not history_allowed and t != date(2026, 11, 1):
        return []
    return [
        d for d in docs
        if d["status"] == "approved"
        and d["product"] == "v2"
        and d["internal_allowed"]
        and d["version"] not in revoked
        and date.fromisoformat(d["valid_from"]) <= t
        and (d["valid_until"] is None or t < date.fromisoformat(d["valid_until"]))
    ]


def release(index_version, cache_version, *, revoked=frozenset()):
    eligible = [d["version"] for d in applicable("2026-11-01", revoked=revoked)]
    if index_version != cache_version or index_version not in eligible:
        return "HOLD", eligible
    d = next(d for d in docs if d["version"] == index_version)
    # Two exercise questions reuse the same candidate unit; these are literal-presence checks only.
    normal_question_has_basis = "状態マスターを参照" in d["content"]
    missing_version_question_has_basis = "版が不明なら未決" in d["content"] and "担当SEへ返す" in d["content"]
    if not (normal_question_has_basis and missing_version_question_has_basis):
        return "HOLD", eligible
    return "LOCAL_SWITCH_OK", eligible


if __name__ == "__main__":
    assert [d["version"] for d in applicable("2026-11-01")] == ["v2"]
    assert [d["version"] for d in applicable("2026-10-30", history_allowed=True)] == ["v1"]
    assert release("v2", "v1")[0] == "HOLD"
    assert release("v2", "v2")[0] == "LOCAL_SWITCH_OK"
    assert release("v2", "v2", revoked={"v2"})[0] == "HOLD"
    print("T=2026-11-01 eligible:", [d["version"] for d in applicable("2026-11-01")])
    print("F1 mixed index/cache:", release("v2", "v1"))
    print("F2 matched index/cache + normal/unknown condition:", release("v2", "v2"))
    print("F3 v2 revoked, no v1 fallback:", release("v2", "v2", revoked={"v2"}))
    print("F4 historical 2026-10-30 with history permission:", [d["version"] for d in applicable("2026-10-30", history_allowed=True)])
