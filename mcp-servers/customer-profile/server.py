import asyncio
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.llm import call_claude
from shared.schemas import CustomerProfileInput, CustomerProfileOutput

PROMPT = (Path(__file__).parent / "prompt.md").read_text()

server = Server("customer-profile")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="build_profile",
            description="Build a detailed customer persona with pain points, buying trigger, and relevance score.",
            inputSchema=CustomerProfileInput.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    inp = CustomerProfileInput(**arguments)
    user_content = f"ICP:\n{inp.recommended_icp}\n\nSignals:\n{json.dumps(inp.signals, indent=2)}"
    result = await call_claude(PROMPT, user_content, CustomerProfileOutput)
    return [TextContent(type="text", text=result.model_dump_json())]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
