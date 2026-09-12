Scenario-specific elaborations on the extraction categories (transcript-ingest/SKILL.md
§ What each fact becomes, § What becomes a page edit).

## Repeated information

Repeated information extracts once, at first mention — later restatements
of the same fact are not separate edits.

## New template-type confidence

`New` template-type confidence (pc vs npc is the recurring fork): commit to
a type only on textual evidence (the source labels them, an existing page
states their status, they're addressed as "you"/the party). Evidence absent
→ still pick the likelier type but note `(type unconfirmed)` on the page
(e.g. in its one-line description) so the human review pass rules on it.

## Combat

Don't build a separate combat-summary artifact — this system has no
downstream consumer specced for one. Extract combat's *durable* consequences
only, as Stat edits citing the transcript ("DM: everyone's level 6 now") —
round-by-round blow detail is table color, not page content, unless it's the
kind of tactically-notable sequence worth a Session Log entry (see
master-kyzil.md's Session 04 entry for the worked example — narrative beats
plus a trimmed tactics reference, not a full round-by-round log); PC stats
have exactly one home (the PC's own `vault/campaigns/shattered-sea/pcs/<name>.md` page) and it isn't a
combat log.

## Who's talking vs. who they're talking as

transcript-label only resolved the physical speaker. If a `**Nick (DM):**`
line is voicing a named NPC ("I offer you a fair price," said in-scene), attribute the
resulting Fact/Appear edit to the NPC, not to "the DM" — read the
surrounding scene for a first/third-person shift and context. Same when a
player voices their own companion NPC.
