from typing import Dict, Any
from app.services.rag import retriever

class RetrieverAgent:
    name = "retriever_agent"

    async def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        topic = payload.get("topic", "general")
        entities = payload.get("entities", {})
        docs = retriever.find(topic, entities)
        return {"sources": docs}
