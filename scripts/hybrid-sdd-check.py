#!/usr/bin/env python3
"""Deterministic checks for the hybrid SDD public contract."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, NoReturn

CLASSES = {"engineering", "agent-system", "campaign-architecture", "creative-system"}
ROUTES = {"full-sdd", "existing-skill"}
FORBIDDEN_AGENCY = {
    "mandatory_allegiance", "authored_player_decision", "fixed_scene_sequence",
    "fixed_ending", "predetermined_route", "required_player_choice",
}
CANON_STATES = {"unchanged", "proposal", "accepted-truth"}
ACCEPTANCE = {"not-required", "pending", "accepted", "modified", "rejected"}


def fail(message: str) -> NoReturn:
    raise ValueError(message)


def load(path: Path) -> list[dict[str, Any]]:
    if path.is_dir():
        paths = sorted(path.glob("*.json"))
        if not paths:
            fail(f"no JSON fixtures in {path}")
        result: list[dict[str, Any]] = []
        for child in paths:
            result.extend(load(child))
        return result
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {path}: {exc}")
    if isinstance(value, list):
        records = value
    elif isinstance(value, dict):
        records = value.get("cases", value.get("records", [value]))
    else:
        fail(f"{path} must contain an object or array")
    if not isinstance(records, list) or not all(isinstance(x, dict) for x in records):
        fail(f"{path} records must be objects")
    return records


def text_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value.lower()]
    if isinstance(value, dict):
        result: list[str] = []
        for key, item in value.items():
            result.append(str(key).lower())
            result.extend(text_values(item))
        return result
    if isinstance(value, list):
        result = []
        for item in value:
            result.extend(text_values(item))
        return result
    return [str(value).lower()]


def classify(record: dict[str, Any]) -> dict[str, str]:
    kind = str(record.get("request_kind", "")).lower()
    request = " ".join(text_values(record.get("request", "")))
    if kind in {"mixed", "mixed-request"} or "mixed" in request:
        return {"work_class": "mixed", "route": "split"}
    if kind in {"routine-content", "routine-npc", "npc"} or "ordinary npc" in request:
        return {"work_class": "routine-content", "route": "existing-skill"}
    if kind in {"entity-collision", "proposed-canon", "canon-boundary"}:
        return {"work_class": "campaign-architecture", "route": "full-sdd"}
    if kind in CLASSES:
        return {"work_class": kind, "route": "full-sdd"}
    if any(word in request for word in ("skill", "agent", "wiki behavior", "harness")):
        return {"work_class": "agent-system", "route": "full-sdd"}
    if any(word in request for word in ("regional conflict", "multi-session", "campaign structure")):
        return {"work_class": "campaign-architecture", "route": "full-sdd"}
    if any(word in request for word in ("reputation system", "faction turn", "quest system", "encounter system")):
        return {"work_class": "creative-system", "route": "full-sdd"}
    return {"work_class": "engineering", "route": "full-sdd"}


def check_classification(records: list[dict[str, Any]]) -> None:
    if not records:
        fail("classification fixture is empty")
    for record in records:
        expected = record.get("expected")
        if not isinstance(expected, dict):
            fail(f"{record.get('scenario_id', '?')}: expected route is required")
        actual = classify(record)
        wanted_class = str(expected.get("work_class", ""))
        wanted_route = str(expected.get("route", ""))
        if wanted_class or wanted_route:
            if actual != {"work_class": wanted_class, "route": wanted_route}:
                fail(f"{record.get('scenario_id', '?')}: expected {wanted_class}/{wanted_route}, got {actual}")
        elif actual != {"work_class": "mixed", "route": "split"}:
            fail(f"{record.get('scenario_id', '?')}: expected mixed/split, got {actual}")
        if not expected.get("reason_contains"):
            fail(f"{record.get('scenario_id', '?')}: rationale boundary is required")
        if not expected.get("scope_boundary"):
            fail(f"{record.get('scenario_id', '?')}: scope boundary is required")
        if wanted_class in CLASSES and wanted_route != "full-sdd":
            fail(f"{record.get('scenario_id', '?')}: substantial work must use full-sdd")
        if wanted_class == "routine-content" and wanted_route != "existing-skill":
            fail(f"{record.get('scenario_id', '?')}: routine content must use existing-skill")
        if wanted_class in {"mixed", ""} and actual["work_class"] == "mixed":
            slices = record.get("expected", {}).get("slices", record.get("slices"))
            if not isinstance(slices, list) or len(slices) < 2:
                fail(f"{record.get('scenario_id', '?')}: mixed request must split slices")
            routes = {
                item.get("route", item.get("expected", {}).get("route"))
                for item in slices if isinstance(item, dict)
            }
            if routes != {"full-sdd", "existing-skill"}:
                fail(f"{record.get('scenario_id', '?')}: mixed slices need both routes")


def require(record: dict[str, Any], fields: tuple[str, ...], label: str) -> None:
    missing = [field for field in fields if not record.get(field)]
    if missing:
        fail(f"{label}: missing {', '.join(missing)}")


def agency_errors(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_fields = ("value", "actors", "pressures", "open_outcomes", "conditional_possibilities", "independent_motion", "if_nobody_intervenes")
    for field in require_fields:
        if not record.get(field):
            errors.append(f"missing {field}")
    if record.get("player_owned_decisions") is False:
        errors.append("player-owned decisions missing")
    if record.get("continuity") is False:
        errors.append("continuity missing")
    for forbidden in FORBIDDEN_AGENCY:
        if record.get(forbidden) or forbidden in set(text_values(record)):
            errors.append(f"screenplay constraint: {forbidden}")
    for value in text_values(record):
        if any(phrase in value for phrase in ("must join", "must choose", "fixed ending", "scene 1 then scene 2")):
            errors.append("screenplay constraint in evidence")
    return errors


def check_agency(records: list[dict[str, Any]]) -> None:
    for record in records:
        errors = agency_errors(record)
        if record.get("expected_failure"):
            expected = record.get("expected_error", "")
            if not errors or (expected and not any(str(expected).lower() in error.lower() for error in errors)):
                fail(f"{record.get('evidence_id', '?')}: expected agency failure")
        elif errors:
            fail(f"{record.get('evidence_id', '?')}: {'; '.join(errors)}")


def check_canon(records: list[dict[str, Any]]) -> None:
    for record in records:
        label = str(record.get("evidence_id", "canon"))
        if record.get("expected_failure"):
            invalid_write = record.get("writes_fact") and record.get("acceptance") != "accepted"
            invalid_exposure = not record.get("reveal", True) and record.get("visibility") in {"players", "public"}
            if not (invalid_write or invalid_exposure):
                fail(f"{label}: expected canon failure was not represented")
            continue
        state = record.get("canon_state", record.get("state"))
        if state is not None and state not in CANON_STATES:
            fail(f"{label}: invalid canon state {state}")
        acceptance = record.get("acceptance", record.get("dm_acceptance"))
        if acceptance is not None and acceptance not in ACCEPTANCE:
            fail(f"{label}: invalid acceptance state {acceptance}")
        if record.get("equivalent") and record.get("owner_resolution") != "reuse":
            fail(f"{label}: equivalent entity must reuse owner")
        if record.get("uncertain_collision") and record.get("owner_resolution") not in {"ambiguous", "report-collision"}:
            fail(f"{label}: uncertain collision must remain visible")
        if record.get("writes_fact") and acceptance != "accepted":
            fail(f"{label}: accept-before-write violation")
        if record.get("proposal") and state == "accepted-truth" and acceptance != "accepted":
            fail(f"{label}: proposal became accepted truth before DM acceptance")
        if not record.get("reveal") and record.get("visibility") in {"players", "public"}:
            fail(f"{label}: unrevealed material exposed")


def validate_topology(record: dict[str, Any]) -> None:
    label = str(record.get("evidence_id", "topology"))
    nodes = record.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        fail(f"{label}: nodes are required")
    by_id: dict[str, dict[str, Any]] = {}
    for node in nodes:
        if not isinstance(node, dict) or not node.get("id") or not node.get("artifact") or not node.get("owner"):
            fail(f"{label}: each node needs id, artifact, and owner")
        node_id = str(node["id"])
        if node_id in by_id:
            fail(f"{label}: duplicate node {node_id}")
        by_id[node_id] = node
    for node in nodes:
        dependencies = node.get("depends_on", [])
        if not isinstance(dependencies, list):
            fail(f"{label}: depends_on must be a list")
        for dependency in dependencies:
            if dependency not in by_id:
                fail(f"{label}: unresolved dependency {dependency}")
    waves: dict[str, list[dict[str, Any]]] = {}
    for node in nodes:
        waves.setdefault(str(node.get("wave", "serial")), []).append(node)
    for wave, members in waves.items():
        if wave.startswith("parallel"):
            artifacts = [str(member["artifact"]) for member in members]
            if len(artifacts) != len(set(artifacts)):
                fail(f"{label}: parallel wave shares canonical artifact")
            for member in members:
                if any(dependency in {str(other["id"]) for other in members} for dependency in member.get("depends_on", [])):
                    fail(f"{label}: dependent tasks cannot be parallel")
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node_id: str) -> None:
        if node_id in visiting:
            fail(f"{label}: dependency cycle")
        if node_id in visited:
            return
        visiting.add(node_id)
        for dependency in by_id[node_id].get("depends_on", []):
            visit(str(dependency))
        visiting.remove(node_id)
        visited.add(node_id)
    for node_id in by_id:
        visit(node_id)
def check_topology(records: list[dict[str, Any]]) -> None:
    for record in records:
        try:
            validate_topology(record)
        except ValueError as exc:
            if record.get("expected_failure"):
                expected = str(record.get("expected_error", "")).lower()
                if expected and expected not in str(exc).lower():
                    fail(f"{record.get('evidence_id', '?')}: expected error does not match")
                continue
            raise
        if record.get("expected_failure"):
            fail(f"{record.get('evidence_id', '?')}: expected topology failure was not represented")


def check_verification(records: list[dict[str, Any]]) -> None:
    hard = {"hard_gate", "deterministic"}
    semantic = {"semantic_review", "blind_paired"}
    semantic_axes = {"playability", "specificity", "continuity", "agency", "dm-usefulness"}
    for record in records:
        label = str(record.get("evidence_id", "?"))
        kind = record.get("kind", record.get("verification_kind"))
        if kind in semantic:
            if record.get("deterministic") is not False or record.get("deterministic_failure"):
                fail(f"{label}: semantic review cannot be deterministic lint")
            if record.get("axis") not in semantic_axes or record.get("evaluator") != "independent-blind-paired":
                fail(f"{label}: semantic review needs independent fixed-axis evidence")
            continue
        if kind not in hard:
            if record.get("expected_failure"):
                continue
            fail(f"{label}: unknown verification boundary")
        if record.get("expected_failure"):
            expected = str(record.get("expected_error", "")).lower().replace("-", " ")
            check = str(record.get("check", "")).lower().replace("-", " ")
            violation = str(record.get("violation", "")).lower().replace("-", " ")
            evidence = f"{check} {violation} {record.get('field', '')}".lower()
            if not expected or expected not in evidence:
                fail(f"{label}: expected objective failure lacks matching evidence")
            continue
        if record.get("record_type") == "completion_evidence":
            required = ("route", "context_used", "context_omitted", "work_status", "dm_acceptance", "canon_state", "filing", "measurement")
            missing = [field for field in required if field not in record]
            if missing:
                fail(f"{label}: completion evidence missing {', '.join(missing)}")
            if record["work_status"] == "accepted" and record["dm_acceptance"] != "accepted":
                fail(f"{label}: accepted Work requires DM acceptance")
            if record["canon_state"] == "accepted-truth" and record["dm_acceptance"] != "accepted":
                fail(f"{label}: accepted truth requires acceptance")
        if record.get("record_type") == "compatibility":
            required_phases = {"specify", "clarify", "plan", "checklist", "tasks", "analyze", "implement", "converge"}
            if not required_phases.issubset(set(record.get("lifecycle_phases", []))):
                fail(f"{label}: Spec Kit lifecycle is incomplete")
            if record.get("managed_files_unchanged") is not True:
                fail(f"{label}: managed files must remain unchanged")


def check_plan(records: list[dict[str, Any]]) -> None:
    for record in records:
        label = str(record.get("evidence_id", "plan"))
        if record.get("work_class") == "engineering":
            require(record, ("technical_context", "architecture", "storage", "testing", "platform", "performance", "constraints", "source_structure"), label)
            if any(key in record for key in ("agency", "canon_impact", "player_owned_decisions")):
                fail(f"{label}: engineering plan contains campaign-only vocabulary")
        elif record.get("work_class") in {"agent-system", "campaign-architecture", "creative-system"}:
            require(record, ("context_used", "context_omitted"), label)
        else:
            fail(f"{label}: invalid plan work_class")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("classify", "agency", "canon", "topology", "plan", "verify"):
        command = sub.add_parser(name)
        command.add_argument("--fixtures", required=True, type=Path)
    args = parser.parse_args()
    try:
        records = load(args.fixtures)
        if args.command == "classify":
            check_classification(records)
        elif args.command == "agency":
            check_agency(records)
        elif args.command == "canon":
            check_canon(records)
        elif args.command == "topology":
            check_topology(records)
        elif args.command == "plan":
            check_plan(records)
        else:
            check_verification(records)
        print(f"PASS {args.command}: {len(records)} fixture record(s)")
        return 0
    except (ValueError, OSError) as exc:
        print(f"FAIL {args.command}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
