import asyncio
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.schemas import AudienceReasoningInput, AudienceReasoningOutput

PROMPT = (Path(__file__).parent / "prompt.md").read_text()

server = Server("audience-reasoning")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="reason_audience",
            description="Identify targetable audiences and recommend the best ICP for a campaign.",
            inputSchema=AudienceReasoningInput.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    inp = AudienceReasoningInput(**arguments)
    user_content = f"Signals:\n{json.dumps(inp.signals, indent=2)}\n\nThemes:\n{json.dumps(inp.themes, indent=2)}"
    return [TextContent(type="text", text=json.dumps({
        "system_prompt": PROMPT,
        "user_content": user_content,
        "output_schema": AudienceReasoningOutput.model_json_schema(),
    }))]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
