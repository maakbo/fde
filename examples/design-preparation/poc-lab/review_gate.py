"""Synthetic, local review gate for SCHEMA-v2 drafts; no real approval or action."""

import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path

from jsonschema import Draft202012Validator

DECISIONS = {"use_as_review_draft", "return_for_correction", "reject"}
REVIEWER = "reviewer-A"  # Fictional role setting, never authentication.


def digest(value):
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def fixtures_dir(path=None):
    return Path(path or os.environ.get("FDE_POC_FIXTURES_DIR") or
                Path(__file__).resolve().parent.parent).resolve()


def load_checker(directory):
    path = fixtures_dir(directory) / "check-prompt-output.py"
    spec = importlib.util.spec_from_file_location("fde_prompt_checker", path)
    if spec is None or spec.loader is None:
        raise ValueError("checker unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def input_issues(request):
    """Check only the settled synthetic input contract before checker.issues()."""
    if not isinstance(request, dict):
        return ["input: expected object"]
    errors = []
    for field in ("case_id", "request_id"):
        if not isinstance(request.get(field), str) or not request[field]:
            errors.append(f"input: {field} must be nonempty string")
    sources = request.get("sources")
    if not isinstance(sources, list):
        errors.append("input: sources must be array")
        return errors
    seen = set()
    for i, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f"input: sources[{i}] must be object")
            continue
        sid = source.get("id")
        if not isinstance(sid, str) or not sid:
            errors.append(f"input: sources[{i}].id must be nonempty string")
        elif sid in seen:
            errors.append(f"input: duplicate source ID {sid}")
        else:
            seen.add(sid)
        for field in ("version", "text"):
            if not isinstance(source.get(field), str):
                errors.append(f"input: sources[{i}].{field} must be string")
    return errors


def targets(request, candidate, contract):
    return {"input": digest(request), "candidate": digest(candidate), "contract": digest(contract)}


def review_record(request, candidate, contract, decision, reason, reviewer=REVIEWER):
    """Construct an exercise record; caller still must submit it to evaluate()."""
    return {"reviewer": reviewer, "decision": decision, "reason": reason,
            "targets": targets(request, candidate, contract)}


def evaluate(request, candidate, review=None, *, directory=None, contract=None):
    """Return a narrow exercise state. A record is data, not a human attestation."""
    checker = load_checker(directory)
    schema = checker.SCHEMA if contract is None else contract
    bound = targets(request, candidate, schema)
    errors = input_issues(request)
    if errors:
        return {"state": "invalid_input", "issues": errors, "targets": bound}
    # The previous checker supplies SCHEMA-v2 and input-reference checks.
    errors = checker.issues(candidate, request)
    if contract is not None:
        Draft202012Validator.check_schema(schema)
        errors += ["contract: " + e.message for e in Draft202012Validator(schema).iter_errors(candidate)]
    if errors:
        return {"state": "invalid_candidate", "issues": errors, "targets": bound}
    if review is None:
        return {"state": "pending_review", "issues": [], "targets": bound}
    if not isinstance(review, dict) or review.get("targets") != bound:
        return {"state": "pending_review", "issues": ["review: absent or stale targets"], "targets": bound}
    if review.get("reviewer") != REVIEWER:
        return {"state": "pending_review", "issues": ["review: role outside exercise setting"], "targets": bound}
    decision, reason = review.get("decision"), review.get("reason")
    if not isinstance(decision, str) or decision not in DECISIONS or not isinstance(reason, str) or not reason.strip():
        return {"state": "pending_review", "issues": ["review: decision or reason invalid"], "targets": bound}
    return {"state": decision, "issues": [], "targets": bound,
            "review": {"reviewer": REVIEWER, "decision": decision, "reason": reason}}


def revise(request, original, revised, *, reason, version, old_review=None,
           directory=None, contract=None):
    """Keep both snapshots and re-evaluate the replacement without old review."""
    if not isinstance(reason, str) or not reason.strip() or not isinstance(version, str) or not version.strip():
        raise ValueError("revision reason and version required")
    before, after = copy.deepcopy(original), copy.deepcopy(revised)
    previous = evaluate(request, before, old_review, directory=directory, contract=contract)
    current = evaluate(request, after, directory=directory, contract=contract)
    return {"original": before, "revised": after, "revision": {"version": version,
            "reason": reason, "original_hash": digest(before), "revised_hash": digest(after)},
            "previous": previous, "current": current}


def main():
    parser = argparse.ArgumentParser(description="Replay supplied synthetic fixtures only")
    parser.add_argument("--fixtures-dir", type=Path)
    parser.add_argument("--case-id", required=True)
    args = parser.parse_args()
    directory = fixtures_dir(args.fixtures_dir)
    requests = json.loads((directory / "prompt-inputs.json").read_text())
    outputs = json.loads((directory / "prompt-outputs.json").read_text())
    request = next(r for r in requests if r["case_id"] == args.case_id)
    candidate = next(r["output"] for r in outputs if r["case_id"] == args.case_id)
    print(json.dumps(evaluate(request, candidate, directory=directory), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
