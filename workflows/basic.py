import asyncio
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step, Event

class ProcessingEvent(Event):
    intermediate_result: str

class OneStepWorkflow(Workflow):
    @step
    async def step_one(self, ev: StartEvent) -> StopEvent:
        return StopEvent(result="Hello, World")

async def main():
    w = OneStepWorkflow(timeout=10, verbose=False)
    result = await w.run()
    print(result)

asyncio.run(main())
