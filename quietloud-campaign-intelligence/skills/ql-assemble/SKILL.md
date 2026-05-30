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

## Narration

Render the complete campaign pack as a readable document in this order — not as JSON:

1. **Persona** — name, pain point summary, buying trigger, relevance score
2. **Selected method** — one line
3. **Asset** — headline and copy in native format
4. **Visual direction** — one descriptive sentence
5. **Grounded claims** — bullet list of claims backed by source material
6. **Needs review** — clearly labelled section for warnings, unverified assumptions, and confidentiality risks

End with the human gate question: "Approve for export, request edits, or reject?"

## Carry forward

Nothing — this is the terminal step. Output goes to the human.

## Rules

- A human must explicitly approve before anything is exported or published
- The validation summary must be honest — do not bury warnings
