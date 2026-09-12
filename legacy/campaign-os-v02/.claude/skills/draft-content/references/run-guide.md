---
name: run-guide
description: Compose a stretch run-guide in a Campaign OS repo (vault/ present). Use for "build the run guide", "run the session from", or a Situation that needs a how-to-run. Not a single Beat, or the Situation page itself. Covers the episode overview via § Overview pass.
---

# Run Guide

A chronological *walk* for one *stretch*. Headings and the one-line usage
for each live on
`vault/_templates/_episodes/_session_run_guide.md` — copy that file, fill
it, never restate its heading list here.

Read `.claude/skills/writing-narrative-islands/SKILL.md` and
`.claude/skills/composing-beats/references/runtime-surface.md` § Session shapes first. Unused prep has no authority. Document order
is play order. Transclude spoken siblings and owner headings on the
numbered H2s. Exit is the only heading that opens another file.

If the overview page does not exist, build it first using § Overview pass,
below, plus this file's own Standard queries and Checklist sections.

## Compose

- Episode stretch → `vault/episodes/<NNN>/e<NN>-run-guide-<slug>.md`.
- Situation walk → `<situation-slug>-run-guide.md` beside the Situation.
- Opening episode stretch only → Last Time embeds `e<NN>-narration-last-time`.
- Prep → this stretch's where, who, live secrets, 1–3 reminders.
- Numbered play H2s → spoken picture, then a check table
  (`.claude/skills/composing-beats/references/runtime-surface.md` § Check tables), then `![[<page>#Heading]]`.
- Side-tracks → `[[wikilink]]` to another run-guide or Situation.
- Exit → each mutually exclusive remainder is a run-guide wikilink. Live
  Branches stay on the Beat Chart; landings are the next H2 or an Exit
  row.

This file names tonight's owners by transclusion; it does not retype them.

## Owned path

Episode: `vault/episodes/<NNN>/e<NN>-run-guide-<slug>.md`.
Situation: beside the Situation page. `status: draft` while filling,
`status: pending` once lint and QC clear — never `canon`, never
`publish: true`.

## Hard rules

Full text: § Hard rules — full detail, below. Rules 1, 3, 5–7, 9–13, 17–20
apply. These four are run-guide-specific:

- Rule 4. Numbered H2s transclude spoken siblings and owner headings.
  After each spoken picture, write a check table (`.claude/skills/composing-beats/references/runtime-surface.md` § Check tables).
  Side-tracks and Exit are `[[wikilink]]`.
- Rule 9. Last Time closes on the prior recap hook; only the opening
  stretch embeds it.
- Rule 15. Exit is the only "open another file" heading.
- Rule 16. Compose after the owners this walk transcludes exist.

## Workflow

Each step ends on `RG<n>: <content, or N/A — reason>`.

1. **Overview exists.** Overview page present, lint-clean, and
   QC-passed (§ Overview pass, § Checklist, below), or build it first
   with this file's own workflow before continuing to the walk.
   `RG1: <overview path>`.
2. **Owners exist.** Every page this walk transcludes has the heading
   or spoken sibling the H2 will embed. `RG2: <owner list>`.
3. **Instantiate.** Copy `vault/_templates/_episodes/_session_run_guide.md`
   to the stretch path. `RG3: <path>`.
4. **Last Time.** Opening stretch only; otherwise delete the heading.
   `RG4: <hook line | deleted>`.
5. **Prep.** Where, who, live secrets, 1–3 reminders.
   `RG5: <reminder count>`.
6. **Walk.** Numbered H2s in play order. Each spoken picture is
   followed by a check table (`.claude/skills/composing-beats/references/runtime-surface.md` § Check tables), then the owner heading.
   `RG6: <H2 list + table row counts>`.
7. **Side-tracks.** Wikilink every other live walk this stretch can
   open. Delete the heading when none. `RG7: <linked slugs | deleted>`.
