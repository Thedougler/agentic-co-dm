# Worked Example

Fixture — placeholder names, not real campaign content.

User: "I need a campaign overview — pirates fighting over a sea that's
dying."

Standard queries: `grep -rl "type: campaign" vault/campaigns/` → empty
(first ongoing-subtype page for this repo). `grep -ril "shattered sea"
vault/` → empty. Clean to create.

Interview answers (given together): pitch — "the Sea itself is dying, and
whoever controls the last living currents controls everything that comes
after"; three truths — reefs are visibly bleaching and sailors blame a
specific sunken thing, an old trade concordat is fracturing over who gets
the dwindling safe routes, a prophecy names a "Tideglass Heir" nobody's
found; starting location — the port town of Tidefall; Icons — the Dravosi
Crown (a faction, needs a Front — hand off to `.claude/skills/draft-content/references/faction.md`) and a named
sea-witch (backdrop for now, no Front yet); inspiration/tone — nautical
tragedy, hope under pressure, refuses to make the dying sea reversible by
a single McGuffin; safety — the table flagged death-by-exposure and
large-scale death/genocide themes as off-screen-only (described, not
dwelt on), no hard lines named; session zero — shared connection: everyone
already works the Tidefall docks.

```markdown
---
type: campaign
status: pending
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: []
summary: "A dying sea, a fracturing trade concordat, and a prophecy nobody can find — the party starts as dockworkers in a port town running out of water to fish."
tier: core
subtype: ongoing
campaigns: [Shattered Sea]
---

# Shattered Sea

*A sea is dying, and whoever holds its last living currents holds everything after.*

## Overview

### Ongoing Campaign — The Premise

The reefs are bleaching in living memory, and sailors already blame
something specific and sunken for it — not vague decline, a named cause
nobody's confirmed.

### Ongoing Campaign — The Three Truths

1. Reefs across the Sea are visibly dying, and every sailor has a theory
   about the same sunken cause.
2. The [[dravosi-crown|Dravosi Crown]]'s trade concordat is fracturing
   over who controls the dwindling safe routes.
3. A prophecy names a "Tideglass Heir" who could reverse the dying — nobody
   living has found them.

### Ongoing Campaign — Key Figures

- **The Crown** [[dravosi-crown]] is the trade power everyone still
  answers to, for now — see their own page for their active Front.
- **The sea-witch** [[name]] is blamed by half the port for the dying reefs
  and thanked by the other half for what fish are left; no active Front
  yet, backdrop for now.

### Ongoing Campaign — The Starting Situation

The party starts as working dockhands in Tidefall, the port town the
setting spirals outward from — pulled together by the same collapsing
catch, not a shared quest yet.

**Questions to answer before Session Zero:**

- What does your PC stand to lose specifically when the reefs finish dying?
- Does the party share a single starting connection (a patron, an
  organization) or does each PC bring an individual relationship to
  another PC? Shared: everyone already works the Tidefall docks.

## Safety & Tone

**Sensitive topics discussed:** death by exposure, large-scale
death/ecological collapse.

**Hard lines** (never comes up): none named.

**Off-screen content** (can happen, described vaguely, not played out):
death by exposure, large-scale death — named but kept off-screen per the
table's request.

**Safety cue:** "pause for a second."

## GM Notes

### Ongoing Campaign — Inspiration & Themes

**Inspiration.** Nautical tragedy, faction politics over a shrinking
resource.

**Themes.** What do you owe the people who depend on a dying thing you
can't personally save?

**Tone.** Hope under pressure, not despair — consequences land, but the
dying sea is never reversible by a single found McGuffin; that refusal is
deliberate.

No additional GM-only secrets beyond the Icons' own pages at this time.
```

This satisfies the checklist: subtype set with the other fork's H3s
deleted, no Front mechanics restated (the Crown's page owns that), Safety &
Tone filled from an actual table discussion rather than left empty, a named
PC-facing session-zero question plus an explicit shared-connection answer,
and template H2s in the fixed order with no visibility split.
