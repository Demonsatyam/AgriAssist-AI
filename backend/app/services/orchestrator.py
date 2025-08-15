from app.services import nlp
from app.services.tools import weather, irrigation, market
from app.services.rag import retriever

# Returns dict compatible with app.schemas.query.QueryResponse

def answer_query(text: str, locale: str = "en-IN", farm_id: str | None = None):
    intent = nlp.classify_intent(text)
    entities = nlp.extract_entities(text)

    sources: list[dict] = []
    reasoning_chunks: list[str] = []

    if intent == "irrigation":
        wx = weather.get_outlook(entities)  # {rain_prob_48h, temp_c}
        rec = irrigation.recommend(entities, wx)  # {action, window, reason}
        docs = retriever.find("irrigation", entities)
        sources += docs
        reasoning_chunks.append(rec["reason"])
        window = f" {rec['window']}" if rec.get("window") else ""
        answer = f"{rec['action']} irrigation{window}."
        confidence = min(95, 70 + (wx.get("rain_prob_48h", 0) // 5))

    elif intent == "market":
        mt = market.get_trend(entities)  # {latest, suggestion, explain}
        docs = retriever.find("market", entities)
        sources += docs
        reasoning_chunks.append(mt["explain"])
        answer = f"{mt['suggestion']}: latest ₹{mt['latest']}"
        confidence = 78

    elif intent == "pest":
        # Text-only pest Q for now – advise using the image classifier route
        docs = retriever.find("pest", entities)
        sources += docs
        answer = "Please upload a field image on the Pest page for accurate classification."
        reasoning_chunks.append("Image-based detection yields higher accuracy.")
        confidence = 60

    else:
        docs = retriever.find("general", entities)
        sources += docs
        answer = docs[0]["excerpt"] if docs else "No specific guidance found."
        reasoning_chunks.append("Answer derived from retrieved guidance.")
        confidence = 62

    return {
        "answer": answer,
        "reasoning": " ".join(reasoning_chunks).strip(),
        "sources": sources[:4],
        "confidence": int(max(0, min(confidence, 99)))
    }