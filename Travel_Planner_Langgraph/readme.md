# 🌍 AI Travel Planner (Multi-Agent System using LangGraph + LangChain)

This project is an AI-powered Travel Planner built using **LangGraph**, **LangChain agents**, and a custom multi-tool LLM setup. It uses classified routing to intelligently answer user queries related to:
- 🗺️ Travel Itinerary Planning
- 💰 Budget Estimation
- 🎡 Activities & Sightseeing Suggestions

---

## 🧠 Features

- ✅ Intelligent agent routing (activity / budget / itinerary / fallback)
- ✅ ReAct-based agents using LangChain with tool invocation
- ✅ LangGraph orchestration with state tracking
- ✅ MongoDB checkpointing for session persistence
- ✅ Supports external tool/function calls (e.g., search API)

---

## 🔧 Project Structure

```
travel-planner/
├── agents/
│   ├── activity_agent.py
│   ├── budget_agent.py
│   └── itinerary_agent.py
├── tools/
│   ├── activity_tool.py
│   ├── budget_tool.py
│   └── itinerary_tool.py
├── prompts/
│   ├── activity_prompt.py
│   ├── budget_prompt.py
│   └── itinerary_prompt.py
├── state.py
├── my_llm.py
├── graph_runner.py      # (Class-based LangGraph controller)
└── README.md
```

---

## 🚀 How It Works

1. **User enters a travel-related query** (e.g., "Plan me a 3-day itinerary for Paris")
2. The system classifies the query into one of:
   - `activity`, `budget`, `itinerary`, or `fallback`
3. Based on classification, the respective agent runs:
   - Executes a LangChain tool with an LLM prompt
4. The result is streamed back as the final answer

---

## 🛠️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/<your-username>/travel-planner.git
cd travel-planner
```

2. **Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up MongoDB**

Make sure your MongoDB Atlas connection string is configured in `graph_runner.py`.

5. **Run the Planner**

```bash
python graph_runner.py
```

---

## 🧪 Example Queries

- "Plan me a 5-day itinerary for Bali with family"
- "Suggest fun activities for a couple trip to Goa for 3 days"
- "What's the estimated budget for a 3-day trip to Manali with friends from ahmedabad?"

---

## 📦 Tech Stack

- 🔹 **LangChain + LangGraph**
- 🔹 **Python 3.10+**
- 🔹 **MongoDB Atlas** (for checkpointing)
- 🔹 **Groq / OpenAI LLMs**

