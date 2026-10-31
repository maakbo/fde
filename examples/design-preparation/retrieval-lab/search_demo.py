"""Exercise-only local literal search. No network, embeddings, LLM, or production index."""

import json
from pathlib import Path

DATA = json.loads((Path(__file__).parent / "fixture.json").read_text())


def units(join_p2=False):
    out = []
    for source in DATA["sources"]:
        if not source["allowed"]:
            continue  # Exercise-only eligibility filter before candidate generation; not real auth.
        if join_p2 and source["id"] == "P2":
            out.append((source, "§1–§3", "。".join(s["text"] for s in source["sections"])))
        else:
            out.extend((source, s["position"], s["text"]) for s in source["sections"])
    return out


def search(term, *, join_p2=False, scope=False):
    matches = []
    for source, position, body in units(join_p2=join_p2):
        if scope and not (
            source["product"] == "予約管理v2"
            and source["state"] == "承認済み現行"
            and source["audience"] == "内部設計"
            and source["allowed"]
        ):
            continue
        if term in body:
            matches.append((source["id"], position))
    return matches


if __name__ == "__main__":
    # The term change is explicit and manual; this script does not infer intent.
    print("original phrase / loose split:", search("候補を絞り込む"))
    print("manual term '状態条件' / scoped split:", search("状態条件", scope=True))
    print("manual term '状態条件' / scoped linked:", search("状態条件", scope=True, join_p2=True))
    print("CSV / scoped split:", search("CSV", scope=True))
    print("CSV / scoped linked:", search("CSV", scope=True, join_p2=True))
    assert all(source_id != "P9" for term in ("候補を絞り込む", "状態条件", "CSV") for source_id, _ in search(term))
    print("P9 allowed=false excluded from unscoped searches: yes (exercise filter, not auth)")
