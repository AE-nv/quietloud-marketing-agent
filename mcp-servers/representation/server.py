import asyncio
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.llm import call_claude
from shared.schemas import RepresentationInput, RepresentationOutput

PROMPT = (Path(__file__).parent / "prompt.md").read_text()

server = Server("representation")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="assemble",
            description="Assemble all pipeline outputs into a complete, validated campaign representation.",
            inputSchema=RepresentationInput.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    inp = RepresentationInput(**arguments)
    user_content = f"Pipeline outputs:\n{json.dumps(inp.model_dump(), indent=2)}"
    result = await call_claude(PROMPT, user_content, RepresentationOutput)
    return [TextContent(type="text", text=result.model_dump_json())]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
