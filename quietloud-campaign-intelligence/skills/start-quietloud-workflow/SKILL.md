---
name: quietloud
description: Turn internal project knowledge into a validated campaign pack — personas, copy, visual direction, and human-gated export.
---

# Start QuietLoud Campaign Workflow

## Trigger

Use this skill when the user wants to turn internal project knowledge into a campaign asset.

Trigger phrases: "start a campaign", "run the QuietLoud workflow", "turn this into a campaign", "generate campaign assets from this", "create a campaign pack".

## What you need from the user

Ask the user to provide at least one of:
- A Confluence page or project delivery note (paste the text)
- A Teams thread or internal discussion (paste or describe it)
- A wiki note or internal briefing

If nothing is provided, read and combine these mock files:
- `mock-data/confluence-page.md`
- `mock-data/teams-thread.json`
- `mock-data/wiki-note.md`

Combine all provided content into a single string before calling step 1.

## How tool calls work in this pipeline

Every tool in this pipeline returns a **prompt package** — not a final answer. The package looks like:
```json
{
  "system_prompt": "...",
  "user_content": "...",
  "output_schema": { ... }
}
```

For each step:
1. Call the tool with the required inputs
2. Receive the prompt package
3. **You generate the output**: follow `system_prompt`, process `user_content`, produce a JSON response that matches `output_schema` exactly
4. Parse that JSON as this step's result and pass the relevant fields as inputs to the next tool

Return only valid JSON. Do not wrap in markdown fences. Do not add extra fields.

---

## Pipeline

### Step 1 — Signal Extraction
Tool: `quietloud-signal-extraction__extract_signals`
Input: `{ "raw_content": "<combined input text>" }`
You generate: `{ "signals": [...], "themes": [...], "quotable_facts": [...] }`
Show the user: a brief summary of signals and themes found.

### Step 2 — Audience Reasoning
Tool: `quietloud-audience-reasoning__reason_audience`
Input: `{ "signals": [...], "themes": [...] }` (from step 1)
You generate: `{ "audiences": [...], "recommended_icp": "..." }`
Show the user: the recommended ICP and why.

### Step 3 — Customer Profile
Tool: `quietloud-customer-profile__build_profile`
Input: `{ "recommended_icp": "...", "signals": [...] }` (from steps 1–2)
You generate: `{ "persona": "...", "pain_points": [...], "buying_trigger": "...", "relevance_score": N, "assumptions": [...] }`
Show the user: the persona card.

### Step 4 — Outreach Method
Tool: `quietloud-outreach-method__select_method`
Input: `{ "persona": "...", "signals": [...] }` (from steps 1, 3)
You generate: `{ "method": "...", "rationale": "...", "required_sections": [...] }`
Show the user: recommended method + rationale. Let them confirm or override.

### Step 5 — Executing Agent
Tool: `quietloud-executing-agent__plan_execution`
Input: `{ "method": "...", "persona": "...", "signals": [...] }` (from steps 1, 3, 4)
You generate: `{ "generation_plan": "...", "tone": "...", "cta": "...", "missing_inputs": [...] }`

### Step 6 — Message + Visual (call both tools, generate both outputs)

#### Step 6a — Message Formatting
Tool: `quietloud-message-formatting__format_message`
Input: `{ "generation_plan": "...", "persona": "...", "tone": "...", "cta": "..." }` (from steps 3, 5)
You generate: `{ "copy": "...", "headline": "...", "cta": "...", "grounded_claims": [...], "warnings": [...] }`

#### Step 6b — Graphical Pipeline
Tool: `quietloud-graphical-pipeline__generate_visual`
Input: `{ "generation_plan": "...", "persona": "...", "method": "..." }` (from steps 3, 4, 5)
You generate: `{ "style_direction": "...", "layout_notes": "...", "image_prompt": "..." }`

### Step 7 — Complete Representation
Tool: `quietloud-representation__assemble`
Input: all outputs from steps 3, 4, 6a, 6b combined.
You generate: the full RepresentationOutput schema with `human_confirmation_status: "pending"`.

---

## Final output

Present the complete representation:

```
CAMPAIGN PACK
─────────────────────────────
Persona:        <persona>
Pain points:    <list>
Buying trigger: <trigger>
Relevance:      <score>/10

Method:         <method>

COPY
Headline: <headline>
---
<copy>
---
CTA: <cta>

VISUAL DIRECTION
Style:        <style_direction>
Layout:       <layout_notes>
Image prompt: <image_prompt>

VALIDATION
✓ Grounded claims:         <list>
⚠ Assumptions:             <list>
🔍 Human review required:  <list>
🔒 Confidentiality risks:  <list>

Status: PENDING HUMAN CONFIRMATION
─────────────────────────────
```

Ask: "Do you want to approve this campaign pack for export, request edits, or reject it?"

Do NOT export or publish anything until the user explicitly approves.
