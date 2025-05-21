from agents.visa_agent import get_visa_agent
from agents.budget_agent import get_budget_agent
from agents.flight_agent import get_flight_agent
from agents.hotel_agent import get_hotel_agent
from agents.activity_agent import get_activity_agent

visa_agent = get_visa_agent()
budget_agent = get_budget_agent()
flight_agent = get_flight_agent()
hotel_agent = get_hotel_agent()
activity_agent = get_activity_agent()

visa_response = visa_agent.run("visa requirements for Indian citizens traveling to Australia")
budget_response = budget_agent.run("budget plan for a trip to Melbourne from May 24 to May 30, 2025 with a budget of $2000")
flight_response = flight_agent.run("flight options from Mumbai to Melbourne on May 24, 2025")
hotel_response = hotel_agent.run("hotel options in Melbourne from May 24 to May 30, 2025 under $200")
activity_response = activity_agent.run("activities in Melbourne from May 24 to May 30, 2025 under $100")

print("Visa Response:", visa_response)
print("\n"+"-"*80+"\n")
print("Budget Response:", budget_response)
print("\n"+"-"*80+"\n")
print("Flight Response:", flight_response)
print("\n"+"-"*80+"\n")
print("Hotel Response:", hotel_response)
print("\n"+"-"*80+"\n")
print("Activity Response:", activity_response)