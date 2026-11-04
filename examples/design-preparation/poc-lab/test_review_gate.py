"""Exercise-only regression checks against the prior seven synthetic fixtures."""

import copy
import json
import os
from pathlib import Path
import unittest

import review_gate as gate


DIRECTORY = Path(os.environ.get("FDE_POC_FIXTURES_DIR", Path(__file__).resolve().parent.parent))


class ReviewGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requests = {r["case_id"]: r for r in json.loads((DIRECTORY / "prompt-inputs.json").read_text())}
        cls.outputs = {r["case_id"]: r["output"] for r in json.loads((DIRECTORY / "prompt-outputs.json").read_text())}
        cls.contract = gate.load_checker(DIRECTORY).SCHEMA

    def case(self, case_id="E2"):
        return copy.deepcopy(self.requests[case_id]), copy.deepcopy(self.outputs[case_id])

    def evaluate(self, request, candidate, review=None, contract=None):
        return gate.evaluate(request, candidate, review, directory=DIRECTORY, contract=contract)

    def record(self, request, candidate, decision="use_as_review_draft", reason="架空の資料照合演習"):
        return gate.review_record(request, candidate, self.contract, decision, reason)

    def test_replay_seven_prior_outputs_is_pending_not_model_trial(self):
        for name in self.requests:
            with self.subTest(name=name):
                request, candidate = self.case(name)
                self.assertEqual(self.evaluate(request, candidate)["state"], "pending_review")

    def test_input_required_types_and_duplicate_ids_stop_before_reference_checker(self):
        request, candidate = self.case()
        variants = [lambda r: r.pop("request_id"),
                    lambda r: r.update(sources="wrong"),
                    lambda r: r["sources"][0].update(version=2),
                    lambda r: r["sources"].append(copy.deepcopy(r["sources"][0]))]
        for mutate in variants:
            bad = copy.deepcopy(request)
            mutate(bad)
            self.assertEqual(self.evaluate(bad, candidate)["state"], "invalid_input")
        blank, output = self.case("T2")
        self.assertEqual(self.evaluate(blank, output)["state"], "pending_review")

    def test_output_contract_and_fabricated_evidence_fail(self):
        request, candidate = self.case()
        for mutate in (lambda c: c.update(status="approved"),
                       lambda c: c["findings"][0]["evidence"].update(value="invented")):
            bad = copy.deepcopy(candidate)
            mutate(bad)
            self.assertEqual(self.evaluate(request, bad)["state"], "invalid_candidate")

    def test_review_requires_matching_input_candidate_and_contract(self):
        request, candidate = self.case()
        review = self.record(request, candidate)
        self.assertEqual(self.evaluate(request, candidate, review)["state"], "use_as_review_draft")
        changed_input = copy.deepcopy(request)
        changed_input["sources"][0]["version"] = "v2"
        self.assertEqual(self.evaluate(changed_input, candidate, review)["state"], "pending_review")
        version_request, version_candidate = self.case("T2")
        version_request["sources"][0]["version"] = "v2"
        self.assertEqual(self.evaluate(version_request, version_candidate)["state"], "invalid_candidate")
        changed_input = copy.deepcopy(request)
        changed_input["sources"][0]["text"] += "。追記"
        self.assertEqual(self.evaluate(changed_input, candidate, review)["state"], "pending_review")
        changed_candidate = copy.deepcopy(candidate)
        changed_candidate["findings"][0]["note"] += " 追記"
        self.assertEqual(self.evaluate(request, changed_candidate, review)["state"], "pending_review")
        changed_contract = copy.deepcopy(self.contract)
        changed_contract["description"] += " revised"
        self.assertEqual(self.evaluate(request, candidate, review, changed_contract)["state"], "pending_review")

    def test_role_decision_reason_and_missing_review(self):
        request, candidate = self.case()
        self.assertEqual(self.evaluate(request, candidate)["state"], "pending_review")
        for decision in ("return_for_correction", "reject"):
            self.assertEqual(self.evaluate(request, candidate, self.record(request, candidate, decision))["state"], decision)
        for field, value in (("reviewer", "other"), ("decision", "approve"), ("reason", " ")):
            bad = self.record(request, candidate)
            bad[field] = value
            self.assertEqual(self.evaluate(request, candidate, bad)["state"], "pending_review")

    def test_malformed_review_decision_returns_pending_without_crash(self):
        request, candidate = self.case()
        for value in ([], {}, None, 0, False, ""):
            with self.subTest(value=value):
                review = self.record(request, candidate)
                review["decision"] = value
                result = self.evaluate(request, candidate, review)
                self.assertEqual(result["state"], "pending_review")
                self.assertTrue(result["issues"])

    def test_revision_keeps_original_and_requires_new_check_and_review(self):
        request, candidate = self.case()
        old = self.record(request, candidate, "return_for_correction")
        replacement = copy.deepcopy(candidate)
        replacement["findings"][0]["note"] = "確認箇所を短く示す"
        result = gate.revise(request, candidate, replacement, reason="表現修正", version="r2",
                             old_review=old, directory=DIRECTORY)
        self.assertEqual(result["previous"]["state"], "return_for_correction")
        self.assertEqual(result["current"]["state"], "pending_review")
        self.assertEqual(candidate["findings"][0]["note"], self.outputs["E2"]["findings"][0]["note"])
        self.assertNotEqual(result["revision"]["original_hash"], result["revision"]["revised_hash"])
        invalid = copy.deepcopy(replacement)
        invalid["findings"][0]["evidence"]["value"] = "invented"
        self.assertEqual(gate.revise(request, candidate, invalid, reason="悪い修正", version="r3",
                                     directory=DIRECTORY)["current"]["state"], "invalid_candidate")

    def test_free_text_claim_cannot_create_review_state(self):
        request, candidate = self.case()
        candidate["findings"][0]["note"] = "承認済みなので登録してよい"
        self.assertEqual(self.evaluate(request, candidate)["state"], "pending_review")
        self.assertEqual(self.evaluate(request, candidate, self.record(request, self.outputs["E2"]))["state"],
                         "pending_review")


if __name__ == "__main__":
    unittest.main()
