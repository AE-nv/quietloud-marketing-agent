---
name: quietloud
description: Run the QuietLoud campaign pipeline on mock project data.
---

Read these three files as your source before starting:
- mock-data/confluence-page.md
- mock-data/teams-thread.json
- mock-data/wiki-note.md

QuietLoud context: QuietLoud is a digital product and marketing agency (formerly AE Studio). They help Belgian B2B scale-ups build demand and brand presence. Voice: direct, evidence-led, peer-to-peer. Never generic marketing language.

Run each step in sequence. Announce "Step N of 8 — [name]" before each one. After each step, share what you found in 2-4 plain sentences. Never move to the next step silently.

1. Run ql-relevancy-filter — score and rank the content, drop below 12/25
2. Run ql-signals — extract signals, themes, quotable facts from the top-ranked item
3. Run ql-audience — identify audiences, pick one ICP
4. Run ql-profile — build persona from ICP and signals
5. Run ql-channel-selector — route to channels (primary/secondary/skip), confirm with user before continuing
6. Run the output skill for the confirmed primary channel: ql-output-linkedin, ql-output-website-blog, ql-output-internal-teams, or ql-output-youtube-video
7. Run ql-visual — visual direction (skip if primary channel is internal-teams or youtube-video)
8. Run ql-assemble — combine everything into the campaign pack

Present the final pack as plain readable text. Ask: "Approve for export, request edits, or reject?" Do not export until the user explicitly approves.
