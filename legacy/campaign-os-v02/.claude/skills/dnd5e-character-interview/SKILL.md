---
name: dnd5e-character-interview
description: Conduct the 20-question D&D character interview in a Campaign OS repo — building a new PC page, or filling an existing one's gaps. Use for "interview my character", "run me through the character questionnaire", session-zero work, or guided Q&A into a character's background/personality/motivations. Not combat stats (combat-profiles) or a canon PC page (canon-review).
---

# D&D Character Interview

This skill has one deliberate deviation every other Prep-family skill
doesn't have — see § Owned paths.

The only skill that originates `vault/campaigns/shattered-sea/pcs/<name>.md` content. Uses Nick's
20-question framework — a warm, conversational interview, not a form to
fill out — to build a new PC page, or resume one that's missing pieces.

## Standard queries

Run before starting any interview:

```
grep -ril "<character name>" vault/campaigns/shattered-sea/pcs/ vault/ 2>/dev/null
```

A hit on `vault/campaigns/shattered-sea/pcs/` is **Resume Mode** (§ below), not a duplicate to avoid — PC
pages are expected to start thin and fill in over time. A hit on `vault/`
(an NPC stub already exists under this name — the party met them before
they were a PC, or a name collision) is a DM escalation: stop and ask,
don't silently proceed as if it's the same entity or a different one.
Empty output: a genuinely new PC, start fresh.

## Owned paths

Writes `vault/campaigns/shattered-sea/pcs/<name>.md` directly. PCs are canon-by-nature (player-authored,
not table-witnessed) — a page lands here directly at `status: canon` once
the interview is complete, no separate approval step, never a reviewed
ledger line the way `world-update`'s faction-clock advances require — see
§ Workflow step 5.

Also writes `vault/campaigns/shattered-sea/pcs/interviews/<name>-interview.md` — the verbatim Q&A record
(`vault/_templates/_campaigns/_pcs/_pc_interview.md`), same direct write as `vault/campaigns/shattered-sea/pcs/<name>.md`. The
transcript is the frozen historical record of what was literally asked and
answered; `vault/campaigns/shattered-sea/pcs/<name>.md` is the current synthesized state built from it.
Resume Mode appends a new dated round to the transcript — it never rewrites
an earlier round's record.

Never touches `vault/` (an NPC/faction/location this PC's answers mention
gets wikilinked, never authored inline here — that's the owning prep
skill's job). Never sets `publish:` — that's the publish proposal's move,
same as any other page.

## The 20 questions

Ask one at a time, in order, prefixed with its number ("**Question 1 of
20.**") so the player knows where they are. Acknowledge each answer
briefly, then move on — no follow-ups, all 20 cover the ground. "Skip" or
"Next" is a completely valid answer; note the question as unanswered and
continue without comment. Full numbered list of all 20 questions, plus the
verbatim opening and closing lines: `references/twenty-questions.md`.

## Frontmatter fill (not one of the 20)

Ask once, together, after the 20 questions: player name (who plays this
character), class/level (`class_levels`), and current HP/AC if the player
has a character sheet handy. **Fill only what the player states — a
missing stat is a stub note, not a guess**; a PDF sheet or later session
completes it via canon-review. Equipment/items the player mentions are
Overview prose, never frontmatter.

The template also carries an optional `role:` key
(`villain | ally | rival | recurring | contact`, `vault/_templates/_campaigns/_pcs/_pc.md`) — stays
absent for the ordinary case. No new interview question for it; fill it
only if the player or DM explicitly states the PC occupies one of those
narrative functions (e.g. a PvP rival arc), never inferred from the
interview answers.

The template's "Read while recording" line points to this PC's own
`<name>-voice-script.md`; generate it with the `script-writer` skill if
it doesn't already exist.

## Resume Mode

The standard-queries hit routes here. Read the existing `vault/campaigns/shattered-sea/pcs/<name>.md` by
**answer content, not by question text** — an older document may use
different wording or numbering; extract answers and map them to the
current 20 questions by topic. Identify which questions have no usable
answer yet, tell the player what's missing by topic (not a bare list of
numbers), then ask only the missing ones, current wording, current
numbering. The output replaces the existing content for the sections
touched — never preserve old question wording, and never re-ask an
already-answered question. Append a new dated round to
`vault/campaigns/shattered-sea/pcs/interviews/<name>-interview.md` covering only the questions actually
asked this round — never rewrite an earlier round to match current wording.

## Output structure — mapped onto the pc template

Template headings stay fixed, in order, nothing added or removed:
`## Overview · ## Backstory · ## Arc Notes (DM Only) · ## Session Log`.
The 20 answers route by content, not as a preserved Q&A transcript — no
"Interview Answers" section exists on the pc template, and a raw Q&A dump
here would duplicate what these sections already state in synthesized form.
The verbatim record lives on its own page instead (§ Owned paths,
`vault/campaigns/shattered-sea/pcs/interviews/<name>-interview.md`), never inline on `vault/campaigns/shattered-sea/pcs/<name>.md`.
Full section-by-section mapping of every question to its landing section,
including the Mortis hidden/visible split and the Arc Notes thread list:
`references/output-structure.md`.

## Hand-off to canon-review

Once every section is drafted, write `vault/campaigns/shattered-sea/pcs/<name>.md` and
`vault/campaigns/shattered-sea/pcs/interviews/<name>-interview.md` directly at `status: canon`
(canon-by-nature — § Owned paths; a player-character interview is canon by
default, no separate sign-off step) — this skill performs the write itself,
immediately, it does not queue it for a separate session. `created:`/
`updated:` = today's real date (fill in the template's `"{date}"`
placeholder).

