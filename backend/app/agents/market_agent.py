from typing import Dict, Any
from app.services.tools import market

class MarketAgent:
    name = "market_agent"

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        entities = payload.get("entities", {})
        mt = market.get_trend(entities)
        return {"trend": mt}
