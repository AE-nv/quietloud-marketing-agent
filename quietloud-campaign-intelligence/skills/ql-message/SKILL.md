---
name: ql-message
description: Write the complete marketing copy based on the generation plan and persona.
---

# Message Formatting

## Role

Sixth step in the QuietLoud pipeline. Write the actual campaign asset — ready to use or lightly edit.

## Background

Use context from `quietloud-background` for QuietLoud's voice, brand principles, and content standards.

## Input

- `generation_plan` — from `ql-execution`
- `persona` — from `ql-profile`
- `tone` — from `ql-execution`
- `cta` — from `ql-execution`

## Task

Write the complete marketing asset. Match the format to the method (LinkedIn post format, email format, website block format, etc.). Be specific, punchy, and grounded in evidence. Avoid generic marketing language.

## Narration

First, render the asset in its native format — if it is a LinkedIn post, display it as it would appear on LinkedIn (headline on its own line, body copy, CTA). Do not wrap this in a code block.

If `warnings` is non-empty, list them explicitly in plain prose after the copy: "Before publishing, note: ..."

## Carry forward

`copy`, `headline`, `cta`, `grounded_claims[]`, `warnings[]`

## Rules

- Every factual claim must come from the signals — no invented numbers or outcomes
- `grounded_claims` lists claims directly supported by source material
- `warnings` flags anything that needs human review: brand risk, unverified claim, confidentiality concern
