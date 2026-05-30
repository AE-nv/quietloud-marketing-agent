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

1. Run ql-signals — extract signals, themes, quotable facts
2. Run ql-audience — identify audiences, pick one ICP
3. Run ql-profile — build persona from ICP and signals
4. Run ql-method — pick outreach format
5. Run ql-execution — write the content brief
6. Run ql-message — write the campaign copy
7. Run ql-visual — write visual direction and image prompt
8. Run ql-assemble — combine everything into the campaign pack

Present the final pack as plain readable text, not JSON. Ask: "Approve for export, request edits, or reject?" Do not export until the user explicitly approves.
