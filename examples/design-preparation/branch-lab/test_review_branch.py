import copy
import unittest

from review_branch import plan_review


POLICY = {
    "full_review_from": 4,
    "source_version": "v1",
    "route_rules": [
        {"change_kind": "api", "route": "api-review"},
        {"change_kind": "ui", "route": "ui-review"},
        {"change_kind": "data", "route": "data-review"},
    ],
}


def source(source_id="S1", **changes):
    item = {"id": source_id, "version": "v1", "scope": "api", "state": "approved", "allowed": True}
    item.update(changes)
    return item


def payload(**changes):
    item = {
        "work_id": "WORK-7",
        "revision": "r2",
        "change_kind": "api",
        "risk_points": 3,
        "breaking_change": False,
        "source_retrieval": "available",
        "sources": [source()],
    }
    item.update(changes)
    return item


class ReviewBranchTests(unittest.TestCase):
    def test_normal_routes(self):
        for kind in ("api", "ui", "data"):
            with self.subTest(kind=kind):
                result = plan_review(payload(change_kind=kind, sources=[source(scope=kind)]), POLICY)
                self.assertEqual(result["status"], "review_packet_ready")
                self.assertEqual(result["route"], f"{kind}-review")
                self.assertEqual(result["depth"], "standard")
                self.assertTrue(result["pending_human_review"])
                self.assertFalse(result["authorization"])

    def test_threshold_boundary_and_breaking_change(self):
        for points, depth in ((3, "standard"), (4, "full"), (5, "full")):
            with self.subTest(points=points):
                self.assertEqual(plan_review(payload(risk_points=points), POLICY)["depth"], depth)
        self.assertEqual(plan_review(payload(risk_points=0, breaking_change=False), POLICY)["depth"], "standard")
        self.assertEqual(plan_review(payload(risk_points=0, breaking_change=True), POLICY)["depth"], "full")

    def test_invalid_required_values(self):
        for field, value in (("risk_points", None), ("risk_points", True), ("risk_points", "4"),
                             ("breaking_change", None), ("breaking_change", 0),
                             ("change_kind", None), ("work_id", None)):
            with self.subTest(field=field, value=value):
                result = plan_review(payload(**{field: value}), POLICY)
                self.assertEqual(result["status"], "invalid_input")
                self.assertFalse(result["pending_human_review"])
        for field in ("risk_points", "breaking_change", "sources"):
            with self.subTest(missing=field):
                item = payload()
                del item[field]
                self.assertEqual(plan_review(item, POLICY)["status"], "invalid_input")
        for threshold in (None, True, "4"):
            changed = {**POLICY, "full_review_from": threshold}
            self.assertEqual(plan_review(payload(), changed)["status"], "invalid_input")

    def test_unknown_and_conflicting_route(self):
        self.assertEqual(plan_review(payload(change_kind="ops"), POLICY)["status"], "unknown_category")
        changed = copy.deepcopy(POLICY)
        changed["route_rules"].append({"change_kind": "api", "route": "other-review"})
        self.assertEqual(plan_review(payload(), changed)["status"], "conflicting_routes")

    def test_selects_per_item_with_all_exclusion_reasons(self):
        items = [source(), source("S2", allowed=False), source("S3", scope="ui"),
                 source("S4", state="draft"), source("S5", version="v2")]
        result = plan_review(payload(sources=items), POLICY)
        self.assertEqual(result["selected_source_ids"], ["S1"])
        self.assertEqual(result["excluded_sources"], [
            {"id": "S2", "reasons": ["not_allowed"]},
            {"id": "S3", "reasons": ["scope_mismatch"]},
            {"id": "S4", "reasons": ["not_approved"]},
            {"id": "S5", "reasons": ["version_mismatch"]},
        ])

    def test_all_excluded_and_unknown_metadata(self):
        result = plan_review(payload(sources=[source(allowed=False)]), POLICY)
        self.assertEqual(result["status"], "sources_excluded")
        self.assertEqual(result["retained_work"], {"id": "WORK-7", "revision": "r2"})
        self.assertFalse(result["pending_human_review"])
        for item in (source(scope="ops"), source(state="unknown"), source(allowed="yes"),
                     source(scope=[]), {**source(), "extra": "unknown"}):
            with self.subTest(item=item):
                result = plan_review(payload(sources=[source(), item]), POLICY)
                self.assertEqual(result["status"], "clarification_needed")
                self.assertEqual(result["selected_source_ids"], [])

    def test_retrieval_failure_is_manual_fallback_without_proceeding(self):
        item = payload(source_retrieval="unavailable")
        del item["sources"]
        result = plan_review(item, POLICY)
        self.assertEqual(result["status"], "source_unavailable")
        self.assertEqual(result["reason"], "manual_source_retrieval_fallback")
        self.assertEqual(result["retained_work"], {"id": "WORK-7", "revision": "r2"})
        self.assertIsNone(result["route"])
        self.assertFalse(result["pending_human_review"])

    def test_missing_retrieval_state_cannot_become_ready(self):
        item = payload()
        del item["source_retrieval"]
        result = plan_review(item, POLICY)
        self.assertEqual(result["status"], "invalid_input")
        self.assertIsNone(result["route"])
        self.assertFalse(result["pending_human_review"])
        self.assertFalse(result["authorization"])

    def test_inputs_are_not_mutated(self):
        item, policy = payload(), copy.deepcopy(POLICY)
        originals = copy.deepcopy((item, policy))
        plan_review(item, policy)
        self.assertEqual((item, policy), originals)


if __name__ == "__main__":
    unittest.main()
