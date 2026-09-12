# Output Structure — mapped onto the rule template

Read this when filling a rule page's sections, after § Standard queries and
§ Interview in `.claude/skills/rule-prep/SKILL.md` have already run.

The required H2s for `type: rule` are fixed: `## Mechanics`,
`## Provenance` — nothing added, nothing removed, this order (same
template `.claude/skills/draft-content/references/item.md` uses). No `## Player-Known`/`## DM Only` split:
`publish:`/`status:` on the page itself is the visibility gate, not a
heading name (`.claude/skills/composing-beats/references/runtime-surface.md` §8, enforced repo-wide by lint W20/W21
— no type is exempt). Content flows top-to-bottom under the page's
one-line description, in the order below, before `## Mechanics` — no
sub-heading of its own. The Player-Known/DM-only distinction below is a
*drafting* lens (what the table can learn through play vs. what only the
DM sees), not a page structure — the same precedent the npc guide's own
Output structure already established.

**Player-Known material**, first:

- **Flavor description** — 2–4 sentences, `[!read-aloud]` callout if the
  content has a presence at the table (a subclass's identity, a spell's
  cast description); plain prose otherwise (a background, a subsystem
  rule). No mechanical content here.
- **Stat line** for anything with a governed subtype worth stating
  plainly: `*[Subtype] · [base class, if subclass] · [level, if
  applicable]*`.

**DM-only material**, written after the Player-Known material and before
`## Mechanics`, never partitioned into its own heading: the rule's own
Toy-equivalent table plus anything that helps the DM run it but hasn't
reached the table yet:

| Field | What goes here |
|---|---|
| `core_fantasy` | The one-sentence niche (Hard Rule 3). |
| `balance_citation` | The 2 RAW comparables, or the specific benchmark row, that justify this design (Hard Rule 4). |
| `pc_connection` | Hard Rule 2's connection — which PC, or the DM's house-rule reason. Required, wikilinked if a PC. |
| `subclass_trap_checked` | Which "watch out" trap was checked and how it was avoided — `subclass` subtype only, `N/A` otherwise (Hard Rule 5). |

**`## Mechanics`** — every effect the rule has, each one `[HB]`/`[RAW]`-
labeled, bounded (action cost/range/duration/recovery), with edge cases
named where they'd plausibly come up at the table. For a `class`, this
section holds the full level 1–20 feature table; for a `subclass`, the
3rd/6th/10th/14th (or class-specific) feature set; for a `spell`, the full
stat block (casting time, range, components, duration, description, at
higher levels); for a `feat`, its complete text; for a `species`, the
standard trait template from `.claude/skills/rule-prep/references/species-design.md`.

**`## Provenance`** — where this rule came from: which PC or DM request
prompted it, what edition/book precedent it reflavors if any, and the
date/session it was approved at the DM Review Gate.
