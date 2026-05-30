---
name: ql-channel-selector
description: Route selected content to the right output channels. Returns primary/secondary/skip with rationale.
---

You have: persona, signals, and top_item from prior steps.

Enabled channels: `linkedin`, `website-blog`, `internal-teams`, `youtube-video`.

For each enabled channel, judge: **primary**, **secondary**, or **skip** — based on audience match, format match, and effort/payoff. Give one-line rationale for each.

Present the recommendation clearly and ask: "Confirm this channel routing, or adjust?"
Do not proceed to any output skill until the user confirms.

Carry forward: channel_routing (primary channel + secondary channels).
Rule: only choose from enabled channels. Never invent new ones.
