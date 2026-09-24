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

### Route and context

- `route`: `agent-system` / `full-sdd`.
- `context_used`: feature spec, constitution v3.1.0, root routing, `CONTEXT.md`,
  hybrid SDD, wiki authority, policy-owner map, CLI contract, owner skills, and
  skill-creator evaluation tooling.
- `context_omitted`: campaign entity/session bodies, unrelated craft bodies,
  full wiki index/log/manifest, generated Spec Kit adapters, and CLI internals
  not implicated by a runtime contract.
- `owners_affected`: root/docs/wiki authority plus the 44 owner skills changed
  by T009–T039 and their existing eval sets.
- `owners_resolved`: root routing inventory resolves to existing owner paths;
  no route was redirected or removed.
- `dependencies`: authority surfaces before owner normalization; named owner
  pages/contracts before dependent presentation; shared canonical surfaces
  serialized; disjoint skill surfaces were delegated concurrently.

### Validation and quality evidence

- `V-001`/`V-004`: direct-owner, subtype, bounded-read, focused-retrieval, and
  canonical-isolation assertions were added. The supported trigger runner
  completed after temporary schema mapping, but does not execute typed
  assertions; no full behavioral pass is claimed.
- `V-002`/`V-003`: parent-return, dependency-order, bounded-child, focused
  retrieval, deliberate-omission, parent-resume, and ingest-parent context
  contracts plus eval cases were added. Static contract review passed; no full
  scenario executor exists in the current runner.
- `V-005`/`V-006`: `scripts/wiki lint`, `scripts/wiki lint fix`, and
  `scripts/wiki health` ran. The real vault reported one pending identity
  finding before repair and 134 remaining findings after the no-op registered
  fixer; `identity.py` consumed 52–88 seconds. Health did not reach green.
  This is a pre-existing real-vault blocker, recorded as error `e-208`.
- `V-007`: 66 live capabilities were reviewed (65 root-table routes plus
  `wiki-lint`); all 44 changed skills expose the four boundary concepts or
  clear equivalents, specialized craft remains, and no new runtime/database/
  ledger/global-DAG/node machinery was found. Eleven live capabilities have no
  dedicated `evals/evals.json`; the matrix remains the route-level coverage
  contract.
- Targeted eval runner: `claude-haiku-4-5-20251001`, one run/query, four
  workers, 45-second timeout. Mapped trigger runs exited 0 but reported 0/8
  wiki-query, 0/8 faction-design, 0/19 session-beats, 0/10 wiki-lint, 0/7
  wiki-ingest, and 0/10 place-design trigger passes. The runner only supports
  trigger rates and cannot grade typed assertions; direct repository eval
  shapes fail its incompatible `query`/`should_trigger` schema.
- `deterministic_checks`: all changed eval JSON parsed with unique IDs;
  `specify integration status --json` returned `ok`, default `omp`, and four
  installed integrations. `scripts/check-omp-baseline.sh` failed before
  feature-specific checks because `.omp/config.yml` uses memory backend
  `mnemopi`, while the baseline requires `off` (error `e-209`).
- `pytest`: not applicable; no executable runtime contract changed.
- `templates/rules/styles`: unchanged because this feature changes routing and
  handoff guidance, not artifact shape or validation semantics. Generated Vale
  vocabulary was not edited.

### Final status

- `work_status`: produced with explicit blockers reported above.
- `canon_state`: unchanged by the feature; no campaign page/template change
  was authored for this implementation.
- `filing`: feature artifacts and owner guidance remain on branch
  `028-skill-graph-architecture`; generated Spec Kit adapters remain unchanged.
- `measurement`: measured runner exit/results and real CLI timings above;
  no token reduction claim made.

### Baseline

The pre-change cold baseline used the same mapped trigger configuration against
temporary `git archive HEAD` owner snapshots with
`claude-haiku-4-5-20251001`, one run/query, four workers, and a 45-second
timeout. Runs exited 0 but reported `0/4` wiki-query, `0/4` faction-design,
`0/15` session-beats, `0/8` wiki-lint, `0/6` wiki-ingest, and `0/9`
place-design trigger passes. The current mapped runs likewise reported zero
trigger passes, but current eval sets are larger. The runner cannot execute
typed behavior assertions, so no per-case behavior delta is claimed.
## Cold assertion matrix

Each scenario uses cold, focused context and the weakest sufficient executor
model. Assertions are behavioral; static heading presence is supporting evidence
only.

| Scenario | Required assertions | Named failure prevented |
|---|---|---|
| V-001 | direct owner selection for faction, wiki question, page repair, typed beat, and city; subtype dispatch stays local; unrelated skills are absent | wrong owner |
| V-002 | parent objective survives; bounded children return evidence; prerequisites precede dependents; disjoint writes remain concurrency-eligible; parent rejoins | lost parent or invalid dependency order |
| V-003 | owner, target, canon, contract, validation, dependencies, and omissions are projected; focused retrieval resumes the same owner; unrelated prior-child artifacts are absent | broad inherited context |
| Safeguard review | authority pointers precede duplicate-procedure removal; existing craft, entity, canon, validation, and approval safeguards remain visible after normalization | authority refactor deletes safeguards |
| V-004 | query answer is cited and canonical wiki pages, manifests, indexes, and logs are unchanged except CLI-permitted derived observations | read operation mutates wiki |
| V-005 | complete lint findings are exposed; registered deterministic repair runs; semantic findings return to the artifact owner; affected scope reruns to clean or a specific blocker | prose-only completion |
| V-006 | health `context.act`, `next`, and ordered `focus` drive maintenance; no second planner reranks the action list | competing maintenance owner |
| V-007 | every live route exposes Input, Work, Done, and Capability Handoff or clear equivalents; craft and completion tests remain; forbidden machinery is absent | flattened craft or duplicate graph machinery |

For every assertion, record the route, files supplied and omitted, owner
handoffs, dependency evidence, deterministic result, semantic review, and
produced/failed status. Use `SC-001` through `SC-010` and the named failures in
`spec.md` as the coverage index.

Record: route; context used/omitted; owners affected/resolved; dependencies; deterministic checks; cold quality review; produced/failed status; unchanged campaign canon; filing; and measured/estimated/inferred context results. Do not claim token improvement without equivalent measured samples.