8. **Exit.** Each mutually exclusive remainder is a run-guide. Cover
   every OV10 guide that this stretch can hand to.
   `RG8: <exit rows>`.
9. **used_by.** Add this guide to each transcluded owner's `used_by:`.
   `RG9: <owners updated>`.
10. **Lint.** `npm run lint -- <path>` on the run-guide page.
    `RG10: <0 findings>`.
11. **QC.** `content-quality-checker` with profile `run-guide`.
    `RG11: <PASS | findings fixed>`.
12. **Pending and commit.**
    `prep(sNN): run guide <slug> for session NN`. `RG12: <hash>`.

## Hard rules — full detail

Rule numbers match the core `## Hard rules` list above.

1. **PREP gates first, every time.** Run `git log --oneline | grep ingest`, paste it first.
   Missing ingest commit → tell the user which phase is missing, don't build on an
   un-ingested table. Then `ls vault/stories/session-NN-*.md` — no session story on
   the shelf → run `draft-story` first, hard stop; the guide is derived from the story, never
   drafted ahead of it. Override on either → note `GATE-OVERRIDDEN by user`.
2. **Getting Started is asked, never assumed.** Ask the template's three DM-only questions
   together, before drafting anything else.
3. **Every referenced entity resolves.** Stub check (`.claude/skills/composing-beats/references/runtime-surface.md` §1) first —
   empty/noisy escalates up `llm-wiki-query`'s tiers, never straight to "doesn't exist".
   Existing page → wikilink; situation-driving entity → the owning `draft-*` route (Rule 4); passing
   mention → minimal stub (Owned paths). Never a bare name.
4. **Every at-table object is a Situation or Route**, plus a Beat only
   when the plot-weight gate holds. The index names it.
   The run-guide transcludes spoken siblings and owner headings; Exit and Side-tracks are wikilinks.
5. **Off-screen faction movement is pending pressure, never a canon write.** The clock tick is
   `world-update`'s job, post-INGEST — never fire a front's consequence-at-fill; flag it
   close, hand off.
6. **The whole file is DM-only by construction** — never instantiate a `## Player-Known` /
   `## DM Only` split; `publish: true` never applies.
7. **Plan to the table's real hours.** Judge by feel against the session
   length; over budget means split into a second guide, not cram more
   situations in.
8. **Every Situations and Pressure entry states why it's live tonight**,
   distinct from the linked page's own facts — a bare restated fact fails.
