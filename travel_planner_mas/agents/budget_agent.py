from utils.openai_api_key import openai_api_key
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from tools.budget_tool import calculate_budget_plan  # import from budget_tool.py

def get_budget_agent(openai_api_key=openai_api_key):
    llm = ChatOpenAI(temperature=0, model="gpt-4", openai_api_key=openai_api_key)

    agent = initialize_agent(
        tools=[calculate_budget_plan],
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    return agent


