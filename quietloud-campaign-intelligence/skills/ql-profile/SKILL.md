---
name: ql-profile
description: Build a detailed customer persona with pain points, buying trigger, and relevance score.
---

# Customer Profile

## Role

Third step in the QuietLoud pipeline. Turn the recommended ICP into a concrete human persona.

## Background

Use context from `quietloud-background` for QuietLoud's target market and positioning.

## Input

- `recommended_icp` — from `ql-audience`
- `signals[]` — from `ql-signals`

## Task

Build a persona that represents the human who should receive the campaign asset. Be specific — pain points should describe real frustrations, not generic marketing concerns.

## Narration

Before the JSON, write 2–3 sentences introducing the persona:
- Who they are and why the signals point to this person specifically
- The single biggest assumption made and how confident you are in it
- The buying trigger in plain language

## Carry forward

`persona`, `pain_points[]`, `buying_trigger`, `relevance_score`, `assumptions[]`

## Rules

- `persona` is a name + one-line description (e.g. "Mia — Head of Marketing at a 120-person SaaS scale-up")
- `buying_trigger` describes a specific moment or event, not a general state
- `relevance_score` is 1–10 — how strongly the signals match this persona
- `assumptions` lists anything not confirmed by the source signals
