---
type: dm-screen
status: pending
publish: false
aliases: ["Session 08 DM Screen"]
created: "2026-08-03"
updated: "2026-08-10"
tags: [exploration, intrigue, maritime]
summary: "Session 08's dashboard for the Basin refit and the Calveno crawl."
tier: supporting
parent_run_guide: "[[run-guide]]"
session_number: 8
campaigns: [Shattered Sea]
uid: 1644652f-3470-4729-872d-02ac312e09c7
---

# Session 08: DM Screen

## Party Combat Strip

![[party-combat.base]]

## Tonight's Moments

```base
filters:
  and:
    - 'type == "moment"'
    - 'session_number == this.session_number'
views:
  - type: table
    name: "Tonight's Moments"
    order:
      - file.name
      - moment_number
      - locations
      - encounter
    groupBy:
      property: moment_number
      direction: ASC
```

## Tonight's statblocks

None tonight. Nobody plans a fight, so no moment sets a `statblocks:` array, and this section stays empty by design.

## Encounter Launchers

None tonight. No moment carries an `encounter:` link. The [[calveno-districts|Calveno Districts page]] has six street fights ready if the table wants one, DM's call only.

## Map Links

- [[calveno-map|Calveno map]], open in a second pane for jumping districts across the crawl.
