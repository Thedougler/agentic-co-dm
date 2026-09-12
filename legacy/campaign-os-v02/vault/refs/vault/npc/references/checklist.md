---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The NPC-specific checks that run after the shared checklist — the Wants line, the five Toy fields, the Opening move."
created: "2026-08-03"
updated: "2026-08-08"
tags: [survival]
uid: 3daa3f45-6763-4b52-9308-363d171f79f2
---

# Draft — NPC Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
NPC-only additions. `vault/_templates/_campaigns/_npcs/_npc.md` owns this
page's layout; this checklist never adds or reorders a heading or block.

- [ ] Opening `**Wants:**` line present (The Wants Line,
      `.claude/skills/draft-content/references/npc.md`).
- [ ] All five Toy Chest fields present, each passing its field rule:
      vector / behavior / situation / vibe+tic / one-sentence connection
      (`vault/refs/vault/npc/references/toy.md`).
- [ ] `link_of_relevance` (the PC-Connection Requirement) is echoed under
      `## Relationships`, not left in the Toy Chest alone.
- [ ] Opening move present for any NPC appearing in a session, or
      correctly omitted (The Opening Move, `.claude/skills/draft-content/references/npc.md`).
- [ ] Quote passes The Quote Is Theirs test
      (`.claude/skills/draft-content/references/npc.md`).
- [ ] Read-aloud sized correctly for the NPC's session status
      (`vault/refs/vault/npc/references/output.md`).
- [ ] A roleplaying crib note is present, if the NPC needed one
      (`vault/refs/vault/npc/references/output.md`).
- [ ] `subtype:` set explicitly to `major`, `minor`, or `recurring` — never
      left absent.
- [ ] `## Stats & Combat` present only when this NPC needs combat numbers
      (`vault/refs/vault/npc/references/output.md`).
- [ ] `## Goals & Fronts` present only for `subtype: major`/`recurring`
      with a real Front, absent otherwise (the Front decision rule,
      `vault/refs/vault/faction/references/front.md`).
