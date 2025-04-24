import asyncio
from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import (
    AgentWorkflow,
    ReActAgent,
)
from llama_index.core.tools import FunctionTool

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

async def main():
    """
    Demonstrates an AgentWorkflow using multiple ReActAgent agents with Ollama.
    One agent handles math operations (add, subtract), and another is configured
    to perform information lookups using an external RAG system.
    """
    llm = Ollama(model="llama3.2:latest")

    calculator_agent = ReActAgent(
        name="calculator",
        description="Performs basic arithmetic operations",
        system_prompt="You are a calculator assistant. Use your tools for any math operation.",
        tools=[
            FunctionTool.from_defaults(add),
            FunctionTool.from_defaults(subtract)
        ],
        llm=llm,
    )

    async def query_xyz(query: str) -> str:
        """Pretend to query a knowledge base."""
        return f"Looking up info for: {query}"

    query_agent = ReActAgent(
        name="info_lookup",
        description="Looks up information about XYZ",
        system_prompt="Use your tool to query a RAG system to answer information about XYZ",
        tools=[FunctionTool.from_defaults(query_xyz)],
        llm=llm
    )

    agent = AgentWorkflow(
        agents=[calculator_agent, query_agent],
        root_agent="calculator"
    )

    response = await agent.run(user_msg="Can you add 5 and 3?")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())

