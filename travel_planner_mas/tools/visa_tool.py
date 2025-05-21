from langchain.tools import tool
from utils.openai_api_key import openai_api_key
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model="gpt-4")

@tool
def search_visa_openai(nationality: str, destination_country: str) -> str:
    """
    Provides visa requirement guidance for a given nationality and destination using OpenAI.
    Simulates embassy-like information with disclaimers.
    """
    prompt = f"""
You are a travel visa assistant.

Provide visa requirement guidance for a citizen of {nationality} traveling to {destination_country}.

Include:
- Whether a visa is required
- Type of visa (if needed)
- Duration of stay allowed
- Key documents typically required
- Disclaimer to consult official sources

Format clearly in bullet points.
    """

    try:
        response = llm.predict(prompt)
        return response
    except Exception as e:
        return f"Visa search error using OpenAI: {str(e)}"

