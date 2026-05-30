import asyncio
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.schemas import OutreachMethodInput, OutreachMethodOutput

PROMPT = (Path(__file__).parent / "prompt.md").read_text()

server = Server("outreach-method")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="select_method",
            description="Select the best outreach or asset method for the campaign based on persona and signals.",
            inputSchema=OutreachMethodInput.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    inp = OutreachMethodInput(**arguments)
    user_content = f"Persona:\n{inp.persona}\n\nSignals:\n{json.dumps(inp.signals, indent=2)}"
    return [TextContent(type="text", text=json.dumps({
        "system_prompt": PROMPT,
        "user_content": user_content,
        "output_schema": OutreachMethodOutput.model_json_schema(),
    }))]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
