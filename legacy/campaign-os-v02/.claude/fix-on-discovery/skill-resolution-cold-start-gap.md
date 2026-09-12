---
status: resolved
lever: skill+rule
target: .claude/rules/skills.md, .claude/skills/
---

# Scoped `<subtree>/.claude/skills/` entries were invisible to direct invocation until the subtree was already touched

**Resolution:** REFACTOR-PLAN.md P3.3 collapsed all skill roots
(`content/.claude/skills/`, `content/pcs/.claude/skills/`,
`content/campaign/shattered-sea/episodes/.claude/skills/`,
`utils/.claude/skills/`) into the single always-visible `.claude/skills/`
root. Every skill is now model-invocation-visible from session start —
there is no longer a subtree that must be touched first for a skill's name
to resolve. `.claude/rules/skills.md` states the current single-root
contract; directory scoping no longer exists in this repo.

**Original gap:** `content/ref/draft/draft-npc.md`, `item-prep`, `location-prep`, `content/ref/draft/draft-ship.md`
(previously under `content/.claude/skills/`) failed to resolve by name
("Unknown skill") when invoked as a near-first action in a session, while
`draft-faction.md` (same directory, same scoping) resolved fine — a
cold-start timing gap, not a special case: nested
`<subtree>/.claude/skills/` entries only surfaced once the harness had
scanned that subtree, which happened as a side effect of reading a file
there, not at session start.

**RED:** REFACTOR-PLAN.md P0.6 (2026-08-01 audit): "70 'Unknown skill'
errors across 15 sessions ... one session burned ~120 turns on it."
