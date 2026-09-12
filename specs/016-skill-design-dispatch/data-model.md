# Data Model: Skill Design Dispatch

Entities are jobs and outcomes. No database.

## In-scope instruction file

A file this routing applies to.

| Kind | In |
|---|---|
| Source skill (`SKILL.md` and its bundled references/scripts) | yes |
| Standing project instruction / sticky rule (`AGENTS.md`, `.omp/AGENTS.md`, `RULES.md`) | yes |
| Subagent definition | yes |
| Agent-writing authority (`writing-for-agents`) | yes |
| Constitution | no |
| Feature specs | no |
| Generated Spec Kit command adapters | no |
| Campaign wiki | no |

`.omp/AGENTS.md` and `.claude/CLAUDE.md` that only import `AGENTS.md` are not a second gate.

## Instruction edit

One proposed change to one or more in-scope files.

| Field | Rule |
|---|---|
| Targets | In-scope paths named before write |
| Class | `design-impact` \| `not` |
| Writer | designated writer if design-impact (unless owner overrule); else session agent |
| Overrule | explicit owner skip only; silence is not overrule |

Classify before any target changes.

## Design-impact

True if the change would alter any of:

1. Skill triggering (`description` / trigger)
2. Workflow ownership (which skill or agent does a step)
3. Standing load (what is always in context)
4. Creating a new skill or subagent

Length is not a field. Borderline of those four → `design-impact`. New skill or new subagent → always `design-impact`.

## Scoped prompt

Handoff from session agent to designated writer (or into parked work).

| Field | Rule |
|---|---|
| Outcome | What must be true when done |
| Files | In-scope targets |
| Bounds | What must not change |
| Job | One design job, not an unbounded rewrite |

## Parked dispatch

Tracked incomplete design-impact work.

| Field | Rule |
|---|---|
| Title | `Parked skill design: <outcome>` |
| Label | `ready-for-agent` |
| Body | The scoped prompt |
| Targets on disk | Match content at dispatch start |

States: `open` → `resumed` → `done`. Search existing `Parked skill design:` issues before creating another for the same job.

## Dispatch outcome

| Value | When |
|---|---|
| `session-agent` | Class is not design-impact, or owner overruled |
| `dispatched` | Designated writer landed the change; session agent verified; no rewrite |
| `parked` | Designated writer could not complete; targets restored; issue exists |
| `out-of-scope` | File is not in-scope; this routing does not apply |

## Relationships

- Instruction edit → one class → one writer (unless mixed request, then split)
- Design-impact + writer available → dispatched
- Design-impact + writer unavailable → parked dispatch
- Parked dispatch → later session resumes from issue body, no original chat
- Successful dispatch → session agent verifies, does not rewrite
