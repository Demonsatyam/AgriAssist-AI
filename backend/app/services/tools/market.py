# Mock market adapter – replace with eNAM later

def get_trend(entities: dict) -> dict:
    # Could read entities["crop"] or location; fixed mock for now
    return {"latest": 2610.0, "suggestion": "Hold", "explain": "Prices up marginally over last 5 days."}