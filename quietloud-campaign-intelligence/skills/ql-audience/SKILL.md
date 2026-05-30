---
name: ql-audience
description: Identify target audiences from campaign signals and recommend the best ICP to target first.
---

# Audience Reasoning

## Role

Second step in the QuietLoud pipeline. Determine who the content is relevant for and pick the single best target.

## Background

Use context from `quietloud-background` to understand QuietLoud's existing audiences and where they want to expand reach.

## Input

- `signals[]` — from `ql-signals`
- `themes[]` — from `ql-signals`

## Task

Identify which external audiences would genuinely care about these signals and themes. Then recommend the single best ICP to target first.

Consider audiences like: ops leaders, CMOs without brand equity, founders acting as CMO, growth marketers, CROs, category-specific verticals.

## Narration

Before returning the JSON, write 2–4 sentences explaining:
- Which audiences surfaced and the strongest signal-to-segment connection for each
- Why the recommended ICP was prioritised over the others — name the specific signal that tipped it

## Carry forward

`audiences[]`, `recommended_icp`

## Rules

- Only surface audiences with a clear connection to the signals
- `recommended_icp` is a single one-line description of the best target
- Base reasoning strictly on the signals — do not invent audiences
