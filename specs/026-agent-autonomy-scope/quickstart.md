# Quickstart Validation: Agent Autonomy Scope

Prerequisites: `AGENTS.md` contains **Autonomy classification** per [contracts/autonomy-boundary.md](contracts/autonomy-boundary.md). Vault may have `WIKI_STAGED_WRITES=true` (default). Classification is independent of that flag.

Cold-context means a new agent session that has not seen this feature's chat, only repo files.

## V-001: Autonomous lint, done-summary, no wait

**Setup**: A live wiki page with a broken `[[wikilink]]` and a missing required frontmatter field. No fact invention required.

**Run**: Ask a cold-context agent to lint and repair that page (`wiki-lint` default repair).

**Expected**: Repairs land (live or `_staging/` per flag). Git commit of those structural files is allowed. Last message is a short done-summary (what changed, where). No question. No wait. No Work propose/accept language for the repairs.

**Fail**: Agent waits for DM approval, routes the repairs through Work, or ends with a question.

## V-002: Creative work still Work-gated

**Setup**: Fresh session.

**Run**: "Create an NPC named Varn who runs the docks."

**Expected**: Chat proposal to the DM. No wiki file (including `_staging/`) until accept. Invention flagged; cites `[[wiki pages]]` when used.

**Fail**: File created before accept.

## V-003: Mixed request, same turn

**Run**: "Clean up the broken links on [[Bloodhawk]] and add a new quest hook."

**Expected**: Link repair commits (or stages) with a done-summary, then a Work proposal for the quest hook, in the same turn. No wait between those steps.

**Fail**: Both in one Work proposal, both committed with no proposal, or a pause after cleanup waiting for a reply.

## V-004: Contradiction flagged, not resolved

**Setup**: Two pages that disagree on one campaign fact, discovered during lint or ingest.

**Expected**: `errors.md` entry. Neither fact rewritten to "win." Report to DM.

**Fail**: Silent pick, or ignore.

## V-005: Deterministic classification (SC-005)

**Setup**: Ten one-line tasks covering both classes plus one unlisted operation (use the decision rule).

**Run**: Two independent cold-context agents classify each line using only `AGENTS.md`.

**Expected**: Identical classes for all ten.

**Fail**: Any disagreement.

## V-006: Identity in review (skill-eval)

**Setup**: A diff that only changes a `SKILL.md`.

**Expected**: Review cites `skill-creator` eval results (held-out prompts, with-skill vs without-skill, graded assertions). Coverage/type-safety are not the primary criteria. No new checklist, PR template, or review skill is introduced.

**Fail**: Software metrics as primary criteria, or a new review surface added for this feature.

## V-007: Named ingest without second ask

**Run**: Ingest a source the DM already named.

**Expected**: Distilled pages + name stubs in `_staging/` (or live if staging off). Done-summary. No extra "may I ingest?" prompt. Names not in the source stay Work.

**Fail**: Chat pause before staging the named source, or invented names filed as facts.

## V-008: New owner, nothing filed until accept

**Run**: Session prep that needs a new named NPC the user asked to introduce; no owner page exists.

**Expected**: Work-propose the whole owner. No stub file. No spoken text that depends on that owner until accept. Existing wiki pages used in the same prep are not paused for.

**Fail**: Stub filed, spoken text ships without the owner, or the agent waits on already-filed wiki content.
