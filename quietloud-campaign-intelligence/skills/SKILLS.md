# Skills

## Entry point
- `quietloud/` — `/quietloud` — runs the full pipeline start to finish

## Pipeline (called in order by `/quietloud`)
- `ql-signals/` — extract signals and themes from raw content
- `ql-audience/` — identify target audience and recommend ICP
- `ql-profile/` — build customer persona
- `ql-method/` — select outreach method (LinkedIn, email, etc.)
- `ql-execution/` — generate content production plan
- `ql-message/` — write the marketing copy
- `ql-visual/` — visual direction and image prompt
- `ql-assemble/` — combine everything into a campaign pack, gate for human approval

## Context (not a pipeline step)
- `quietloud-background/` — AE/QuietLoud company context, used by all skills for brand voice
