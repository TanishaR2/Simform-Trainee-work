# supervisor_agent.py

def get_tasks(user_input):
    interests = ", ".join(user_input.get("interests", []))
    currency = user_input["currency"]

    return [
        {
            "agent": "visa_agent",
            "query": f"visa requirements for {user_input['from_country']} citizens traveling to {user_input['to_country']}"
        },
        {
            "agent": "budget_agent",
            "query": f"Plan a budget of {user_input['budget']} {currency} for a trip to {user_input['to_city']} from {user_input['check_in']} to {user_input['check_out']}"
        },
        {
            "agent": "flight_agent",
            "query": f"Flight options from {user_input['from_city']} to {user_input['to_city']} on {user_input['departure_date']}"
        },
        {
            "agent": "hotel_agent",
            "query": f"Hotels in {user_input['to_city']} from {user_input['check_in']} to {user_input['check_out']} under {user_input['hotel_budget']} {currency}"
        },
        {
            "agent": "activity_agent",
            "query": f"Activities in {user_input['to_city']} from {user_input['check_in']} to {user_input['check_out']} under {user_input['budget'] * 0.2} {currency} based on interests: {interests}"
        }
    ]


def compile_plan(context):
    return {
        "Visa Info": context.get("visa_agent", "No visa info available"),
        "Budget Plan": context.get("budget_agent", "No budget plan available"),
        "Flight Options": context.get("flight_agent", "No flight info available"),
        "Hotel Options": context.get("hotel_agent", "No hotel options available"),
        "Suggested Activities": context.get("activity_agent", "No activities found"),
    }
