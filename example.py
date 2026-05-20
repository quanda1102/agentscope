from src.agentscope.model import OpenAIChatModel
from src.agentscope.agent import ReActAgent, UserAgent
from src.agentscope.formatter import OpenAIChatFormatter
from src.agentscope.memory import InMemoryMemory
import asyncio
import os

import os
from pathlib import Path

def load_env(path=".env"):
    env_path = Path(path)
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        os.environ.setdefault(key, value)

load_env()

from src.agentscope.tool import (
    Toolkit,
    execute_shell_command,
    execute_python_code,
    view_text_file,
)

provider = OpenAIChatModel(
    model_name=os.getenv("LLM_MODEL"),
    api_key=os.getenv("LLM_API_KEY"),
    stream=True,
    client_kwargs={
        "base_url": os.getenv("LLM_BASE_URL"),
    },
)


async def main() -> None:
    """The main entry point for the ReAct agent example."""
    toolkit = Toolkit()

    toolkit.register_tool_function(execute_shell_command)
    toolkit.register_tool_function(execute_python_code)
    toolkit.register_tool_function(view_text_file)

    agent = ReActAgent(
        name="Friday",
        sys_prompt="You are a helpful assistant named Friday.",
        model=provider,
        formatter=OpenAIChatFormatter(),
        toolkit=toolkit,
        memory=InMemoryMemory(),
    )

    user = UserAgent("User")

    msg = None
    while True:
        msg = await user(msg)
        if msg.get_text_content() == "exit":
            break
        msg = await agent(msg)


asyncio.run(main())
