import logging
from langchain.tools import tool
from prompts.itinerary_prompt import itinerary_prompt
from my_llm import llm

logger = logging.getLogger("ItineraryTool")

class ItineraryTool:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template

    def run(self, query: str) -> str:
        """
        Suggests itinerary options based on trip details.
        """
        logger.info("🛠️ [Itinerary Tool] Invoked with query: %s", query)
        formatted_prompt = self.prompt_template.format(query=query)
        response = self.llm.invoke(formatted_prompt).content
        logger.info("📄 [Itinerary Tool] Response generated successfully.")
        return response

# Tool wrapper
itinerary_tool_instance = ItineraryTool(llm=llm, prompt_template=itinerary_prompt)

@tool
def run_itinerary_tool(query: str) -> str:
    """
    This function allows to make a query from itinerary tool defined and run it
    """
    return itinerary_tool_instance.run(query)
