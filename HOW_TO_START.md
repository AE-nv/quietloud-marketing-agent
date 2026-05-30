# How to Start — QuietLoud Campaign Intelligence

## Prerequisites

- [OpenAI Codex](https://github.com/openai/codex) installed (`codex --version`)
- Git access to this repo

---

## 1. Clone and install

```bash
git clone https://github.com/AE-nv/quietloud-marketing-agent
cd quietloud-marketing-agent
./setup.sh
```

The script registers the plugin marketplace and installs `quietloud-campaign-intelligence`. No Python, no API keys, no manual configuration.

---

## 2. Run it

**From the terminal** — opens a new Codex session with the prompt pre-loaded:

```bash
codex "start a quietloud campaign"
```

**From inside a running Codex session** — use the slash command:

```
/quietloud
```

Codex will ask which project to highlight. You can:
- **Paste** a Confluence page, Teams thread, or wiki note
- **Ask Codex to search** — it will query Confluence via Atlassian MCP and suggest a project
- **Say nothing** — it will use the built-in mock data from `mock-data/`

---

## 3. What happens next

Codex runs the pipeline step by step, narrating each stage as it goes:

| Step | What you see |
|---|---|
| Signal Extraction | Plain-prose summary of signals, themes, and the most striking fact |
| Audience Reasoning | Which audiences surfaced and why the recommended ICP was chosen |
| Customer Profile | Persona introduction with pain points and buying trigger |
| Method Selection | One sentence — chosen format and why it fits |
| Content Brief | Angle and key proof point for the asset |
| Copy Writing | The asset rendered in its native format (LinkedIn post, email, etc.) |
| Visual Direction | Designer brief — colour mood, layout, image prompt |
| Assembly | Full campaign pack as plain text |

At the end, Codex asks: **approve, edit, or reject**. Nothing is published until you say yes. If you request edits, Codex re-runs from the relevant step — not from the beginning.

---

## 4. Understand the flow

See [`CODEX_FLOW.md`](./CODEX_FLOW.md) for Mermaid diagrams.
See [`quietloud-campaign-intelligence/skills/SKILLS.md`](./quietloud-campaign-intelligence/skills/SKILLS.md) for the skill map.

---

## Troubleshooting

**Tools don't appear in Codex**
→ Open a brand new Codex session after running `setup.sh`.

**`./setup.sh` permission denied**
→ Run `chmod +x setup.sh` first.

**Already ran setup, want to reinstall**
→ `setup.sh` is safe to re-run — it skips already-registered items.

**Codex can't find Confluence pages**
→ Make sure Atlassian OAuth is authorised. Run `/quietloud` and follow the authentication prompt if it appears.
