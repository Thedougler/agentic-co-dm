# Contract: Efficiency Telemetry and Promotion

Agent-facing local contract. Normal telemetry is redacted JSONL; no raw prompt, campaign, wiki, model, or provider content is stored merely for measurement.

## Trace input

`efficiency-trace.py record` accepts a structured record with at least:

```json
{
  "schema_version": 1,
  "trace_id": "stable-id",
  "policy_version": "config-version",
  "sitting_class": "prep",
  "work_status": "accepted",
  "measurement_status": "complete",
  "model_family": "model-family",
  "tokenizer_family": "native-family",
  "encoding": "encoding-name",
  "trajectory": {
    "request": 0,
    "loaded_context": 0,
    "retrieval": 0,
    "tools": 0,
    "failures": 0,
    "retries": 0,
    "model_input": 0,
    "model_output": 0,
    "final_work": 0
  },
  "retrieval": {
    "queries": 0,
    "fetches": 0,
    "tokens": 0,
    "attempted_collections": [],
    "fallbacks": [],
    "useful": 0,
    "unused": 0
  },
  "source_components": [
    {"owner": "user-request", "tokens": 0, "secondary_provenance": []}
  ],
  "quality": {
    "hard_gate_failures": 0,
    "semantic_non_inferior": true,
    "dm_acceptance": "accepted",
    "dm_revisions": 0,
    "runtime_failures": 0
  }
}
```

The helper validates enum values, required identity, non-negative counts, and exclusive primary ownership. It must reject raw-content fields in normal records and must not infer missing meanings.

## Report output

Reports expose, with `measured`, `estimated`, or `inferred` labels and denominators where derived:

- total trajectory, input, and output tokens;
- tokens by exclusive source component;
- retrieval queries, fetches, and retrieval tokens;
- retry amplification;
- hard-gate failure rate;
- DM acceptance and revision rates;
- runtime/tool failure rate;
- useful versus unnecessary retrieval;
- produced, accepted, failed, incomplete, complete-trace, and measurement-gap counts;
- same-kind comparison class and job identity.

Failed and incomplete sittings remain in reports with failure reasons but are excluded from accepted-Work denominators. Audit and replay stay metadata and are not comparison classes.

## Schema evolution and retention

- Every record carries `schema_version`.
- Additive fields remain readable by older-compatible readers when defaults are defined.
- Incompatible records are moved to a quarantine surface with an observable error; history is not guessed, rewritten, or silently dropped.
- Normal traces are retained locally for 90 days and then pruned by an explicit retention operation.
- Sanitized fixtures and pinned baselines may be committed; normal trace files remain gitignored.

## Retrieval and attribution

Record every attempted QMD collection and fallback while preserving `wiki → shattered-sea → legacy` precedence. A fetched page is useful only when accepted Work cites/links it or an independent evaluator confirms that it supplied a required fact, rule, or safety constraint. Fetched-but-unused pages are unnecessary retrieval. Fallback material never overrides current accepted canon.

Each measured token occurrence has exactly one primary source owner. Secondary provenance is metadata only and cannot contribute to component totals.

## Promotion policy

The maintainer-owned `config/efficiency.yaml` defines:

- at least 10 same-kind paired cases;
- at least a 5% median trajectory-token reduction;
- zero new hard-gate failures;
- blind paired semantic non-inferiority using the fixed rubric;
- no material runtime-failure or DM-revision increase;
- low-risk auto-promotion only after a 10% canary;
- moderate-risk shadow replay and canary review;
- high-risk human review;
- rollback on any hard-gate failure or material quality regression.

Risk mapping is fixed by the feature contract: deterministic low-risk cleanup may auto-promote; retrieval, routing, context budgets, and tool exposure require shadow/canary review; semantic compression, model, canon, schema, instruction, policy, and threshold changes require human review.

## Tokenizer compatibility

Comparisons are valid only within the same model/tokenizer family and encoding. The native-tokenizer policy cannot activate until the separate governance change updates the current repository-wide tiktoken authority. The trace still records tokenizer identity now so incompatible comparisons fail closed.
