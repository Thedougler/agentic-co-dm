# Quickstart Validation: Agent Autonomy Scope

Prerequisites: constitution X is the four-line canon; `AGENTS.md` points at it; `scripts/check-agent-standards.py` is green (`AGENT001`–`AGENT003`). Vault may have `WIKI_STAGED_WRITES=true` (default). Staging is not a wait.

Cold-context means a new agent session that has not seen this feature’s chat, only repo files.

Cite [contracts/agent-autonomy.md](contracts/agent-autonomy.md) and [data-model.md](data-model.md). Do not duplicate rule tables here.

## V-001: Autonomous lint, done-summary, no wait

**Setup**: A live wiki page with a broken `[[wikilink]]` and a missing required frontmatter field.

**Run**: Ask a cold-context agent to lint and repair that page (`wiki-lint` default repair).

**Expected**: Repairs land (live or `_staging/` per flag). Applicable wiki-lint is green. Last message is a short done-summary (what changed, where). No question. No wait.

**Fail**: Agent waits, asks, or reports done while wiki-lint for that page still fails.

## V-002: User-said new NPC is filed

**Setup**: Fresh session.

**Run**: "Create an NPC named Varn who runs the docks."

**Expected**: Owner page filed (staging if flag on). Checkable rules for that write green. Short done-summary. No chat accept step.

**Fail**: Chat proposal only; no file; or wait for accept.

## V-003: Mixed request, one summary

**Run**: "Clean up the broken links on [[Bloodhawk]] and add a new quest hook."

**Expected**: Both land. One done-summary after green.

**Fail**: Only cleanup, only hook, a pause between, or two approval questions.

## V-004: More recent user statement wins

**Setup**: User says Varn runs the docks, then says Varn runs the inner lock.

**Expected**: Filed page matches the inner lock. No question about the conflict.

**Fail**: Ask which is true, or keep the docks as current truth.

## V-005: Two agents complete the same task (SC-005)

**Setup**: Same one-line task: "lint this page and create NPC Varn who runs the docks."

**Run**: Two independent cold-context agents.

**Expected**: Both file the lint repair and the NPC, reach green, done-summary. Neither waits.

**Fail**: Either waits or omits a requested slice.

## V-006: Identity in review (skill-eval)

**Setup**: A diff that only changes a `SKILL.md`.

**Expected**: Review cites `skill-creator` eval results (held-out prompts, with-skill vs without-skill, graded assertions). Coverage/type-safety are not the primary bar. No new checklist, PR template, or review skill.

**Fail**: Software metrics as primary criteria, or a new review surface added for this feature.

## V-007: Checker enforces the contract

**Run**:

```bash
.venv/bin/python scripts/check-agent-standards.py --json
```

**Expected**: exit 0 when instruction files match AGENT001–003.

**Negative**: Re-insert `## Work gate` in a skill → AGENT001 fail, exit ≠ 0. Add `.agents/skills/My Skill/notes.txt` on a branch → AGENT002 fail.

**Fail**: Script missing, or fail does not block done.

## V-008: New owner the user asked for is filed before spoken

**Run**: Session prep that needs a new named NPC the user asked to introduce; no owner page exists.

**Expected**: Agent files the owner page, then may write spoken that depends on it. No accept pause.

**Fail**: Spoken ships with no owner page, or agent waits for accept before filing.
