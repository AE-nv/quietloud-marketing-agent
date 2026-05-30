# QuietLoud Campaign Intelligence — How It Runs in Codex

## Full Pipeline Flow

```mermaid
sequenceDiagram
    actor User
    participant Codex as Codex (GPT model)
    participant Tool as MCP Tool
    participant Server as MCP Server (Python)

    User->>Codex: "Start a QuietLoud campaign workflow"
    Codex->>Codex: Loads SKILL.md — knows the pipeline

    Note over Codex,Server: Step 1 — Signal Extraction
    Codex->>Server: extract_signals({ raw_content })
    Server-->>Codex: { system_prompt, user_content, output_schema }
    Codex->>Codex: Generates → { signals[], themes[], quotable_facts[] }

    Note over Codex,Server: Step 2 — Audience Reasoning
    Codex->>Server: reason_audience({ signals, themes })
    Server-->>Codex: { system_prompt, user_content, output_schema }
    Codex->>Codex: Generates → { audiences[], recommended_icp }

    Note over Codex,Server: Step 3 — Customer Profile
    Codex->>Server: build_profile({ recommended_icp, signals })
    Server-->>Codex: { system_prompt, user_content, output_schema }
    Codex->>Codex: Generates → { persona, pain_points[], buying_trigger, relevance_score }

    Note over Codex,Server: Step 4 — Outreach Method
    Codex->>Server: select_method({ persona, signals })
    Server-->>Codex: { system_prompt, user_content, output_schema }
    Codex->>Codex: Generates → { method, rationale, required_sections[] }
    Codex-->>User: Shows recommendation — user can confirm or override

    Note over Codex,Server: Step 5 — Executing Agent
    Codex->>Server: plan_execution({ method, persona, signals })
    Server-->>Codex: { system_prompt, user_content, output_schema }
    Codex->>Codex: Generates → { generation_plan, tone, cta }

    Note over Codex,Server: Step 6 — Message + Visual (parallel)
    Codex->>Server: format_message({ generation_plan, persona, tone, cta })
    Server-->>Codex: { system_prompt, user_content, output_schema }
    Codex->>Codex: Generates → { copy, headline, cta, grounded_claims[], warnings[] }

    Codex->>Server: generate_visual({ generation_plan, persona, method })
    Server-->>Codex: { system_prompt, user_content, output_schema }
    Codex->>Codex: Generates → { style_direction, layout_notes, image_prompt }

    Note over Codex,Server: Step 7 — Complete Representation
    Codex->>Server: assemble({ all prior outputs })
    Server-->>Codex: { system_prompt, user_content, output_schema }
    Codex->>Codex: Generates → complete campaign pack

    Codex-->>User: Shows full campaign pack
    User->>Codex: Approves / edits / rejects
```

---

## What Each MCP Server Actually Does

```mermaid
flowchart LR
    A[Codex calls tool\nwith structured input] --> B[MCP Server\nvalidates input\nassembles prompt]
    B --> C["Returns prompt package\n{ system_prompt\n  user_content\n  output_schema }"]
    C --> D[Codex reasons\nover the package]
    D --> E[Codex generates\nJSON output]
    E --> F[Output flows\nto next step]
```

> The MCP servers are **prompt assemblers**, not AI agents. No API key needed — all reasoning happens inside Codex.

---

## Install Once, Use Forever

```mermaid
flowchart TD
    A[git clone] --> B[./setup.sh]
    B --> C[Creates .venv\nInstalls mcp + pydantic]
    C --> D[Registers 8 MCP servers\nwith Codex]
    D --> E[Installs\nquietloud-campaign-intelligence\nplugin]
    E --> F[Open new Codex session]
    F --> G["Say: Start a QuietLoud campaign workflow"]
```
