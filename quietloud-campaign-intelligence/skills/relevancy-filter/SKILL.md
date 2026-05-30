---
name: ql-relevancy-filter
description: Score and rank content items before drafting. Drops anything below 12/25.
---

You have: the raw content items passed from the orchestrator.

Score each item on five dimensions (1–5 each):
- **Market timeliness** — is this topic live in the market right now? Use web search to check if needed.
- **Audience fit** — does it speak to QuietLoud's target audiences?
- **AE credibility** — does AE have genuine authority on this topic?
- **Freshness** — is this genuinely new or already well-covered internally?
- **Distinctiveness** — does it say something the market hasn't heard?

Sum to a score out of 25. Drop anything below 12. Return the ranked shortlist with a score and one-line "why now" per item.

Write 2-3 sentences: what scored highest and why, and what (if anything) was dropped.

Carry forward: ranked_content, top_item, why_now.
Rule: do not draft any copy — only decide what's worth publishing and in what order.
