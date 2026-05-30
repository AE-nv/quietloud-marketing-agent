---
name: quietloud-start
description: Turn internal project knowledge into a validated campaign pack — personas, copy, visual direction, and human-gated export.
---

# Start QuietLoud Campaign Workflow

## Trigger

Use this skill when the user wants to turn Confluence knowledge into a social campaign post with grounded metrics and generated visuals.

## Data Sources

- Primary source: Atlassian Confluence through MCP configured in `quietloud-campaign-intelligence/.mcp.json`.
- If the user provides no Confluence target, ask for a Confluence page link, title, or query.

## Workflow

1. Retrieve source pages from Confluence.
2. Spawn a `metrics-extractor` sub-agent to extract only explicit, concrete metrics and claims from the source text.
3. Spawn a `metrics-validator` sub-agent to map each metric to source evidence snippets and drop ungrounded claims.
4. Spawn a `post-writer` sub-agent to create a social post draft from validated metrics.
5. Generate image direction and call Codex built-in image generation using the final prompt.
6. Return one final JSON result with post + visual + validation metadata.

## Agent Rules

- Never fabricate numbers, percentages, timelines, or outcomes.
- Do not include client-sensitive names unless they are explicitly present in source text and clearly intended for external use.
- If not enough grounded metrics exist, return a usable post with conservative phrasing and add flags in `review_flags`.

## Output Contract

Return only this JSON shape:

```json
{
  "source_pages": [
    { "id": "string", "title": "string", "url": "string" }
  ],
  "key_metrics": [
    { "metric": "string", "value": "string", "evidence": "string" }
  ],
  "post": {
    "platform": "linkedin",
    "headline": "string",
    "body": "string",
    "cta": "string",
    "hashtags": ["string"]
  },
  "visual": {
    "image_prompt": "string",
    "image_ref": "string"
  },
  "review_flags": ["string"]
}
```

## Completion

- Present the JSON result and a short human-readable summary.
- End by asking whether to refine copy, regenerate the image, or approve for export.
