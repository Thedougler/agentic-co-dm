---
paths:
  - "vault/refs/**"
  - "docs/guardrails/**"
  - ".claude/skills/**/SKILL.md"
  - "_templates/**"
---
Authoring standard for this repo's guidance corpus — CLAUDE.md, skills,
rules, and runbooks. This is a stateless system: every session reads these
files cold, so bloat here costs every future session, not just this one.

`vault/stories/**` and `vault/ideas/**` are narrative
and raw material governed by their owning skills' contracts (`draft-story`,
`campaign-writers-room`) — this file's
corpus-doc standard does not apply there. `docs/rulings/**` is
exempt from the "no historical narration" line — decision records keep
their "why"/history, governed by `campaign-domain-modeling`'s contract.

- State current behavior only. Never "used to be", "no longer", "was
  retired", a migration/provenance note, or any other historical narration —
  `git log` is the history.
- No meta-commentary about the agent's own reasoning, process, or this
  file's maintenance philosophy. State the rule. A non-obvious constraint
  gets one line, not a paragraph.
- State only the correct action, invocation, or usage. Never document an
  incorrect version for contrast — a rule that needs a wrong example to
  land is unclear, not under-illustrated.
- DRY: a fact or instruction lives in exactly one file. Every other file
  that needs it links to that file instead of restating it — same
  transclusion-vs-wikilink test as vault/CLAUDE.md rule 8.
- Terse: the rule, not an essay defending it.

Frontmatter `description:` fields on skills are exempt from the terseness
line above — they are the model's trigger-matching surface and are
authored per `writing-for-agents`'s contract, not this one.
