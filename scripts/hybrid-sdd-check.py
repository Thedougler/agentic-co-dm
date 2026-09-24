#!/usr/bin/env python3
"""Deterministic checks for the hybrid SDD public contract."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, NoReturn

CLASSES = {"engineering", "agent-system", "campaign-architecture", "creative-system"}
ROUTES = {"full-sdd", "existing-skill"}
ROUTINE_SKILLS = {"npc-design", "place-design", "item-design", "spell-design", "monster-design"}
FORBIDDEN_AGENCY = {
    "mandatory_allegiance", "authored_player_decision", "fixed_scene_sequence",
    "fixed_ending", "predetermined_route", "required_player_choice",
}
CANON_STATES = {"unchanged", "proposal", "accepted-truth"}
ACCEPTANCE = {"not-required", "pending", "accepted", "modified", "rejected"}
FILING_STATES = {"not-filed", "staged", "filed", "promoted"}
OWNER_RESOLUTIONS = {"reuse", "ambiguous", "report-collision", "missing"}
VERIFICATION_CHECKS = {
    "schema", "type", "lifecycle", "relationship", "beat-kind", "filename",
    "owner", "link", "canon-precedence", "entity-before-spoken", "dm-explicitness",
    "reveal", "visibility", "accept-before-write", "closed-vocabulary",
}


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
        if not isinstance(record.get("request"), str) or not record["request"].strip():
            fail(f"{record.get('scenario_id', '?')}: sanitized request is required")
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
        reasons = expected["reason_contains"]
        if not isinstance(reasons, list) or not all(isinstance(reason, str) for reason in reasons):
            fail(f"{record.get('scenario_id', '?')}: reason_contains must be a list of strings")
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
            for item in slices:
                if not isinstance(item, dict):
                    fail(f"{record.get('scenario_id', '?')}: mixed slice must be an object")
                slice_expected = item.get("expected", item)
                slice_class = slice_expected.get("work_class")
                slice_route = slice_expected.get("route")
                if slice_route not in ROUTES:
                    fail(f"{record.get('scenario_id', '?')}: invalid mixed slice route {slice_route}")
                if slice_route == "full-sdd" and slice_class not in CLASSES:
                    fail(f"{record.get('scenario_id', '?')}: full-SDD slice needs a valid work class")
                if slice_route == "existing-skill":
                    if slice_class != "routine-content" or slice_expected.get("skill_route") not in ROUTINE_SKILLS:
                        fail(f"{record.get('scenario_id', '?')}: routine slice needs an existing skill route")
        if wanted_class == "routine-content" and expected.get("skill_route") not in ROUTINE_SKILLS:
            fail(f"{record.get('scenario_id', '?')}: routine content needs an existing skill route")


def require(record: dict[str, Any], fields: tuple[str, ...], label: str) -> None:
    missing = [field for field in fields if not record.get(field)]
    if missing:
        fail(f"{label}: missing {', '.join(missing)}")


def agency_errors(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_fields = (
        "value", "actors", "pressures", "open_outcomes", "conditional_possibilities",
        "independent_motion", "if_nobody_intervenes", "player_owned_decisions", "continuity",
    )
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
        if record.get("kind") == "ownership":
            check_ownership(record)
            continue
        if record.get("expected_failure"):
            acceptance = record.get("acceptance", record.get("dm_acceptance"))
            invalid_write = record.get("writes_fact") and acceptance != "accepted"
            invalid_exposure = record.get("reveal") in {False, "unrevealed", "hidden"} and record.get("visibility") in {"players", "public"}
            if not (invalid_write or invalid_exposure):
                fail(f"{label}: expected canon failure was not represented")
            continue
        state = record.get("canon_state", record.get("state"))
        if state is not None and state not in CANON_STATES:
            fail(f"{label}: invalid canon state {state}")
        acceptance = record.get("acceptance", record.get("dm_acceptance"))
        if acceptance is not None and acceptance not in ACCEPTANCE:
            fail(f"{label}: invalid acceptance state {acceptance}")
        if "owner_artifacts" in record and (not isinstance(record["owner_artifacts"], list) or not record["owner_artifacts"]):
            fail(f"{label}: owner_artifacts must identify a canonical owner")
        if "provenance" in record and (not isinstance(record["provenance"], list) or not record["provenance"]):
            fail(f"{label}: provenance must be recorded")
        if "filing" in record and record["filing"] not in FILING_STATES:
            fail(f"{label}: invalid filing state {record['filing']}")
        if "owner_resolution" in record and record["owner_resolution"] not in OWNER_RESOLUTIONS:
            fail(f"{label}: invalid owner resolution {record['owner_resolution']}")
        if record.get("equivalent") and record.get("owner_resolution") != "reuse":
            fail(f"{label}: equivalent entity must reuse owner")
        if record.get("uncertain_collision") and record.get("owner_resolution") not in {"ambiguous", "report-collision"}:
            fail(f"{label}: uncertain collision must remain visible")
        if record.get("writes_fact") and acceptance != "accepted":
            fail(f"{label}: accept-before-write violation")
        if record.get("writes_fact") and record.get("dm_acceptance", acceptance) != "accepted":
            fail(f"{label}: DM acceptance must precede fact write")
        if state == "accepted-truth" and acceptance != "accepted":
            fail(f"{label}: accepted truth requires DM acceptance")
        if record.get("proposal") and state == "accepted-truth" and acceptance != "accepted":
            fail(f"{label}: proposal became accepted truth before DM acceptance")
        if record.get("reveal") in {False, "unrevealed", "hidden"} and record.get("visibility") in {"players", "public"}:
            fail(f"{label}: unrevealed material exposed")


def check_ownership(record: dict[str, Any]) -> None:
    label = str(record.get("evidence_id", "ownership"))
    required = ("mechanism", "identity_mechanism", "evidence_path", "evidence_result", "owner_resolution")
    missing = [field for field in required if not record.get(field)]
    if missing:
        fail(f"{label}: missing {', '.join(missing)}")
    if record.get("owner_resolution") not in OWNER_RESOLUTIONS:
        fail(f"{label}: invalid owner resolution {record.get('owner_resolution')}")
    if record.get("opaque_ids_used") is not False:
        fail(f"{label}: opaque IDs are not an identity mechanism")
    if record.get("equivalent") and record.get("owner_resolution") != "reuse":
        fail(f"{label}: equivalent candidate must reuse its owner")
    if record.get("uncertain_collision"):
        if record.get("owner_resolution") not in {"ambiguous", "report-collision"}:
            fail(f"{label}: uncertain collision must remain visible")
        if record.get("collision_reported") is not True or record.get("new_owner_allowed") is not False:
            fail(f"{label}: uncertain collision needs a blocking collision report")
        if not isinstance(record.get("owner_candidates"), list) or len(record["owner_candidates"]) < 2:
            fail(f"{label}: uncertain collision needs multiple owner candidates")
    elif record.get("owner_resolution") == "reuse" and not record.get("owner_artifact"):
        fail(f"{label}: reused owner artifact is required")


def validate_topology(record: dict[str, Any]) -> None:
    label = str(record.get("evidence_id", "topology"))
    if record.get("work_class") not in CLASSES or record.get("route") != "full-sdd":
        fail(f"{label}: topology needs a full-SDD work class and route")
    if record.get("status") not in {"pending", "ready", "in-progress", "verified", "complete"}:
        fail(f"{label}: invalid topology status")
    if not record.get("expected_failure"):
        if not isinstance(record.get("context_used"), list) or not record["context_used"]:
            fail(f"{label}: context_used is required")
        if not isinstance(record.get("context_omitted"), list) or not record["context_omitted"]:
            fail(f"{label}: context_omitted is required")
    nodes = record.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        fail(f"{label}: nodes are required")
    by_id: dict[str, dict[str, Any]] = {}
    for node in nodes:
        if not isinstance(node, dict) or not node.get("id") or not node.get("artifact") or not node.get("owner") or not node.get("evidence"):
            fail(f"{label}: each node needs id, artifact, owner, and evidence")
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
    node_order = {str(node["id"]): index for index, node in enumerate(nodes)}
    for node in nodes:
        node_id = str(node["id"])
        for dependency in node.get("depends_on", []):
            if node_order[str(dependency)] >= node_order[node_id]:
                fail(f"{label}: dependency must precede dependent node")
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
            if record.get("rubric_version") or record.get("contamination") is not None:
                if not record.get("rubric_version") or record.get("contamination") is not False or record.get("judgment_only") is not True:
                    fail(f"{label}: semantic review needs a fixed uncontaminated judgment record")
            if not isinstance(record.get("non_inferior"), bool):
                fail(f"{label}: semantic review must record non-inferiority")
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
            validate_objective_violation(record, label)
            continue
        if record.get("record_type") == "hard_gate_matrix":
            checks = record.get("checks")
            if not record.get("deterministic") or record.get("deterministic_failure") or record.get("result") != "pass":
                fail(f"{label}: hard-gate matrix must pass deterministically")
            if not isinstance(checks, list) or not checks or not set(checks).issubset(VERIFICATION_CHECKS):
                fail(f"{label}: hard-gate matrix contains an unknown check")
        if record.get("record_type") == "completion_evidence":
            required = (
                "route", "context_used", "context_omitted", "owners_affected", "owners_resolved",
                "dependencies", "deterministic_checks", "quality_review", "work_status",
                "dm_acceptance", "canon_state", "filing", "measurement",
            )
            missing = [field for field in required if field not in record]
            if missing:
                fail(f"{label}: completion evidence missing {', '.join(missing)}")
            if record.get("route") not in ROUTES or record.get("work_status") not in {"produced", "accepted", "failed", "incomplete"}:
                fail(f"{label}: completion evidence has invalid route or Work state")
            if record.get("dm_acceptance") not in ACCEPTANCE or record.get("canon_state") not in CANON_STATES:
                fail(f"{label}: completion evidence has invalid acceptance or canon state")
            if record["work_status"] == "accepted" and record["dm_acceptance"] != "accepted":
                fail(f"{label}: accepted Work requires DM acceptance")
            if record["canon_state"] == "accepted-truth" and record["dm_acceptance"] != "accepted":
                fail(f"{label}: accepted truth requires acceptance")
            if not isinstance(record.get("state_separation"), dict):
                fail(f"{label}: completion evidence must separate lifecycle and Work states")
        if record.get("record_type") == "compatibility":
            required_phases = {"specify", "clarify", "plan", "checklist", "tasks", "analyze", "implement", "converge"}
            if not required_phases.issubset(set(record.get("lifecycle_phases", []))):
                fail(f"{label}: Spec Kit lifecycle is incomplete")
            if record.get("managed_files_unchanged") is not True:
                fail(f"{label}: managed files must remain unchanged")
            if record.get("existing_routes_preserved") is not True or record.get("second_integration") is not False:
                fail(f"{label}: existing integrations and routes must be preserved")


def validate_objective_violation(record: dict[str, Any], label: str) -> None:
    """Confirm that a negative fixture contains the objective evidence it claims."""
    check = str(record.get("check", "")).lower().replace("-", " ")
    violation = str(record.get("violation", "")).lower().replace("-", " ")
    if check == "type" and record.get("value") in record.get("allowed_values", []):
        fail(f"{label}: invalid type fixture uses an allowed value")
    if check == "lifecycle" and record.get("value") in record.get("allowed_values", []):
        fail(f"{label}: invalid lifecycle fixture uses an allowed value")
    if "relationship" in violation and not record.get("value"):
        fail(f"{label}: relationship violation needs a value")
    if "filename" in violation and record.get("filename_status") != "invalid":
        fail(f"{label}: filename violation needs invalid filename evidence")
    if check == "link" and record.get("link_status") != "broken":
        fail(f"{label}: link violation needs broken-link evidence")
    if check == "owner" and record.get("owner_resolution") not in {"missing", "ambiguous", "report-collision"}:
        fail(f"{label}: owner violation needs missing or unresolved owner evidence")
    if check == "canon precedence" and (record.get("accepted_truth_preserved") is not False or record.get("selected_source") == record.get("authoritative_source")):
        fail(f"{label}: canon-precedence violation is not evidenced")
    if check == "entity before spoken" and not (record.get("entity_resolved") is False and record.get("spoken_artifact_written") is True):
        fail(f"{label}: entity-before-spoken violation is not evidenced")
    if check == "dm explicitness" and not (record.get("dm_addressed") is False or record.get("dm_explicit") is False):
        fail(f"{label}: DM explicitness violation is not evidenced")
    if check in {"reveal", "visibility"} and record.get("visibility") not in {"players", "public"}:
        fail(f"{label}: exposure violation needs a player/public visibility")
    if check == "accept before write" and not (record.get("writes_fact") is True and record.get("dm_acceptance") != "accepted"):
        fail(f"{label}: accept-before-write violation is not evidenced")


def check_plan(records: list[dict[str, Any]]) -> None:
    for record in records:
        label = str(record.get("evidence_id", "plan"))
        if record.get("work_class") == "engineering":
            require(record, ("technical_context", "architecture", "storage", "testing", "platform", "performance", "constraints", "source_structure"), label)
            if any(key in record for key in ("agency", "canon_impact", "player_owned_decisions", "factions", "open_outcomes")):
                fail(f"{label}: engineering plan contains campaign-only vocabulary")
        elif record.get("work_class") in {"agent-system", "campaign-architecture", "creative-system"}:
            require(record, ("context_used", "context_omitted"), label)
            if record.get("route") != "full-sdd":
                fail(f"{label}: substantial plan must use full-sdd")
        else:
            fail(f"{label}: invalid plan work_class")


def read_yaml(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
        # JSON is valid YAML and keeps this public checker standard-library-only.
        try:
            value = json.loads(text)
        except json.JSONDecodeError:
            try:
                import yaml
            except ImportError as exc:
                fail(f"PyYAML is required for non-JSON YAML preset manifests: {exc}")
            try:
                value = yaml.safe_load(text)
            except yaml.YAMLError as exc:
                fail(f"invalid YAML preset manifest {path}: {exc}")
    except (OSError, UnicodeError) as exc:
        fail(f"cannot read preset manifest {path}: {exc}")
    if not isinstance(value, dict):
        fail(f"preset manifest {path} must be a mapping")
    return value


def check_preset(package: Path) -> None:
    """Validate the repository-owned preset without installing it."""
    if not package.is_dir() or package.name != "creative-llm-wiki":
        fail("preset package must be the creative-llm-wiki directory")
    manifest_path = package / "preset.yml"
    manifest = read_yaml(manifest_path)
    if manifest.get("schema_version") != "1.0":
        fail("preset manifest must use schema_version 1.0")
    preset = manifest.get("preset")
    if not isinstance(preset, dict) or preset.get("id") != "creative-llm-wiki":
        fail("preset manifest must identify creative-llm-wiki")
    for field in ("name", "version", "description", "author"):
        if not isinstance(preset.get(field), str) or not preset[field].strip():
            fail(f"preset metadata requires {field}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", preset["version"]):
        fail("preset version must be semantic x.y.z")
    requires = manifest.get("requires")
    if not isinstance(requires, dict) or not isinstance(requires.get("speckit_version"), str):
        fail("preset requires a Spec Kit version constraint")
    provides = manifest.get("provides")
    templates = provides.get("templates") if isinstance(provides, dict) else None
    if not isinstance(templates, list) or not templates:
        fail("preset must provide at least one template")
    seen: set[tuple[str, str]] = set()
    for entry in templates:
        if not isinstance(entry, dict) or not all(isinstance(entry.get(field), str) for field in ("type", "name", "file")):
            fail("each preset template needs string type, name, and file")
        pair = (entry["type"], entry["name"])
        if pair in seen:
            fail(f"duplicate preset template {entry['name']}")
        seen.add(pair)
        if entry["type"] not in {"template", "command", "script"}:
            fail(f"invalid preset template type {entry['type']}")
        relative = Path(entry["file"])
        if relative.is_absolute() or ".." in relative.parts:
            fail(f"preset template path escapes package: {entry['file']}")
        if not (package / relative).is_file():
            fail(f"preset template file is missing: {entry['file']}")

    metadata = manifest.get("hybrid_sdd")
    if not isinstance(metadata, dict) or metadata.get("package_role") != "meta-preset":
        fail("preset must declare its hybrid SDD meta-preset role")
    provenance_path = package / "provenance.json"
    validation_path = package / "validation.json"
    try:
        provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
        validation = json.loads(validation_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f"preset metadata is unreadable: {exc}")
    candidates = provenance.get("source_candidates") if isinstance(provenance, dict) else None
    adaptations = provenance.get("adaptations") if isinstance(provenance, dict) else None
    if not isinstance(candidates, list) or not candidates:
        fail("preset provenance must include a pinned source candidate")
    for candidate in candidates:
        required = ("source_url", "release_or_commit", "retrieved_at", "license", "inspection", "trust")
        if not isinstance(candidate, dict) or any(not candidate.get(field) for field in required):
            fail("each preset candidate needs source, pin, retrieval, license, inspection, and trust evidence")
        if candidate.get("trust") not in {"staged-untrusted", "quarantined"}:
            fail("preset candidates must remain untrusted staging inputs")
        inspection = candidate.get("inspection")
        if not isinstance(inspection, dict) or any(inspection.get(surface) is not True for surface in ("manifest", "templates", "commands", "scripts", "hooks")):
            fail("preset candidate executable surfaces must be inspected")
    if not isinstance(adaptations, list) or not adaptations:
        fail("preset must contain selective provenance-linked adaptations")
    candidate_ids = {candidate.get("candidate_id") for candidate in candidates}
    for adaptation in adaptations:
        required = ("adaptation_id", "source_candidate", "artifact", "selection", "authority", "verification")
        if not isinstance(adaptation, dict) or any(not adaptation.get(field) for field in required):
            fail("each preset adaptation needs selection, artifact, authority, and verification")
        if adaptation["source_candidate"] not in candidate_ids:
            fail("preset adaptation references an unknown source candidate")
        if adaptation.get("selection") in {"wholesale", "copy-complete-package"}:
            fail("preset adaptations must be selective")
    if not isinstance(validation, dict) or validation.get("status") != "validated":
        fail("preset validation metadata must be validated")
    if validation.get("third_party_runtime_dependencies") != []:
        fail("preset must not declare third-party runtime dependencies")
    if validation.get("existing_authorities_preserved") is not True:
        fail("preset must preserve existing authorities")
    if validation.get("installed_third_party_presets") is not False:
        fail("preset must not install third-party presets")


MAINTAINED = ("AGENTS.md", "docs", ".agents", "scripts", "tools", "tests", "package.json", "README.md")
RULE_ID = re.compile(r"^[A-Z]{2,}[0-9]{3}$")


def _git(root: Path, *args: str) -> str:
    import subprocess

    proc = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if proc.returncode != 0:
        fail(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout


def _plan_section_tokens(text: str, heading: str) -> list[str]:
    """Backticked tokens from the first column of the table under a ``###`` heading."""
    tokens: list[str] = []
    inside = False
    for line in text.splitlines():
        if line.startswith("#"):
            inside = line.lstrip("#").strip().startswith(heading)
            continue
        if not inside or not line.startswith("|") or set(line) <= {"|", "-", " "}:
            continue
        first = line.strip().strip("|").split("|")[0]
        tokens.extend(re.findall(r"`([^`]+)`", first))
    return tokens


