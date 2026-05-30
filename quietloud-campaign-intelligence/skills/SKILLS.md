# Skills

## Entry point
- `quietloud/` — `/quietloud` — runs the full pipeline start to finish

## Pipeline (called in order by `/quietloud`)
- `relevancy-filter/` — score and rank content on 5 dimensions (market timeliness, audience fit, AE credibility, freshness, distinctiveness). Drop below 12/25.
- `ql-signals/` — extract signals, themes, quotable facts from top-ranked content
- `ql-audience/` — identify target audiences, recommend one ICP
- `ql-profile/` — build customer persona
- `channel-selector/` — route to channels (primary/secondary/skip), confirm with user
- `output-linkedin/` — draft LinkedIn post, delegates voice to ae-linkedin-post
- `output-website-blog/` — draft 500-900 word blog in AE register
- `output-internal-teams/` — draft internal Teams/Newsflash, Dutch-friendly
- `output-youtube-video/` — produce video package (not copy)
- `ql-visual/` — visual direction and image prompt (linkedin + website-blog only)
- `ql-assemble/` — combine everything, human approval gate

## Context (not a pipeline step)
- `quietloud-background/` — AE/QuietLoud company context, used by all skills for brand voice
