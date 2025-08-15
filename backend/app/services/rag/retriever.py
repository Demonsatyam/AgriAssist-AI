# Stub retriever – return source items shaped like schemas.common.Source

def find(topic: str, entities: dict) -> list[dict]:
    if topic == "irrigation":
        return [{"title": "IMD 48h Forecast", "excerpt": "Rain chance ~70%"}]
    if topic == "market":
        return [{"title": "eNAM Market Feed", "excerpt": "5-day upward trend"}]
    if topic == "pest":
        return [{"title": "ICAR Rice Pests Guide", "excerpt": "Use image-based classification for accuracy"}]
    return [{"title": "ICAR Best Practices", "excerpt": "General agronomy guidance."}]