#!/usr/bin/env python3
"""Recalculate this fictional example; no model, workplace or rollout evaluation."""
import argparse
import csv
import json
import math
from pathlib import Path


def ratio(numerator, denominator):
    return numerator / denominator if denominator else None


def summarize(rows, column):
    counts = {"tp": 0, "fn": 0, "fp": 0, "tn": 0, "critical_fn": 0}
    for row in rows:
        for key in ("needs_fix", "critical", column):
            if row[key] not in ("0", "1"):
                raise ValueError(f"{row['id']}: invalid {key}")
        actual = row["needs_fix"] == "1"
        warned = row[column] == "1"
        if row["critical"] == "1" and not actual:
            raise ValueError("critical row must need correction")
        counts["tp" if actual and warned else "fn" if actual else "fp" if warned else "tn"] += 1
        counts["critical_fn"] += int(actual and not warned and row["critical"] == "1")
    tp, fn, fp, tn = (counts[k] for k in ("tp", "fn", "fp", "tn"))
    return dict(counts, accuracy=ratio(tp+tn, len(rows)),
                precision=ratio(tp, tp+fp), recall=ratio(tp, tp+fn),
                fpr=ratio(fp, fp+tn), fnr=ratio(fn, tp+fn))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=Path(__file__).with_name("cases.csv"))
    args = parser.parse_args()
    with args.cases.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    result = {"evidence": "synthetic labels and assumptions; no model/workplace run",
              "undefined_ratio": "null means N/A, not 0 or 100%"}
    for candidate in ("a", "b"):
        result[candidate] = summarize(rows, f"candidate_{candidate}_warning")
    # Hypotheses of this case, in human-minutes. Do not substitute for observed benefit.
    baseline = sum((14, 10, 4, 2))
    targets = []
    for review in (8, 12):
        proposed = sum((6, review, 4, 2))
        gain = baseline - proposed
        needed = math.ceil((120+60)/gain) if gain > 0 else None
        targets.append(dict(review=review, baseline=baseline, proposed=proposed,
                            gain_per_use=gain, needed_uses=needed,
                            eligible_opportunities=40, fraction=ratio(needed, 40) if needed is not None else None,
                            all_40_net_minutes=40*gain-60,
                            feasible_under_assumptions=needed is not None and needed <= 40))
    result["benefit_hypotheses"] = targets
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
