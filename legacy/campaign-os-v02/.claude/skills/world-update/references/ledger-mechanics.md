# Ledger mechanics — where proposals land

**File:** `vault/episodes/NNN/world-turn-<YYYY-MM-DD>.md`, where `NNN` is the
directory found by the Gate check above — never `vault/episodes/NNN/state-changes.md` (that file's
writer is ingest only, per `vault/refs/runbook-wiki.md` § Who writes what; a world
turn is a separate, separately-reviewed proposal, not an addendum to an already-
processed session ledger). Get today's real date with `date +%Y-%m-%d` — never guess
it. If a file for today already exists (a second on-demand turn same day), re-read it
from disk and append new lines rather than creating a second file for the same date;
ask the DM if it's ambiguous which turn a new proposal belongs to. This covers only a
*same-date* rerun — a rerun on a later day, with an earlier day's file still awaiting
`canon-review`'s apply, is the Gate's Cross-day idempotency check's job, run before
triage, not here.

**Frontmatter and headings** — instantiate `_templates/session-world-turn.md`
(never freeform; vault/CLAUDE.md rule 4). Its `subtype: world-turn` is what
resolves this file against a real template for W84's frontmatter-schema
check — a bare `type: session` with no `subtype:` has no matching
template and fails lint.

**Grammar** — identical to `vault/refs/runbook-ingest.md`'s Phase 4 citation shape, unmodified:
`- [ ] VERB target :: change (citation)`. Same closed verb set:

| Verb | Mechanized? | When a Front advance uses it |
|---|---|---|
| `FACT` | No (manual — prose) | The Front's own `**Clock:** ... — filled: n` line changing, and/or `**Lifecycle:**` flipping on a fill or a dormant trigger firing. Every advance uses this. A `**Lifecycle:**` flip also means re-checking every Front on that page and setting frontmatter `has_active_front: true`/`false` to match whether any is now `active` — fold that into the same `FACT` line, don't write a second one. |
| `APPEAR` | Yes (append to `## Session Log`) | Logging the turn itself: append `- sNN — <Front name> advanced to n/N, <outcome>` to the *Front's own owning page's* `## Session Log` (born on first real entry — no template scaffolds it empty) — this is the session-by-session log a Front's block has no field for. Also used when an existing NPC/location becomes newly relevant to this turn. |
| `NEW` | Yes (template-instantiate) | A brewing thread crystallizes into a wholly new page (npc/location/quest) the wiki has no stub for yet — never a new *faction or NPC*; that's `.claude/skills/draft-content/references/faction.md`'s job even mid-turn (Hard Rule 5). |
| `QUEST` | Yes (YAML edit) | A Front's fill resolves or fails an existing `quest_status` (via its `**Quest link:**`). |
| `REVIEW` | No (canon-review queue) | The deep read turned up a contradiction between the faction page and the recap/ledger — append a CONTRADICTION block (format: `transcript-ingest` skill's CONTRADICTION example) to the page being read, then log this line. |

Every ordinary advance therefore writes at least two lines: one `FACT` (the Clock/
Lifecycle edit) and one `APPEAR` (the dated log entry on the Front's own owning page).
`MOVE`, `STAT` are PC/prep-migration verbs with no natural use here — if a
world turn seems to need one, that's a sign the change belongs to a different phase,
not this skill.

**Citations** — the grammar requires a trailing parenthetical
containing an `L`-number; nothing checks which file the `L` refers to. A session
ledger's citation points at a transcript line; a world-turn ledger's citation points
at the **wiki page line that states the trigger or evidence** (`grep -n` it, paste it,
cite it — the same "read it or don't claim it" discipline, aimed at canon instead of a
transcript). Example: `(vault/campaigns/shattered-sea/factions/tideglass-concordat.md L36)`.

**`STAT`/`QUEST` change syntax uses the Unicode arrow `→`, never ASCII `->`.**

**`APPEAR`'s emitted form:** it appends a plain bullet —
`- sNN — <desc>` — never a `[[wikilink]]`. No page is ever named after a session
directory, so a bare `sNN` citation is what's always resolvable; there is no
wikilink here to trip `wiki_lint` W3, and nothing to correct by hand as part of
closing out.

## Never edits canon directly

Same L2 seam INGEST uses: this skill's entire output is ledger lines for a human to
review. `canon-review` applies them, by hand for `FACT`/`REVIEW`, per its own
manual-merge steps. This holds by convention, not a gate: propose the line, even
under pressure to "just fix the page directly, it's obviously right."
