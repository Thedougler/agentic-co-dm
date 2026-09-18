# Quickstart Validation: Agent Autonomy Scope

Prerequisites: `AGENTS.md` contains **Autonomy classification** per [contracts/autonomy-boundary.md](contracts/autonomy-boundary.md). Vault may have `WIKI_STAGED_WRITES=true` (default). Classification is independent of that flag.

Cold-context means a new agent session that has not seen this feature's chat, only repo files.

## V-001: Autonomous lint, no Work prompt

**Setup**: A live wiki page with a broken `[[wikilink]]` and a missing required frontmatter field. No fact invention required.

**Run**: Ask a cold-context agent to lint and repair that page (`wiki-lint` default repair).

**Expected**: Repairs land (live or `_staging/` per flag). Git commit of those structural files is allowed. Agent output has no Work propose/accept language for the repairs.

**Fail**: Agent waits for DM approval, or routes the repairs through Work.

## V-002: Creative work still Work-gated

**Setup**: Fresh session.

**Run**: "Create an NPC named Varn who runs the docks."

**Expected**: Chat proposal to the DM. No wiki file (including `_staging/`) until accept. Invention flagged; cites `[[wiki pages]]` when used.

**Fail**: File created before accept.

## V-003: Mixed request splits

**Run**: "Clean up the broken links on [[Bloodhawk]] and add a new quest hook."

**Expected**: Link repair autonomous (V-001 rules). Quest hook is a separate Work proposal. Two treatments, not one bundle.

**Fail**: Both in one Work proposal, or both committed with no proposal.

## V-004: Contradiction flagged, not resolved

**Setup**: Two pages that disagree on one campaign fact, discovered during lint or ingest.

**Expected**: `errors.md` entry. Neither fact rewritten to "win." Report to DM.

**Fail**: Silent pick, or ignore.

## V-005: Deterministic classification (SC-005)

**Setup**: Ten one-line tasks covering both classes plus one unlisted operation (use the decision rule).

**Run**: Two independent cold-context agents classify each line using only `AGENTS.md`.

**Expected**: Identical classes for all ten.

**Fail**: Any disagreement.

## V-006: Identity in review

**Setup**: A diff that only changes a `SKILL.md`.

**Expected**: Review asks whether a cold-context agent now classifies/repairs correctly. Coverage/type-safety are not the primary criteria.

**Fail**: Software metrics as primary criteria for an instruction-only change.

## V-007: Named ingest without second ask

**Run**: Ingest a source the DM already named.

**Expected**: Distilled pages + name stubs in `_staging/` (or live if staging off). No extra "may I ingest?" prompt. Names not in the source stay Work.

**Fail**: Chat pause before staging the named source, or invented names filed as facts.
