import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.llm import call_claude
from shared.schemas import GraphicalPipelineInput, GraphicalPipelineOutput

PROMPT = (Path(__file__).parent / "prompt.md").read_text()

server = Server("graphical-pipeline")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="generate_visual",
            description="Generate visual direction, layout notes, and an image prompt for the campaign asset.",
            inputSchema=GraphicalPipelineInput.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    inp = GraphicalPipelineInput(**arguments)
    user_content = (
        f"Generation plan:\n{inp.generation_plan}\n\n"
        f"Persona:\n{inp.persona}\n\n"
        f"Method: {inp.method}"
    )
    result = await call_claude(PROMPT, user_content, GraphicalPipelineOutput)
    return [TextContent(type="text", text=result.model_dump_json())]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
