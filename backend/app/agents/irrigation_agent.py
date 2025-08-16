from typing import Dict, Any
from app.services.tools import weather, irrigation

class IrrigationAgent:
    name = "irrigation_agent"

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        entities = payload.get("entities", {})
        wx = weather.get_outlook(entities)
        rec = irrigation.recommend(entities, wx)
        return {"wx": wx, "rec": rec}
