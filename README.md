# AI Agent Study with LlamaIndex and Ollama

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

### Sample Tool

The `multiply` function is a basic example of a tool that can be called by the AI agent when needed:

```python
def multiply(a: int, b: int) -> int:
    """Multiplies two integers and returns the resulting integer"""
    return a * b
```

### How to Run
```bash
python agents/using_sample_tool.py
```
