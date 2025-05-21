from utils.openai_api_key import openai_api_key
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from tools.visa_tool import search_visa_openai

def get_visa_agent():
    llm = ChatOpenAI(temperature=0, model="gpt-4", openai_api_key=openai_api_key)
    tools = [search_visa_openai]

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        handle_parsing_errors=True,
    )
    return agent

visa_agent_call = get_visa_agent()
response = visa_agent_call.run("Visa requirements for Indian citizen traveling to USA")
print(response)
