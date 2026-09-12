---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-15"
updated: "2026-08-15"
tags: [craft]
summary: "QC profile for a type: beat page."
uid: e7a3c4b1-2f5d-4a9e-8c1f-3d6e9b0f2a48
---

# QC profile: beat

For a `type: beat` page (`beat_type:` hook | development | cliffhanger |
climax | resolution). Check against `.claude/skills/composing-beats/SKILL.md`
and the owning beat-type skill named in `owner_skill:`.

Template: `vault/_templates/_episodes/_beat_<beat_type>.md`.

| CATEGORY | Contract | How to check |
|---|---|---|
| COLD-RUNNABILITY | The beat runs cold from the page alone: the narration embed is present, `entry_state:` is a concrete condition (not a placeholder), and `handoff:` names real beat types or pages. | Confirm the page's narration-open embed resolves to a real sibling file. Read `entry_state:` and `handoff:` for concreteness. |
| GRAVITY | The Player Gravity section's Link of Relevance traces to an established PC investment, not a generic proximity claim. | Cite `.claude/skills/composing-beats/references/audits.md` § Gravity audit; check each row against a real PC dial/terminal node. |
| CONSEQUENCE | `if_ignored:` states an observable world change, not a vague or absent consequence. | Read `if_ignored:` against `.claude/skills/composing-beats/references/audits.md` § Gravity audit's if-ignored standard. |
| WORLD-ACTING | The beat happens TO the party — actors act, the world moves — with no prescribed player action. | Read Actors and Conditional Reactions for actor-driven language; flag any line that tells the party what to do. |
| FRONTMATTER | Every non-OPTIONAL key of the beat's template; `status:` `draft`/`pending`; `publish: false`. | Diff frontmatter against the matching `_beat_<beat_type>.md` template. |
