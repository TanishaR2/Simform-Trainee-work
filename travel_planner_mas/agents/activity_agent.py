# travel_agents/agents/activity_agent.py
from utils.openai_api_key import openai_api_key
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from tools.activities_tool import search_activities_openai

# Tool definition
activity_tool = Tool(
    name="activity_suggestion_tool",
    func=lambda query: str(search_activities_openai(**eval(query))),
    description=(
        "Use this to suggest a day-wise itinerary based on destination, number of travel days, "
        "and optional interests like 'history', 'food', 'adventure', 'art', or 'nature'. "
        "Input must be a dictionary with keys: to_city (str), travel_days (int), interests (list)."
    )
)

# Activity Agent constructor
def get_activity_agent(openai_api_key=openai_api_key):
    llm = ChatOpenAI(temperature=0, model="gpt-4", openai_api_key=openai_api_key)

    agent = initialize_agent(
        tools=[search_activities_openai],
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    return agent



