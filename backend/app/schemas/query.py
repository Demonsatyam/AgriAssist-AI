from pydantic import BaseModel
from typing import List, Optional
from .common import Source

class QueryRequest(BaseModel):
    text: str
    locale: Optional[str] = "en-IN"
    farm_id: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    reasoning: str
    sources: List[Source] = []
    confidence: int