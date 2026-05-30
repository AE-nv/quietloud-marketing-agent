---
name: ql-method
description: Select the best outreach or asset method for the campaign based on persona and signals.
---

# Outreach Method

## Role

Fourth step in the QuietLoud pipeline. Choose the single best format for the campaign asset.

## Background

Use context from `quietloud-background` to align with QuietLoud's content strategy and channels.

## Input

- `persona` — from `ql-profile`
- `signals[]` — from `ql-signals`

## Task

Choose the method that best matches the persona's context and the nature of the signals.

Available methods: `linkedin_post`, `email`, `website_block`, `faq`, `snippet`, `hubspot_note`, `sales_talking_points`

## Output

```json
{
  "method": "linkedin_post",
  "rationale": "string",
  "required_sections": ["string"]
}
```

## Rules

- Choose one method — do not hedge with multiple options
- `rationale` explains specifically why this method fits this persona and these signals
- `required_sections` lists the structural parts the asset needs (e.g. hook, proof point, CTA)
