# Contract: Agent Autonomy

Owner after implement:

| Meaning | Owner |
|---------|--------|
| Four-line canon | `.specify/memory/constitution.md` principle X (v3.0.0) |
| Why / examples / done-summary / project identity | `AGENTS.md` |
| Executable rules | `rules/registry.yml` `AGENT001` `AGENT002` `AGENT003` via `scripts/check-agent-standards.py` |

Skills MUST NOT ship a competing gate or a copied four-line block.

## Canon (FR-003)

1. If the user said it, it is canon.
2. If the user said it more recently, that is more canon.
3. If a transcript says it, after ASR issues are fixed, it is canon.
4. DM-placed ingest files are canon as long as they do not contradict 1–3.

File that work. No Work gate. No DM-approval pause. No extra canon steps.

## Agent loop (FR-008, FR-009, FR-010, FR-012)

1. Do the requested work, including FR-002 maintenance and user-requested new content.
2. Run applicable checkable rules. On fail, repair the cause and rerun. Do not rewrite the rule away. Do not ask the user. Do not interrupt with findings or contradiction alerts.
3. When green, one short done-summary: what changed, where. No question. No wait.

## AGENTS.md (why / examples only)

- Point at constitution X for canon.
- Point at AGENT001–003 / wiki-lint for the contract.
- State done-summary shape.
- Keep **Project identity**: skills/instructions/guidance are primary deliverables; scripts support them; skill-eval is the review bar (held-out prompts, with-skill vs without-skill, graded assertions). MUST NOT add a checklist, PR template, or review skill.
- Delete the `autonomous` / `dm-gated` table and wait rule.

Do not say "autonomous GM".

## Checkable rules

### AGENT001 (BLOCK)

Agent-facing instruction files MUST NOT describe Work-gate, DM-approval-wait, or extra canon workflow.

Scan: `AGENTS.md`, `wiki/AGENTS.md`, `docs/agents/**/*.md`, `.agents/skills/**/*.md`.

Fail on procedure language including: `## Work gate`, `dm-gated`, `file nothing until accept`, `wiki write after DM accept`, `Work-propose`, `wait for accept`.

### AGENT002 (BLOCK)

Every agent-facing file MUST use a predictable path and searchable name:

- `.agents/skills/<kebab>/SKILL.md`
- `.agents/skills/<kebab>/<kebab>.md`
- `docs/agents/<kebab>.md`
- `docs/agents/<kebab>.yml`
- `AGENTS.md`, `wiki/AGENTS.md`, `.omp/AGENTS.md`

This feature bulk-renames the existing tree to match and updates references. `CHECKS.md` / `CONSOLIDATE.md` remorph to kebab.

### AGENT003 (BLOCK)

A `specs/*/spec.md` Functional Requirement that contains `agent-facing` MUST cite at least one `rules/registry.yml` id. This feature’s spec cites `AGENT001`, `AGENT002`, `AGENT003`. Every existing spec that contains that phrase MUST cite an id.

### Wiki lint (already exists)

Broken links, required frontmatter, template HARD keys, Vale on wiki pages. Unchanged by this feature except agents must reach green before done-summary.

## work.md delta

Remove Propose / Decide acceptance waits. File what the Canon section makes canon. Keep non-gate material (table aim, reflection) only if it does not reintroduce a pause. `policy-owners.yml` MUST NOT require mutation acceptance as a chat gate.

## Skill delta

Delete `## Work gate` sections. Point at `AGENTS.md` only if a pointer is required; do not copy canon.

## Staged writes

`WIKI_STAGED_WRITES` does not change the loop. Writes may land in `_staging/`. That is not a wait.

## Invariants

1. No approval wait after a user request this feature covers.
2. Constitution, AGENTS.md, and AGENT001–003 do not disagree.
3. Same checker on agent path and human path (FR-014).
4. HARD entity-before-spoken remains a completeness rule: file the named owner, then spoken — not a wait for accept.
5. Unsaid invention is not canon (constitution XII).

## Validation

Given each spec acceptance scenario and edge case, this contract yields file → green → done-summary with no question. Two cold-context agents given the same user request both complete it (SC-005).
