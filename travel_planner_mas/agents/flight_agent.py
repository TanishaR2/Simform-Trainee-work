from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from tools.flight_tool import search_flights_openai

def get_flight_agent():
    llm = ChatOpenAI(temperature=0, model="gpt-4")
    tools = [search_flights_openai]

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        handle_parsing_errors=True,
    )
    return agent

