"""架空演習の経路とID対応だけを点検する決定的な例。"""

SOURCE_IDS = {"R01", "R02", "R03", "R04"}
ALLOWED = {"read_supplied", "write_scratch", "check_ids"}


def route(name, references, action, confidence, reviewer_available=True):
    missing = sorted(set(references) - SOURCE_IDS)
    uncovered = sorted(SOURCE_IDS - set(references))
    if action not in ALLOWED:
        status = "DENY_OUT_OF_SCOPE"
    elif missing:
        status = "RETURN_MISSING_SOURCE"
    elif action == "check_ids":
        status = "REPORT_ID_GAPS" if uncovered else "RUN_DETERMINISTIC_CHECK_PASS"
    elif action == "write_scratch":
        status = "DRAFT_SCRATCH" if reviewer_available else "DRAFT_SCRATCH_HOLD_REVIEW"
    else:
        status = "READ_SUPPLIED"
    return f"{name}: confidence={confidence:.2f} action={action} unknown={missing} uncovered={uncovered} route={status}"


if __name__ == "__main__":
    cases = [
        ("N", ["R01", "R02", "R03", "R04"], "write_scratch", 0.70, True),
        ("H", ["R01", "R99"], "write_scratch", 0.99, True),
        ("L", ["R01", "R02", "R03", "R04"], "check_ids", 0.25, True),
        ("X", ["R01"], "write_canonical_and_send", 0.99, True),
        ("U", ["R01", "R02", "R03", "R04"], "write_scratch", 0.70, False),
    ]
    for case in cases:
        print(route(*case))
