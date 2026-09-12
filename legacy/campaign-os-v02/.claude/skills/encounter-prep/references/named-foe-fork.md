# Named foe vs. generic creature — the fork

**Named, may recur:** stop here, hand off to `.claude/skills/draft-content/references/npc.md` with the
encounter's context (role, CR target, one-sentence concept, the PC
connection). Once `.claude/skills/draft-content/references/npc.md` returns a page, wikilink it in Enemy Roster
and quote its `## Stats & Combat` block from that page — don't re-derive
or duplicate the stat block on the encounter page.

**Named for flavor only, no recurrence:** write the stat block inline on
the encounter page itself (§ Wiki placement). Don't invent a name at all
unless the concept clearly implies a singular antagonist (a cult leader, a
rival captain) — generic enemies (guards, bandits, wolves) never need one.
When a name is warranted, pick one consistent with the culture/region it
belongs to — this skill doesn't own a naming method of its own.

**Generic/homebrew creature, no name:** `.claude/skills/draft-content/references/monster.md` owns the design
method now — `vault/refs/vault/monster/references/cr-design.md` for
roles, ability hierarchy, CR math, and telegraphing, and
`vault/refs/vault/monster/references/statblock-format.md` for the codeblock syntax.
Reusable across encounters → hand off to `.claude/skills/draft-content/references/monster.md` for the actual
page (ecology, DM secrets, bestiary registration); quote its
`## Stats & Combat` block into the Enemy Roster, same as a named foe's
page. One-off, never reused → design it here per those same cited files,
write the stat block inline, no page and no hand-off.

## Wiki placement detail

`vault/_templates/_campaigns/_encounter.md` fixes its own required H2s (Opening, Enemy
Roster, Challenge Calibration, Terrain, Tactical Notes, Run Sheet, Raising
the Stakes, Lowering the Stakes, Endings, Stakes, If Ignored, Transition —
`## If They're Stuck` alone is `# OPTIONAL` — enforced by W1/W5 reading the
template directly), and the whole page is DM-only by construction — no
`## Player-Known` / `## DM Only` split needed.
`draft-run-guide` uses `type: session`
for its own page shape — a single fixed-name file per
session — distinct from encounter pages:

- **Every encounter gets its own file** — `vault/campaigns/shattered-sea/encounters/<slug>.md` —
  even a one-off tied to a single session. `draft-run-guide` never
  authors encounter substance itself (its own Hard Rule 3); it links and
  quotes this skill's output, so there must always be a real file to link
  to.
- **Whether a foe or creature gets its own page** (`.claude/skills/draft-content/references/npc.md`,
  `.claude/skills/draft-content/references/monster.md`) or stays inline here → the fork above. This skill never
  authors an NPC page or a reusable creature page itself — it wikilinks
  and quotes from those pages instead.
