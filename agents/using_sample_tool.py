import asyncio
from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.tools import FunctionTool
from llama_index.core.workflow import Context

def multiply(a: int, b: int) -> int:
    """Multiplies two integers and returns the resulting integer"""
    return a * b

async def main():
    """
    Initializes an AI agent using the LlamaIndex and Ollama integration,
    registers a custom multiply tool, and demonstrates:
    - A stateless tool usage call.
    - Stateful interactions using context (e.g., memory).
    """
    llm = Ollama(model="llama3.2:latest")

    agent = AgentWorkflow.from_tools_or_functions(
        [FunctionTool.from_defaults(multiply)],
        llm=llm
    )

    response = await agent.run("Use the multiply function to multiply 2 and 2.")
    print(response)

    ctx = Context(agent)

    response = await agent.run("My name is Bob.", ctx=ctx)
    print(response)

    response = await agent.run("What was my name again?", ctx=ctx)
    print(response)

asyncio.run(main())
