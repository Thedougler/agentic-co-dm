---
name: dnd-5e-magic-item-design
description: Design, revise, or audit homebrew magic items for D&D 2024/5.5e and write their wiki pages. Use when creating magic weapons, armor, wondrous items, consumables, artifacts, curses, sentient items, or evolving items. Every page ships a runnable item text block a DM can use tonight — item text is the deliverable, everything else supports it.
---

# D&D 5e magic-item design

File what constitution X makes canon. Follow `docs/agents/work.md`.
## Boundary contract

### Input

Take a named item design, revision, or audit request, the caller's objective,
and a bounded brief with wielder/role, tier, constraints, relevant owner
pages, `wiki/templates/item.md`, current rules anchor, and comparator evidence.
Enter directly for the item's mechanics; keep campaign canon and acceptance
gates in force.

### Owner-specific Work

Work only the named item: preserve its pitch, chassis, power-envelope trades,
engagement loop, readable counterplay, 2024/5.5e mechanics, and curse,
concentration, frequency, travel, and combine-rarity gates. Keep the caller's
objective intact while retrieving only evidence needed to make the item
playable and auditable.

### Capability Handoff

Hand off only a bounded seam: check/save choice to `dnd5e-mechanics`,
player-facing tells and item voice to `theatre-of-the-mind`, acquisition sites
and hazards to `dungeon-design`, reveal or evolution timing to `session-beats`,
creature mechanics to `homebrew-monsters-5e`, vault facts to `qmd-retrieval`,
appearance anchors to `visual-references`, and approved item art to
`visual-aids`. Send the item owner, objective, evidence, and exact section
requested; require return evidence naming the child artifact/section and
completion result. Resume item work only after that result satisfies its owner
contract; otherwise report the missing evidence or specific blocker.

### Done

Use the existing `## Done` checklist plus the research, mechanical, and
narrative audits. Completion is observable when the item has its accepted pitch,
substantive template content, comparator matrix, runnable constrained effect,
engagement loop, and any child return evidence.

## Success criteria

- The page has a **runnable item text block** that a DM can use tonight without
  reading anything else on the page. Item text states trigger, action cost,
  frequency, range, targets, duration, limits, and edge cases in 2024 rules
  language.
- Page priority: **Item Name → Item Text → everything else.** Narration and
  classification precede item text; supporting sections follow. Each fact
  appears once — no section restates the item text.
- Invention labeled and proposed; wiki write after DM accept.
- Mechanics calibrated against published peers with working links.

## Refuse gates

- **Work gate.** Chat proposal before writing under `wiki/`. Workspace allowed.
- **Invention.** Set `invention: true` or mark proposed. Cite `[[pages]]`, show
  contradictions. No silent canon.
- **Template lock.** Copy `wiki/templates/item.md`. Fill it with substance.
- **Narration.** `[!narration]` cold portrait. No secrets, DCs, or mechanics.
- **No proprietary paste.** Paraphrase and link public rules.
- **Rarity is a ceiling.** Trade axes; refuse stacking maximum offense, defense,
  mobility, control, and utility at high rarity.
- **Every-hit riders.** Once-per-turn or equivalently calibrated frequency.
- **Concentration / slots.** Preserve concentration; no hidden free spell slots.
- **Curse agency.** Visible tells, player choices, counterplay, consent, exit.
- **Combine ≠ same rarity.** Two same-rarity ceilings combined reassess tier.

## Design process — conversation, not the page

Design outputs stay in conversation or process notes. The wiki page gets the
result, not the journey.

1. **Pitch.** "This is a [item] for a [role] that lets its bearer [experience]
   by paying [cost]." Name experience, fantasy, owner, tier, and counterplay.
2. **Chassis.** Least speculative: reskin → narrow change → equal exchange →
   combine-then-reassess → bespoke only if needed.
3. **Research.** Public rules anchor + three comparator roles with working links.
   Use `references/research-and-comparators.md`. Record observations inline.
4. **Power envelope.** Table offense, defense, action economy, spell access,
   exploration, social. Trade strong axes for weakness, cost, or frequency.
5. **Audit.** Run `references/mechanical-audit.md` and
   `references/narrative-and-wording.md` before the final item text.

Evidence priority: (1) user brief / table limits; (2) 2024/5.5e public rules;
(3) official peers; (4) reputable published homebrew; (5) numerical audit;
(6) theme.

Read `references/item-craft.md` for rarity ceilings, design habits, audit
questions, and failure modes.

## File the wiki note

Copy `wiki/templates/item.md` (consumables) or `wiki/templates/hazard.md`
(flora hazards). Before design, retrieve target PC, hot page, front/quest/
session, signature gear, and three same-tier comparators. State tier, wielder,
acquisition, constraints, attunement, cadence, and strongest party synergy.

Page structure — each section earns its place or gets omitted:

1. **Frontmatter** — `type: item`, plus `campaign`, `region`, `kind`, `rarity`,
   `attunement`, `tags`, and `wiki/AGENTS.md` required fields.
2. **Narration** — `[!narration]` cold portrait via `theatre-of-the-mind`.
3. **Classification line** — kind, rarity, attunement.
4. **Item text** — the runnable mechanic in 2024 rules language. Simple items:
   1–3 sentences. Complex items: bold-label properties with limits and edge
   cases inline. This block is the reason the page exists. No field table
   before or around it — rarity justification, attunement reasoning, wielder
   profile, and balance commentary belong in process notes, not on the page.
   See `references/narrative-and-wording.md` for simple/complex patterns.
5. **At the Table** — only when the item text alone leaves a non-obvious play
   consequence unstated. Never restate mechanics the item text already
   covers. If the item text is complete, omit this section.
6. **Hidden Properties** — unrevealed curse, attunement benefit, conditional
   trigger. Omit when unused.
7. **Connections** — `[[wikilinks]]` that change what happens at the table.
8. **Provenance** — where it came from, when that matters. 1–2 sentences.

Complex items (weapons, relics, artifacts, sentient/cursed/evolving) add
sections only when they change the table. Reveal structure: first sight,
handling, known mechanics, earned lore, DM truth.

Exemplar: `wiki/entities/item/chain-coil-python.md` (trained animal — clean
mechanics block with edge cases and limitations inline, no field table, no
design diary on the page).

## Handoffs

- **theatre-of-the-mind:** item tells, sensory manifestations, cursed/sentient
  voice, player-facing fiction.
- **dungeon-design:** placement, vault/quest, hazards, factions, acquisition.
- **session-beats:** reveal, first-use, escalation, evolution, curse pressure.
- **homebrew-monsters-5e:** item that creates/commands/transforms into a
  creature; keep creature math there.
- **qmd-retrieval:** campaign-vault facts; retrieval before invention.

## Done

- Item text block is runnable: trigger, action cost, frequency, limits, edge
  cases in 2024 language. A DM can run it tonight without a design diary.
- Each fact appears once on the page. No section restates the item text.
- Invention labeled/proposed; wiki write after accept.
- Comparators with working links informed the design.
- Template filled with substance, not empty headings.
