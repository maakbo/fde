"""Local contract exercise; no model, service, or approval operations.

Requires jsonschema. This checks structure and limited input correspondence,
not completeness, semantic correctness, field permission, or business acceptance.
"""
import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
SCHEMA = json.loads((ROOT / "review-findings.schema.json").read_text())
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA)


def issues(output, request):
    errors = ["schema: " + e.message for e in VALIDATOR.iter_errors(output)]
    if errors:
        return errors
    sources = {s["id"]: s for s in request["sources"]}
    if output["request_id"] != request["request_id"]:
        errors.append("reference: request ID differs")
    for finding in output["findings"]:
        if not set(finding["source_ids"]).issubset(sources):
            errors.append("reference: unknown source ID")
        evidence = finding["evidence"]
        sid = evidence["source_id"]
        if sid not in sources or sid not in finding["source_ids"]:
            errors.append("reference: evidence source ID differs")
            continue
        actual = sources[sid][evidence["field"]]
        matches = (evidence["value"] == actual if evidence["field"] == "version"
                   else evidence["value"] in actual)
        if not matches:
            errors.append("reference: evidence does not match input field")
    return errors


def main():
    requests = {r["case_id"]: r for r in json.loads((ROOT / "prompt-inputs.json").read_text())}
    runs = json.loads((ROOT / "prompt-outputs.json").read_text())
    assert len(runs) == len(requests)
    assert {r["case_id"] for r in runs} == set(requests)
    for run in runs:
        found = issues(run["output"], requests[run["case_id"]])
        assert not found, (run["case_id"], found)
        print("PASS schema/reference:", run["case_id"])

    base = next(r["output"] for r in runs if r["case_id"] == "E2")
    request = requests["E2"]
    mutations = []
    candidate = copy.deepcopy(base); candidate.pop("status"); mutations.append(("missing required", candidate))
    candidate = copy.deepcopy(base); candidate["findings"] = "none"; mutations.append(("wrong type", candidate))
    candidate = copy.deepcopy(base); candidate["schema_version"] = "unknown"; mutations.append(("unknown contract", candidate))
    candidate = copy.deepcopy(base); candidate["status"] = "approved"; mutations.append(("unauthorized state", candidate))
    candidate = copy.deepcopy(base); candidate.update(confidence=.99, checks_passed=True); mutations.append(("self-reported checks", candidate))
    candidate = copy.deepcopy(base); candidate["findings"][0]["source_ids"] = ["S99"]; mutations.append(("unknown source", candidate))
    candidate = copy.deepcopy(base); candidate["findings"][0]["evidence"]["value"] = "not present in input"; mutations.append(("invented evidence", candidate))
    candidate = copy.deepcopy(base); candidate["request_id"] = "OTHER"; mutations.append(("wrong request", candidate))
    for label, candidate in mutations:
        found = issues(candidate, request)
        assert found, label
        print("REJECT:", label, "—", found[0])

    # Real references and valid structure cannot establish the claim's meaning.
    candidate = copy.deepcopy(base)
    candidate["findings"][0]["note"] = "承認済みなので登録してよい"
    assert not issues(candidate, request)
    print("UNVERIFIED: false approval note passes schema/reference; independent meaning/permission review required")
    print("Completed local checks only; no acceptance, registration, sending, or model evaluation performed")


if __name__ == "__main__":
    main()
