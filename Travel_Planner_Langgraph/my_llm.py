import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

lllm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    temperature=0,
)
llm = ChatGroq(
    model='gemma2-9b-it',
    temperature=0
)
# Optional: example usage if running this script standalone
if __name__ == "__main__":
    response = llm([SystemMessage(content="You are a helpful travel assistant."),
                    HumanMessage(content="Suggest a good destinations in india with a budget of 10000.")])
    print("LLM response:", response.content)
    
    
