from pydantic import BaseModel
from typing import List
from .common import Source

class PestResult(BaseModel):
    pest_name: str
    severity: str  # e.g., "Low" | "Moderate" | "High"
    treatment_steps: List[str]
    sources: List[Source] = []
    confidence: int