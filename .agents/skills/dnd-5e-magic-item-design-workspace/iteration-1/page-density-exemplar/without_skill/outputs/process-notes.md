# Design Process: Undertow Net

## Design Constraints Satisfied

1. **CR-appropriate uncommon magic item** — designed to be weaker than permanent restraint options but more reliable than a mundane net
2. **Restrains one creature** — explicit "only one creature at a time" rule with mechanical clarity
3. **Simple recharge mechanic** — recharges at dawn each day; can be manually released earlier via command word
4. **Shattered Sea fisher context** — tied to reef work, deep-dweller trade networks, practical crew tool
5. **Marked as invention** — `tier: invention` in frontmatter (no campaign-os source)

## Page Density Strategy

### Structure Adapted from Exemplars

**Salvage-Plate Harness template** (more applicable than Chain-Coil Python):
- Multi-line sensory narration with specific material/tactile details
- Classification line (rarity + item type)
- Field-Detail table for context and mechanical reasoning
- Mechanics block with [HB] tag and clear rule statements
- At the Table section for table dynamics
- Provenance connecting to campaign world
- Connections to relevant wiki entities

**Why this structure over Python's:**
- Harness uses a table to bundle rarity justification + thematic context, which works well when the item's balance and narrative role are equally important
- Python's approach (discrete mechanics bullets) better suits a complex, multi-part tool; the net is simpler and benefits from unified mechanical statement

### Density Calibration

**Narration (exemplar parity):**
- Salvage-Plate: 5 sentences across 4 narrative lines
- Chain-Coil Python: 5 sentences across 4 narrative lines
- Undertow Net: 4 sentences across 5 visual lines (parallel density, emphasizing sensory + magical specificity)

**Field-Detail Table (adapted from Harness):**
- Salvage-Plate: 6 fields (One thing / Rarity / Attunement / PC connection / Current holder / Narrative hook)
- Undertow Net: 5 fields (One thing / Recharge mechanic / Rarity justification / Balance / Fisher connection / Narrative weight) — removed Current holder (would require established NPC) and repurposed toward mechanical clarity and fisher context

**Mechanics block:**
- Salvage-Plate: ~140 words across 4 subsections (rule + edge cases + limitations)
- Undertow Net: ~170 words across 6 subsections (hit resolution / special / release / recharge / limitations + flying caveat) — slightly more detail because net mechanics are less familiar than armor mechanics

**Supporting sections:**
- At the Table: ~90 words (table impact and stakes) — parallel to Harness's section intent (consequences beyond the mechanic text)
- Provenance: ~60 words (origin, trade route, rarity context) — aligned with both exemplars' density
- Connections: 2 entries (trading hub + campaign region) — lighter than Harness but sufficient for a commonly-traded item

### Mechanical Design Decisions

**Restraint vs. Grapple:**
- Chosen "restrained" (familiar 5e condition) over bespoke grapple to reduce complexity
- Escape via Strength check (contestant by Sleight of Hand) to reflect difficulty of untangling rather than overpowering

**Attack Roll Requirement:**
- Adds decision friction (does the caster have proficiency with nets? do they risk the action?)
- Keeps it from being auto-cast removal; a creature with high AC might slip the throw

**One Creature Limitation:**
- Clear balance gate: prevents soft-locking encounters
- Thematic (fisher's tool, not crowd-control treasure)
- Mechanical clarity: no stacking, no "but what if I throw it twice" edge case

**Dawn Recharge:**
- Simple and resonant with fishing/tide cycles
- Clear in-world reset that doesn't require attunement or rituals
- Creates stakes: hold this thing overnight and it breaks free at sunrise if you haven't released it manually

**Strength Contest for Escape:**
- More generous than fixed DC (uncommon item should feel weak after 1–2 rounds of use)
- Contested roll invokes the caster's own competence (if you're *good* at tying nets, your restraint holds harder)
- Avoids saving throws (PC escape routes already crowded with those)

### Naming and Flavor

**Undertow Net:**
- Evocative without being generic ("Binding Net", "Restrain-Net")
- Ties to Shattered Sea water/depth magic system
- Sensory: undertow = unseen pulling force, net = familiar fisher tool
- Works equally for mechanical explanation and player narration

**Kelp and deep-reef origin:**
- Grounds the item in a specific place (deep settlements, not vague arcane source)
- Explains rarity (kelpweavers don't surface often)
- Creates adventure hooks (can you trade for more? who do you know in the deep?)
- Matches exemplars' approach (salvage-plate came from a specific wreck; python from a specific supplier)

## Departures from Exemplars

1. **No current holder:** Salvage-Plate names Kettil at Ormsson's Fittings; Python is owned by Zort. Undertow Net assumes crew-level circulation (multiple holders), which is more typical for an uncommon item. This could be added if the design is promoted to the vault and a specific NPC is tied to it.

2. **Lighter Connections section:** Two entries instead of Harness's embedded references throughout the table. Undertow Net assumes less existing wiki context; if the vault already has deep-reef entities or specific fisher crews, those could expand this.

3. **Table fields re-ordered for clarity:** Harness puts "PC connection" mid-table; Undertow Net groups "Fisher connection" with "Narrative weight" to emphasize practical/thematic use before mechanical nuance. Both orderings serve the same purpose (context before limitations).

## Validation Against Template

✓ **Narration:** standalone cold portrait covering type, scale, material, wear, and non-sight sense (cool, smooth, weight, salt smell, bell-note of stones)
✓ **Classification:** clear (Uncommon wondrous item)
✓ **Item text:** complete mechanical statement with trigger, action, targets, condition, escape, limits
✓ **At the Table:** covers playable consequences (restraint choice, time pressure, stakes at dawn)
✓ **Provenance:** states facts, no meta or process notes
✓ **No empty sections:** Connections and Provenance used; Hidden Properties omitted (none)
✓ **Distilled facts:** no restating of item mechanics in other sections; each section owns its domain

## Quality Gates

- **Mechanical clarity:** a DM reading the Mechanics block can rule on a net use without ambiguity
- **Uncommon rarity coherence:** weaker than permanent or multi-target options, but reliable for single targets
- **Shattered Sea flavor:** tied to reef communities, trading networks, fisher work, without invented NPC dependencies
- **Page density:** matches exemplars in narration, table use, mechanics detail, and supporting context

## Iteration Notes

This iteration prioritizes **mechanical clarity + thematic rootedness** over maximal novelty. The net is intentionally straightforward (single-target restraint with daily recharge) so that a game table can adopt it without rules lawyering. The Shattered Sea context (deep-dweller origin, trade route, fisher crew circulation) gives it campaign weight without requiring established characters or resolved plot threads.

If promoted to the vault, next iterations could:
- Tie a specific holder/crew to strengthen "Current holder" context
- Add Art embeds (net portrait, depth scene, token)
- Deepen kelpweaver lore connections if those entities exist
- Explore higher-rarity variants (charged stones, multi-target version, attunement upgrade)
