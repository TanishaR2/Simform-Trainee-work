from langchain.tools import tool
from langchain_openai import ChatOpenAI
from utils.openai_api_key import openai_api_key
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model="gpt-4")

@tool
def search_activities_openai(to_city: str, travel_days: int, interests: list) -> str:
    """
    Suggests travel activities using OpenAI based on city, travel days, and interests.
    Returns a list of recommended activities with descriptions and links.
    """
    interest_str = ", ".join(interests)
    prompt = f"""
You are a travel guide.

Suggest engaging activities in {to_city} for a {travel_days}-day trip. The user is interested in {interest_str}.

For each day, recommend 1-2 activities. Include:
- Name of activity
- Short description
- Type (cultural, adventure, food, etc.)
- A fictional but realistic booking or reference link

Be concise, friendly, and informative. Format for easy reading.
    """

    try:
        response = llm.predict(prompt)
        return response
    except Exception as e:
        return f"Activity search error using OpenAI: {str(e)}"

