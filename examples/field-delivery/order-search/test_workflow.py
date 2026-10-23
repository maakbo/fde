"""Branch and handoff tests; fake verifier outcomes are not real Java test results."""
import copy
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import workflow


class DevelopmentWorkflow(unittest.TestCase):
    def setUp(self):
        self.request = workflow.create_request()
        # Synthetic SE handoff for the test, not authority inferred from a snapshot.
        self.request["conditions_confirmed"] = True
        self.calls = 0

    def succeeded(self):
        self.calls += 1
        return 0, "fixture: completed checks"

    def test_complete_request_runs_and_returns_to_review(self):
        result = workflow.execute(self.request, self.succeeded)
        self.assertEqual(result["state"], "awaiting_review")
        self.assertEqual(result["conditions"], list(workflow.CONDITIONS))
        self.assertEqual(result["sources"], self.request["sources"])
        self.assertEqual(self.calls, 1)

    def test_missing_false_and_unknown_conditions_do_not_execute(self):
        variants = []
        for field in ("sources", "conditions", "action"):
            request = copy.deepcopy(self.request); del request[field]; variants.append(request)
        for value in (False, "false", None, 0):
            request = copy.deepcopy(self.request); request["conditions_confirmed"] = value; variants.append(request)
        request = copy.deepcopy(self.request); request["unresolved"] = ["R2 date meaning"]; variants.append(request)
        request = copy.deepcopy(self.request); request["conditions"] = ["R1", "R5"]; variants.append(request)
        for request in variants:
            with self.subTest(request=request):
                self.assertEqual(workflow.execute(request, self.succeeded)["state"], "needs_input")
        self.assertEqual(self.calls, 0)

    def test_unknown_trigger_or_forbidden_action_does_not_execute(self):
        for field, value in (("trigger", "webhook"), ("action", "deploy_production")):
            request = copy.deepcopy(self.request); request[field] = value
            self.assertEqual(workflow.execute(request, self.succeeded)["state"], "blocked")
        self.assertEqual(self.calls, 0)

    def test_stale_handoff_must_be_reconfirmed(self):
        self.request["sources"]["requirements.md"] = "older-revision"
        self.assertEqual(workflow.execute(self.request, self.succeeded)["state"], "needs_input")
        self.assertEqual(self.calls, 0)
        fresh = workflow.create_request()
        fresh["conditions_confirmed"] = True
        self.assertEqual(workflow.execute(fresh, self.succeeded)["state"], "awaiting_review")

    def test_failed_verification_is_not_success_or_infinite_retry(self):
        def failed():
            self.calls += 1
            return 1, "fixture: check failed"
        result = workflow.execute(self.request, failed)
        self.assertEqual(result["state"], "failed")
        self.assertEqual(self.calls, 1)

    def test_context_preserves_conditions_without_all_history(self):
        packet = workflow.prepare(self.request)
        self.assertEqual(set(packet["sources"]), set(workflow.SOURCES))
        self.assertIn("R2 includes both boundary dates", packet["decisions"])
        self.assertIn("no merge", packet["limits"])
        self.assertNotIn("conversation", packet)

    def test_absent_source_stops_before_verification(self):
        with patch.object(workflow, "snapshot", side_effect=OSError("unavailable")):
            self.assertEqual(workflow.execute(self.request, self.succeeded)["state"], "needs_input")
        self.assertEqual(self.calls, 0)

    def test_changed_sources_during_run_invalidate_result(self):
        changed = dict(self.request["sources"])
        changed["requirements.md"] = "changed-during-run"
        with patch.object(workflow, "snapshot", side_effect=[self.request["sources"], changed]):
            self.assertEqual(workflow.execute(self.request, self.succeeded)["state"], "needs_input")
        self.assertEqual(self.calls, 1)

    def test_executor_or_handoff_changes_invalidate_existing_request(self):
        for changed_file in ("workflow.py", "work-handoff.md"):
            with self.subTest(changed_file=changed_file), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                for name in set(workflow.SOURCES) | {changed_file}:
                    (root / name).write_text("initial")
                with patch.object(workflow, "ROOT", root):
                    request = workflow.create_request()
                    request["conditions_confirmed"] = True
                    (root / changed_file).write_text("revised contract")
                    self.assertEqual(workflow.execute(request, self.succeeded)["state"], "needs_input")
        self.assertEqual(self.calls, 0)

    def test_unsupported_execution_environment_starts_no_process(self):
        with patch.object(workflow.os, "name", "nt"), patch.object(workflow.subprocess, "Popen") as spawn:
            self.assertEqual(workflow.execute(self.request)["state"], "blocked")
            code, _ = workflow.local_checks()
            self.assertNotEqual(code, 0)
            spawn.assert_not_called()


if __name__ == "__main__":
    unittest.main()
