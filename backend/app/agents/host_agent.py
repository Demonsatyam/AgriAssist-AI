from typing import Dict, Any
from app.services import nlp
from app.agents.irrigation_agent import IrrigationAgent
from app.agents.market_agent import MarketAgent
from app.agents.retriever_agent import RetrieverAgent

class HostAgent:
    def __init__(self):
        self.irrigation = IrrigationAgent()
        self.market = MarketAgent()
        self.retriever = RetrieverAgent()

    async def handle(self, text: str, locale: str = "en-IN", farm_id: str | None = None) -> Dict[str, Any]:
        intent = nlp.classify_intent(text)
        entities = nlp.extract_entities(text)

        if intent == "irrigation":
            ir = await self.irrigation.handle({"entities": entities})
            rv = await self.retriever.handle({"topic": "irrigation", "entities": entities})
            rec = ir["rec"]; sources = rv["sources"]
            window = f" {rec['window']}" if rec.get("window") else ""
            return {
                "answer": f"{rec['action']} irrigation{window}.",
                "reasoning": rec["reason"],
                "sources": sources[:4],
                "confidence": 80
            }

        if intent == "market":
            mt = await self.market.handle({"entities": entities})
            rv = await self.retriever.handle({"topic": "market", "entities": entities})
            tr = mt["trend"]; sources = rv["sources"]
            return {
                "answer": f"{tr['suggestion']}: latest ₹{tr['latest']}",
                "reasoning": tr["explain"],
                "sources": sources[:4],
                "confidence": 78
            }

        if intent == "pest":
            rv = await self.retriever.handle({"topic": "pest", "entities": entities})
            return {
                "answer": "Please upload a field image on the Pest page for accurate classification.",
                "reasoning": "Image-based detection yields higher accuracy.",
                "sources": rv["sources"][:4],
                "confidence": 60
            }

        rv = await self.retriever.handle({"topic": "general", "entities": entities})
        ans = rv["sources"][0]["excerpt"] if rv["sources"] else "No specific guidance found."
        return {
            "answer": ans,
            "reasoning": "Answer derived from retrieved guidance.",
            "sources": rv["sources"][:4],
            "confidence": 62
        }
