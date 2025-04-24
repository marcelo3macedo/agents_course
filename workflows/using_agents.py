from llama_index.core.agent.workflow import AgentWorkflow, ReActAgent
from llama_index.llms.ollama import Ollama

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

llm = Ollama(model="llama3.2:latest")

multiply_agent = ReActAgent(
    name="multiply_agent",
    description="Is able to multiply two integers",
    system_prompt="A helpful assistant that can use a tool to multiply numbers.",
    tools=[multiply],
    llm=llm,
)

addition_agent = ReActAgent(
    name="add_agent",
    description="Is able to add two integers",
    system_prompt="A helpful assistant that can use a tool to add numbers.",
    tools=[add],
    llm=llm,
)

workflow = AgentWorkflow(
    agents=[multiply_agent, addition_agent],
    root_agent="multiply_agent",
)

import asyncio

async def main():
    response = await workflow.run(user_msg="Can you add 5 and 3?")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
