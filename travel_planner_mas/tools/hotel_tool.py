from langchain.tools import tool
from utils.openai_api_key import openai_api_key
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model="gpt-4")

@tool
def search_hotels_openai(to_city: str, check_in: str, check_out: str, hotel_budget: float) -> str:
    """
    Suggests hotels using OpenAI based on city, check-in/out dates, and budget.
    Returns a list of hotel suggestions with descriptions and booking links.
    """
    prompt = f"""
You are a hotel concierge assistant.

Suggest 3-5 hotel options in {to_city} for a stay from {check_in} to {check_out}, under a total budget of ${hotel_budget}.

For each hotel, include:
- Hotel name
- Short description (location, quality, suitability)
- Estimated price/night
- A fictional but realistic booking link

Format for easy reading.
    """

    try:
        response = llm.predict(prompt)
        return response
    except Exception as e:
        return f"Hotel search error using OpenAI: {str(e)}"

