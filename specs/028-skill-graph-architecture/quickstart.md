# Quickstart: Validate Skill Graph Architecture

## Prerequisites

- Repository venv available.
- Feature branch `028-skill-graph-architecture`.
- An accountable issue linked before implementation begins.
- Current Spec Kit and OMP baseline healthy.
- Skill evaluations use the weakest available model that can complete the scenario.

## V-001 — Direct owner routing

Run cold focused prompts for a faction page, wiki question, page repair, typed beat, and city request.

Expected:
- each request selects the named existing owner directly;
- place/beat subtype ownership changes use their existing local seam;
- no generic router or unrelated skill body is loaded.

Covers SC-001, SC-007, and wrong-owner failure.

## V-002 — Parent return and dependency order

Run a cold session-content request requiring a missing faction and place.

Expected:
- the parent retains the session objective;
- faction and place owners receive only their artifacts;
- independent disjoint writes may run concurrently;
- dependent spoken/session work starts only after both owner contracts pass;
- control returns to the parent and the original artifact closes.

Covers SC-002, SC-003, lost-parent failure, and invalid dependency ordering.

## V-003 — Context projection

Record files/instructions supplied to each capability in V-002.

Expected:
- each child receives its owner instructions, target evidence, relevant canon, and governing output contract;
- unrelated prior-child content is absent;
- focused retrieval resumes the same capability when evidence is insufficient.

Covers SC-004 and broad-context failure.

## V-004 — Read/write isolation

Snapshot canonical wiki content and tracking files, then run cold wiki-query and wiki-context-pack requests that discover a plausible useful edit.

Expected:
- answer is grounded and cited;
- no campaign page, manifest, index, or log content changes;
- only CLI-derived cache/timing side effects explicitly allowed by the wiki CLI contract may change.

Covers SC-005 and read-mutation failure.

## V-005 — Validation feedback

On a disposable configured vault, create one deterministic structural finding and one semantic owner-level finding. Exercise the documented write/maintenance route through the actual CLI:

```bash
scripts/wiki lint <vault-relative-path>
scripts/wiki lint fix <vault-relative-path>
scripts/wiki lint <vault-relative-path>
```

Expected:
- complete findings are visible;
- registered deterministic repair is attempted through the existing fixer path;
- semantic repair routes to the artifact owner;
- affected scope reruns;
- completion occurs only when clean or a specific blocker is reported.

Covers SC-006 and premature-completion failure.

## V-006 — Health remains the action owner

```bash
scripts/wiki health
```

Expected:
- guidance consumes `context.act`, `next`, and ordered `focus`;
- `wiki-status` does not independently rerank the maintenance action list;
- no second planner or ledger appears.

Covers SC-008 and FR-022.

## V-007 — Boundary and craft review

For every capability in the live root routing inventory, inspect its owning skill and cold eval evidence.

Expected:
- Input, Work, Done, and Capability Handoff are explicit or clearly equivalent;
- owner-specific completion tests and craft remain intact;
- every named failure in `spec.md` maps to an evaluation;
- no global DAG, graph runtime/database, persistent workflow ledger, generic orchestrator capability, universal state schema, or bespoke node class exists.

Covers SC-007 through SC-010 and flattened-craft/new-machinery failures.

## V-008 — Existing repository checks

Run only after implementation:

```bash
.venv/bin/python -m pytest <targeted-tests-from-tasks>
scripts/check-omp-baseline.sh
specify integration status --json
```

If implementation changes wiki/template/validation behavior, run the real affected wiki scope:

```bash
scripts/wiki lint <affected-vault-relative-paths>
```

Expected:
- targeted behavioral checks pass;
- OMP baseline exits 0;
- Spec Kit integration reports `ok`, default `omp`, four integrations installed;
- affected wiki scope is clean where applicable.

## Evidence record

Record: route; context used/omitted; owners affected/resolved; dependencies; deterministic checks; cold quality review; produced/failed status; unchanged campaign canon; filing; and measured/estimated/inferred context results. Do not claim token improvement without equivalent measured samples.
