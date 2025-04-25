# Hugging Face`s Agents Course

This project is a simple study of AI agents using [`llama-index`](https://github.com/jerryjliu/llama_index) and [Ollama](https://ollama.com/).
The course is available in:
- https://huggingface.co/learn/agents-course

## Agent Workflow Example

The file [`agents/using_sample_tool.py`](agents/using_sample_tool.py) demonstrates how to:
- Initialize an LLM using `Ollama` with a locally available model (e.g., `llama3.2:latest`).
- Define and register a custom tool (`multiply`) that the AI agent can call.
- Use both **stateless** and **stateful** interactions:
  - Stateless: The agent calls the tool directly based on the prompt.
  - Stateful: The agent remembers prior context using `Context`, enabling memory-like behavior.

## Multi-Agent Workflow Example
The file agents/multi_agent_workflow.py showcases:
- A multi-agent architecture using ReActAgent with tools like add and subtract.
- A calculator agent that can handle math operations.
- An info_lookup agent designed to query external sources (e.g., a RAG system).
- Use of AgentWorkflow to compose and route between agents based on the user prompt.

### Key Features
- ReActAgent lets the LLM reason and act step-by-step using thoughts, actions, and observations.
- Tool delegation: Different agents are responsible for different kinds of tasks.

## Workflows
The file agents/multi_step_workflow.py demonstrates:
- How to build custom workflows using the Workflow API from llama-index.
- Creating step-based execution with state passed between steps.
- Use of custom event classes like ProcessingEvent for structured inter-step communication.

## Langgraph
Alfred’s email processing system:
- Read incoming emails
- Classify them as spam or legitimate
- Draft a preliminary response for legitimate emails
- Send information to Mr. Wayne when legitimate (printing only)