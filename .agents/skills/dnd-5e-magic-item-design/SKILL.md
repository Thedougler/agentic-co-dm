---
name: dnd-5e-magic-item-design
description: Design, revise, or audit engaging and mechanically sound homebrew magic items for D&D 2024/5.5e. Use when creating magic weapons, armor, wondrous items, consumables, artifacts, curses, sentient items, or evolving items. Every design must be grounded in comparable official content or reputable published homebrew found through current web research.
---

# D&D 5e magic-item design

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Refuse gates

- **Work gate.** Show a chat proposal before writing under `wiki/`. Write only
  after DM acceptance. Workspace outputs are allowed before acceptance.
- **Invention.** Never present invention as wiki fact. Set `invention: true` (or
  mark proposed), cite `[[pages]]`, show contradictions, and propose for
  acceptance. No silent canon — including new curses, maker myths, extra daily
  powers, stacked envelopes, or undeclared campaign plots on existing items.
- **Template lock.** Copy `wiki/templates/item.md` only. Fill narration,
  classification, and runnable effect with substance — not empty headings.
- **Narration.** Spoken look is `[!narration]` cold portrait. No secrets, DCs,
  or unearned names.
- **Pitch first.** Write a Signature / pitch sentence (object + distinctive verb
  + why it belongs) before the page draft or final numbers.
- **Web grounding.** Current public 2024/5.5e rules anchor before final numbers;
  at least three comparator roles (chassis, effect/role, boundary) with working
  links. Votes, ratings, or a single anecdote are not balance evidence. Label
  2014 material legacy and recalibrate — do not silently reuse it as 2024.
- **No proprietary paste.** Never paste WotC book text; paraphrase and link
  public rules or benchmarks.
- **Rarity is a ceiling.** Refuse to stack maximum offense, defense, mobility,
  control, and utility merely because the rarity is high. Trade axes.
- **Every-hit riders.** Unbounded “on every hit” needs a once-per-turn (or
  equivalently calibrated) frequency — Extra Attack, TWF, and reactions multiply.
- **Concentration / slots.** Do not silently remove concentration or grant
  hidden free spell slots from an item.
- **Curse agency.** Reject curse as secret plot punishment or unilateral loss of
  player control. Require visible tells, player choices, counterplay, consent,
  and an exit or redirect.
- **Travel loops.** Reject trivializing travel forever (impossible to track +
  auto-navigate + daily anywhere teleport). Preserve exploration identity with
  limits and counterplay; check ranger/rogue/scout niches.
- **Combine ≠ same rarity.** Two same-rarity ceilings combined do not stay that
  rarity by default — remove, narrow, cost, raise tier, or add a hard limit.

## Central principle

An item promises a specific experience, has a readable decision loop, and earns
its place. Mechanics are legal 2024/5.5e language, calibrated against published
peers. Power is traded, not stacked. Prefer delete and clarify. State
assumptions, uncertainty, and tuning knobs. Keep designs setting-agnostic unless
the brief supplies canon.

## Build the item

1. **Pitch.** One sentence: “This is a [item] for a [role] that lets its bearer
   [choice/experience] by paying [cost or risk].” Name experience, fantasy,
   owner, tier, and counterplay.
2. **Chassis.** Prefer least-speculative: reskin → narrow change → equal
   exchange → combine-then-reassess rarity → bespoke only if needed.
3. **Research packet.** Public rules anchor + three comparator roles. Record
   actionable observations and working links in the matrix — no bibliography
   page. Use `references/research-and-comparators.md`.
4. **Power envelope.** Table reliable/burst offense, defense, action economy,
   spell access, exploration, social. Trade a strong axis for weakness, cost,
   narrowness, or frequency. Audit the whole party.
5. **Engagement loop.** Tell → Choice → Cost → Payoff → Counterplay. Include a
   normal turn, a tempting costly use, and what happens if ignored.
6. **Limits and audit.** Attunement, charges, recharge, duration, targets,
   concentration, stacking, failure, curse consent/exit, tuning knobs. Run
   `references/mechanical-audit.md` and `references/narrative-and-wording.md`
   before final player-facing text.

Evidence priority when conflicts: (1) user brief/table limits; (2) current
2024/5.5e public rules; (3) official peers; (4) reputable published homebrew;
(5) numerical audit/playtest; (6) theme.

Read `references/item-craft.md` for rarity ceilings, design habits, default
output, campaign wiki workflow, audit questions, and failure modes.

## File the wiki note

Copy `wiki/templates/item.md` (consumables) or `wiki/templates/hazard.md` (flora
hazards). Pass item jobs in `wiki/AGENTS.md` Layout. Before design, retrieve
target PC, hot page, front/quest/session, signature gear, and three same-tier
comparators. State tier, wielder, acquisition, constraints, attunement, cadence,
and strongest party synergy.

1. **Frontmatter** — `type: item`, plus `campaign`, `region`, `kind`, `rarity`,
   `attunement`, `tags`, and `wiki/AGENTS.md` required fields. Omit unused keys
   including `owner`.
2. **Spoken look** — `[!narration]` cold portrait.
3. **Classification** — kind and rarity (or hazard start/notice).
4. **One runnable effect** — terse 2024/5.5e text; trigger, action type,
   prerequisite, target/range, roll/DC, effect, duration, uses/charges/recharge,
   concentration, stacking, edge case. At-table grammar from `obsidian-markdown`.
5. **At the Table** — playable-tonight consequence only (no design diary). Omit
   only with documented N/A rationale in process notes — silent omit fails.

Complex items (weapons, relics, artifacts, sentient/cursed/evolving) add sections
only when they change the table. Separate reveal into first sight, handling,
known mechanics, earned lore, and DM truth. Design-process artifacts (matrix,
envelope, loop) stay in conversation/process notes — not the wiki note.

## Handoffs

- **theatre-of-the-mind:** item tells, sensory manifestations, cursed/sentient
  voice, player-facing fiction without map assumptions.
- **dungeon-design:** placement, vault/quest, hazards, factions, gates around
  acquiring or losing it.
- **session-beats:** reveal, first-use, escalation, evolution, curse pressure,
  payoff timing.
- **homebrew-monsters-5e:** item that creates/commands/transforms into a monster;
  keep creature math there.
- **qmd-retrieval:** campaign-vault facts; do not invent setting details when
  retrieval is silent.

## Done

- Pitch/Signature present; template filled with substance; narration
  perceivable-only.
- Invention labeled/cited/proposed; wiki write only after accept.
- Comparator matrix with working links; rarity treated as ceiling with trades.
- Runnable effect states trigger, frequency/limits, and hard constraints;
  every-hit / concentration / travel / combine-rarity gates held when relevant.
- Engagement loop readable; mechanical + narrative audits run; tuning knobs
  stated.
- DM can run the item tonight without a design diary on the page.
