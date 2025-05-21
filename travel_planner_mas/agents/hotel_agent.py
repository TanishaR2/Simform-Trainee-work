# travel_agents/agents/hotel_agent.py
from utils.openai_api_key import openai_api_key
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
# from tools.hotel_tool import mock_hotel_search
from tools.hotel_tool import search_hotels_openai
import os

# Initialize Hotel Agent
def get_hotel_agent(openai_api_key=openai_api_key):
    llm = ChatOpenAI(temperature=0, model="gpt-4", openai_api_key=openai_api_key)

    agent = initialize_agent(
        tools=[search_hotels_openai],
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    return agent

