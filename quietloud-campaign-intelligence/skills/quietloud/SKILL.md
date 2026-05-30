---
name: quietloud
description: Full QuietLoud campaign pipeline — from internal knowledge to a validated campaign pack ready for human approval.
---

# QuietLoud Campaign Orchestrator

## Trigger

Use this skill when the user wants to run the full QuietLoud campaign pipeline.

## Input

Before executing the pipeline, ask for which project we want to highlight. This project maybe be:

- A Confluence page (link, title, or pasted text)
- A Teams thread or internal discussion
- A wiki note or project briefing

The user may also ask that you search for a project to highlight. If so, please use available context information (Atlassian, Confluence, etc...) to search through old AE Studio / Quietloud project that can be used as reference and suggest this project before proceding with the pipelie.

Before perform the pipeline, collect information about the suggested project to fill your context

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

After `ql-assemble`, present the complete campaign pack not as JSON, but as a textual explination about your research and ask:

> "Do you want to approve this for export, request edits, or reject it?"

Do not export or publish anything until the user explicitly approves.
