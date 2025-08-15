# Extremely lightweight intent & entity extraction; swap with LLM later
import re

IRRIGATION_KEYS = ("irrigate", "irrigation", "water now", "water today")
MARKET_KEYS = ("price", "market", "sell", "mandi")
PEST_KEYS = ("pest", "disease", "leaf", "worm", "spots")

KNOWN_CROPS = ("wheat", "rice", "paddy", "mustard", "cotton", "maize")
KNOWN_STAGES = ("tillering", "flowering", "harvest", "sowing")
KNOWN_PLACES = ("prayagraj", "ara", "patna", "pune")


def classify_intent(text: str) -> str:
    t = text.lower()
    if any(k in t for k in IRRIGATION_KEYS):
        return "irrigation"
    if any(k in t for k in MARKET_KEYS):
        return "market"
    if any(k in t for k in PEST_KEYS):
        return "pest"
    return "general"


def extract_entities(text: str) -> dict:
    t = text.lower()
    crop = next((c for c in KNOWN_CROPS if c in t), None)
    stage = next((s for s in KNOWN_STAGES if s in t), None)
    location = next((p.title() for p in KNOWN_PLACES if p in t), None)
    return {"crop": crop, "stage": stage, "location": location}