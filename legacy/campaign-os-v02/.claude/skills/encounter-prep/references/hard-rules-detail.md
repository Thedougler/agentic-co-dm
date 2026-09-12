# Hard rules — full detail

Rule numbers match the core `## Hard rules` list in
`.claude/skills/encounter-prep/SKILL.md`.

## Shared hard rules (cited, not restated)

Every rule below adds only the encounter-specific detail the shared text
doesn't carry. The underlying rules themselves are bound once, by name, in
`vault/refs/vault/_common/hard-rules.md`: **The Stub Check** (about to
create anything — Standard queries above cover this skill's own stub-check
grep shapes); **The PC-Connection Requirement** (Rule 1 below names only
the field it lands in); **The Toy Field Discipline** (Rule 2 below names
only this skill's field mapping); **The Player Character Boundary** (never
write what a PC decides, feels, thinks, or wants; opposition goals predate
the party and advance on their own timeline; frame consequences as
pressures, never `if players do X then Y` chains more than one step deep —
full doctrine `.claude/skills/composing-beats/references/audits.md` §1); **The Status Gate**
(never flip `status:` to `canon` or touch `publish:` — those are
`transcript-ingest`'s and PUBLISH's exclusive moves); **[[degrade|Degrade By Asking]]**
(Rule 9 below points at this skill's own trigger list); **Reuse Before
Inventing** (Rule 5 below names only this skill's reskin pointer); and
**Calibrate Against The Real Party** (Rule 4 below names only this skill's
own procedure).

1. **The PC-Connection Requirement lands in the Toy table's
   `link_of_relevance` row** — not just working notes, so a later session
   can grep for it (`.claude/skills/composing-beats/references/runtime-surface.md` §2).
2. **Toy field mapping.** `primary_goal`: what this encounter *proves*,
   thematically, not a tactical description. `consistent_method`: the
   opposition's behavior/tactics, doable at the table, not personality
   analysis. `active_problem`: the situation already in motion before the
   party arrives, not enemy intent (`.claude/skills/composing-beats/references/runtime-surface.md` §3).
3. **No named foe or reusable creature gets its own page's content authored
   here unless it's a genuine one-off.** A named antagonist who may recur
   is the npc guide's page; a generic creature meant to recur across
   encounters is `.claude/skills/draft-content/references/monster.md`'s page — hand off to the right one, then
   quote (§ Wiki placement). Inventing a villain's Toy Chest, Three Villain
   Questions, or a creature's ecology inline here duplicates a sibling
   skill's owned content.
4. **Run `combat-calibration.md`'s procedure before finalizing enemy count
   or difficulty** — read the party's actual stats and Session Log
   (Standard queries) first (`.claude/skills/composing-beats/references/runtime-surface.md` §5).
5. **Reskin bias and its worked example** live in
   `vault/refs/vault/monster/references/statblock-format.md` § Recall vs. write from
   scratch — cite it, don't re-derive. Only build a full custom stat block,
   per `vault/refs/vault/monster/references/cr-design.md`'s method, when
   the mechanical concept genuinely has no print analog.
6. **Cap distinct creature types at three per encounter.** More than
   three types in one fight is hard to run at the table
   (`.claude/skills/encounter-prep/references/encounter-composition.md` § Creature-type cap). A bigger
   set-piece uses waves of the same 2–3 types, not a fourth type added on
   top.
7. **Every encounter has an *if ignored* consequence**, or it's a resolved
   set-piece, not a sandbox situation (`.claude/skills/composing-beats/references/audits.md` §4, the
   tick test). A vague "tensions rise" fails the tick test — name the
   observable change.
8. **Multi-faction encounters discount the CR budget ~25%** when two or
   more enemy groups are present but not coordinated against the party
   (they're also fighting each other) — full budget only if both groups
   coordinate against the party.
9. **Full trigger list for degrading by asking (this skill's own cases)**:
   `.claude/skills/encounter-prep/references/degrade-by-asking.md`.
10. **Check-and-numbers discipline is pinned.** A resolvable check anywhere
    on this page exists only as a `[!check]` callout carrying full anatomy
    (ability/skill, DC, labeled `**Success:**`/`**Failure:**` tiers per the
    `callouts` skill's `.claude/skills/callouts/references/check.md`) or as a genuine DC-menu table
    where every row carries that same anatomy. An attack roll is never
    framed as a DC — state it as an attack vs AC (5e SRD). Every resolved
    loop (gp, XP, HP, duration, count) states its number; no vague
    threshold ("a strong showing", "enough misses"). W70 enforces bare DCs
    outside `[!check]`.
11. **The encounter page owns the fight's operative numbers.** Per
    `vault/refs/runbook-wiki.md` § Operative-mechanics ownership, a sibling
    `vault/episodes/NNN/` scene file for the same fight never restates or omits
    the per-round numbers (DCs, HP thresholds, phase triggers) — it
    transcludes this page's operative blocks with `![[page#Heading]]`. The
    encounter page and the scene file cross-link both directions and each
    states its side of the ownership.
12. **Every combat encounter ships a Run Sheet.** One section the DM runs
    the whole fight from: a foe roster tracker (init, AC, HP, flee
    threshold, one-line action script per foe/group), a round script
    (bold-led R1/R2+/trigger bullets), and statblocks reached by wikilink
    or transclusion at point of use — never restated (W62 stays
    satisfied).
13. **Every reachable ending gets written text.** Whenever this page states
    odds for a win/defeat/disengage branch, `## Endings` writes what
    actually happens for each — a phase win condition, the defeat/TPK
    aftermath, the disengage/flee outcome. Plot-defense phrasing ("don't
    let a PC...", "the party can't...") is banned unless immediately
    followed by a let-it-happen fallback stating the actual consequence.
14. **A gating beat ships its hint ladder.** Any encounter that gates
    progress on an objective or puzzle solve carries `## If They're Stuck`:
    three rungs — a free environmental tell, a costed nudge, and a
    fiction-costed bail-out. Skip the section entirely for a straight
    fight with no such gate; never leave a gate with no ladder.
15. **The unit skeleton is required, start to finish.** Opening states a
    one-line Dramatic Question — the question this encounter exists to
    answer, with the standing rule that once play answers it the page
    moves straight to `## Transition`. The page always closes with a
    `## Transition` block: condition → explicit goto wikilink with elapsed
    in-fiction time, every written branch skip on its own line.
