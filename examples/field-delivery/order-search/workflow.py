"""Local development handoff demonstration, not a scheduler or agent service."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import signal
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
SOURCES = ("requirements.md", "design.md", "OrderSearchService.java", "OrderSearchServer.java",
           "OrderSearchTest.java", "acceptance.py", "run.py", "workflow.py", "work-handoff.md")
CONDITIONS = ("R1", "R2", "R3", "R4", "R5", "R6")


def snapshot():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES}


def create_request():
    return {
        "work_id": "order-search-local-review", "trigger": "manual_handoff",
        "action": "verify_local", "conditions_confirmed": False,
        "unresolved": [], "conditions": list(CONDITIONS), "sources": snapshot()
    }


def prepare(request):
    if not isinstance(request, dict):
        return {"state": "needs_input", "reason": "request must be an object", "owner": "SE"}
    required = {"work_id", "trigger", "action", "conditions_confirmed", "unresolved", "conditions", "sources"}
    if not required <= request.keys():
        return {"state": "needs_input", "reason": "missing handoff fields", "owner": "SE"}
    if (not isinstance(request["work_id"], str) or not request["work_id"].strip()
            or type(request["conditions_confirmed"]) is not bool
            or not isinstance(request["unresolved"], list)
            or not all(isinstance(x, str) for x in request["unresolved"])
            or not isinstance(request["conditions"], list)
            or not all(isinstance(x, str) for x in request["conditions"])
            or not isinstance(request["sources"], dict)):
        return {"state": "needs_input", "reason": "invalid field types", "owner": "SE"}
    if request["trigger"] != "manual_handoff":
        return {"state": "blocked", "reason": "only manual handoff is installed", "owner": "workflow owner"}
    if request["action"] != "verify_local":
        return {"state": "blocked", "reason": "action outside local verification scope", "owner": "decision owner"}
    if not request["conditions_confirmed"] or request["unresolved"]:
        return {"state": "needs_input", "reason": "conditions require confirmation", "owner": "SE"}
    if sorted(request["conditions"]) != sorted(CONDITIONS):
        return {"state": "needs_input", "reason": "acceptance conditions differ", "owner": "SE"}
    try:
        current_sources = snapshot()
    except OSError:
        return {"state": "needs_input", "reason": "source file unavailable", "owner": "SE/developer"}
    if request["sources"] != current_sources:
        return {"state": "needs_input", "reason": "source revision changed or missing", "owner": "SE/developer"}
    return {
        "state": "ready", "work_id": request["work_id"], "action": "verify_local",
        "sources": dict(request["sources"]), "conditions": list(request["conditions"]),
        "goal": "Check implementation against agreed search behavior; return evidence for review",
        "decisions": ["R2 includes both boundary dates", "R5 empty results are normal",
                      "Use plain Java classes; requirements are not changed by a test result"],
        "tools": {"command": [sys.executable, "run.py"], "environment": "JDK16+, Python3, localhost only"},
        "limits": ["no external data", "no merge", "no production deployment"],
        "return": "executed checks, evidence, unresolved items and recipient; human review remains",
        "resume": "reconfirm changed sources and unresolved conditions before a new run"
    }


def local_checks(timeout=90):
    if os.name != "posix":
        return -1, "local workflow execution requires POSIX; no process was started"
    process = None
    try:
        process = subprocess.Popen([sys.executable, str(ROOT / "run.py")], cwd=ROOT,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                   start_new_session=True)
        output, _ = process.communicate(timeout=timeout)
        return process.returncode, output
    except subprocess.TimeoutExpired:
        return -1, "local verification timed out; process cleanup requested"
    except OSError as error:
        return -1, str(error)
    finally:
        if process is not None and process.poll() is None:
            # Stop only the process group created for this local run on POSIX.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.communicate()


def execute(request, verifier=None):
    packet = prepare(request)
    if packet["state"] != "ready":
        return packet
    if verifier is None:
        if os.name != "posix":
            return {"state": "blocked", "reason": "local execution requires a POSIX environment",
                    "owner": "workflow owner"}
        verifier = local_checks
    code, output = verifier()
    try:
        current_sources = snapshot()
    except OSError:
        return {"state": "needs_input", "reason": "source unavailable after execution",
                "owner": "SE/developer", "output": output}
    if packet["sources"] != current_sources:
        return {"state": "needs_input", "reason": "sources changed during execution",
                "owner": "SE/developer", "output": output}
    if code != 0:
        return {"state": "failed", "reason": "local verification failed; no automatic retry",
                "owner": "developer", "exit_code": code, "output": output}
    return {"state": "awaiting_review", "work_id": packet["work_id"], "sources": packet["sources"],
            "conditions": packet["conditions"], "output": output, "owner": "reviewer",
            "next": "inspect evidence and remaining limitations; this does not authorize release"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("request", nargs="?", type=Path)
    parser.add_argument("--new-request", action="store_true", help="print a snapshot to inspect before handoff")
    parser.add_argument("--execute", action="store_true", help="run the fixed local tests after validation")
    args = parser.parse_args()
    if args.new_request:
        print(json.dumps(create_request(), ensure_ascii=False, indent=2))
        return
    if args.request is None:
        parser.error("request JSON is required")
    try:
        request = json.loads(args.request.read_text())
    except (OSError, json.JSONDecodeError) as error:
        print(json.dumps({"state": "needs_input", "reason": str(error)}, ensure_ascii=False))
        sys.exit(2)
    result = execute(request) if args.execute else prepare(request)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["state"] not in ("ready", "awaiting_review"):
        sys.exit(2)


if __name__ == "__main__":
    main()
