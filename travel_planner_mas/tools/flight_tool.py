from langchain.tools import tool
from langchain_openai import ChatOpenAI
from utils.openai_api_key import openai_api_key
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model="gpt-4")
# from serpapi import GoogleSearch
# from utils.serpApi import SERPAPI_KEY
@tool
def search_flights_openai(origin: str, destination: str, date: str) -> str:
    """
    Simulates a flight search using OpenAI. Returns 3-5 plausible flight options.
    """
    prompt = f"""
You are a helpful travel assistant.

Provide 3-5 plausible flight options from {origin} to {destination} on {date}.
Each option should include:
- Airline name
- Departure and arrival times
- Flight duration
- Estimated price in INR
- A fictional but realistic booking link

Be concise, but informative. Format clearly for display.
    """

    try:
        response = llm.predict(prompt)
        return response
    except Exception as e:
        return f"Flight search error using OpenAI: {str(e)}"