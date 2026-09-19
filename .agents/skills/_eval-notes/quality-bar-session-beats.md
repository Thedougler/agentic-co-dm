# Quality bar — session-beats family

Destination path (when landed): `.agents/skills/_eval-notes/quality-bar-session-beats.md`

Repo read: `/home/box/agentic-co-dm` @ `main`, citing commits:

- **`6b7fcfa`** — *Expand typed beat skill evals and sharpen adversarial gates* (hook / development / cliffhanger / climax / resolution eval suites expanded; refuse language added to development / cliffhanger / resolution SKILL.md).
- **`d4e03b9`** — *Sharpen adversarial gates from batch 4 eval failures* (cliffhanger consecutive-refuse; climax non-combat acceptance; resolution refuse ungrounded existential threats).

This note is the eval-author bar for **composition and typed beat skills**. New or uplifted suites should match this depth, not the thinner craft-only suites that preceded Batch A/B/C.

---

## Bar skills and eval counts

| Skill | Eval count (bar) | Role |
|---|---:|---|
| `session-beats` | **13** | Composition: Beat Chart, polarity, threads, escalation, recompute, agency |
| `hook-beats` | **10** | Typed fill — strong start |
| `development-beats` | **10** | Typed fill — decision-space bump |
| `cliffhanger-beats` | **10** | Typed fill — physical contest |
| `climax-beats` | **9** | Typed fill — earned convergence |
| `resolution-beats` | **9** | Typed fill — afterscene / arc echo |

**Target for new / uplifted suites: ~9–13 evals.** Below ~8 is thin unless the skill is a tiny ops helper with a hard process surface. Above ~14 usually means duplicate prompts — prefer sharper adversarial coverage over volume.

Bar suites mix:

1. **Positive craft** — improve / fill a beat correctly (often one wiki-grounded “happy path”).
2. **Hostile principle-violation** — prompts that ask the skill to break its own gates; success is refuse / redesign / offer alternatives.

---

## Assertion style

### Bar skills today (`expectations[]` strings)

Session-beats family still uses the older shape:

```json
"expectations": [
  "Does not place two Cliffhangers consecutively without a genuine Development.",
  "..."
]
```

Strings are readable but untyped: graders must infer whether a miss is content, structure, process, guardrail, or quality.

### Batch A/B/C (`assertions[{text,type}]`)

City / region / lore / npc / place, item / spell / vehicle, and wiki-ops use:

```json
"assertions": [
  { "text": "Does not present an invented plague… as established wiki fact", "type": "guardrail" },
  { "text": "Surfaces existing Mercatura facts…", "type": "content" },
  { "text": "Shows a chat proposal / work gate before writing under wiki/", "type": "process" },
  { "text": "Output follows wiki/templates/….md structure", "type": "structure" },
  { "text": "Narration… without secrets, DCs, or unearned names", "type": "quality" }
]
```

Allowed types: **`content` | `structure` | `process` | `guardrail` | `quality`**.

### Recommendation

- **Keep typed `assertions[{text,type}]` for all new and uplift work** (cold-opens, writing-beats, ABC patches). Better for grading digests and MISS triage.
- **Depth pattern comes from bar prompts**, not from the assertion schema. Copy the *adversarial intent* of session-beats evals 1–13 (and siblings), then express pass criteria as typed assertions.
- Do not invent live wiki lore in fixture-free prompts; use labeled fixtures, generic table situations, or “established fiction” placeholders the skill already knows how to refuse.

---

## Adversarial / principle-violation catalog

Catalog distilled from `session-beats` + typed siblings. Use these shapes when authoring hostile prompts.

### Chart / composition (`session-beats`)

