# Simple rules engine for irrigation decision

def recommend(entities: dict, wx: dict) -> dict:
    prob = wx.get("rain_prob_48h", 0)
    if prob >= 60:
        return {"action": "Delay", "window": "by 24–36 hours", "reason": f"Rain probability ~{prob}% in 48h; conserve water."}
    return {"action": "Irrigate", "window": "today evening", "reason": f"Rain probability low (~{prob}%)."}