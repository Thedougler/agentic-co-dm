# Research: Hybrid Spec-Driven Development

## Decision: Keep generated Spec Kit integrations and templates unchanged

**Rationale**: `specify integration status --json` reports `status: ok`, the default integration remains `omp`, all four installed integrations are present, and no managed files are missing or modified. The OMP baseline also passes. Editing `.agents/skills/speckit-*`, `.omp/commands/speckit.*`, or `.specify/templates/*` would create managed-file drift and duplicate the Spec Kit authority.

**Alternatives considered**: Hand-edit each generated adapter — rejected because the same policy would drift across harnesses. Edit the managed templates — rejected because the repository's current Spec Kit integration is healthy and the hybrid policy can be loaded through the existing `AGENTS.md` context. Reinitialize Spec Kit — rejected by the existing integration and safety policy.

## Decision: Use one compact route map and one progressive-disclosure contract

**Rationale**: `AGENTS.md` is already the repository-wide operating map and `.omp/AGENTS.md` imports it. A short routing section can classify substantial work and point to `docs/agents/hybrid-sdd.md`; the detailed class contracts, artifact fields, ownership rules, and completion evidence stay out of every always-loaded context. This preserves the existing wiki, beat, Work, and design-impact routing authorities.

**Alternatives considered**: Put the full hybrid policy in `AGENTS.md` — rejected as standing-context waste. Add a second Spec Kit lifecycle or command — rejected by the single-source and compatibility requirements. Add a new skill — rejected because the existing Spec Kit phase skills already provide the execution surfaces.

## Decision: Record route identity in the artifact, not in a new database

**Rationale**: Constitution XV requires machine-readable identity, while the repository has no feature database. Substantial feature artifacts and completion evidence will expose `work_class` and `route`; routine content has no feature directory and keeps its established skill route. Existing canonical artifact paths, titles, aliases, wikilinks, manifests, and QMD remain the identity mechanisms.

**Alternatives considered**: Add opaque entity IDs — rejected by FR-016. Add a routing database — rejected as a second authority. Infer class from filenames — rejected because filenames do not reliably express intent.

## Decision: Reuse 012's blind evaluation pattern for semantic non-inferiority

**Rationale**: `specs/012-blind-content-eval/` already establishes independent cold evaluation, applicable axes, pass/fail judgments, and the rule that deterministic shape checks cannot stand in for creative judgment. The new promotion contract will use a blind paired evaluator with a fixed rubric and will treat a new applicable-axis failure as semantic regression. It will not invent numeric creative scoring or copy existing rubrics into `AGENTS.md`.

**Alternatives considered**: Deterministic lint for playability or agency — rejected by FR-027 and Constitution VII. Same-session self-review — rejected because it is not blind. A new weighted 1–5 creative score — rejected as false precision and unnecessary standing load.

## Decision: Separate efficiency telemetry from the 019 sitting/error ledger

**Rationale**: 019 owns sitting records, runtime errors, and same-kind operational notes. The new requirement adds schema versioning, redaction, source-exclusive token attribution, retention, quarantine, metric vectors, and promotion evidence. A dedicated `scripts/efficiency-trace.py` keeps those responsibilities separate while reusing the 019 `prep`/`wrapup` terminology and fixture style.

**Alternatives considered**: Expand `scripts/error-ledger.py` into a full telemetry system — rejected because it would blur ownership and make the existing helper harder to operate. Add a database — rejected because local JSONL is the specified storage and the job does not need queries beyond bounded reports.

## Decision: Make the maintainer policy versioned and keep normal traces local

**Rationale**: `config/efficiency.yaml` is the single owner for retention, sampling, risk classes, canaries, non-inferiority, and rollback thresholds. Normal records go to gitignored `.local/efficiency/traces.jsonl` and contain only redacted metadata, provenance identifiers, and counts. Sanitized fixtures and pinned baselines may be committed. Incompatible records are quarantined with an observable error; history is never rewritten.

**Alternatives considered**: Commit all traces — rejected because prompts, campaign facts, and provider metadata can be sensitive. Store only aggregate reports — rejected because paired replay and failure diagnosis require trace-level evidence. Let agents edit thresholds in records — rejected by FR-039 and FR-043.

## Decision: Treat the tokenizer-policy mismatch as a prerequisite, not a silent migration

**Rationale**: The current repository policy in `docs/agents/token-measurement.md` and `AGENTS.md` requires tiktoken. The feature specification requires each model family's native tokenizer and explicitly requires a separate tracked governance change before changing that authority. The implementation will record tokenizer family/encoding, reject cross-family comparisons, and leave the existing tiktoken helper and policy untouched until that prerequisite lands.

**Alternatives considered**: Change `AGENTS.md` and token policy in this feature — rejected because the spec explicitly forbids a silent override. Ignore the mismatch — rejected because reports would claim incomparable measurements are equivalent. Keep one global tokenizer forever — rejected because it contradicts the accepted feature clarification.

## Decision: Use one standard-library fixture checker as the permanent public seam

**Rationale**: Existing 018 and 019 features use feature-local `fixtures/check.py` scripts that observe files and helper outputs rather than snapshotting instruction wording. The new checker will cover route selection, completion evidence, hard-gate classification, trace schema/retention/quarantine, attribution, and promotion-state behavior. Existing wiki, link, and OMP checks remain separate authorities.

**Alternatives considered**: Add pytest and a large unit suite — rejected by the repository's current fixture pattern and Constitution XVII. Test only Markdown strings — rejected because it would pin prose rather than behavior. Put all checks into OMP baseline — rejected because this feature is not an OMP-only concern.

## Decision: No external service contract

**Rationale**: The feature exposes repository-local agent contracts and command-line helpers only. The two contract files document those public seams; no HTTP API, database schema, or external provider integration is introduced.

**Alternatives considered**: Add a hosted telemetry service — rejected as out of scope, privacy-expensive, and unnecessary for one local campaign repository.
