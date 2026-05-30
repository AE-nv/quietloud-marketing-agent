# Wintercircus Hackathon - May 30
**QuietLoud Campaign Intelligence Codex Plugin x Soda Straw**
12h build - 10:00 kickoff - 20:00 demo

---

## What we're building

Codex workflow plugin for QuietLoud.

The user starts a QuietLoud workflow inside Codex. The workflow takes internal project knowledge, such as a Confluence page, mocked Teams thread, wiki note, or pasted briefing. It extracts marketable signals, reasons about the best target audience, selects output formats, generates message assets and representative visuals, assembles a complete campaign representation, and asks for human confirmation before export.

**Track:** AI Agents - automate real workflows

**One-liner:**
> QuietLoud is a Codex workflow plugin that turns internal project knowledge into a validated campaign pack, with specialized workflow agents for audience reasoning, messaging, representative visual generation, and human approval.

---

## Product thesis

QuietLoud already has useful campaign material hidden inside project work, internal discussions, and delivery notes. The hard part is turning that internal knowledge into something an external audience understands and cares about.

This workflow should demonstrate that loop:

```text
Internal knowledge -> signals -> audience/ICP -> selected formats -> message assets + representative visuals -> complete representation -> human confirmation
```

The plugin is not a generic AI copywriter. It is a grounded campaign intelligence workflow inside Codex.

---

## Plugin-first direction

Instead of building a full standalone app first, build QuietLoud as a Codex plugin with a single clear entry point:

```text
Start workflow for QuietLoud
```

That command launches a structured workflow inside Codex and writes the resulting campaign artifacts into the workspace.

The plugin can later grow into a standalone app or connect to a website/CMS, but the hackathon MVP should prove the workflow first.

## Active workflow

1. **Input layer**
   Use pasted content, Confluence sample data, mocked Teams messages, wiki notes, and optional web search enrichment.

2. **Signal extraction**
   Determine what happened, what data exists, what was learned, and what QuietLoud could promote.

3. **Audience and ICP reasoning**
   Identify the targetable audience: internal, external, HR, startups, marketing, CRO, or other specific personas.

4. **Customer profile**
   Produce a persona with pain points, buying trigger, relevance score, and supporting evidence.

5. **Recommended outreach or asset methods**
   The workflow proposes useful formats: snippet, LinkedIn post, email, FAQ, website block, HubSpot note, sales talking points, or visual asset.

6. **User format selection**
   The user makes a multi-select choice of which formats to generate. This is an interactive checkpoint before final generation.

7. **Executing agent**
   Turn the selected formats into a concrete generation plan.

8. **Message formatting**
   Generate the written asset for the deliverable audience: tone, angle, CTA, and structure.

9. **Graphical pipeline**
   Use the generated message, selected bullets, CTA, selected format, and optional reference image to create a visual representative of the asset. For LinkedIn, this should be an attachment image that explains or reinforces the post/text. If image generation is not live, produce the exact image-generation prompt and layout direction.

10. **Complete representation**
   Combine customer profile, selected formats, message assets, visual representative or image prompt, and claim-validation notes.

11. **Human confirmation**
   The user approves, edits, or rejects before export. No automatic publishing in the hackathon MVP.

---

## Workflow roles

These are workflow roles, not necessarily persistent runtime agents:

- **Signal Extraction Agent** - extracts what happened, what was learned, and what can be marketed.
- **ICP Reasoning Agent** - identifies likely audience segments and validates customer-profile fit.
- **Outreach Strategy Agent** - chooses the best method or channel for the campaign representation.
- **Message Formatting Agent** - writes the channel-specific message.
- **Graphical Pipeline Agent** - creates a representative visual attachment or exact image prompt based on the generated message, selected bullets, CTA, and optional reference image.
- **Validation Agent** - separates grounded claims, assumptions, risks, and human-review items.

Important framing:

> The plugin deploys a structured workflow of specialized roles. Image generation is one optional output branch inside the graphical pipeline, not the destination of the full workflow.

## What's already in place

- `QUIETLOUD_IDEA.md` - text brief for the product idea.
- `QUIETLOUD_WORKFLOW.md` - Mermaid workflow matching the current design.
- Initial whiteboard direction for the agent pipeline.

