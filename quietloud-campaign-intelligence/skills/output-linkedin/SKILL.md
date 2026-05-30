---
name: ql-output-linkedin
description: Draft a LinkedIn post from the selected content. Delegates voice rules to ae-linkedin-post.
---

You have: top_item, persona, signals, and channel_routing from prior steps.

Turn the content into a LinkedIn post brief: identify the post type (insight, story, data, question), the hook, the key proof point, and the CTA. Then apply the voice, format, and hashtag rules from the `ae-linkedin-post` skill to produce the draft.

Display the post as it would appear on LinkedIn — hook on its own line, body, CTA, hashtags. Do not wrap in a code block.

Flag any claim not directly supported by the source signals: "Before publishing, note: ..."

Carry forward: linkedin_draft, grounded_claims, warnings.
Rule: return draft copy only. Never post.
