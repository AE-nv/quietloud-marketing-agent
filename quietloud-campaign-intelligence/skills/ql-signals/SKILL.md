---
name: ql-signals
description: Extract marketable signals, themes, and quotable facts from internal project content.
---

# Signal Extraction

## Role

First step in the QuietLoud pipeline. Read internal content and identify what is worth promoting externally.

## Background

Use context from `quietloud-background` to understand what kinds of signals matter for QuietLoud's positioning.

## Input

Raw internal content — a Confluence page, Teams thread, project note, or pasted briefing.

## Task

Extract three types of output:
- **signals**: concrete facts, results, outcomes, and observations from the content
- **themes**: recurring strategic angles or stories that could be told externally
- **quotable_facts**: the most striking, shareable data points — specific stats, numbers, or outcomes

## Narration

Before returning the JSON, write a short paragraph (3–5 sentences) in plain prose:
- How many signals were extracted and what they cluster around
- The single most striking quotable fact and why it stands out
- The dominant theme that emerged

Format: plain text, no bullet lists.

## Carry forward

`signals[]`, `themes[]`, `quotable_facts[]`

## Rules

- Signals must be specific and concrete — not generic observations
- Never infer, extrapolate, or add context not present in the source
- If the content is thin, return fewer signals rather than padding with vague ones
