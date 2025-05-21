# router_agent.py

from agents.visa_agent import get_visa_agent
from agents.budget_agent import get_budget_agent
from agents.flight_agent import get_flight_agent
from agents.hotel_agent import get_hotel_agent
from agents.activity_agent import get_activity_agent


def get_agent_map():
    return {
        "visa_agent": get_visa_agent(),
        "budget_agent": get_budget_agent(),
        "flight_agent": get_flight_agent(),
        "hotel_agent": get_hotel_agent(),
        "activity_agent": get_activity_agent(),
    }


def route_task(task, agent_map):
    agent_name = task["agent"]
    query = task["query"]
    agent = agent_map.get(agent_name)

    if not agent:
        return f"❌ Agent '{agent_name}' not found."

    try:
        return agent.run(query)
    except Exception as e:
        return f"❌ Error running {agent_name}: {str(e)}"
