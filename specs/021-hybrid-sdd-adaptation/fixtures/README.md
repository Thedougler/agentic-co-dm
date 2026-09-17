# Hybrid SDD Fixture Contract

These sanitized fixtures are the permanent behavioral seam for feature 021. They contain identifiers, counts, enums, and evidence only; they do not contain prompts, campaign prose, model output, provider metadata, or fictional canon.

## Stable scenario identifiers

Route fixtures use `scenario_id` values `A-agent-system`, `B-campaign-architecture`, `C-creative-system`, `D-routine-npc`, `E-engineering`, `F-entity-collision`, and `G-mixed-request`. Evidence and verification fixtures use descriptive stable IDs prefixed by their surface, for example `agency-regional-conflict`, `canon-existing-alias`, `topology-valid`, and `verification-hard-gates`. Telemetry fixtures use `trace_id` values that remain unique within their fixture set.

Identifiers are contract keys, not opaque entity IDs. A fixture may reference a canonical owner by its repository path or title, but never invents a second identity mechanism.

## Route record

Each JSON object in `routes/` has:

```json
{
  "scenario_id": "A-agent-system",
  "request_kind": "agent-system",
  "expected": {
    "work_class": "agent-system",
    "route": "full-sdd",
    "reason_contains": ["future agent behavior"],
    "scope_boundary": "system-change"
  },
  "request": "sanitized request description"
}
```

Routine records set `work_class` to `routine-content`, name the existing `skill_route`, set `route` to `existing-skill`, and use `scope_boundary: routine-content`. Mixed records contain `slices`, with one full-SDD system slice and one existing-skill routine slice.

## Evidence record

Each object in `evidence/` has an `evidence_id`, `kind`, and fields required by that verifier. Values are sanitized observations: names of actors or owner artifacts, enum values, booleans, counts, paths, and conditional consequence labels. Negative fixtures include `expected_failure` and the objective rule that must reject them.

Agency records expose `actors`, `pressures`, `open_outcomes`, `conditional_possibilities`, `independent_motion`, and `if_nobody_intervenes`. Canon records expose owner-resolution evidence, `current_truth`, `affected_truth`, `proposal`, `reveal`, `visibility`, `acceptance`, and `filing`. Topology records expose nodes with `artifact`, `owner`, `depends_on`, `wave`, and `evidence`; parallel nodes must have disjoint artifacts. Engineering records use technical fields without campaign-only requirements.

Verification records distinguish `hard_gate` checks from `semantic_review`; semantic judgments are paired-evaluator evidence, never deterministic lint results. Completion records use the vocabulary in the hybrid SDD contract.

## Telemetry record

Each object in `telemetry/` is a redacted trace input. It has `schema_version`, `trace_id`, `policy_version`, `sitting_class`, `work_status`, `measurement_status`, model/tokenizer identity, numeric `trajectory`, `retrieval`, exclusive `source_components`, `quality`, and redacted timestamps. Counts are non-negative integers. Each measured token occurrence has one primary source owner; secondary provenance is metadata only.

Fixtures may include `expected_error`, `expected_quarantine`, `expected_measurement_gap`, and `expected_report` assertions consumed by `check.py`. Normal local traces use `.local/efficiency/` and are never committed. Additive schema fields require a defined default; incompatible records must be quarantined without rewriting history.
