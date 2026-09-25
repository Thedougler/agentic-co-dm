---
title: "{{title}}"
category: entities
tags: ["{{campaign}}", vehicle]
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: vehicle
reveal: unrevealed
campaign: "{{campaign}}"
visibility: dm
kind: vessel
region: ""
berth: ""
summary: ""
---
<!-- Copy-start scaffold. Jobs: Look; sheet; components; crew stations; handling; combat.
     After combat, shared omit-if-empty owner sections in this order (Red Lady / Dead Lady practice):
     At a Glance → Connections → At the Table → Provenance → Art.
     Pass is vehicle jobs in wiki/AGENTS.md Layout. Omit unused sections.

     Every sheet and component line carries a number; where canon is silent, the peer craft's figure is canon under the rule in `llm-wiki`.
     Numbers one-home: hull AC/HP (and other sheet numbers) live under Components/Sheet headings, not an unheaded blob.
     Handling vs At the Table: one play loop — do not duplicate the same run advice in both.
     Provenance is ownership/history facts only — forbid meta ingest Provenance on DM pages.
-->

# {{title}}

> [!narration] Narration
> <!-- Load `.agents/skills/theatre-of-the-mind` → mode: standalone cold portrait → subject: object. -->
> Write a standalone cold portrait in flowing prose — as long as the craft requires to be pictured at its berth or underway. Cover silhouette, scale, material, and usable features a character can interact with. The portrait paints a drawable picture a player can recognize and distinguish. No secrets, DCs, or unearned names.

## Sheet

- **Size.**
- **Type.**
- **Speed.**
- **Crew (min).**
- **Passengers.**
- **Cargo.**

## Components

- **Hull.** AC, HP, damage threshold.
- **Helm.**
- **Movement.**
- **Weapons.** Armed craft only. Omit when unarmed.

## Decks

Areas at body scale (size in feet), one usable feature each, and who stands watch. Omit for a craft too small to walk.

## Crew stations

Named stations, who mans them now against the minimum, and compact numbers for every fighter aboard.

## Handling

Conditions, maneuvers, and limits that change a choice. Do not restate this loop under At the Table.

## Combat

Initiative, ramming, boarding, and destruction when the craft fights. Omit when it does not enter play as a fighting craft.

## At a Glance

Name the captain, the errand this week, standing orders on meeting the party, and the next step with a time.

## Hidden Cargo & History

Concealed cargo, true flag, sealed compartments, or who is hunting this craft. Omit when unused.

## Connections

- [[page]]. State what this tie does at the table.

<!-- Omit Connections when unused. -->

## At the Table

Explain how to run the craft tonight. Cover approach, berth, pursuit, or boarding choice. Omit when unused. Do not duplicate Handling.

## Provenance

State the chassis source, rename history, and contested ownership. Facts only. Do not include ingest or process meta. Omit when unused.

## Art

<!-- Art embeds: wiki/attachments/{subject-slug}-{role}.ext — roles: banner|portrait|token|battlemap|overview|reference|handout|teaser. Flat folder; omit Art when unused. -->
