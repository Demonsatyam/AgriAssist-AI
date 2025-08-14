from pydantic import BaseModel
from typing import List, Optional, Literal
from .common import Source

class IrrigationAdvice(BaseModel):
    action: Literal["Irrigate", "Delay"]
    next_window: Optional[str] = None  # e.g., "In 24–36 hours"
    reasoning: str
    sources: List[Source] = []
    confidence: int