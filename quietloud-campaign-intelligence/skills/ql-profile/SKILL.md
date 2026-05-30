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

## Output

```json
{
  "persona": "string",
  "pain_points": ["string"],
  "buying_trigger": "string",
  "relevance_score": 8,
  "assumptions": ["string"]
}
```

## Rules

- `persona` is a name + one-line description (e.g. "Mia — Head of Marketing at a 120-person SaaS scale-up")
- `buying_trigger` describes a specific moment or event, not a general state
- `relevance_score` is 1–10 — how strongly the signals match this persona
- `assumptions` lists anything not confirmed by the source signals
