# Start QuietLoud Campaign Workflow

## Trigger

Use this skill when the user wants to turn internal project knowledge into a campaign asset.

Trigger phrases: "start a campaign", "run the QuietLoud workflow", "turn this into a campaign", "generate campaign assets from this", "create a campaign pack".

## What you need from the user

Ask the user to provide at least one of:
- A Confluence page or project delivery note (paste the text)
- A Teams thread or internal discussion (paste or describe it)
- A wiki note or internal briefing

If nothing is provided, use the mock data at:
- `/Users/gilles.lenaerts/codespace/sodastraw/wintercircus/mock-data/confluence-page.md`
- `/Users/gilles.lenaerts/codespace/sodastraw/wintercircus/mock-data/teams-thread.json`
- `/Users/gilles.lenaerts/codespace/sodastraw/wintercircus/mock-data/wiki-note.md`

Combine all provided content into a single `raw_content` string before calling step 1.

## Pipeline — run in this exact sequence

### Step 1 — Signal Extraction
Call tool: `quietloud-signal-extraction__extract_signals`
Input: `{ "raw_content": "<combined input text>" }`
Output: `signals[]`, `themes[]`, `quotable_facts[]`
Show the user: a brief summary of the signals and themes found.

### Step 2 — Audience Reasoning
Call tool: `quietloud-audience-reasoning__reason_audience`
Input: `{ "signals": [...], "themes": [...] }` (from step 1)
Output: `audiences[]`, `recommended_icp`
Show the user: the recommended ICP and why.

### Step 3 — Customer Profile
Call tool: `quietloud-customer-profile__build_profile`
Input: `{ "recommended_icp": "...", "signals": [...] }` (from steps 1–2)
Output: `persona`, `pain_points[]`, `buying_trigger`, `relevance_score`, `assumptions[]`
Show the user: the persona card with pain points and buying trigger.

### Step 4 — Outreach Method
Call tool: `quietloud-outreach-method__select_method`
Input: `{ "persona": "...", "signals": [...] }` (from steps 1, 3)
Output: `method`, `rationale`, `required_sections[]`
Show the user: the recommended method and rationale. Ask for confirmation or let them override.

### Step 5 — Executing Agent
Call tool: `quietloud-executing-agent__plan_execution`
Input: `{ "method": "...", "persona": "...", "signals": [...] }` (from steps 1, 3, 4)
Output: `generation_plan`, `tone`, `cta`, `missing_inputs[]`

### Step 6 — Message + Visual (run together, show results side by side)

#### Step 6a — Message Formatting
Call tool: `quietloud-message-formatting__format_message`
Input: `{ "generation_plan": "...", "persona": "...", "tone": "...", "cta": "..." }` (from steps 3, 5)
Output: `copy`, `headline`, `cta`, `grounded_claims[]`, `warnings[]`

#### Step 6b — Graphical Pipeline
Call tool: `quietloud-graphical-pipeline__generate_visual`
Input: `{ "generation_plan": "...", "persona": "...", "method": "..." }` (from steps 3, 4, 5)
Output: `style_direction`, `layout_notes`, `image_prompt`

### Step 7 — Complete Representation
Call tool: `quietloud-representation__assemble`
Input: all outputs from steps 3, 4, 6a, 6b combined into the full RepresentationInput schema.
Output: `customer_profile`, `selected_method`, `message_asset`, `visual_direction`, `validation_summary`, `human_confirmation_status`

## Final output to show the user

Present the complete representation clearly:

```
CAMPAIGN PACK
─────────────────────────────
Persona:       <persona>
Pain points:   <list>
Buying trigger:<trigger>
Relevance:     <score>/10

Method:        <method>

COPY
Headline: <headline>
---
<copy>
---
CTA: <cta>

VISUAL DIRECTION
Style: <style_direction>
Layout: <layout_notes>
Image prompt: <image_prompt>

VALIDATION
✓ Grounded claims: <list>
⚠ Assumptions: <list>
🔍 Human review required: <list>
🔒 Confidentiality risks: <list>

Status: PENDING HUMAN CONFIRMATION
─────────────────────────────
```

Then ask: "Do you want to approve this campaign pack for export, request edits, or reject it?"

Do NOT export or publish anything until the user explicitly approves.
