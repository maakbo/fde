"""Independent v2 branch cases; run from an fde clone.

python3 examples/design-preparation/branch-lab/test_forward.py
python3 examples/design-preparation/branch-lab/test_forward.py --module examples/design-preparation/branch-lab/review_branch.py
"""

import argparse
import copy
import importlib.util
from pathlib import Path
import unittest


parser = argparse.ArgumentParser()
parser.add_argument(
    "--module",
    default=str(Path(__file__).with_name("review_branch.py")),
    help="Path to review_branch.py, relative to cwd or absolute",
)
arguments, _unknown = parser.parse_known_args()
spec = importlib.util.spec_from_file_location("review_branch_forward", Path(arguments.module))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

POLICY = {
    "full_review_from": 7,
    "source_version": "v2",
    "route_rules": [
        {"change_kind": kind, "route": f"{kind}-review"}
        for kind in ("api", "ui", "data")
    ],
}


def source(source_id, scope, allowed=True, version="v2", state="approved"):
    return {
        "id": source_id,
        "version": version,
        "scope": scope,
        "state": state,
        "allowed": allowed,
    }


def payload(kind="ui", points=6, breaking=False, sources=None):
    return {
        "work_id": "ORDER-SEARCH-9",
        "revision": "r3",
        "change_kind": kind,
        "risk_points": points,
        "breaking_change": breaking,
        "source_retrieval": "available",
        "sources": [source("U2", "ui")] if sources is None else sources,
    }


MIXED = [
    source("U2", "ui"),
    source("A-denied", "api", allowed=False),
    source("D-old", "data", version="v1"),
    source("A-v2", "api"),
]


class IndependentV2Cases(unittest.TestCase):
    def check_case(self, item, **expected):
        before = copy.deepcopy((item, POLICY))
        result = module.plan_review(item, POLICY)
        for field, value in expected.items():
            self.assertEqual(result[field], value, field)
        self.assertEqual(result["retained_work"], {"id": "ORDER-SEARCH-9", "revision": "r3"})
        self.assertIs(result["authorization"], False)
        self.assertIs(result["pending_human_review"], result["status"] == "review_packet_ready")
        self.assertEqual((item, POLICY), before)
        return result

    def test_ui_mixed_6(self):
        self.check_case(
            payload(sources=MIXED),
            status="review_packet_ready", route="ui-review", depth="standard",
            selected_source_ids=["U2"],
            excluded_sources=[
                {"id": "A-denied", "reasons": ["not_allowed", "scope_mismatch"]},
                {"id": "D-old", "reasons": ["scope_mismatch", "version_mismatch"]},
                {"id": "A-v2", "reasons": ["scope_mismatch"]},
            ],
        )

    def test_api_threshold_7(self):
        self.check_case(
            payload("api", 7, sources=[source("A2", "api")]),
            status="review_packet_ready", route="api-review", depth="full",
            selected_source_ids=["A2"],
        )

    def test_data_above_8(self):
        self.check_case(
            payload("data", 8, sources=[source("D2", "data")]),
            status="review_packet_ready", route="data-review", depth="full",
            selected_source_ids=["D2"],
        )

    def test_false_and_zero(self):
        self.check_case(
            payload(points=0, breaking=False),
            status="review_packet_ready", route="ui-review", depth="standard",
            selected_source_ids=["U2"],
        )

    def test_duplicate_ids(self):
        self.check_case(
            payload(sources=[source("SAME", "ui"), source("SAME", "api")]),
            status="clarification_needed", route=None, selected_source_ids=[],
        )

    def test_all_excluded(self):
        self.check_case(
            payload(sources=[source("A2", "api"), source("D-old", "data", False, "v1")]),
            status="sources_excluded", route=None, selected_source_ids=[],
        )

    def test_null_points(self):
        self.check_case(payload(points=None), status="invalid_input", route=None)

    def test_null_breaking(self):
        self.check_case(payload(breaking=None), status="invalid_input", route=None)

    def test_unknown_kind(self):
        self.check_case(payload("ops"), status="unknown_category", route=None)

    def test_retrieval_unavailable(self):
        item = payload()
        item["source_retrieval"] = "unavailable"
        del item["sources"]
        self.check_case(
            item, status="source_unavailable", route=None,
            reason="manual_source_retrieval_fallback",
        )

    def test_retrieval_missing(self):
        item = payload()
        del item["source_retrieval"]
        self.check_case(
            item, status="invalid_input", route=None,
            reason="invalid_source_retrieval_state", selected_source_ids=[],
        )

    def test_same_payload_twice(self):
        item = payload(sources=MIXED)
        before = copy.deepcopy((item, POLICY))
        self.assertEqual(module.plan_review(item, POLICY), module.plan_review(item, POLICY))
        self.assertEqual((item, POLICY), before)


if __name__ == "__main__":
    unittest.main(argv=["forward-test"], verbosity=2)