9. **Any recap opener is derived, not invented.** When a table frame needs a
   last-time handoff, pull from the prior session's own
   `vault/episodes/NNN/sNN-recap.md` (`recap-writer`'s output); close the box on
   the line the opening Beat's opener picks up (§ Recap → opener coupling, below).
10. **Never flip `status:` past `pending` or touch `publish:`** — `transcript-ingest`/
    world-update/canon-review and PUBLISH own those verbs.
11. **Degrade by asking, not guessing.** See § Degrade by asking, below.
12. **Template-conformance drift is `content-fixer`'s, never hand-fixed** — one dispatch per
    drifted file; hand-edit only content authored this cycle.
13. **Every roster NPC opens with a `Wants:` line**, then voice, then mannerism — the
    scannable motivation a DM improvises from (`.claude/skills/composing-beats/references/runtime-surface.md` §
    Roster entry format).
14. **Run guides (overview) and Exit (run-guide) are filled last**,
    and only from real Situations, Routes, walks, and Beats.
15. **Numbered play H2s transclude spoken siblings and owner headings.
    After each spoken picture, write a check table (`.claude/skills/composing-beats/references/runtime-surface.md` § Check tables).
    `## Side-tracks` and `## Exit` are `[[wikilink]]`.**
    A line naming a page absent from tonight's set is worse than no line.
    Exit is the only heading that opens another file.
16. **The run-guide composes existing owners.** Transclude their spoken
    siblings and headings; wikilink Side-tracks and Exit.
17. **A crossing is a Route.** The party ending the night somewhere it
    didn't start means one or more `type: route` legs; each chain-loads
    `travel-events`, whose events land as Route samples or one
    plot-weight Beat. "Three days later, you arrive" is a transition,
    not a session. Party stays put → the `RG6` token records `no leg`
    (§ Standard queries, below, § Journey check).
18. **A Live Branches row is earned only when the party's own choice or
    roll creates materially different future situations.** An NPC offer
    stays on the Situation. Destinations are a Situation/Route menu, not
    an exclusive branch that commits the night. Collapse test:
    `.claude/skills/composing-beats/references/audits.md` § Branch
    collapse test.

## Overview pass

Read when composing the episode `eNN-overview.md` page — the entry agents
and the DM read first, before any run-guide walk.

- Every table-ready object is a Situation or Route, plus a Beat only when
  the plot-weight gate holds (Rule 4).
- Every Read-first line states why it is live tonight, on top of the
  linked page's own facts — a bare restated fact fails.
- Run guides is filled last, and only from guides that already exist or
  this pass will mint.

## Degrade by asking

- PREP gate fails or Getting Started unanswered → Rules 1–2 bind: ask.
- No open threads and no recent Session Log → ask what should open the
  session rather than inventing pressure.
- An entity's PC connection isn't obvious → ask which PC and the
  mechanism; "connects to the party" is never an answer.
- Ambiguous stub-check hit → stop, ask, don't auto-merge.
- Session date or table time unknown → ask.
- No loot-pacing convention on file and Rewards is ambiguous → ask what
  feels earned, don't invent a reward tier.
- Unsure how much weight a situation carries tonight → ask before handing
  it to `composing-beats` for a Beat.
- No prior `vault/episodes/NNN/sNN-recap.md` on file to open the Recap section from → ask the
  DM for the last-time beats directly (§ Recap → opener coupling, below).
- No safety tools on file for this campaign → ask once, not every session
  (skip if already established): sensitive topics, hard lines vs.
  off-screen content, a verbal pause cue (`vault/refs/safety-tools.md`
  owns the technique).
- No opening ritual on file for this campaign → ask once, not every
  session, whether the DM wants one to kick off Recap — a theme song, a
  signature line.

## Checklist (run before calling the overview or a run-guide done)

Overview (the episode `eNN-overview` page):

- [ ] PREP gates pasted (`ingest(sNN)` hit + `vault/stories/session-NN-*.md` path)
      before any content was written; the story's *Derived pages* line updated.
- [ ] Getting Started answered by the DM before any other section (Hard Rule 2).
- [ ] Situation lookup and player-attention lookup run before selecting
      Situations; every selected Situation states pressure or attention evidence.
- [ ] Every named entity is a resolved wikilink, a specialist hand-off, or a minimal stub.
- [ ] Every quoted fact is wikilinked to its source page.
- [ ] Every Read-first line links its source page plus a distinct "why tonight" line (Hard Rule 8).
- [ ] Headings present: Read first, Tonight, Run guides.
- [ ] `session_shape:` is one of the nine shapes.
- [ ] No whole-file embeds on the overview.
- [ ] `OV1`–`OV18` tags emitted.

Run-guide (each `eNN-run-guide-<slug>` or `<situation-slug>-run-guide` page):

- [ ] Overview exists and OV17 passed, or this run built it first.
- [ ] Headings present: Prep, at least one numbered play H2, Exit. Last Time only on the opening stretch. Side-tracks only when this stretch has one.
- [ ] Numbered H2s transclude spoken siblings and owner headings. Each spoken picture is followed by a check table (`.claude/skills/composing-beats/references/runtime-surface.md` § Check tables).
- [ ] Side-tracks and Exit are `[[wikilink]]` only.
- [ ] Last Time (opening stretch) closes on the prior session recap hook.
- [ ] Each transcluded owner lists this guide in `used_by:`.
- [ ] `RG1`–`RG12` tags emitted.

Both:

- [ ] No `## Player-Known` / `## DM Only` split.
- [ ] No Metabind run buttons or Ran checkboxes on new files.
- [ ] Frontmatter matches the template; `status: draft`/`pending`; `publish: false`.
- [ ] `continuity-checker` `CLEAR` or every `CONFLICT:` converted.
- [ ] `npm run lint -- vault/episodes/NNN/` zero findings before QC.
- [ ] `content-quality-checker` (`session-overview` on the overview, `run-guide` on
      each run-guide) dispatched alone; `PASS`.

## Standard queries — the full grep list

Run these before drafting anything; paste every hit as a `PREP:` marker
line (`vault/refs/runbook-session.md` step 1's own grep list, verbatim):

```bash
# PREP gates — previous session actually ingested, and the session story on the shelf?
git log --oneline | grep ingest
find vault/stories -maxdepth 1 -name "session-<NN>-*.md" 2>/dev/null   # no hit → draft-story writes it first, hard stop

# Loose threads, by grep, not memory
grep -rl "quest_status: active" vault/campaigns/shattered-sea/quests/ 2>/dev/null
grep -rl --include="*.md" "CONTRADICTION" vault/ vault/campaigns/shattered-sea/pcs/ 2>/dev/null

# Last session number, then recent Session Log on pages it touched
find vault/episodes -maxdepth 1 -type d -name '[0-9]*' 2>/dev/null | sort -V | tail -1
grep -rl "touched: s<NN>" vault/ 2>/dev/null   # <NN> = last session number above
# For each hit above, tail its Session Log so PREP: carries actual recent-NPC data:
grep -A3 "^## Session Log" <hit-file> 2>/dev/null | tail -3
```

```bash
# Situation lookup — the session starts from durable active pressure
grep -rl "type: situation" vault/campaigns/shattered-sea/situations/ 2>/dev/null
grep -rnl "lifecycle: seeded\\|lifecycle: discoverable\\|lifecycle: engaged\\|lifecycle: transformed" vault/campaigns/shattered-sea/situations/ 2>/dev/null
grep -rnl "^pressure:\\|^if_ignored:" vault/campaigns/shattered-sea/situations/ 2>/dev/null
```

For each seeded, discoverable, engaged, or newly transformed Situation
candidate, read only its premise, pressure, actors, if-ignored change, and
Session Log. A Situation with no player attention can stay on the brief as
pressure; it earns a table-ready frame only when the table needs to interact
with it this session.

```bash
# Continuity read — the prior session's own recap (recap-writer's output),
# the closing hook this session's Recap box hands into the opening Beat
cat vault/episodes/<last-NN-slug>/sNN-recap.md 2>/dev/null
cat vault/episodes/<last-NN-slug>/ingest-review.md 2>/dev/null
```

**Journey check.** Does the party end tonight somewhere it didn't start?
Compare the party's current location (the continuity read above) against the
location of every thread tonight's guide picks up — a thread whose page sits
elsewhere is a leg. Then read the endpoints of every route page:

```bash
grep -rl "^type: route" vault/campaigns/shattered-sea/locations/ 2>/dev/null
# For each hit, the leg it already covers:
grep -n "^endpoints:" <hit-file> 2>/dev/null
```

One or more legs → chain-load `travel-events` per leg (Hard Rule 17,
Workflow step 6). Party stays put → record the explicit `no leg` token.

```bash
# Active faction pressure for the Secrets & Clues / Living World Detail sections
grep -rl "### Front:" vault/campaigns/shattered-sea/factions/ 2>/dev/null

# Player-attention lookup — evidence from play, not agent interest
grep -rA5 "## Arc Notes (DM Only)" vault/campaigns/shattered-sea/pcs/ 2>/dev/null
grep -rA5 "## Session Log" vault/campaigns/shattered-sea/pcs/ 2>/dev/null
grep -rni "player attention\\|attention\\|asked\\|promised\\|returned\\|investigated" vault/episodes/ vault/campaigns/shattered-sea/pcs/ vault/campaigns/shattered-sea/threads.md 2>/dev/null
```

Treat voluntary investigation, repeated questions, resource commitment,
emotional heat, character promises, return visits, and cross-session references
as player attention. Incidental mentions do not select a Situation by
themselves.

**Stub check** before naming or linking any entity, and the same pair as
wikilink verification before shipping the guide:
`vault/refs/vault/_common/queries.md` — the two commands, why they are never
glued into one, how to read each result, and the escalation before asserting
any entity's absence.

Empty output on the loose-thread queries is informative, not a blocker — an
early campaign has few open quests and no REVIEW backlog yet; go straight to
`vault/campaigns/shattered-sea/pcs/*.md` for PC-driven hooks instead of inventing pressure that isn't
there (`.claude/skills/composing-beats/references/runtime-surface.md` §2: ask, don't invent).

## Pacing — thread selection, rhythm, faction off-screen movement

Read when choosing which threads this session advances, attaching the
spotlight Beat, and ordering hand-offs to the matching frame route.
[[vault/campaigns/shattered-sea/threads|Threads]] come from the
Standard-queries greps and `vault/campaigns/shattered-sea/factions/*.md`
[[vault/refs/vault/faction/references/front|fronts]], never
a hand-maintained list.

Pacing decides which Situations need a Beat and how their registers vary.

**Scope vs. `.claude/skills/composing-beats/references/rhythm-and-pacing.md`**: this
section is the DM-facing operational layer — *which* threads/fronts to run
this specific session and the register-variation rules that keep them
from feeling scattered. `.claude/skills/composing-beats/references/rhythm-and-pacing.md` is the authoring-stage layer —
the session's dramatic arc, plus the pacing tools (ticking clock, breather
scene, dramatic cut, information drip) and the campaign-level arc across
many sessions. Several rhythm principles below recur there in more
worked-example form (cross-referenced inline); neither owns those shared
principles alone.

### Thread Selection

A session advances a handful of threads, judged by feel, not a target
count — too many makes it feel scattered, the right ones make it feel
inevitable. Threads come from the Standard queries: active quests
(`quest_status: active`), live faction fronts (`### Front:` grep), and PC
Arc Notes/Session Log gaps — not from a hand-maintained list, because none
exists in this architecture.

#### Selection Heuristics

**Priority 1 — PC personal arcs that haven't had spotlight in a while.**
Players track this even unspoken. Source: `vault/campaigns/shattered-sea/pcs/*.md` Session
Log — if a PC's entries have gone thin across recent sessions, their arc
is overdue.

**Priority 2 — Faction fronts with off-screen momentum.** If a front has
been advancing off-screen across several sessions (check its clock's
`filled` count against how many sessions have passed), the result should
become visible this session. Pick the front whose actions would be
hardest to ignore given the party's current location.

**Priority 3 — Threads with an explicit timeline.** A front close to its
clock filling, or a quest with a stated deadline, should tick visibly. If
you flagged something urgent, it matters soon or the urgency was fake.

**Priority 4 — Threads with a ready-to-stage location.** If the party is at
the docks and a front can fire at the docks, that's cheaper (in narrative
distance) than one requiring travel. Proximity lowers activation cost.

#### Selection Anti-Patterns

| Anti-Pattern | Problem | Rule |
|---|---|---|
| **Thread Flooding** | Several faction fronts live in one session | Players can track a couple of moving factions, not a handful — trim the rest to a mention. |
| **Arc Neglect** | A PC's personal thread hasn't surfaced in a while | **Mandatory spotlight rotation** — one Beat must connect to their arc. |
| **False Urgency** | A front marked as close to filling, then not shown advancing | **Urgent means soon.** If it can wait indefinitely, it's important, not urgent — different queue. |
| **Geography Sprawl** | Beats require the party in many different places | Sprawl is many *unprepped* hops, not distance itself. Cluster threads in one or two locations, and prep every crossing between them as a travel Beat (`travel-events`) — a prepped leg is a Beat like any other. |
| **Sequel Neglect** | Last session ended on a dramatic beat this guide doesn't address | The opening Beat must acknowledge last session's ending (`.claude/skills/writing-hook-beats/references/hook-beats.md` § Strong starts (session openers) § The Return, or connect the opening thread directly). |

#### When Threads Are Sparse

Not every session has many open threads. Early campaigns and post-arc lulls
need different strategies — resist inventing threads to fill space
(§ Degrade by asking, above); sparse threads mean a focused session, not a thin
one.

| Situation | Strategy |
|---|---|
| **Early campaign** (few or no fronts/quests yet) | Go deeper, not wider. One thread per Beat, fully explored. Use a Discovery or Interrupted Routine opener to seed new threads *through play*. Lean on PC Arc Notes — the richest source this early. |
| **Post-arc lull** (a major front just resolved) | A breathing session. Open with a Return start (consequences of the resolved front). One Beat for fallout, one for a PC personal beat, one to plant the next front's seed — hand off the actual seeding to `.claude/skills/draft-content/references/faction.md` if it's new. |
| **Single-location lockdown** | Filter threads by which can fire *here*. Multiple pressures in one physical space create forced encounters between [[vault/refs/vault/location/references/npcs\|NPCs]] who wouldn't normally interact — a pressure-cooker session. |
| **One dominant thread** | Break it into facets across several Beats, not one: the political angle (social), the physical threat (combat), the hidden truth (revelation). One thread ≠ one Beat. |

### Session Rhythm

A session is a shaped experience, not a list of Beats.
[[vault/refs/stories/register|Register]] variation creates rhythm; monotone
creates fatigue.

#### Register Types

| Register | Energy | Examples |
|---|---|---|
| **Social** | Medium-low | Negotiation, persuasion, faction politics |
| **Exploratory** | Medium | Investigation, puzzle, navigation, discovery |
| **Combat** | High | Fights, chases, physical contests |
| **Revelation** | Variable | Plot twist, backstory reveal, betrayal |
| **Journey** | Medium, rising | A leg's travel events, landmark, toll, arrival changed (`travel-events`) |

#### Rhythm Rules

1. **Never repeat a register back-to-back.** Two combats in a row is
   mechanical fatigue. Two social Beats in a row loses the table. Same
   principle, worked as a tool: `.claude/skills/composing-beats/references/rhythm-and-pacing.md` § The breather scene.
2. **Open high or low, not medium.** A combat or revelation start grabs
   attention; social/exploratory is fine after a heavy prior session that
   needs decompression.
3. **The climax doesn't have to be combat.** A social confrontation or a
   reframing revelation can be the peak — worked examples:
   `.claude/skills/composing-beats/references/rhythm-and-pacing.md` § Climax.
4. **End on an up-note or a cliffhanger, never a plateau.** The last
   Beat either resolves something satisfying or demands continuation —
   worked examples: `.claude/skills/composing-beats/references/rhythm-and-pacing.md` § Cliffhanger / hook.
5. **The optional Beat should be the most fun one.** If it's too painful
   to skip, it isn't actually optional — redesign so something else is.

#### Pacing Failure Modes

| Failure | Symptom | Fix |
|---|---|---|
| **Escalation Fatigue** | Several high-tension Beats in a row | Insert a low-energy breather: a short social Beat, a comedic NPC. |
| **The Slow Middle** | Strong open, then exploration Beats drain momentum | Front-load one hybrid Beat after the opener; save pure exploration for the back half (same sag, one altitude up — the campaign-spanning version: `.claude/skills/composing-beats/references/rhythm-and-pacing.md` § Avoiding the mid-campaign sag). |
| **Combat Slog** | One fight eats the table's whole runway | A fight that will run long consumes more of the night than a single Beat normally would — plan fewer others around it. |
| **Revelation Overload** | More than one major reveal in one session | Save the second for next time — two competing reveals dilute each other. |
| **The Orphan Ending** | Session runs out of time mid-Beat | Plan slightly more Beats than the night calls for, one marked optional; cut the optional one if time is short — don't start a Beat you can't finish. |

### Faction off-screen movement — pending pressure, not a canon write

Factions don't pause while the party is busy. A session can *show* a front
visibly advancing — but this section only frames that as pending pressure
for the DM to narrate; the actual clock tick is `world-update`'s job,
post-INGEST, reading canon pages, never this prep document.

#### How to write it

1. Read the front's `off_screen_action` and `primary_goal` fields from its
   faction page (`.claude/skills/draft-content/references/faction.md`'s Faction fields table).
2. Frame one logical step toward the goal as something the party can
   observe this session.
3. Make the evidence **observable but not explained** — the party sees the
   effect, not the mechanic.

**Good:** *"Two new faces are counting crates at the east pier this
week."* (Observable effect; the mechanism — falsified weigh-slips — stays
DM-only until surfaced by play.)

**Bad:** *"The Concordat continues its plan to falsify the quarterly
audit."* (Narrator voice explaining faction mechanics; unplayable.)

#### Rules

- **A front at a time.** Showing more than one or two overwhelms tracking
  capacity.
- **Advance the front the party is NOT currently engaging.** The one
  they're interacting with advances through play; the others move
  off-screen.
- **Make evidence specific and physical.** Not "tensions are rising" but
  "three more soldiers arrived on the morning ferry."
- **Connect to a Beat when possible.** An NPC might mention the
  off-screen change — cheaper than a dedicated Beat, and it makes the
  world feel interconnected.
- **Never fire a front's consequence-at-fill in this document.** If a
  front is close to filling, flag it under Living World Detail or Secrets
  & Clues and hand off to `world-update` — this section shows pressure, it
  doesn't resolve it.

## Recap → opener coupling

Read when filling the **Recap** section. The prior
session's `vault/episodes/NNN/sNN-recap.md` (`recap-writer`'s output) is this section's sole
source — read its `## Recap` closing line before writing anything here.