| Pattern | Example prompt intent | Success looks like |
|---|---|---|
| **Forced chart / linear rail** | “Run every scene in order no matter what” | Situations + triggers + recompute; no guaranteed fire order |
| **Linear combat rail** | Ambush → monster → chase → bridge, exact order | Refuse consecutive Cliffhangers; insert Development; keep off-ramps |
| **Mandatory final battle** | Peace negotiated; still demand boss fight Climax | Negotiated / exposed outcome *is* the Climax |
| **Negate player agency** | Abandon quest → postpone village goal until after finale | Promote player-created goal; retire obsolete beats |
| **Combat-only session** | Six consecutive combats, no social/investigate/travel/recovery | Alternate; escalation without fight stacking |
| **Secret betrayal without clues** | Ally steals key between scenes; no detection chance | Motive + tells + fair detection before irreversible |
| **Rewind failure** | Fail chase → quiet rewind to checkpoint | Failure is real state; recompute; different route/Climax OK |
| **Climax without foreshadow** | Dragon / volcano / cursed crown never planted | Harvest middle threads; plant first or restructure |
| **Detail-only Development** | “Just add how large the army is” | Decision-space bump, not elaboration |
| **Inflated Resolution** | Personal Climax → two-hour Resolution with combats/NPCs/prophecy | Scope match; brief afterscene |
| **Fiat Contest** | Scout loses regardless of rolls | Transparent procedure; rolls matter |
| **Clue-less trap / one lever** | No investigation; one correct lever or session stops | Discoverable clues; multiple solutions / costly bypass |
| **Costless Second Chance** | Death → revive unharmed, no lasting effect | Rare, costly, fiction-based; preserve sacrifice |

### Hook (`hook-beats`)

- Two active Hooks / alternate Hooks → **one Hook per session**
- Extended recap before pressure → **pressure first, one spoken delivery**
- Action Hook → Cliffhanger (wrong polarity) / cerebral Hook → Development → **enforce polarity handoff**
- Author PC actions / internal monologue → **present pressure; wait for commitment**
- Fresh-start teleport ignoring prior session / PC goals → **connect to ending or live goal**
- Hook absorbs politics / multi-NPC / Climax setup → **sole job: start action + commitment**
- Single mandatory path (“only way adventure works”) → **≥2 viable responses + ignore/fail/redirect costs**
- Invent spectacle over established resume point → **resume actual ending state**

### Development (`development-beats`)

- Detail-only / no bump → **reframe decision space**
- Full mystery resolve in one beat → **one facet; leave Cliffhanger something to test** (SKILL refuse)
- Three Developments, no Cliffhangers → **break chain with Cliffhangers**
- Threadless world-building / abandoned-thread railroad → **connect or reject as filler/railroad**
- Combat inside Development → **hand physical contest to Cliffhanger**
- Author PC decisions → **reveal; hand back choice**
- Single interpretation / forced path → **≥2 responses**
- Invent ungrounded lore pantheon → **wiki ground or stub; serve live thread**

### Cliffhanger (`cliffhanger-beats`)

- Predetermined outcome (“villain escapes no matter what”) → **contest stays in doubt**
- Random encounter, tests nothing learned → **test a Development-revealed thread**
- Consecutive Cliffhangers / ride momentum into another C → **refuse; Development handoff** (SKILL refuse)
- No retreat / fight-to-death only → **≥2 responses + off-ramp unless fiction forbids**
- Max stakes immediately after Hook → **scale early; save strongest for Climax**
- Quiet failure → success → **failure changes physical situation**
- Session-spanning multi-phase siege as Cliffhanger → **keep short; Climax owns extended**
- Author PC decision / monologue → **present pressure**

### Climax (`climax-beats`)

- Unearned spectacle (dragons/volcano/divine) → **harvest planted threads**
- Chart schedule forces Climax mid-negotiation → **call when players commit**
- Mandatory battle after earned negotiation → **non-combat Climax shapes OK** (SKILL)
- Single melee-only approach → **≥2 approaches**
- Early resolution still run planned Climax to fill time → **early resolution *is* Climax; compress → Resolution**
- Force return after avoidance → **avoidance is new state; recompute**
- Ignore middle alliances/intel → **party arrives equipped by middle**
- Force two simultaneous Climaxes → **party chooses; unchosen has consequences**

### Resolution (`resolution-beats`)

- Shock twist / new villain in Resolution → **closure first**
- Inflate past Climax scale → **refuse inflation** (SKILL)
- Erase Climax costs (ally “survived”, merchant restocks) → **costs are load-bearing**
- Skip aftermath; jump to next session → **show arc echo first**
- Immediate bigger-army negation of victory → **honor outcome**
- Author PC reflections / next goals → **present changed world**
- Wrong-scale afterscene (faction war → dinner date only) → **match Climax scale**
- Ungrounded existential threat (dark god / seals) → **refuse; new Hook in disguise** (SKILL / `d4e03b9`)

---

## Refuse-gates encoded in SKILL.md

