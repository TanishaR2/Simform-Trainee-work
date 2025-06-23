from tools.itinerary_tool import run_itinerary_tool
from my_llm import llm  # Your LLM instance
from langgraph.prebuilt import create_react_agent

# Create ReAct itinerary agent
itinerary_agent = create_react_agent(
    model=llm,
    tools=[run_itinerary_tool],
    name="ItineraryAgent"
)

