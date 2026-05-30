import asyncio
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.llm import call_claude
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
    result = await call_claude(PROMPT, inp.raw_content, SignalExtractionOutput)
    return [TextContent(type="text", text=result.model_dump_json())]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
