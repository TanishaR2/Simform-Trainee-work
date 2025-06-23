import logging
from langchain.tools import tool
from prompts.budget_prompt import budget_prompt
from my_llm import llm

logger = logging.getLogger("BudgetTool")

class BudgetTool:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template

    def run(self, query: str) -> str:
        """
        Generates per-person travel budget in markdown table format.
        """
        logger.info("🛠️ [Budget Tool] Invoked with query: %s", query)
        formatted_prompt = self.prompt_template.format(query=query)
        response = self.llm.invoke(formatted_prompt).content
        logger.info("📄 [Budget Tool] Response generated successfully.")
        return response


# Tool wrapper
budget_tool_instance = BudgetTool(llm=llm, prompt_template=budget_prompt)

@tool
def run_budget_tool(query: str) -> str:
    """
    This function allows to make a query from budget tool defined and run it
    """
    return budget_tool_instance.run(query)
