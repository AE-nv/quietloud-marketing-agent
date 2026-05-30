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

Run each skill in sequence. Before invoking each skill, announce the step to the user in plain prose ("Step N of 8 — [what you are about to do]"). After each skill returns, summarise what was found or decided in 2–4 plain-prose sentences before invoking the next step. Never move to the next step in silence.

### Step 1 — Signal Extraction

Announce: "Extracting signals, themes, and quotable facts from the source content."

Invoke `ql-signals`.

After it returns, tell the user:
- How many signals were found and what they cluster around
- The single most striking quotable fact
- The dominant theme

Then carry `signals[]`, `themes[]`, and `quotable_facts[]` forward.

### Step 2 — Audience Identification

Announce: "Identifying target audiences and selecting the best ICP."

Invoke `ql-audience` with `signals[]` and `themes[]`.

After it returns, tell the user:
- Which audience segments surfaced
- Which ICP was recommended and the one signal that drove that choice

Then carry `recommended_icp` forward.

### Step 3 — Persona Building

Announce: "Building a customer persona for the recommended ICP."

Invoke `ql-profile` with `recommended_icp` and `signals[]`.

After it returns, introduce the persona in plain prose:
- Who they are and why the signals point to this person
- The buying trigger in plain language
- The key assumption made and your confidence level

Then carry `persona`, `pain_points`, `buying_trigger`, `relevance_score`, and `assumptions[]` forward.

### Step 4 — Method Selection

Announce: "Selecting the best outreach format for this persona."

Invoke `ql-method` with `persona` and `signals[]`.

After it returns, state in one sentence the chosen method and the specific reason it fits this persona. Surface the required sections briefly.

Then carry `method` and `required_sections[]` forward.

### Step 5 — Content Brief

Announce: "Building the content generation plan."

Invoke `ql-execution` with `method`, `persona`, and `signals[]`.

After it returns, tell the user:
- The angle the asset will open with and why
- The key proof point that will carry the most weight
- Any missing inputs that would improve the output

Then carry `generation_plan`, `tone`, `cta`, and `missing_inputs[]` forward.

### Step 6 — Copy Writing

Announce: "Writing the campaign copy."

Invoke `ql-message` with `generation_plan`, `persona`, `tone`, and `cta`.

After it returns, render the asset in its native format — do NOT wrap it in JSON or a code block. If it is a LinkedIn post, display it as it would appear. If it is an email, show subject line and body.

If `warnings` is non-empty, list them explicitly in plain prose immediately after the copy: "Before publishing, note: ..."

Then carry `copy`, `headline`, `cta`, `grounded_claims[]`, and `warnings[]` forward.

### Step 7 — Visual Direction

Announce: "Generating visual direction."

Invoke `ql-visual` with `generation_plan`, `persona`, and `method`.

After it returns, describe the visual concept in 2 sentences as if briefing a designer verbally — colour mood, what is in the frame, what it should make the viewer feel.

Then carry `style_direction`, `layout_notes`, and `image_prompt` forward.

### Step 8 — Assembly

Announce: "Assembling the complete campaign pack."

Invoke `ql-assemble` with all prior outputs.

After it returns, render the complete campaign pack as a readable document — not as JSON:

1. **Persona** — name, pain point summary, buying trigger, relevance score
2. **Selected method** — one line
3. **Asset** — headline and copy in native format
4. **Visual direction** — one descriptive sentence
5. **Grounded claims** — bullet list of claims backed by source material
6. **Needs review** — clearly labelled section for warnings, unverified assumptions, and confidentiality risks

## Human Gate

After `ql-assemble`, present the complete campaign pack not as JSON but as a plain-text explanation of your research and findings, then ask:

> "Do you want to approve this for export, request edits, or reject it?"

Do not export or publish anything until the user explicitly approves. If they request edits, identify which step produced the content to change and re-run from that step forward, not from the beginning.
