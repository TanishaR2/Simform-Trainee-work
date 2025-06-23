# graph_runner.py

import uuid
import logging
import time
import warnings
from typing import Dict

from pymongo import MongoClient
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.mongodb import MongoDBSaver

from my_llm import llm
from agents.activity_agent import activity_agent
from agents.budget_agent import budget_agent
from agents.itinerary_agent import itinerary_agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from state import TravelState


# --- Suppress Deprecated Warnings ---
warnings.filterwarnings("ignore", message="Convert_system_message_to_human will be deprecated!")

# --- Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("TravelPlanner")


class TravelPlannerGraph:
    def __init__(self):
        self.checkpointer = self._init_checkpointer()
        self.app = self._build_graph()

    def _init_checkpointer(self):
        client = MongoClient("mongodb+srv://tanisha02ramani:YJgGMon09SP6sFGj@langgraphchatbot.rswb2mq.mongodb.net/")
        return MongoDBSaver(client)

    # --- Agent Execution Nodes ---
    def run_budget_agent(self, state: TravelState) -> TravelState:
        logger.info("Invoking Budget Agent")
        result = budget_agent.invoke({"messages": state["messages"]})
        return {**state, "messages": state["messages"] + [result["messages"][-1]]}

    def run_activity_agent(self, state: TravelState) -> TravelState:
        logger.info("Invoking Activity Agent")
        result = activity_agent.invoke({"messages": state["messages"]})
        return {**state, "messages": state["messages"] + [result["messages"][-1]]}

    def run_itinerary_agent(self, state: TravelState) -> TravelState:
        logger.info("Invoking Itinerary Agent")
        result = itinerary_agent.invoke({"messages": state["messages"]})
        return {**state, "messages": state["messages"] + [result["messages"][-1]]}

    def fallback_agent(self, state: TravelState) -> TravelState:
        logger.warning("Fallback Agent Triggered – Invalid classification.")
        fallback_msg = AIMessage(content="Sorry, I couldn't classify your request. Please rephrase or specify if it's about budget, activities, or itinerary.")
        return {**state, "messages": state["messages"] + [fallback_msg]}

    def agent_classifier(self, state: TravelState) -> TravelState:
        query = state["messages"][-1].content
        logger.info(f"User query received: {query}")

        classification_prompt = [
            SystemMessage(
                content=(
                    "You are a router for a travel assistant system. Available agents are: "
                    "`activity`, `budget`, and `itinerary`. "
                    "Based on the user's query, return only one word: `activity`, `budget`, or `itinerary`. "
                    "No explanation. Just the word."
                )
            ),
            HumanMessage(content=query)
        ]

        result = llm.invoke(classification_prompt).content.strip().lower()
        logger.info(f"Agent classified as: {result}")

        state["agent_type"] = result if result in ["activity", "budget", "itinerary"] else "fallback"
        return state

    def _build_graph(self):
        workflow = StateGraph(TravelState)

        workflow.add_node("agent_classifier", self.agent_classifier)
        workflow.add_node("activity", self.run_activity_agent)
        workflow.add_node("budget", self.run_budget_agent)
        workflow.add_node("itinerary", self.run_itinerary_agent)
        workflow.add_node("fallback", self.fallback_agent)

        workflow.set_entry_point("agent_classifier")

        workflow.add_conditional_edges(
            "agent_classifier",
            lambda state: state["agent_type"],
            {
                "activity": "activity",
                "budget": "budget",
                "itinerary": "itinerary",
                "fallback": "fallback",
            }
        )

        workflow.add_edge("activity", END)
        workflow.add_edge("budget", END)
        workflow.add_edge("itinerary", END)
        workflow.add_edge("fallback", END)

        return workflow.compile(checkpointer=self.checkpointer)

    def run(self, user_input: str) -> str:
        logger.info("Starting Travel Planner Workflow")
        initial_state = {
            "messages": [HumanMessage(content=user_input)],
            "agent_type": "",
            "human_feedback": [],
        }
        thread_id = str(uuid.uuid4())
        logger.info(f"Thread ID: {thread_id}")
        thread_config = {"configurable": {"thread_id": thread_id}}

        try:
            final_state = self.app.invoke(initial_state, config=thread_config)
            return final_state["messages"][-1].content
        except Exception as e:
            logger.exception(f"Error during workflow execution: {e}")
            return "Something went wrong while processing your request. Please try again."


# --- CLI Test ---
if __name__ == "__main__":
    planner = TravelPlannerGraph()

    queries = [
        "Suggest a low budget plan for a 4-day trip to Goa with friends",
        "Plan a pocket-friendly budget for a 5-day trip to Manali for two friends.",
        "Plan me an itinerary for 3 days in New York",
        "Plan me some activities to do or some sightseeing in Mussoorie"
    ]

    for query in queries:
        response = planner.run(query)
        print("\n\nQuery:", query)
        print(response)
        time.sleep(15)
