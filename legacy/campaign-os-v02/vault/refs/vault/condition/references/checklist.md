---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The condition-specific checks after the shared checklist — the rule-vs-condition boundary, absorbed categories, condition_status, and the no-numbers rule."
created: "2026-08-09"
updated: "2026-08-09"
tags: [horror]
uid: f2aa55d9-1be7-49d7-962f-2e3557402200
---

# Draft — Condition Checklist

Run `vault/refs/vault/_common/checklist.md` first; these are the
condition-only additions.

- [ ] The Rule-vs-Condition Boundary test was actually run — nothing on
      this page is a save DC, a damage die, a duration, or any other
      number that belongs on a `type: rule, subtype: condition` page
      instead.
- [ ] `## Nature` states plainly which of the five absorbed categories
      (disease, curse, mutation, madness, poison-effect) this page is,
      not a generic "affliction" line.
- [ ] `## Onset & Symptoms` states what an onlooker would notice, not
      only what the carrier feels, and whether the progression is staged
      or sudden.
- [ ] `## Transmission & Origin` names a real mechanism (contact,
      ingestion, inhalation, casting, inheritance, exposure) and either a
      real origin or an explicit "no origin worth naming" — never left
      implicit.
- [ ] `## Cure & Mechanical Effect` states the cure/treatment state
      (mundane remedy, specific magic, ritual, or no known cure) and
      closes with either a working `[[rule-slug]]` link to the
      mechanical counterpart page or the explicit "no mechanical effect
      — narrative only" line — never silence on the mechanical link.
- [ ] `condition_status` reflects the affliction's actual current state
      (active/dormant/cured) in this campaign, not left at the template
      default by accident.
