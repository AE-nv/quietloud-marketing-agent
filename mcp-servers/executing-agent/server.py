import asyncio
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from shared.llm import call_claude
from shared.schemas import ExecutingAgentInput, ExecutingAgentOutput

PROMPT = (Path(__file__).parent / "prompt.md").read_text()

server = Server("executing-agent")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="plan_execution",
            description="Turn a selected outreach method into a detailed content generation plan.",
            inputSchema=ExecutingAgentInput.model_json_schema(),
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    inp = ExecutingAgentInput(**arguments)
    user_content = (
        f"Method: {inp.method}\n\n"
        f"Persona:\n{inp.persona}\n\n"
        f"Signals:\n{json.dumps(inp.signals, indent=2)}"
    )
    result = await call_claude(PROMPT, user_content, ExecutingAgentOutput)
    return [TextContent(type="text", text=result.model_dump_json())]


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
