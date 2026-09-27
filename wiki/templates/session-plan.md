---
title: "{{title}}"
category: journal
tags: ["{{campaign}}", session-prep]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: session-prep
kind: session-plan
reveal: unrevealed
campaign: "{{campaign}}"
session: ""
visibility: dm
question: ""
summary: ""
---
<!-- Fact-only: every line gives the DM a fact, ruling, or response. Keep a section only when this session spends it; delete unused sections, rows, and these comments. Chart rules and audit checks: session-beats. File as Session-<n>-00-<title>.md. -->

# {{title}}

<!-- Required. The lines the DM runs the night by, one fact each. The session question is a design note for agents and goes in the frontmatter; each beat's card goes in that beat's frontmatter. -->

**Opening situation.** What is already happening when play begins.
**Current beat.** [[Session-{{session}}-01-label]] · **Next beat.** [[Session-{{session}}-02-label]]

## Beats

<!-- Required. One row per charted beat, in play order. -->

|  # | Beat | Type | Starts when | What changes | Minutes |
| -: | ---- | ---- | ------- | ------------ | -----: |
| 01 | [[Session-{{session}}-01-label]] | Hook | Play begins |  |  |
| 02 | [[Session-{{session}}-02-label]] | Development |  |  |  |
| 03 | [[Session-{{session}}-03-label]] | Cliffhanger |  |  |  |
| 04 | [[Session-{{session}}-04-label]] | Climax |  |  |  |
| 05 | [[Session-{{session}}-05-label]] | Resolution | The climax resolves |  |  |

<!-- Optional under Beats: keep each `###` table only when it exists. -->

### Floating Beats

| Beat | Bring in when | Drop when |
| ---- | ------------- | --------- |
|      |               |           |

### Climax Candidates

| Candidate | Earned when | What it settles |
| --------- | ----------- | --------------- |
| [[beat]]  |             |                 |

### Branches

| Beat | If the party… | Then |
| ---- | ------------- | ---- |
| [[beat]] |           |      |

### Critical Routes

| Conclusion | Route 1 | Route 2 | Route 3 |
| ---------- | ------- | ------- | ------- |
|            |         |         |         |

## Threads

| Thread | Source | Introduced | Returns | Resolved |
| ------ | ------ | ---------- | ------- | -------- |
| [[page]] | A PC's goal, a mystery, a relationship, or a resource | [[beat]] | [[beat]] | [[beat]] |

````col
```col-md
flexGrow=1
===
## Opposition Plan

**[[npc]] or [[faction]]** — what it wants this session and the means.

| Step | Without the party | Seen in |
| ---: | ----------------- | ------- |
| 1    |                   | [[beat]] |
| 2    |                   | [[beat]] |
| 3    |                   | [[beat]] |
```

```col-md
flexGrow=1
===
## PC Hooks

| PC | What matters to them this session | Beat |
| -- | --------------------------------- | ---- |
| [[pc]] |                               | [[beat]] |
```
````

## Clues

<!-- About ten true, concrete facts, unattached until play shows where they belong. -->

- [ ] A short usable fact the characters can discover.

## Improv Kit

- **Places.** [[place]] · [[place]]
- **People.** [[npc]] · [[npc]]
- **Opposition.** [[creature]] · [[faction]]
- **Spare names.** Four or five names that fit the setting.

**If play stalls.** The opposition's next move and what the characters see; an unused clue and what reveals it; a floating beat that fits anywhere.
