# QuietLoud Campaign Intelligence - Idea Brief

## One-liner

QuietLoud is a Codex workflow plugin that turns internal project knowledge into a validated campaign pack, with specialized workflow agents for audience reasoning, messaging, representative visual generation, and human approval.

## Current Direction

The plugin helps QuietLoud move from scattered internal knowledge to targeted marketing output from inside Codex. It reads inputs such as Confluence pages, mocked Teams discussions, wiki notes, project descriptions, pasted briefs, and optional web search results.

From those inputs, it starts a structured workflow, extracts useful signals, identifies who the story is relevant for, selects the right output formats, generates message assets and representative visuals, and assembles a complete representation for human confirmation.

The core point is not generic AI copywriting. The core point is grounded campaign intelligence: the plugin uses existing company knowledge to decide what is worth promoting, who should care, how to reach them, and what the final campaign asset should look like.

## Plugin-First Thesis

The first version should not be a full standalone app. It should be a Codex workflow plugin with a clear entry point:

```text
Start workflow for QuietLoud
```

That entry point launches a structured campaign workflow inside Codex and writes the output artifacts into the workspace. This keeps the MVP focused on the actual intelligence loop instead of spending hackathon time on generic app scaffolding.

The plugin can still use Soda Straw and external tools where available, but the workflow must work with pasted content and mocks.

## Problem

Useful marketing material already exists inside internal conversations and project documentation, but it is not shaped for external audiences. Teams often know what was built, learned, or delivered, but turning that into a targeted campaign takes manual interpretation:

- finding relevant source material
- understanding what actually happened
- deciding which audience should care
- translating internal language into external messaging
- choosing the right channel or asset type
- creating visual and copy direction
- validating that claims are true and safe to publish
- getting human approval before anything leaves the company

## Target Users

Primary users:

- QuietLoud marketing team
- growth or campaign owners
- consultants who want to turn project work into marketable proof

Future users:

- sales teams enriching HubSpot or CRM records
- account teams preparing targeted outreach
- leadership teams reviewing campaign opportunities

## Main Inputs

MVP inputs:

- pasted Confluence or project content
- mocked Teams threads
- wiki or internal notes
- optional web search enrichment

Future inputs:

- live Confluence connector
- live Teams connector
- HubSpot or CRM data
- LinkedIn signals
- QuietLoud website CMS

## Core Workflow

1. **Start workflow**
   Launch the QuietLoud workflow from Codex.

2. **Input layer**
   Collect internal knowledge from pasted content, Confluence samples, mocked Teams threads, wiki notes, or optional search.

3. **Signal extraction**
   Identify what happened, what data exists, what was learned, what was built, and what QuietLoud could do with it.

4. **Audience and ICP reasoning**
   Determine who the content is relevant for, such as internal teams, external prospects, HR, startups, marketing teams, CROs, or another specific audience.

5. **Customer profile**
   Create a persona with pain points, buying triggers, relevance score, evidence, and missing assumptions.

6. **Recommended outreach or asset methods**
   Recommend which formats fit the opportunity and audience:
   - snippet
   - LinkedIn draft
   - email
   - FAQ
   - website block
   - HubSpot note
   - sales talking points
   - visual asset

7. **User format selection**
   Ask the user to choose one or more formats to generate. This must support multi-select, because one campaign opportunity can produce multiple useful assets.

8. **Executing agent**
   Convert the selected formats into a concrete generation plan, including required sections, tone, CTA, proof points, and missing inputs.

9. **Message formatting**
   Generate the written asset for the deliverable audience.

10. **Visual representative generation**
   Use the generated message, selected bullets, CTA, selected format, and optional reference image to create a representative visual attachment or exact image-generation prompt. For LinkedIn, this means an attachment image that explains or reinforces the post/text.

11. **Complete representation**
   Combine the profile, selected formats, message assets, visual representative or image prompt, CTA, and validation notes into one reviewable output.

12. **Human confirmation**
   The user approves, edits, or rejects the representation. This is the final gate before export.

13. **Export**
   Export to a website preview, LinkedIn draft, HubSpot note, or campaign handoff. In the hackathon MVP, export can be mocked.

## Workflow Roles

These are specialized workflow roles. They do not need to be persistent autonomous subagents for the MVP.

