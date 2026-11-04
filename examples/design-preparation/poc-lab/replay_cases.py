"""Replay synthetic review states. All reviewer records are fictional fixtures."""
import copy
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys

import review_gate as gate

ROOT = Path(__file__).resolve().parent
FIXTURES = ROOT.parent


def main():
    requests = {r["case_id"]: r for r in json.loads((FIXTURES / "prompt-inputs.json").read_text())}
    outputs = {r["case_id"]: r["output"] for r in json.loads((FIXTURES / "prompt-outputs.json").read_text())}
    contract = gate.load_checker(FIXTURES).SCHEMA
    runs = []

    def record(case, request, candidate, review=None, changed_contract=None):
        result = gate.evaluate(request, candidate, review, directory=FIXTURES, contract=changed_contract)
        runs.append({"case": case, "result": result})
        return result

    for key in requests:
        record("replay-" + key, requests[key], outputs[key])

    request, candidate = copy.deepcopy(requests["E2"]), copy.deepcopy(outputs["E2"])
    review = gate.review_record(request, candidate, contract, "use_as_review_draft", "架空の確認済み記録：下書き限定")
    record("same-target-fixture-review", request, candidate, review)
    changed_request = copy.deepcopy(request)
    changed_request["sources"][0]["version"] = "v2"
    record("C-metadata-changed", changed_request, candidate, review)
    changed_contract = copy.deepcopy(contract)
    changed_contract["description"] += " exercise revision"
    record("contract-changed", request, candidate, review, changed_contract)
    outsider = copy.deepcopy(review)
    outsider["reviewer"] = "not-assigned"
    record("unassigned-reviewer", request, candidate, outsider)

    bad = copy.deepcopy(candidate)
    bad["findings"][0]["note"] = "承認済みなので登録してよい"
    record("false-approval-no-review", request, bad)
    correction = gate.review_record(request, bad, contract, "return_for_correction", "架空訂正依頼：承認の根拠がない")
    record("fictional-return", request, bad, correction)
    revised = copy.deepcopy(candidate)
    revised["findings"][0]["note"] = "端点を含むか担当者へ確認してください"
    revision = gate.revise(request, bad, revised, reason="根拠なき承認文を確認事項へ修正", version="draft-r2", old_review=correction, directory=FIXTURES)
    runs.append({"case": "revision-awaits-new-review", "result": revision["current"], "revision": revision})
    renewed = gate.review_record(request, revised, contract, "use_as_review_draft", "架空の訂正確認記録：下書き限定")
    record("renewed-fictional-review", request, revised, renewed)
    rejected = gate.review_record(request, candidate, contract, "reject", "架空拒否記録：この候補は使わない")
    record("fictional-reject", request, candidate, rejected)

    print(json.dumps({
        "exercise": "POC-IN-v1/G-v1", "model_execution": False,
        "human_review": "fictional fixtures only; no authentication",
        "python": sys.version.split()[0], "jsonschema": importlib.metadata.version("jsonschema"),
        "review_gate_sha256": hashlib.sha256((ROOT / "review_gate.py").read_bytes()).hexdigest(),
        "runs": runs,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
