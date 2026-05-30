---
name: quietloud
description: Full QuietLoud campaign pipeline — from internal knowledge to a validated campaign pack ready for human approval.
---

# QuietLoud Campaign Orchestrator

## Trigger

Use this skill when the user wants to run the full QuietLoud campaign pipeline.

## Input

Ask the user for source content:
- A Confluence page (link, title, or pasted text)
- A Teams thread or internal discussion
- A wiki note or project briefing

If nothing is provided, use the mock data in `mock-data/`.

## Pipeline

Run each skill in sequence, passing output forward as input to the next.

1. Invoke `ql-signals` — extract signals, themes, and quotable facts from the source content
2. Invoke `ql-audience` — identify target audiences and recommend the best ICP
3. Invoke `ql-profile` — build a customer persona from the ICP and signals
4. Invoke `ql-method` — select the best outreach method for the persona
5. Invoke `ql-execution` — generate a content production plan
6. Invoke `ql-message` — write the marketing copy
7. Invoke `ql-visual` — generate visual direction and image prompt
8. Invoke `ql-assemble` — combine all outputs into a complete campaign pack

After each step, carry the relevant output fields forward. Do not repeat work already done by a previous skill.

## Human Gate

After `ql-assemble`, present the complete campaign pack and ask:

> "Do you want to approve this for export, request edits, or reject it?"

Do not export or publish anything until the user explicitly approves.
