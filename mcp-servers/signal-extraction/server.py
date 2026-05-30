import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.schemas import SignalExtractionInput, SignalExtractionOutput

PROMPT = (Path(__file__).parent / "prompt.md").read_text()

server = Server("signal-extraction")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="extract_signals",
            description="Extract marketable signals, themes, and quotable facts from internal project content.",
            inputSchema=SignalExtractionInput.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    inp = SignalExtractionInput(**arguments)
    return [TextContent(type="text", text=json.dumps({
        "system_prompt": PROMPT,
        "user_content": inp.raw_content,
        "output_schema": SignalExtractionOutput.model_json_schema(),
    }))]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