What's not in place yet:

- Plugin scaffold.
- Mock data payloads.
- UI wireframe.
- Concrete agent prompts.
- Source-grounding validator.

---

## Connector and plugin status

| Source or tool | Path | Hackathon status |
|---|---|---|
| Anthropic / Claude | Soda Straw or direct configured environment | Needed for agent reasoning |
| Tavily / web search | Soda Straw web-search straw | Optional enrichment |
| Confluence | Sample export or pasted content | Use mock/sample first |
| Teams | Mock thread | Mock only |
| HubSpot | Future export/enrichment | Skip for MVP |
| LinkedIn | Draft output only | No scraping, no posting |
| Codex image generation | Visual prompt or generated image | Optional, keep mockable |
| QuietLoud website | Preview/export target | Mock export unless already available |

---

## Plugin and Codex strategy

Use a Codex plugin as the main delivery shape. Use external plugins/tools only where they make the demo stronger, but do not make the workflow depend on unclear tooling.

**Soda Straw / plugin layer:**

- Treat external services as replaceable tools behind Soda Straw.
- Use Tavily/web search as the realistic enrichment plugin if available.
- Mock Teams and Confluence unless connectors are already ready.
- Keep HubSpot, LinkedIn, and website publishing as future export targets.

**Codex usage:**

- Use Codex as the runtime surface for starting and running the QuietLoud workflow.
- Use Codex heavily for shaping prompts, generating mock data, and writing output artifacts.
- In the product flow, Codex appears explicitly in the graphical pipeline as optional image generation or image-prompt generation.
- Do not make Codex itself the runtime dependency for every step unless that is the deliberate architecture decision.

**Hackathon position:**

The product should be plugin-first and tool-ready, not integration-blocked. The demo must still work with pasted content and mocks.

---

## Build plan

**Wire demo-able:**

- Codex plugin scaffold or documented plugin entry point.
- `Start workflow for QuietLoud` command/skill.
- Pasted/mock input collection.
- Signal extraction output.
- Audience/ICP reasoning output.
- Customer profile card.
- Outreach method selector/recommendation.
- Executing agent step.
- Message formatting branch.
- Graphical pipeline branch that creates a representative image attachment or exact image prompt.
- Complete representation view.
- Human confirmation gate.

**Mock explicitly:**

- Teams connector.
- Confluence connector if no straw is ready.
- HubSpot enrichment.
- LinkedIn posting.
- QuietLoud website publishing.

**Do not build:**

- LinkedIn scraping.
- Fully automated CRM enrichment.
- Direct publish without human approval.
- Persistent database.
- Broad multi-source ingestion before the main loop works.

---

## Demo story

> "QuietLoud has a project note and some internal discussion. Watch the Codex workflow turn it into a targeted campaign pack."

1. Start the QuietLoud workflow in Codex.
2. Paste or load sample Confluence/project content.
3. Add mocked Teams context.
4. Run signal extraction.
5. Show the target audience reasoning and customer profile.
6. Let the workflow recommend an outreach method.
7. Generate message formatting, then create a representative visual attachment or image prompt based on that message.
8. Show the complete representation:
   - customer profile
   - selected formats
   - LinkedIn or website draft
   - CTA
   - visual representative attachment or image prompt
   - grounded claims
   - human-review warnings
9. Human confirms export.

Soda Straw line:
> "Every external source and credential can be managed through Soda Straw. The workflow can use connected tools without exposing keys in the frontend."

---

## Claude build guardrail

When asking Claude to build, use this constraint:

> Build the QuietLoud Campaign Intelligence Codex workflow plugin only. Use mocked or pasted inputs. Make the visible pipeline match: Start workflow -> Input -> Signal Extraction -> Audience/ICP Reasoning -> Customer Profile -> Recommended Formats -> User Multi-select Format Choice -> Executing Agent -> Message Formatting -> Visual Representative Generation -> Complete Representation -> Human Confirmation. If visual output is selected, generate an attachment image or exact image prompt that explains the selected post/text using the message, bullets, CTA, and optional reference image. Do not implement real LinkedIn, HubSpot, Teams, Confluence, or website publishing unless explicitly asked.
