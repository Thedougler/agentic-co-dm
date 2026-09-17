# Data Model: Hybrid Spec-Driven Development

The feature has no database. Durable policy and feature contracts are Markdown/YAML; normal telemetry is redacted local JSONL; sanitized fixtures are committed.

## Work Classification

One decision made before a substantial artifact is written.

| Field | Rule |
|---|---|
| `work_class` | Exactly `engineering`, `agent-system`, `campaign-architecture`, or `creative-system` for full SDD. |
| `route` | `full-sdd` for those classes; routine established campaign content uses its existing skill route and has no feature directory. |
| `reason` | Names the behavior/system change that makes full SDD necessary, or states why routine content stays outside it. |
| `slice` | Mixed requests identify the SDD-worthy system slice and the routine-content slice separately. |
| `status` | `classified` before writing; `complete` only after the applicable evidence contract passes. |

## Hybrid Specification

The feature artifact that owns behavior and acceptance.

| Field | Rule |
|---|---|
| `work_class` / `route` | Machine-readable identity from Work Classification. |
| `objective` / `value` | Observable outcome and value for agents, the DM, players, or the campaign. |
| `ground_truth` | Existing constitution, AGENTS, docs, schemas, ADRs, owner pages, current wiki state, retrieval results, and environment facts that remain authoritative. |
| `acceptance` | Independently testable scenarios and measurable success evidence. |
| `failures` | Named failure modes with the requirement or check that prevents each one. |
| `scope` | Explicit in-scope and out-of-scope boundaries. |
| `agency` | Required for campaign-facing/reusable creative work: player-owned decisions, open outcomes, independent world motion, pressures, and conditional possibilities. |
| `canon_impact` | Current truths, affected truths, proposals, owner pages, contradictions, provenance, reveal, and visibility consequences. |
| `state` | `draft` → `clarified` → `planned` → `implemented` → `converged`; this does not replace campaign lifecycle or Work acceptance. |

## Canon Impact Record

The boundary record used when a feature may touch campaign material.

| Field | Rule |
|---|---|
| `owner_artifacts` | Existing canonical pages, skills, templates, contracts, scripts, or configuration that own the affected facts. |
| `current_truth` | Accepted facts that remain unchanged. |
| `affected_truth` | Accepted facts that may be changed, with contradictions visible. |
| `proposal` | Invented or conditional material that is not accepted canon. |
| `reveal` / `visibility` | Existing reveal and audience boundary; unrevealed material remains protected. |
| `acceptance` | `not-required` for deterministic non-fact maintenance; `required` until DM acceptance for campaign-facing fact changes. |

## Dependency Node

One planned task or artifact relationship.

| Field | Rule |
|---|---|
| `artifact` | Canonical write surface or named deliverable. |
| `owner` | Single active writer for the artifact. |
| `depends_on` | Required predecessor nodes; no invented edge merely to display a DAG. |
| `wave` | Serial or parallel execution grouping. Parallel nodes must have disjoint canonical write surfaces. |
| `evidence` | Check or review that closes the node. |
| `state` | `pending` → `ready` → `in-progress` → `verified` → `complete`; blocked nodes retain a named reason. |

## Completion Evidence

The structured evidence surface used in the final report or a saved completion record.

| Field | Rule |
|---|---|
| `route` | Work class and route actually taken. |
| `context` | Authoritative context used and intentionally omitted. |
| `owners` | Affected and resolved canonical artifacts plus single-writer ownership. |
| `dependencies` | Resolved topology and any unresolved named gap. |
| `checks` | Deterministic commands and results, including hard-gate results. |
| `quality_review` | Agency, continuity, creative, or blind semantic review where applicable. |
| `work_status` | `produced`, `accepted`, `failed`, or `incomplete`. |
| `dm_acceptance` | `not-required`, `pending`, `accepted`, `modified`, or `rejected`. |
| `canon_state` | `unchanged`, `proposal`, or `accepted-truth`; only existing acceptance rules may produce the last state. |
| `filing` | `not-filed`, `staged`, `filed`, or `promoted`. |
| `measurement` | Complete trace, explicit measurement gap, or not-applicable with reason. |

## Trace Record

One redacted useful trajectory for one `prep` or `wrapup` sitting.

| Field | Rule |
|---|---|
| `schema_version` | Required explicit version. Readers support additive changes and quarantine incompatible records. |
| `trace_id` / `policy_version` | Stable record identity and maintainer-policy version. |
| `sitting_class` | `prep` or `wrapup`; audit/replay are metadata only. |
| `work_status` | `produced`, `accepted`, `failed`, or `incomplete`. |
| `measurement_status` | `complete` or `measurement-gap`; disabled telemetry cannot be a complete comparison sample. |
| `model_family` / `tokenizer_family` / `encoding` | Required for comparison compatibility; cross-family comparisons are rejected. |
| `trajectory` | Request, loaded context, retrieval, tools, failures, retries, model input/output, and final Work; idle/unrelated activity is excluded. |
| `retrieval` | Query count, fetch count, fetch tokens, attempted collections, fallback sequence, and useful/unused classification. |
| `tokens` | Input, output, total, source-component counts, and one exclusive primary owner for every occurrence. |
| `quality` | Hard-gate failures, semantic evaluation result, DM acceptance, DM revision, and runtime/tool failures. |
| `timestamps` | Redacted timing metadata sufficient for retention, not raw conversation content. |
| `retention` | Normal records are local and retained for 90 days; sanitized fixtures/baselines may be committed. |

## Efficiency Policy

Maintainer-owned versioned policy at `config/efficiency.yaml`.

| Field | Rule |
|---|---|
| `schema_version` | Policy schema identity. |
| `retention_days` | 90 for normal local traces. |
| `comparison_classes` | Initially `prep` and `wrapup`; audit/replay metadata only. |
| `minimum_pairs` | 10 same-kind paired cases. |
| `minimum_median_reduction` | 0.05 trajectory-token reduction. |
| `risk_classes` | Deterministic low-risk cleanup; retrieval/routing/budget/tool-exposure moderate-risk; semantic/model/canon/schema/instruction/policy changes high-risk. |
| `canary` / `shadow` / `human_review` | Required promotion path by risk class. |
| `rollback` | Any hard-gate failure or material semantic/runtime/DM-revision regression. |
| `owner` | Maintainers; agents may propose but not silently alter thresholds or gates. |

## Semantic Evaluation

One blind paired comparison of baseline and candidate outputs.

| Field | Rule |
|---|---|
| `evaluator` | Independent of the optimization author and does not see the authoring session. |
| `rubric_version` | Fixed, versioned semantic-quality rubric. |
| `applicable_axes` | Playability, specificity, continuity, player agency, and DM usefulness as applicable. |
| `verdict` | `pass` or `fail` per applicable axis and overall. |
| `non_inferior` | Candidate introduces no new applicable-axis failure across the paired cases. |
| `contamination` | Any evaluator that saw authoring context is invalid and cannot close promotion. |

## State Relationships

```text
request
  → classification
  → hybrid specification (or routine skill route)
  → plan with owners/dependencies
  → tasks with bounded waves
  → Work and implementation
  → deterministic checks + blind semantic review
  → completion evidence
  → DM acceptance when required
  → accepted truth or non-canon filing

prep/wrapup sitting
  → redacted trace
  → same-kind report
  → paired baseline comparison
  → risk path (auto | shadow/canary | human)
  → promote or rollback
```

Invalid transitions include writing accepted campaign truth before DM acceptance, treating a measurement gap as a complete sample, comparing different tokenizer families, draining/quarantining by rewriting history, and running parallel writes on one canonical artifact.