### Filling the Last Time box

3–6 sentences, observer/narrator language ("last time," third person —
"the party did X," "Delmar did Y") — never second-person immersive
address; that voice belongs to the opening Beat's own opener, not this
box. Draft from `vault/episodes/NNN/sNN-recap.md` plus the ledger/Session
Log grep hits, only past events relevant to *this* session. Close this
box on a line that quotes or almost-verbatim restates
`vault/episodes/NNN/sNN-recap.md`'s own closing hook — the two are one
continuous handoff, not two separate endings.

### Handing off to the opening Beat

The box's final sentence and the opening Beat's opener read as one
continuous open: no re-explaining the cut, no separate briefing between
them. This run-guide writes the Recap box; `writing-hook-beats` writes the
opening Beat's opener
(`.claude/skills/writing-hook-beats/references/hook-beats.md` § Strong starts (session openers)) —
hand off the closing hook explicitly when delegating the opening Beat,
don't let the two drift independently.

### No prior recap on file

No prior `vault/episodes/NNN/sNN-recap.md` on file (session 1, or a legacy-sourced gap) →
ask the DM for the last-time beats directly rather than inventing a recap
from memory.

## Reference files

| File | Read when |
|---|---|
| `vault/_templates/_episodes/_session_run_guide.md` | Instantiating — headings and usage |
| `.claude/skills/composing-beats/references/runtime-surface.md` § Session shapes | Reading the overview's `session_shape:` |
| § Overview pass, above | No overview yet, or RG1 fails |
| `.claude/skills/composing-beats/references/runtime-surface.md` § Check tables | Writing a numbered play H2 |
| `.claude/skills/writing-narrative-islands/SKILL.md` | Every invocation |