def check_diff(plan: Path, base: str, root: Path) -> dict[str, Any]:
    """SC-014 a/c: added files must be in the plan's New files table; deleted paths stay unreferenced."""
    text = (root / plan).read_text(encoding="utf-8")
    new_tokens = set(_plan_section_tokens(text, "New files"))
    deleted_tokens = _plan_section_tokens(text, "Deleted or folded")
    status_lines = _git(root, "diff", "--name-status", "--no-renames", f"{base}...HEAD").splitlines()
    added = sorted(line.split("\t", 1)[1] for line in status_lines if line.startswith("A\t"))
    deleted = sorted(line.split("\t", 1)[1] for line in status_lines if line.startswith("D\t"))
    unlisted = [path for path in added if not path.startswith("specs/") and path not in new_tokens]

    needles: dict[str, str] = {}
    for token in deleted_tokens:
        token = token.strip()
        if RULE_ID.match(token):
            needles[token] = token
            continue
        matches = [
            path for path in deleted
            if path == token or path.endswith("/" + token) or (token.endswith("/") and (path.startswith(token) or ("/" + token) in path))
        ]
        for path in matches:
            needles[path] = path
            if token.endswith("/"):
                needles[token] = token
    present = sorted(path for path in needles if "/" in path and not path.endswith("/") and (root / path).exists())

    tracked = [
        line for line in _git(root, "ls-files", "--", *MAINTAINED).splitlines()
        if (root / line).is_file()
    ]
    referenced: list[dict[str, Any]] = []
    for relative in tracked:
        try:
            lines = (root / relative).read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(lines, 1):
            for needle in needles:
                if needle in line:
                    referenced.append({"path": needle, "file": relative, "line": number})
    status = "fail" if unlisted or present or referenced else "pass"
    return {
        "status": status,
        "added": added,
        "deleted": deleted,
        "unlisted_added": unlisted,
        "deleted_still_present": present,
        "deleted_referenced": referenced,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("classify", "agency", "canon", "topology", "plan", "verify"):
        command = sub.add_parser(name)
        command.add_argument("--fixtures", required=True, type=Path)
    preset = sub.add_parser("preset")
    preset.add_argument("--package", required=True, type=Path)
    diff = sub.add_parser("diff", help="diagnostic: plan New files / Deleted or folded tables against a git diff")
    diff.add_argument("--plan", required=True, type=Path)
    diff.add_argument("--base", required=True)
    args = parser.parse_args()
    try:
        if args.command == "diff":
            root = Path(_git(Path.cwd(), "rev-parse", "--show-toplevel").strip())
            report = check_diff(args.plan, args.base, root)
            print(json.dumps(report, indent=2))
            return 0 if report["status"] == "pass" else 1
        if args.command == "preset":
            check_preset(args.package)
            print("PASS preset: creative-llm-wiki package validated")
            return 0
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
