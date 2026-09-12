---
type: calendar
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/calendar.md"   # OPTIONAL — the guide or skill that owns this page's quality
created: "{date}"
updated: "{date}"
tags: []
tier: supporting         # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
reckoning: ""             # this calendar's own year-counting era, written exactly as it appears in a date, e.g. "Dalereckoning (DR)" — a calendar always has one
current_date: ""          # this calendar's in-fiction "now", in its own units and reading order, e.g. "15 Eleint, 1495 DR"
within: ""                 # OPTIONAL — quoted vault-relative wikilink to the world or region this calendar is used in, e.g. "[[worlds/faerun]]"
campaigns: []              # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 2512096c-5186-43a0-86e2-b0c154e559d7
---

# <Calendar Name>

*One-line description: who reckons time this way, and where it came from.*

## Overview

Who set this timekeeping system, the fixed point it counts from, and who
actually uses it now. State how far its authority reaches too: one
culture, one faith, or the whole setting. This page states the system's
units, holidays, and cycles. The sequence of things that actually
happened stays on a `lore` page (a `## History` timeline); wikilink that
page here instead of restating any of its entries.

## Structure

<Every unit this calendar uses, smallest to largest. Start from the
day, then whatever grouping this setting has above it (a week or its own
name for one), on up through the month and the year. Name each unit and
state how many of the smaller unit make one of the next. Never assume a
24-hour day, a 7-day week, a 12-month year, or any other Earth-derived
count.>

| Unit | Name(s) | Made of | Notes |
|---|---|---|---|
| <Year> | <Name, if any.> | <N> <months> | <How years are counted or numbered.> |
| <Month> | <Name(s).> | <N> <days> | <Order, if it matters.> |
| <Week> | <Name, if any.> | <N> <days> | <Delete this row if this setting has no week-level grouping.> |
| <Day> | <Name(s), if any.> | (n/a) | <How a day breaks down, if that split matters at the table.> |

## Intercalary Days & Leap Rule

OPTIONAL. Delete outright when every day in this calendar falls inside a
normal month and no day is ever added or removed on a cycle.

<Days that fall outside the month structure (between months, at year's
end), plus any rule that adds or removes a day on a recurring cycle to
keep the calendar in line. Name what triggers it and how often.>

## Holidays & Observances

OPTIONAL. Delete outright until at least one holiday has real, sourced
content. Never fill this heading with a placeholder row.

<Named days worth marking: festivals, rites, taboos, the day people
actually date years by.>

| Holiday | When | What it marks |
|---|---|---|
| <Name> | <Date or position in the structure above.> | <What it celebrates or observes, and what a party passing through would actually see or do.> |

## Moons

OPTIONAL. Delete outright when this setting has no moon, or its moon or
moons track no cycle worth naming.

<Every moon worth tracking.>

| Moon | Cycle | Notes |
|---|---|---|
| <Name> | <Length of one full cycle, in this calendar's own days.> | <What its phases mean at the table, if anything, such as a tide or a timed ritual window.> |

## Seasons

OPTIONAL. Delete outright when this setting has no seasons distinct
enough to change what a party can do.

<Every season this calendar marks.>

| Season | Falls | What changes |
|---|---|---|
| <Name> | <Position in the structure above.> | <Weather, travel, availability: whatever a party actually feels.> |