- **Signal Extraction Agent** extracts what happened, what was learned, and what can be marketed.
- **ICP Reasoning Agent** identifies likely audience segments and validates customer-profile fit.
- **Outreach Strategy Agent** chooses the best method or channel for the campaign representation.
- **Message Formatting Agent** writes the channel-specific message.
- **Graphical Pipeline Agent** creates a representative visual attachment or exact image prompt based on the generated message, selected bullets, CTA, and optional reference image.
- **Validation Agent** separates grounded claims, assumptions, risks, and human-review items.

Important framing:

> The plugin deploys a structured workflow of specialized roles. Image generation is one optional output branch inside the graphical pipeline, not the destination of the full workflow. When selected, the image must represent the final message, not decorate it generically.

## Hackathon MVP

Recommended MVP:

> Codex workflow plugin from pasted or sample Confluence/project knowledge plus mocked Teams context to a complete campaign representation.

The demo should focus on a narrow but complete loop:

1. Start workflow for QuietLoud in Codex.
2. Load sample internal content.
3. Extract signals.
4. Generate target customer profiles.
5. Select or recommend the best audience.
6. Show recommended outreach or asset formats.
7. Let the user multi-select formats to generate:
   - outreach snippet
   - mailing/email
   - FAQ
   - website block
   - LinkedIn draft
   - visual asset
8. Run the executing agent.
9. Generate message formatting.
10. Generate a representative visual attachment or image prompt from the message, bullets, CTA, and optional reference image.
11. Show the complete representation:
   - customer profile
   - selected formats
   - LinkedIn draft, website block, email, FAQ, or selected assets
   - CTA
   - visual representative attachment or image prompt
   - grounded claims
   - unsupported assumptions
   - human-review warnings
12. Confirm export.

## Validation Definition

For the MVP, validation means the output clearly separates:

- claims grounded in the source input
- assumptions inferred by the model
- claims that need human confirmation
- possible confidentiality risks
- brand or tone risks

Validation does not mean fully automated legal, brand, or publishing approval.

## Viability Notes

Most viable for hackathon:

- Use pasted or sample Confluence/project knowledge.
- Mock Teams if no connector is ready.
- Use web search only as enrichment.
- Keep HubSpot, LinkedIn, and website publishing as export destinations or future integrations.

Less viable for first version:

- LinkedIn scraping as a primary input
- fully automated CRM enrichment
- direct publishing without human approval
- broad multi-source ingestion before the main loop works
- real image generation as a dependency for the demo

## Plugin and Codex Strategy

There is a difference between the product being a Codex plugin and the demo being blocked on external plugins.

For the MVP, the Codex workflow should present external data sources as tool/plugin slots:

- Confluence/project source
- Teams context
- Tavily or web search enrichment
- HubSpot enrichment/export
- LinkedIn draft/export
- QuietLoud website preview/export

Only the sources that are actually ready should be live. Everything else should be mocked clearly.

Codex should be used in three ways:

- **Runtime surface:** start and run the QuietLoud workflow.
- **Build-time:** help generate sample data, prompts, workflow docs, and validation rules.
- **Product-flow:** support the graphical pipeline with image generation or image-prompt generation.

Do not frame the first version as "Codex does everything." That is too vague. The sharper architecture is:

> The Codex plugin orchestrates specialized workflow steps. Codex is the workflow surface and can power the visual generation step, while Soda Straw provides controlled access to external tools.

## Product Positioning

Position this as a campaign intelligence assistant, not a copy generator.

Good framing:

> "Start a QuietLoud workflow in Codex and turn internal project knowledge into a validated campaign representation."

Avoid framing it as:

> "AI writes marketing posts automatically."

The stronger story is that the workflow helps QuietLoud discover reusable marketing value inside work that already happened, then package it for the right audience with human validation.

## Claude Build Guardrails

When asking Claude to build, use these constraints:

- Build the QuietLoud Campaign Intelligence Codex workflow plugin only.
- Do not build or reference any other product direction.
- Use mocked or pasted inputs.
- Make the visible pipeline match the workflow in `QUIETLOUD_WORKFLOW.md`.
- Include an interactive multi-select checkpoint where the user chooses which formats to generate: outreach, mailing/email, FAQ, website block, LinkedIn draft, visual asset, or other selected formats.
- Do not implement real LinkedIn, HubSpot, Teams, Confluence, or website publishing unless explicitly asked.
- Do not hide validation inside a generic "done" state; show grounded claims, assumptions, and human-review warnings.

## Open Questions

- What exact sample content should be used for the demo?
- Which three audience categories should be available first?
- Should the first output be a LinkedIn draft, a website block, or a campaign pack?
- Should Codex image generation produce a real image, or only a prompt/style direction?
- What should the human confirmation export button do in the mock?
