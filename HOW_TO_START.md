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

That's it. The script:
- Finds the bundled Python 3.12 from Codex (no manual install needed)
- Creates a `.venv` and installs dependencies
- Registers all 8 MCP servers with Codex
- Installs the `quietloud-campaign-intelligence` plugin

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

Codex will ask you for input. You can:
- **Paste** a Confluence page, Teams thread, or wiki note
- **Say nothing** — it will use the built-in mock data from `mock-data/`

---

## 3. What happens next

Codex runs the pipeline step by step:

| Step | What you see |
|---|---|
| Signal Extraction | Summary of marketable signals found in your content |
| Audience Reasoning | Recommended target audience (ICP) |
| Customer Profile | Persona with pain points and buying trigger |
| Outreach Method | Recommended format — you can override |
| Executing Agent | Generation plan (internal, not shown by default) |
| Message + Visual | Draft copy, headline, CTA, and visual direction |
| Complete Pack | Full campaign representation for review |

At the end, Codex asks: **approve, edit, or reject**. Nothing is published until you say yes.

---

## 4. Understand the flow

See [`CODEX_FLOW.md`](./CODEX_FLOW.md) for Mermaid diagrams showing exactly how Codex and the MCP servers interact.

---

## Troubleshooting

**Tools don't appear in Codex**
→ Open a brand new Codex session after running `setup.sh`.

**`setup.sh` fails on Python**
→ Make sure Codex is installed. The script uses Codex's own bundled Python 3.12.

**`./setup.sh` permission denied**
→ Run `chmod +x setup.sh` first.

**Already ran setup, want to re-register**
→ `setup.sh` skips servers that are already registered — safe to re-run.
