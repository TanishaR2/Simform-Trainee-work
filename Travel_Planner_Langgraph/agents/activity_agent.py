from tools.activity_tool import run_activity_tool
from my_llm import llm  # Your LLM instance
from langgraph.prebuilt import create_react_agent

# Create ReAct activity agent
activity_agent = create_react_agent(
    model=llm,
    tools=[run_activity_tool],
    name="ActivityAgent"
)

