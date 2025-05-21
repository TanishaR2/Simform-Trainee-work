# main.py

import streamlit as st
from datetime import date

# Import multi-agent system logic
from agents.supervisor_agent import get_tasks, compile_plan
from agents.router_agent import get_agent_map, route_task
from memory.shared_context import init_context, update_context, get_all_context

# === Streamlit App ===

st.set_page_config(page_title="Multi-Agent Travel Planner", page_icon="✈️")
st.title("🧭 Multi-Agent Travel Planner")
st.markdown("Plan your next adventure with the help of intelligent travel agents!")

# === User Input Form ===
with st.form("trip_form"):
    st.subheader("📝 Enter Trip Details")
    
    from_country = st.text_input("Your Nationality", "India")
    to_country = st.text_input("Destination Country", "Australia")
    from_city = st.text_input("Departure City", "Ahmedabad")
    to_city = st.text_input("Destination City", "Melbourne")
    
    departure_date = st.date_input("Departure Date", date.today())
    check_in = st.date_input("Hotel Check-In Date", date.today())
    check_out = st.date_input("Hotel Check-Out Date", date.today())
    
    travel_days = st.number_input("Trip Duration (days)", min_value=1, value=5)
    interests = st.multiselect("Your Interests", ["nature", "food", "art", "history", "shopping", "adventure"])
    
    currency = st.selectbox("Select Currency", options=["INR", "USD", "EUR", "GBP", "JPY"], index=0)
    budget = st.number_input(f"Total Budget ({currency})", min_value=0, value=50000)
    
    submitted = st.form_submit_button("🚀 Plan My Trip")

# === Agent Execution ===
if submitted:
    st.info("🧠 Agents are planning your trip...")

    # Format user input
    user_input = {
        "from_country": from_country,
        "to_country": to_country,
        "from_city": from_city,
        "to_city": to_city,
        "departure_date": str(departure_date),
        "check_in": str(check_in),
        "check_out": str(check_out),
        "travel_days": travel_days,
        "interests": interests,
        "currency": currency,
        "budget": budget,
        "hotel_budget": budget * 0.3,  # 30% for hotels
    }

    # Initialize shared memory
    context = init_context(user_input)
    agent_map = get_agent_map()
    tasks = get_tasks(user_input)

    # Process each task
    for task in tasks:
        with st.spinner(f"Running {task['agent']}..."):
            response = route_task(task, agent_map)
            update_context(context, task["agent"], response)

    # Compile Final Plan
    final_itinerary = compile_plan(get_all_context(context))

    # Display Itinerary
    st.success("✅ Your travel itinerary is ready!")

    st.subheader("📌 Trip Overview")
    for section, content in final_itinerary.items():
        st.markdown(f"**{section}**")
        st.write(content)
        st.markdown("---")
    st.success("🎉 Happy travels! If you have any questions, feel free to ask.")