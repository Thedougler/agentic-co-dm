# Standard queries — the party-material inventory

Run before deriving any event, paste every hit:

```sh
# Route page — does the way itself already have standing facts?
grep -rl "^type: route" "vault/campaigns/"*"/locations/" 2>/dev/null \
  | xargs grep -l "<endpoint or lane name>" 2>/dev/null

# Stub check — named vessel/hazard/entity on this leg already exist?
grep -ril "<route/leg name or named vessel/hazard>" vault/ 2>/dev/null

# Reusable encounter table for this leg or terrain
grep -rl "^type: table" vault/refs/ 2>/dev/null \
  | xargs grep -il "<terrain/lane>" 2>/dev/null

# Faction pressure that could plausibly reach this leg
grep -rl "### Front:" vault/campaigns/shattered-sea/factions/ 2>/dev/null

# PC hooks this leg could pull on (Hard Rule 1)
grep -rA5 "## Arc Notes (DM Only)" \
  vault/campaigns/shattered-sea/pcs/ 2>/dev/null
```

An existing route page is the leg's baseline — its `travel_time:`,
`traffic:`, `hazard_level:`, and `## Hazards` are read, never re-invented.
The party's own vessel (its page, crew, condition) is live material for
derivation like any thread.

Empty faction/PC-hook output is informative early-campaign, not a blocker —
ask the DM which thread to pull on rather than inventing pressure
(`.claude/skills/composing-beats/references/runtime-surface.md` §2). Reading a stub-check result, and what
empty output does and does not license claiming:
`vault/refs/vault/_common/queries.md`.
