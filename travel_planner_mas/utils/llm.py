from openai_api_key import openai_api_key
from langchain_openai import OpenAI
llm = OpenAI(model="gpt-4", temperature=0, openai_api_key=openai_api_key)