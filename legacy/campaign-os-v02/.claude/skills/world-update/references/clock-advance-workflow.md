# Clock Advance Workflow

The full ritual behind `.claude/skills/world-update/SKILL.md`'s workflow summary. Follow in order. This file
assumes you've already read `.claude/skills/world-update/SKILL.md` (the Gate, the Front template, the ledger
mechanics) — it doesn't repeat those.

A Front's owning page is a faction page or a major/recurring NPC page — every step
below applies identically to either; where the text says "faction" it means "the
Front's owning entity," faction or NPC.

Creative-domain rider applies throughout: facts (what's canon), citations, and the
ledger mechanism are bound rails; how you narrate what a faction *does* inside those
rails is free — a bold, specific proposal beats a timid, generic one every time. The
"Shallow reading" section below is this skill's version of that rule with teeth.

---

## Canon discipline

Every claim traces to something you actually read this turn, cited by file and line.
Not inferred, not remembered from an earlier turn, not extrapolated from vibes.

**Failure modes to avoid:**

- **Timing errors** — a `dormant` Front's clock hasn't started. Check `**Lifecycle:**`
  before assuming a clock is running.
- **DM chat leaking into world state** — an idea floated in conversation isn't fact
  until an `ingest(sNN)` commit or a checked ledger line says so (Hard Rule 4).
- **Invented consequences** — don't narrate a consequence the Front's own
  `**Consequence at fill:**` doesn't say, and never execute it before a fill.
- **Assumed destinations** — never state or imply where the party goes next; that's
  `draft-run-guide`'s job at PREP time, not this skill's.

---

## Cross-day idempotency

Ledger mechanics' "re-read and append" rule only guards a *same-date* rerun; it says
nothing about a rerun on a *later* day between the same two `ingest` commits, where
an earlier day's world-turn file was written but never applied — canon pages don't
show its advances yet, so a fresh triage would double-propose them. Run the
`.claude/skills/world-update/SKILL.md` Gate's cross-day idempotency check before every triage to catch this.

---

## Step 1: Triage every active Front

Run the standard queries, collect every `**Lifecycle:** active` Front (skip `dormant`
unless this turn's evidence shows its trigger firing; skip `resolved` entirely).
Classify each into one tier.

**Fast pre-filter, optional:** `grep -rl "has_active_front: true" vault/campaigns/shattered-sea/factions/ vault/campaigns/shattered-sea/npcs/
2>/dev/null` narrows the standard queries' `-A20` paste to only pages that
already claim an active Front — a page missing the flag but carrying a real
`**Lifecycle:** active` Front (flag drifted stale) still needs the full
standard queries to catch, so treat this as a shortcut, never a replacement.

### HOT — engaged this session
The session recap or a checked ledger line names this Front's faction, or an entity
its Front's prose wikilinks, directly. The party's action changes what the faction
does next.

### WARM — party aware, not engaged this session
The faction/Front has prior plain `sNN` session citations or Session Log entries —
the party knows it exists — but this session's recap doesn't mention it.

### COLD — brewing, unopposed
Neither of the above, but the Front is `active` (has real momentum: a trigger already
firing, a clock already partway filled). A `dormant` Front whose trigger hasn't fired
isn't COLD — it's not running yet; leave it alone.

### Present for confirmation

```
**HOT Fronts (engaged this session):**
1. [Faction — Front name] — [what the party did]

**WARM Fronts (party aware, not engaged):**
1. [Faction — Front name] — [faction's likely move]

**COLD Fronts (brewing):**
1. [Faction — Front name] — [what's advancing unopposed]

Anything to add, remove, or reclassify?
```

**Usually skip** (mined from the legacy faction-simulation eligibility filter,
still the right call here): factions the party has never encountered, background lore
with no current pressure, and `dormant` Fronts whose named trigger hasn't fired. These
aren't COLD — COLD still requires real momentum (§ COLD above); a Front with no
momentum yet isn't eligible for a turn at all.

Wait for DM confirmation before rolling anything.

---

## Step 2: Process each Front

Work HOT, then WARM, then COLD. One Front at a time; finish 2a–2f before starting the
next.

### 2a. Deep read (mandatory before any proposal)

Triage used the `-A20` grep paste. That's not enough to propose an advance. For this
Front:

1. Read the faction page **in full** — not just the Front block: `**Off-screen move if
   unopposed:**`, `## DM Only`, and any other Front on the same page can all bear on
   this one.
2. Follow every wikilink the Front's prose names (`**Quest link:**`, any `[[...]]` in
   `**Trigger conditions:**` or `**Consequence at fill:**`) to the linked page. Read
   its current state.
3. If this is HOT tier, read the session recap section that names this faction, and
   the checked ledger lines it cites.
4. **Once per run** (cache it — don't re-query per Front): find the story's current
   direction.
   ```
   grep -rl --include="*.md" "season_status: active" vault/campaigns/shattered-sea/seasons/ 2>/dev/null
   ```
   A hit → read that season page's Throughline (`## Overview`) and `## Fronts on
   Stage` in full. No hit (no active season yet) →
   ```
   grep -n "." vault/campaigns/shattered-sea/campaign-overview.md
   ```
   and read `### Ongoing Campaign: The Premise` and `### Ongoing Campaign: The
   Truths` as the fallback anchor (Hard Rule 8). Either way, this is what "where the
   season/campaign is headed" means concretely — not a vibe, a cited section.

Then produce a **Context Brief**:

```
**Context Brief — [Faction] — [Front name]**
- **Standing goal/method:** [from `**Primary goal:**` / `**Consistent method:**`,
  quoted or closely paraphrased — not invented]
- **Current position:** [filled count, any linked quest/NPC state, from the page]
- **This turn:** [what specifically changed for this Front — from recap/ledger
  cross-referenced with the page, or "nothing party-driven" for COLD]
- **Off-screen move if unopposed says:** [quote the field]
- **Key detail the -A20 triage paste omitted:** [something from the full page or a
  linked entity that only the deep read surfaced]
- **Converges toward:** [the season Throughline/Front-on-Stage entry, or campaign
  Truth, this advance serves — or "diverges from <X> — flagging" if it visibly pulls
  away; never blank]
```

**Red flags you haven't read deeply enough:** the brief only restates the triage
paste; you can't name the Front's specific goal (not "advance their agenda" — the
actual goal); you followed no wikilinks; the "key detail" is vague or restates
`**Off-screen move if unopposed:**` verbatim with nothing added.

### 2b. Propose

One clear sentence, grounded in the Context Brief, framed by tier:

- **HOT:** "In response to [specific party action from recap], [faction] attempts to
  [concrete action grounded in the Front's goal/method and current position]."
- **WARM:** "While the party is elsewhere, [faction] pursues [the next concrete step
  implied by `**Off-screen move if unopposed:**` and the Context Brief]."
- **COLD:** "Unopposed, [faction] advances [a concrete plan detail from the page, not
  generic 'their agenda']."

**Test:** could someone who only saw the `-A20` triage paste have written this exact
proposal? If yes, the deep read didn't do any work — rewrite it. (See § Shallow
reading below for worked failure/fix pairs.)

### 2c. Roll

```
.claude/skills/roll-dice/roll.sh d20
```

If that script doesn't exist, ask the DM to roll physically and report the number —
never invent a die result; that's roll-dice's own load-bearing rule and it applies
here without exception.

The result is canon. No re-rolling, no softening, no "that doesn't fit."

### 2d. Interpret

| Roll | Outcome |
|---|---|
| 1–5 | **Setback.** The attempt failed or backfired — exposed, wasted, opposition stiffened, an unexpected complication. |
| 6–15 | **Partial.** Real progress with friction — something worked, something didn't; a cost or complication rides along. |
| 16–20 | **Full success.** They got what they were after. The world shifts. |

Tier flavors the interpretation:

- **HOT:** a setback means the faction's response to the party was weak or
  misdirected (the party's action landed harder than expected); a success means the
  faction hits back hard — new pressure the party will feel next session.
- **WARM:** a setback means internal resistance or outside interference while the
  party was elsewhere; a success means they advanced clean — the party returns to
  changed ground.
- **COLD:** a setback means the plan stalled on its own friction (infighting,
  shortage, bad luck); a success means the villain advanced significantly — the hook
  strengthens (§ Cold escalation).

Hard Rule 6: every result changes something. A setback that produces no observable
state change means the proposal (2b) wasn't specific enough — rewrite the proposal,
not the interpretation.

### 2e. Present and collaborate (mandatory, every Front — Hard Rule 7)

Before writing anything, share with the DM: the Context Brief's **Converges toward**
line, the proposal (2b), the roll (2c), and the interpretation (2d) — as the draft
`FACT`/`APPEAR` lines you'd write. Then ask, concretely, not rhetorically: *does this
match how you see the Front moving, or do you want to reinterpret, redirect, or add a
wrinkle?* This is a real discussion per Front, not a rubber stamp shown after the
fact — the DM's read on their own world outranks the roll's mechanical interpretation
whenever the two conflict. Revise the lines to match what the DM lands on before
moving to 2f. Skipping this because the interpretation "obviously" reads one way is
exactly the shortcut Hard Rule 7 exists to close.

### 2f. Check for a fill, then write

Would this result bring `**Clock:** N — filled: X` to `X == N`? → **stop** (Hard Rule
3, stricter than 2e's checkpoint): present the quoted `**Consequence at fill:**` line
and wait for the DM. Only after they confirm do you write the `FACT` line flipping
`**Lifecycle:**` to `resolved` and narrating the consequence; if they say hold, write
the partial advance only (`filled: N-1`) and note in the `APPEAR` log line that the
Front is primed but held.

Otherwise, write the two ledger lines (`FACT` + `APPEAR`, per `.claude/skills/world-update/SKILL.md` § Ledger
mechanics) to the world-turn ledger now, before moving to the next Front — don't batch
writes to the end.

**COLD Fronts** also fold a hook-strength note into the `APPEAR` line's description
(§ Cold escalation).

---

## Collisions

Two Fronts acting against each other in the same window (rival factions, or one
Front's move directly opposing another's):

1. Roll once for the collision, not once per Front.
2. High roll favors whichever side comes out ahead on the Context Briefs — weigh
   resources/leverage, proximity, knowledge, timing, and temperament (which side is
   patient vs. desperate); factor in player interference if either side is aware of
   party action. Ask the DM if it's still not obvious which side that is.
3. Low roll favors the weaker or more desperate side (upsets are allowed and
   interesting).
4. Run 2e (present and collaborate) once for the collision, covering both Fronts
   together, before writing either.
5. Write the result to both Fronts' `FACT`/`APPEAR` line pairs — one collision, two
   sets of ledger lines, never double-rolled.

---

## Cold escalation

Track a COLD Front's accumulated advances by counting its `## Session Log` entries
that mention this Front's name since it went COLD. As they accumulate, the hook
strength named in the `APPEAR` description escalates:

| Advances | Hook strength | What changes |
|---|---|---|
| 0–1 | **Whisper** | Only visible if someone's looking — a rumor at a tavern the party hasn't visited. |
| 2–3 | **Ripple** | Noticeable to an attentive party — an NPC mentions something, a price shifts. |
| 4–5 | **Wave** | Hard to miss — faction agents appear near the party, a resource they rely on is affected. Reclassify the Front WARM next triage. |
| 6+ | **Collision** | Forces engagement — the Front directly touches something the party cares about. Reclassify the Front HOT next triage. |

This is the mechanical version of "villains continue their plans and those plans
eventually reach the party" — not because anyone steered them there, but because the
world is small enough that power moves make waves.

---

## Shallow reading — how this skill fails

The single most common failure: proposing a Front's advance from the `-A20` triage
paste instead of the full deep read. Every such proposal sounds generic — "the
Concordat advances their agenda," "the smugglers send more ships" — and tells the DM
nothing they didn't already know from the page they wrote.

| Shallow (triage-paste-only) | Grounded (deep-read) |
|---|---|
| "The Concordat continues covering the skim." | "The Concordat reassigns the two clerks its `**Off-screen move if unopposed:**` names to falsify last quarter's weigh-slips — but the linked `fixture-salt-writs` quest page's `## Beats` already has the party holding a torn slip fragment, so the falsification has a hole in it the party is positioned to find." |
| "The rival faction sends agents after the party." | "[[fixture-second-courier]], the NPC the Front's DM Only section names as running the actual route, switches to a longer route through the marsh after the party's disruption — slower, but avoids the checkpoint the party staked out; the Context Brief's linked location page notes the marsh route floods at high tide, a complication neither the party nor the Concordat has accounted for yet." |

The left column is what the triage paste alone can produce. The right column needed
the full page, the linked NPC, and the linked location — that's the deep read doing
real work. If a draft proposal reads like the left column, return to 2a.

---

## Quality checklist (run before presenting the ledger)

- [ ] Every processed Front had a Context Brief with at least one detail the `-A20`
      triage paste didn't contain.
- [ ] Every Context Brief named a **Converges toward** line (season Throughline/
      Front-on-Stage, or campaign Truth) — not left blank (Hard Rule 8).
- [ ] Every proposal cites specific facts from the full faction page or a linked
      entity, not generic faction behavior.
- [ ] Every Front's roll and interpretation were presented to the DM (2e) and
      revised to their read before any ledger line was written (Hard Rule 7).
- [ ] Every Front had a `d20` roll via `roll.sh` (or an explicit DM-supplied roll,
      pasted) — never an invented number.
- [ ] Every state claim traces to a `status: canon` page, `vault/episodes/NNN/sNN-recap.md`, or a checked
      `vault/episodes/NNN/state-changes.md` line — never assumed or remembered from an earlier turn.
- [ ] No `**Clock:**`/`**Lifecycle:**` line was flipped to a fill's consequence
      without a pasted DM confirmation (Hard Rule 3).
- [ ] No new Front, faction, or NPC was authored inline (Hard Rule 5) — gaps were
      flagged and handed to `.claude/skills/draft-content/references/faction.md` instead.
- [ ] Every advance wrote both a `FACT` line (Clock/Lifecycle) and an `APPEAR` line
      (the dated log entry) — not one without the other.
- [ ] Every citation is a real `grep -n` hit, pasted, not a guessed line number.
- [ ] Collisions (if any) were resolved once, not double-rolled.
- [ ] COLD Fronts' hook strength was computed from a real Session Log count, not
      guessed.

---

## Worked example (fixture — placeholder names, not real campaign content)

**Setup.** Gate check: `git log --oneline -E --grep '^ingest\(s[0-9]+\)' | head -1`
→ `ingest(s97): the salt road`. Session directory: `vault/episodes/NNN/`.

Standard queries:
```
$ grep -rl --include="*.md" "^### Front:" vault/campaigns/shattered-sea/factions/
vault/campaigns/shattered-sea/factions/tideglass-concordat.md
$ grep -rA20 --include="*.md" "^### Front:" vault/campaigns/shattered-sea/factions/
vault/campaigns/shattered-sea/factions/tideglass-concordat.md:### Front: The Skim Before the Audit
vault/campaigns/shattered-sea/factions/tideglass-concordat.md-**Lifecycle:** active
...
vault/campaigns/shattered-sea/factions/tideglass-concordat.md-**Clock:** 6 segments — filled: 3
vault/campaigns/shattered-sea/factions/tideglass-concordat.md-**Consequence at fill:** The Crown auditor
  signs off clean; the skim becomes permanent policy.
```

Recap check: `grep -n "." vault/episodes/097/s97-recap.md` shows the party
confronted a harbor quartermaster and exposed the salt-tithe fraud publicly this
session. The Concordat isn't named in the recap directly, but the quartermaster is
the NPC the Front's DM Only section names as the Concordat's inside contact — so this
Front triages **HOT**, not COLD, once that link is followed (this is exactly the kind
of connection triage-paste-only reading misses).

Triage presented, DM confirms.

**2a. Deep read.** Full faction page read: `**Off-screen move if unopposed:**`
("reassigns two clerks to falsify weigh-slips"); `## DM Only` names the harbor
quartermaster as the inside contact. `grep -ril "quartermaster" vault/` finds his NPC
page, `status: canon`, now showing (from this session's ingest) that he confessed.
Season query: `grep -rl "season_status: active" vault/campaigns/shattered-sea/seasons/`
hits a fixture season page (season-02); its Throughline reads "can the Concordat's
skim survive the Crown auditor's arrival, or does the harbor's own corruption sink it
first?" Context Brief:

```
**Context Brief — Tideglass Concordat — The Skim Before the Audit**
- **Standing goal/method:** Close the ledger gap before the Crown auditor arrives;
  pays debts early and loudly, never negotiates the tithe rate in public.
- **Current position:** filled 3/6; inside contact was the harbor quartermaster.
- **This turn:** the quartermaster confessed publicly and the harbor is buzzing
  (recap L9-14; his NPC page now status: canon, confession cited to s97).
- **Off-screen move if unopposed says:** reassign two clerks to falsify slips.
- **Key detail the triage paste omitted:** the quartermaster *was* the Front's
  inside contact — his exposure isn't background noise, it's the Front's own
  mechanism getting cut off.
- **Converges toward:** season-02's Throughline directly — the confession is the
  harbor's corruption starting to sink the skim on its own, ahead of the auditor.
```

**2b. Propose (HOT).** "In response to the quartermaster's public confession, the
Concordat scrambles to cut him loose as a liability and accelerate the clerks'
slip-falsification before the auditor hears the rumor too."

**2c. Roll.** `.claude/skills/roll-dice/roll.sh d20` → 4.

**2d. Interpret.** 1–5, Setback, HOT tier: the party's action landed harder than
expected — the falsification attempt is rushed and sloppy.

**2e. Present and collaborate.** Shared the Context Brief, proposal, roll, and
interpretation with the DM. DM agrees the falsification should be sloppy, but wants
the sloppiness to leave a *specific* physical clue (a torn weigh-slip fragment) rather
than a generic "inconsistency," since the party is already tracking paper evidence
this arc — revise the draft lines to name that fragment before writing.

**2f. Fill check.** Would filled 3→4 hit the 6-segment cap? No — write the lines.

```
- [ ] FACT vault/campaigns/shattered-sea/factions/tideglass-concordat.md :: Front "The Skim Before the Audit" Clock filled 3 -> 4 (of 6), setback — rushed slip-falsification after the quartermaster's public confession leaves a torn weigh-slip fragment behind (vault/campaigns/shattered-sea/factions/tideglass-concordat.md L36)
- [ ] APPEAR vault/campaigns/shattered-sea/factions/tideglass-concordat.md :: s97 — Skim Before the Audit front: setback, rushed falsification after losing its inside contact leaves a torn slip fragment; urgency high, hook strength Ripple (vault/campaigns/shattered-sea/factions/tideglass-concordat.md L36)
```

(Both lines correctly cite the faction page's real `**Clock:**` line — `grep -n
"Clock:" vault/campaigns/shattered-sea/factions/tideglass-concordat.md` — not a transcript line, since the
evidence for *why* this is a setback is the recap and the NPC page, but the thing
being changed and its citation anchor is the Front itself.)

**Failure case, same Front.** A tempting shortcut: skip 2a and write "The Concordat
continues covering the skim" straight from the triage paste. This fails the
checklist's first item outright (no Context Brief detail beyond the paste) and misses
that the quartermaster's exposure is a HOT-tier event, not backdrop — the shortcut
would have filed this as COLD and produced a Whisper-strength, generically-worded
line the DM already knew. The deep read is what turns "the faction does something"
into "the faction loses its inside man and panics" — the second is worth the DM's
attention, the first isn't.

**Second failure case, same Front.** A different shortcut: run 2a–2d correctly, then
write the FACT/APPEAR lines straight from 2d's interpretation, skipping 2e. This
misses the DM's torn-slip-fragment call entirely — the line that shipped would name a
generic "inconsistency" instead of the specific clue the DM wanted seeded, and the
DM would only discover the mismatch reading the ledger after the fact. Hard Rule 7
exists because the interpretation step (2d) is mechanical (the roll is canon) but
*how it manifests in the world* is not — that's the DM's call, made in 2e, every
time.
