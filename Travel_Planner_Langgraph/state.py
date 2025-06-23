
# state.py

from typing import List, Dict, Any, Optional
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage


class TravelState(TypedDict):
    messages: List[BaseMessage]
    agent_type: str
    human_feedback: List[str]  # Store human feedback history
    requires_human_input: Optional[bool]  # Flag for interrupt handling