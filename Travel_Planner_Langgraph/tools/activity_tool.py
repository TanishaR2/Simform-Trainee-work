import logging
from prompts.activity_prompt import activity_prompt
from my_llm import llm
from langchain.tools import tool

logger = logging.getLogger("ActivityTool")


class ActivityTool:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template

    def run(self, query: str) -> str:
        logger.info("🛠️ [Activity Tool] Invoked with query: %s", query)
        formatted_prompt = self.prompt_template.format(query=query)
        response = self.llm.invoke(formatted_prompt).content
        logger.info("📄 [Activity Tool] Response generated successfully.")
        return response


# Instantiate the tool class
activity_tool_instance = ActivityTool(llm=llm, prompt_template=activity_prompt)

# Export a clean tool function
@tool("run_activity_tool", return_direct=True)
def run_activity_tool(query: str) -> str:
    """
    This function allows to make a query from activity tool defined and run it
    """
    return activity_tool_instance.run(query)
