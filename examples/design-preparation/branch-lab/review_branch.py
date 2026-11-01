"""Fictional team's deterministic preparation of a software change review.

This module only returns a proposed review packet. It performs no I/O and
cannot approve a change or complete a review.
"""

from __future__ import annotations

from copy import deepcopy


CHANGE_KINDS = {"api", "ui", "data"}
SOURCE_STATES = {"approved", "draft", "retired"}
SOURCE_FIELDS = {"id", "version", "scope", "state", "allowed"}


def _nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def _base(payload):
    """Retain the supplied work identity even when another field is invalid."""
    return {
        "status": None,
        "reason": None,
        "route": None,
        "depth": None,
        "selected_source_ids": [],
        "excluded_sources": [],
        "clarification": [],
        "retained_work": {
            "id": payload.get("work_id") if isinstance(payload, dict) else None,
            "revision": payload.get("revision") if isinstance(payload, dict) else None,
        },
        "pending_human_review": False,
        "authorization": False,
    }


def _stop(result, status, reason):
    result["status"] = status
    result["reason"] = reason
    return result


def plan_review(payload, policy):
    """Return an auditable review preparation decision without side effects.

    ``sources`` is either a list of source metadata records, or absent when
    ``source_retrieval`` is ``"unavailable"``. Each record has exactly id,
    version, scope, state, and allowed. No record content is fetched.
    """
    result = _base(payload)
    if not isinstance(payload, dict) or not isinstance(policy, dict):
        return _stop(result, "invalid_input", "payload_and_policy_must_be_objects")

    if not _nonempty_string(payload.get("work_id")) or not _nonempty_string(payload.get("revision")):
        return _stop(result, "invalid_input", "missing_or_invalid_work_identity")

    kind = payload.get("change_kind")
    if not _nonempty_string(kind):
        return _stop(result, "invalid_input", "missing_or_invalid_change_kind")
    if kind not in CHANGE_KINDS:
        return _stop(result, "unknown_category", "unknown_change_kind")

    points = payload.get("risk_points")
    breaking = payload.get("breaking_change")
    if type(points) is not int or not 0 <= points <= 10:
        return _stop(result, "invalid_input", "risk_points_must_be_integer_0_to_10")
    if type(breaking) is not bool:
        return _stop(result, "invalid_input", "breaking_change_must_be_boolean")

    threshold = policy.get("full_review_from")
    if type(threshold) is not int or not 0 <= threshold <= 10:
        return _stop(result, "invalid_input", "invalid_full_review_from")
    source_version = policy.get("source_version")
    if not _nonempty_string(source_version):
        return _stop(result, "invalid_input", "invalid_source_version")
    rules = policy.get("route_rules")
    if not isinstance(rules, list):
        return _stop(result, "invalid_input", "invalid_route_rules")

    routes = []
    for rule in rules:
        if not isinstance(rule, dict) or set(rule) != {"change_kind", "route"}:
            return _stop(result, "invalid_input", "invalid_route_rule")
        rule_kind, route = rule["change_kind"], rule["route"]
        if not _nonempty_string(rule_kind) or not _nonempty_string(route):
            return _stop(result, "invalid_input", "invalid_route_rule")
        if rule_kind not in CHANGE_KINDS:
            return _stop(result, "unknown_category", "unknown_route_category")
        if rule_kind == kind:
            routes.append(route)
    if len(set(routes)) > 1:
        return _stop(result, "conflicting_routes", "conflicting_route_rules")
    if not routes:
        return _stop(result, "invalid_input", "missing_route_rule")
    route = routes[0]
    if route != f"{kind}-review":
        return _stop(result, "invalid_input", "route_does_not_match_policy_v1")

    if payload.get("source_retrieval") == "unavailable":
        return _stop(result, "source_unavailable", "manual_source_retrieval_fallback")
    if payload.get("source_retrieval") != "available":
        return _stop(result, "invalid_input", "invalid_source_retrieval_state")
    sources = payload.get("sources")
    if not isinstance(sources, list):
        return _stop(result, "invalid_input", "missing_or_invalid_sources")

    seen_ids = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict) or set(source) != SOURCE_FIELDS:
            result["clarification"].append({"index": index, "metadata": deepcopy(source)})
            return _stop(result, "clarification_needed", f"unknown_source_metadata_at_{index}")
        source_id = source["id"]
        if not _nonempty_string(source_id) or source_id in seen_ids:
            result["clarification"].append({"index": index, "metadata": deepcopy(source)})
            return _stop(result, "clarification_needed", f"invalid_or_duplicate_source_id_at_{index}")
        seen_ids.add(source_id)
        if (
            not _nonempty_string(source["version"])
            or not isinstance(source["scope"], str)
            or source["scope"] not in CHANGE_KINDS
            or not isinstance(source["state"], str)
            or source["state"] not in SOURCE_STATES
            or type(source["allowed"]) is not bool
        ):
            result["clarification"].append({"index": index, "metadata": deepcopy(source)})
            return _stop(result, "clarification_needed", f"unknown_source_metadata_at_{index}")

    for source in sources:
        source_id = source["id"]
        reasons = []
        if source["allowed"] is False:
            reasons.append("not_allowed")
        if source["scope"] != kind:
            reasons.append("scope_mismatch")
        if source["state"] != "approved":
            reasons.append("not_approved")
        if source["version"] != source_version:
            reasons.append("version_mismatch")
        if reasons:
            result["excluded_sources"].append({"id": source_id, "reasons": reasons})
        else:
            result["selected_source_ids"].append(source_id)

    if not result["selected_source_ids"]:
        return _stop(result, "sources_excluded", "no_eligible_sources")
    result["status"] = "review_packet_ready"
    result["route"] = route
    result["depth"] = "full" if breaking or points >= threshold else "standard"
    result["pending_human_review"] = True
    return result
