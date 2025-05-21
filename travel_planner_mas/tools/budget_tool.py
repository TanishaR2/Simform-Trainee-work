from langchain.tools import tool

@tool
def calculate_budget_plan(budget: float, currency: str) -> str:
    """
    Calculate and format a fixed-percentage budget split for a trip.

    Splits the total budget into:
      - 40% for flights
      - 30% for hotels
      - 20% for activities
      - 10% for other costs

    Args:
        budget (float): Total budget for the trip.
        currency (str): Currency code (e.g., "INR", "USD").

    Returns:
        str: A formatted string showing allocations for each category
             and the total budget.
    """
    flights = round(budget * 0.4, 2)
    hotels = round(budget * 0.3, 2)
    activities = round(budget * 0.2, 2)
    others = round(budget * 0.1, 2)

    summary = f"""
Trip Budget Planner:
-----------------------
Flights     : {flights} {currency}
Hotels      : {hotels} {currency}
Activities  : {activities} {currency}
Other Costs : {others} {currency}
-----------------------
Total Budget: {budget} {currency}
"""

    return summary.strip()
