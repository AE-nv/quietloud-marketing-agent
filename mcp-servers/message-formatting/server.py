import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.llm import call_claude
from shared.schemas import MessageFormattingInput, MessageFormattingOutput

PROMPT = (Path(__file__).parent / "prompt.md").read_text()

server = Server("message-formatting")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="format_message",
            description="Write the complete marketing asset based on the generation plan and persona.",
            inputSchema=MessageFormattingInput.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    inp = MessageFormattingInput(**arguments)
    user_content = (
        f"Generation plan:\n{inp.generation_plan}\n\n"
        f"Persona:\n{inp.persona}\n\n"
        f"Tone: {inp.tone}\n\n"
        f"CTA: {inp.cta}"
    )
    result = await call_claude(PROMPT, user_content, MessageFormattingOutput)
    return [TextContent(type="text", text=result.model_dump_json())]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
