from tools.budget_tool import run_budget_tool
from my_llm import llm  # Your LLM instance
from langgraph.prebuilt import create_react_agent

# Create ReAct budget agent
budget_agent = create_react_agent(
    model=llm,
    tools=[run_budget_tool],
    name="BudgetAgent"
)