If the standard queries found this PC already `status: canon` (a Resume
Mode gap-fill, not a fresh create), the gap-fill writes directly the same
way — this skill may expand an already-canon page it's filling gaps in, but
a contradiction with existing content (not a gap, an actual conflict)
routes to `canon-review` proper instead of a silent overwrite, same as any
other page (`vault/refs/runbook-wiki.md`'s CONTRADICTION-block rule).

## Degrade by asking

+ Any of the 20 unanswered → ask again later or note it unanswered — never
  invent an answer.
+ Mortis, secret, or "hidden vs. table-visible" ambiguous → ask which,
  don't default either way.
+ Stub check hits an existing `vault/` NPC with this name → stop, name the
  ambiguity, ask the DM before treating it as this PC.
+ HP/AC/class_levels not stated → leave blank with a stub note, never
  guess a number.

## Workflow

1. **Standard queries** — stub check. Empty → fresh create (step 2).
   Hit in `vault/campaigns/shattered-sea/pcs/` → Resume Mode (step 2, gap-fill only). Hit in `vault/` →
   stop and ask.
2. **Interview** — the 20 questions, one at a time (or the missing subset,
   in Resume Mode), then the frontmatter fill.
3. **Instantiate** `vault/_templates/_campaigns/_pcs/_pc.md` and `vault/_templates/_campaigns/_pcs/_pc_interview.md`
   (fresh create) or open both existing pages (Resume Mode) — copy the
   templates, don't retype them.
4. **Fill sections** per § Output structure; log the round verbatim into
   the interview transcript as it's asked, question text as actually
   spoken.
5. **Write `vault/campaigns/shattered-sea/pcs/<name>.md` and `vault/campaigns/shattered-sea/pcs/interviews/<name>-interview.md`**
   directly at `status: canon` once every section is filled (§ Hand-off) —
   no intermediate `status: pending`/`draft` stage on disk the way other
   prep skills do (§ Owned paths).

## Checklist (run before calling the page done)

+ [ ] Standard queries run and pasted; Resume Mode correctly identified,
      or a clean create confirmed.
+ [ ] All 20 questions asked (or, in Resume Mode, only the genuinely
      missing ones) — none invented.
+ [ ] Template H2s present, in order, nothing added or removed; no
      separate raw-Q&A section.
+ [ ] Player/class_levels/hp_max/ac filled only from what the player
      stated — blanks left blank, not guessed.
+ [ ] Hidden-vs-visible call made explicitly for Mortis/Q13/Q19 material,
      not defaulted.
+ [ ] `status: canon` set on write (never `pending`/`draft` left standing).
+ [ ] `vault/campaigns/shattered-sea/pcs/interviews/<name>-interview.md` written alongside `vault/campaigns/shattered-sea/pcs/<name>.md`,
      question wording as actually asked, answers verbatim; a Resume Mode
      round appended, not overwritten.

## Creative-domain rider

Facts, canon, structure, and the hidden-vs-visible call are bound (the
rules stated above — Owned paths, § The 20 questions, § Resume Mode — and
all CLAUDE.md project rules). **Prose style is free** — the
interview is a conversation, not a form; push for the specific, warm,
in-character detail over a safe generic answer, same rider every other
creative campaign skill carries.

## Out of scope

+ Combat stats, DPR, effective HP, or difficulty calibration —
  `combat-profiles`'s job entirely; this skill never computes or writes
  quantitative combat data.
+ An NPC, faction, location, or item this PC's answers mention — those get
  wikilinked, authored by their own owning prep skill, never inline here.
+ Resolving a genuine contradiction on an already-canon PC page —
  `canon-review`'s job (§ Hand-off).
+ Setting `publish: true` — the publish proposal's move, same as any
  other page.

## Reference files

| File | Read for |
|---|---|
| `references/twenty-questions.md` | Full numbered list of all 20 questions, plus the verbatim opening and closing lines. |
| `references/output-structure.md` | Section-by-section mapping of every question's answer onto Overview/Backstory/Arc Notes/Session Log, including the Mortis hidden/visible split. |
| `references/worked-example.md` | Full fixture page (placeholder name, not real campaign content) walking a fresh interview through standard queries, all 20 questions, frontmatter fill, and every template section. |
