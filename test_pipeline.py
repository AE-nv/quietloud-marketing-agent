"""
Quick smoke test — runs each MCP server tool directly and verifies
it returns a valid prompt package. No Codex, no API keys needed.
"""
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Load mock data
ROOT = Path(__file__).parent
confluence = (ROOT / "mock-data/confluence-page.md").read_text()
teams = json.loads((ROOT / "mock-data/teams-thread.json").read_text())
wiki = (ROOT / "mock-data/wiki-note.md").read_text()
RAW = f"{confluence}\n\n---\n\n{wiki}\n\n---\n\n" + "\n".join(
    f"{m['author']}: {m['text']}" for m in teams["messages"]
)

def check_package(name, result):
    pkg = json.loads(result[0].text)
    assert "system_prompt" in pkg, f"{name}: missing system_prompt"
    assert "user_content" in pkg, f"{name}: missing user_content"
    assert "output_schema" in pkg, f"{name}: missing output_schema"
    print(f"  OK  {name}")
    print(f"      system_prompt: {len(pkg['system_prompt'])} chars")
    print(f"      user_content:  {len(pkg['user_content'])} chars")
    print(f"      output_schema: {list(pkg['output_schema'].get('properties', {}).keys())}")
    return pkg

# Direct import workaround (hyphens in directory names)
import importlib.util

def load_server(name):
    path = ROOT / "mcp-servers" / name / "server.py"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

async def run():
    print("\n=== QuietLoud pipeline smoke test ===\n")

    # Step 1
    m = load_server("signal-extraction")
    r = await m.call_tool("extract_signals", {"raw_content": RAW})
    pkg1 = check_package("signal-extraction", r)
    # Simulate Codex output for downstream steps
    signals = ["67 MQLs vs 40 target", "140 webinar registrants vs 80 target",
               "Founder-led LinkedIn outperformed paid 3:1", "420 checklist downloads",
               "Belgian B2B SaaS scale-up, demand gen playbook proven"]
    themes = ["zero-to-pipeline playbook", "founder-led content", "diagnostic asset as lead magnet"]

    # Step 2
    m = load_server("audience-reasoning")
    r = await m.call_tool("reason_audience", {"signals": signals, "themes": themes})
    pkg2 = check_package("audience-reasoning", r)
    recommended_icp = "CMO or founder-as-CMO at Belgian B2B SaaS scale-up (30-200 employees) with strong product but no inbound"

    # Step 3
    m = load_server("customer-profile")
    r = await m.call_tool("build_profile", {"recommended_icp": recommended_icp, "signals": signals})
    pkg3 = check_package("customer-profile", r)
    persona = "Mia — Head of Marketing at a 120-person SaaS scale-up, owns pipeline but has no team"

    # Step 4
    m = load_server("outreach-method")
    r = await m.call_tool("select_method", {"persona": persona, "signals": signals})
    pkg4 = check_package("outreach-method", r)
    method = "linkedin_post"

    # Step 5
    m = load_server("executing-agent")
    r = await m.call_tool("plan_execution", {"method": method, "persona": persona, "signals": signals})
    pkg5 = check_package("executing-agent", r)
    generation_plan = "Write a LinkedIn post in founder voice showing the playbook results"
    tone = "direct, peer-to-peer, evidence-led"
    cta = "Book a 30-min call to see if this playbook fits your situation"

    # Step 6a
    m = load_server("message-formatting")
    r = await m.call_tool("format_message", {
        "generation_plan": generation_plan, "persona": persona,
        "tone": tone, "cta": cta
    })
    pkg6a = check_package("message-formatting", r)

    # Step 6b
    m = load_server("graphical-pipeline")
    r = await m.call_tool("generate_visual", {
        "generation_plan": generation_plan, "persona": persona, "method": method
    })
    pkg6b = check_package("graphical-pipeline", r)

    # Step 7
    m = load_server("representation")
    r = await m.call_tool("assemble", {
        "persona": persona,
        "pain_points": ["no inbound pipeline", "no brand equity in Belgian market"],
        "buying_trigger": "Sales team closing well but pipeline is drying up",
        "relevance_score": 9,
        "assumptions": ["client has budget for agency"],
        "method": method,
        "copy": "We helped a Belgian SaaS scale-up go from zero inbound to 67 MQLs in 10 weeks.",
        "headline": "67 MQLs. 10 weeks. Zero brand equity to start.",
        "cta": cta,
        "grounded_claims": ["67 MQLs vs 40 target", "140 webinar registrants"],
        "warnings": ["client anonymised — confirm NDA allows stat sharing"],
        "style_direction": "clean, professional, LinkedIn-native",
        "image_prompt": "minimalist chart showing MQL growth, brand blue palette"
    })
    check_package("representation", r)

    print("\n=== All steps passed ===\n")

asyncio.run(run())