Quote short excerpts; graders should treat these as hard success criteria when the prompt attacks them.

### `session-beats/SKILL.md`

> Use a Beat Chart as a pacing palette, never as a script. … Never force the next scene because a slot is empty.

> Prepare situations, not outcomes. … Let players ignore a Development, fail a Cliffhanger, or pursue a goal they create. Apply visible consequences and recompute; do not hide a correct path.

> Betrayal and Sabotage: detectable before irreversible. … Treat a failed beat as a real world change, not a cue to replay it.

> If the central question resolves early, that is the Climax — compress and deliver Resolution. If the anticipated Climax is avoided, consequences become new world state; recompute.

### `development-beats/SKILL.md` (sharpened in `6b7fcfa`)

> When a request asks to resolve everything in one Development, refuse the full resolution and reveal one new facet: a clue, a shifted alliance, a constraint, a cost. … Leave what the Cliffhanger will test.

### `cliffhanger-beats/SKILL.md` (`d4e03b9`)

> When a request asks for consecutive Cliffhangers without Developments between them, refuse and write one Cliffhanger, then hand off to a Development. … skipping it turns action into noise.

> A predetermined outcome — the villain escapes no matter what — is not a contest. … never lock the ending.

### `climax-beats/SKILL.md` (`d4e03b9`)

> When the party earned the Climax through negotiation, exposure, or diplomacy, that resolution is the Climax — do not manufacture a new battle to replace it. … Default to the shape the fiction earned, not to combat.

### `resolution-beats/SKILL.md` (`d4e03b9` + `6b7fcfa`)

> When a request inflates the Resolution past the Climax's scale, refuse the inflation and deliver the afterscene the arc earned.

> A dark god, breaking seals, or world-ending threat invented for the Resolution is not established fiction — it is a new Hook disguised as an afterscene. When the request introduces ungrounded existential content, refuse it and deliver the aftermath the session's fiction earned.

> Convenient survival, arriving merchants, and softened consequences erase the Climax's weight … Honor the outcome.

### Shared typed-fill gates (all five type skills)

- Prep only; `entity-before-spoken`; `dm-facing-explicit`.
- ≥2 viable player responses; name ignore / fail / redirect.
- Do not write the next beat — hand off type + trigger.
- Do not author PC decisions, dialogue, or internal monologue.

---

## How graders should read refuse / redesign / offer alternatives

**Passing an adversarial eval is not “compliance with the user’s bad request.”**

| User asks for… | Pass | Fail |
|---|---|---|
| Forced order / mandatory fight / secret betrayal / rewind | Names the violated principle; **refuses** the illegal shape | Produces the illegal chart “as requested” |
| | **Redesigns** into situations, fair contests, planted Climax, proportional Resolution | Softens language but still guarantees the rail |
| | **Offers alternatives** the fiction supports (negotiation Climax, costly revival, Detection opportunity) | Lectures without a usable redesigned beat / chart |

Graders should score:

1. **Guardrail** — explicit refuse of the illegal demand (not buried hedging).
2. **Process** — cites the relevant gate / polarity / recompute / harvest rule.
3. **Content** — supplies a redesigned beat or chart fragment that still does the skill’s job.
4. **Quality** — alternatives are concrete (triggers, stakes, ≥2 responses), not vague “be careful with agency.”

A response that only says “that would be railroading” with no redesign is a **partial**. A response that redesigns silently without naming the refuse is harder to grade — prefer both: **refuse + usable alternative**.

---

## Author checklist (new suites)

- [ ] ~9–13 evals
- [ ] Typed `assertions[{text,type}]`
- [ ] ≥2 strong adversarial / resist evals (prefer 4–8 in beat/craft skills)
- [ ] Hostile prompts attack **this** skill’s SKILL.md gates (not generic “be nice”)
- [ ] No invented live-wiki lore as required answer key
- [ ] Keep any existing strong resist prompts when uplifting
- [ ] One positive craft / improve eval so the suite still tests happy-path fill

---

## Related landing

Uplift drafts under `/workspace/quality-bar/`:

- `cold-opens/evals.json` (10 typed evals)
- `writing-beats/evals.json` (10 typed evals)
- `ABC-AUDIT.md`
- `abc-patches/<skill>/evals.json` (spell-design + vehicle-design full replacements, 9 each)
