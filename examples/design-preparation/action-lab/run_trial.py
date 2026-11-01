"""W20-v1 synthetic local handoff trial. No network or external actions."""

from __future__ import annotations

import argparse
import tempfile
import hashlib
import json
from pathlib import Path


REQUIREMENTS = {
    "R01": "From/To指定で注文日範囲を絞る。空欄側は制限しない。",
    "R02": "両端指定でFrom>Toなら検索せず入力誤りを返す。",
    "R03": "既存参照権限を保つ。検索で閲覧対象を広げない。",
    "R04": "時刻/タイムゾーン解釈は未決。SEへ確認し、下書きで確定しない。",
}
ALLOWED_OPERATIONS = frozenset({"create_review_draft"})


def record(*, version="v1", current="v1", missing=()):
    return {
        "work_id": "ORDER-DATE-42",
        "source_version": version,
        "current_version": current,
        "state": "ready",
        "requirements": {k: v for k, v in REQUIREMENTS.items() if k not in missing},
    }


def draft_text(source):
    req = source["requirements"]
    return (f"# 設計下書き: {source['work_id']}\n\n"
            f"work_id: {source['work_id']}\n"
            f"source_version: {source['source_version']}\n"
            "status: review_waiting (未承認)\n\n"
            "## 対象\n注文日範囲検索の機能追加。確定要件に基づく設計候補。\n\n"
            f"## 条件\n- R01: {req['R01']}\n\n"
            f"## 例外\n- R02: {req['R02']}\n\n"
            f"## 権限\n- R03: {req['R03']}\n\n"
            f"## 未決\n- R04: {req['R04']}\n"
            "- 確認先: SE。レビュー担当が原要件と照合・修正する。\n")


def digest(contents):
    return hashlib.sha256(contents.encode("utf-8")).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def process(source, delivery_id, trigger, workspace, operation="create_review_draft",
            fail_at=None):
    """Return an observable outcome. One local process; no concurrency guarantee."""
    workspace.mkdir(parents=True, exist_ok=True)
    if operation not in ALLOWED_OPERATIONS:
        return {"status": "denied", "reason": "operation_outside_P20-v1", "delivery_id": delivery_id}
    work_id, version = source["work_id"], source["source_version"]
    if source["state"] != "ready":
        return {"status": "input_waiting", "reason": "not_ready"}
    if version != source["current_version"]:
        return {"status": "stale", "reason": "source_version_differs_from_current"}
    missing = sorted(set(REQUIREMENTS) - set(source["requirements"]))
    if missing:
        return {"status": "input_waiting", "reason": "missing_requirements", "missing": missing,
                "return_to": "SE"}
    if source["requirements"] != REQUIREMENTS:
        return {"status": "input_waiting", "reason": "requirement_mismatch", "return_to": "SE"}

    key = f"{work_id}-{version}"
    draft = workspace / f"{key}.md"
    manifest = workspace / f"{key}.json"
    outbox = workspace / "outbox.json"
    contents = draft_text(source)
    expected_digest = digest(contents)
    state = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else None
    messages = json.loads(outbox.read_text(encoding="utf-8")) if outbox.exists() else []
    if state:
        if not draft.exists() or digest(draft.read_text(encoding="utf-8")) != state["draft_sha256"]:
            return {"status": "hold", "reason": "saved_draft_missing_or_changed"}
        if state["draft_sha256"] != expected_digest:
            return {"status": "hold", "reason": "same_key_different_content"}
    else:
        if draft.exists():
            return {"status": "hold", "reason": "unregistered_draft_requires_inspection"}
        if fail_at == "save":
            return {"status": "save_failed", "reason": "injected_before_write", "outbox_count": len(messages)}
        draft.write_text(contents, encoding="utf-8")
        if draft.read_text(encoding="utf-8") != contents:
            return {"status": "save_failed", "reason": "readback_mismatch"}
        state = {"work_id": work_id, "source_version": version,
                 "draft_sha256": expected_digest, "draft_path": str(draft),
                 "state": "saved_not_handed_off"}
        write_json(manifest, state)

    ready = [m for m in messages if m["work_id"] == work_id and m["source_version"] == version
             and m["kind"] == "review_ready"]
    if ready:
        return {"status": "already_recorded", "draft_path": str(draft),
                "outbox_count": len(messages), "original_delivery_id": ready[0]["delivery_id"]}
    if fail_at == "outbox":
        return {"status": "outbox_failed", "reason": "injected_before_write",
                "draft_path": str(draft), "outbox_count": len(messages)}
    message = {"kind": "review_ready", "work_id": work_id, "source_version": version,
               "draft_path": str(draft), "draft_sha256": expected_digest,
               "reviewer": "レビュー担当", "delivery_id": delivery_id, "trigger": trigger,
               "meaning": "保存済み下書きを開ける。人のレビュー・承認は未実施"}
    messages.append(message)
    write_json(outbox, messages)
    if json.loads(outbox.read_text(encoding="utf-8")) != messages:
        return {"status": "outbox_failed", "reason": "readback_mismatch"}
    state["state"] = "review_waiting_outbox_recorded"
    write_json(manifest, state)
    return {"status": "review_waiting_outbox_recorded", "draft_path": str(draft),
            "outbox_count": len(messages), "delivery_id": delivery_id}


def run(run_root):
    # Use a fresh output directory; never merge an older trial implicitly.
    run_root.mkdir(parents=True, exist_ok=False)
    cases = {}
    common = run_root / "N_D"
    cases["N"] = process(record(), "evt-100", "manual", common)
    cases["D"] = process(record(), "evt-101", "state_change", common)
    cases["M"] = process(record(missing={"R03"}), "evt-200", "manual", run_root / "M")
    cases["S"] = process(record(), "evt-300", "manual", run_root / "S", fail_at="save")
    failure_space = run_root / "F"
    cases["F_initial"] = process(record(), "evt-400", "manual", failure_space, fail_at="outbox")
    cases["F_resume"] = process(record(), "evt-401", "resume", failure_space)
    cases["O"] = process(record(version="v0", current="v1"), "evt-500", "manual", run_root / "O")
    cases["X"] = process(record(), "evt-600", "manual", run_root / "X",
                         operation="approve_and_send_externally")

    assert cases["N"]["status"] == "review_waiting_outbox_recorded"
    assert cases["D"]["status"] == "already_recorded" and cases["D"]["outbox_count"] == 1
    assert cases["M"]["missing"] == ["R03"] and not list((run_root / "M").glob("*.md"))
    assert cases["S"]["status"] == "save_failed" and not (run_root / "S" / "outbox.json").exists()
    assert cases["F_initial"]["status"] == "outbox_failed" and cases["F_initial"]["outbox_count"] == 0
    assert cases["F_resume"]["status"] == "review_waiting_outbox_recorded"
    assert len(list(failure_space.glob("*.md"))) == 1
    assert cases["O"]["status"] == "stale" and not list((run_root / "O").glob("*.md"))
    assert cases["X"]["status"] == "denied" and not list((run_root / "X").glob("*.md"))
    write_json(run_root / "observations.json", cases)
    print(json.dumps(cases, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="new, non-existing output directory")
    args = parser.parse_args()
    target = args.output if args.output else Path(tempfile.mkdtemp(prefix="fde-action-")) / "run"
    run(target)
