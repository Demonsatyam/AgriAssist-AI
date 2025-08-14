from pydantic import BaseModel
from typing import List, Literal
from .common import Source

class PricePoint(BaseModel):
    date: str  # ISO date string for mock
    price: float

class MarketTrend(BaseModel):
    latest_price: float
    trend: List[PricePoint]
    suggestion: Literal["Sell", "Hold"]
    sources: List[Source] = []
    confidence: int