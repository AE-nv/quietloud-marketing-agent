---
name: ql-assemble
description: Assemble all pipeline outputs into a complete validated campaign pack ready for human approval.
---

# Complete Representation

## Role

Final step in the QuietLoud pipeline. Combine all prior outputs into one reviewable campaign pack with a clear validation summary.

## Input

All outputs from prior skills:
- `persona`, `pain_points`, `buying_trigger`, `relevance_score` — from `ql-profile`
- `method` — from `ql-method`
- `copy`, `headline`, `cta`, `grounded_claims`, `warnings` — from `ql-message`
- `style_direction`, `layout_notes`, `image_prompt` — from `ql-visual`

## Task

Assemble the complete campaign pack and produce a validation summary that clearly separates grounded claims from assumptions and flags what needs human review.

## Output

```json
{
  "customer_profile": {
    "persona": "string",
    "pain_points": ["string"],
    "buying_trigger": "string",
    "relevance_score": 8
  },
  "selected_method": "string",
  "message_asset": {
    "headline": "string",
    "copy": "string",
    "cta": "string"
  },
  "visual_direction": {
    "style_direction": "string",
    "layout_notes": "string",
    "image_prompt": "string"
  },
  "validation_summary": {
    "grounded_claims": ["string"],
    "unverified_assumptions": ["string"],
    "human_review_required": ["string"],
    "confidentiality_risks": ["string"]
  },
  "human_confirmation_status": "pending"
}
```

## Rules

- Always set `human_confirmation_status` to `"pending"` — never `"approved"`
- A human must explicitly approve before anything is exported or published
- The validation summary must be honest — do not bury warnings
