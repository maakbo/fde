"""Independent boundary audit of the published synthetic review gate."""

import argparse
import copy
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lab", type=Path, default=Path.cwd() / "examples/design-preparation/poc-lab")
    args = parser.parse_args()
    lab = args.lab.resolve()
    fixtures = lab.parent
    sys.path.insert(0, str(lab))
    import review_gate as gate

    requests = json.loads((fixtures / "prompt-inputs.json").read_text())
    outputs = json.loads((fixtures / "prompt-outputs.json").read_text())
    request = next(x for x in requests if x["case_id"] == "E2")
    candidate = next(x["output"] for x in outputs if x["case_id"] == "E2")
    contract = gate.load_checker(fixtures).SCHEMA

    locations = {
        "request": ("case_id", "request_id", "sources"),
        "source": ("id", "version", "text"),
        "candidate": ("schema_version", "request_id", "status", "findings"),
        "finding": ("kind", "source_ids", "evidence", "note"),
        "evidence": ("source_id", "field", "value"),
        "review": ("targets", "reviewer", "decision", "reason"),
    }
    values = (None, 0, True, [], {}, "")
    failures = []
    count = 0
    for location, fields in locations.items():
        for field in fields:
            for value in values:
                count += 1
                req = copy.deepcopy(request)
                out = copy.deepcopy(candidate)
                review = gate.review_record(req, out, contract, "use_as_review_draft", "fixture")
                target = {
                    "request": req,
                    "source": req["sources"][0],
                    "candidate": out,
                    "finding": out["findings"][0],
                    "evidence": out["findings"][0]["evidence"],
                    "review": review,
                }[location]
                target[field] = copy.deepcopy(value)
                try:
                    state = gate.evaluate(req, out, review, directory=fixtures)["state"]
                except Exception as exc:
                    failures.append([location, field, repr(value), type(exc).__name__])
                    continue
                if state not in ("invalid_input", "invalid_candidate", "pending_review"):
                    failures.append([location, field, repr(value), state])

    baseline = gate.review_record(request, candidate, contract, "use_as_review_draft", "fixture")
    if gate.evaluate(request, candidate, baseline, directory=fixtures)["state"] != "use_as_review_draft":
        failures.append(["baseline", "matching fixture review did not reach draft state"])
    changes = {
        "C_metadata_version": lambda req, out, schema: req["sources"][0].update(version="v2"),
        "candidate_note": lambda req, out, schema: out["findings"][0].update(note="changed"),
        "contract_description": lambda req, out, schema: schema.update(description="changed"),
    }
    states = {}
    for label, mutate in changes.items():
        req, out, schema = copy.deepcopy(request), copy.deepcopy(candidate), copy.deepcopy(contract)
        mutate(req, out, schema)
        result = gate.evaluate(req, out, baseline, directory=fixtures, contract=schema)
        states[label] = result["state"]
        if result["state"] != "pending_review":
            failures.append([label, result["state"]])

    print(json.dumps({"type_mutations": count, "stale_review_states": states,
                      "failures": failures}, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
