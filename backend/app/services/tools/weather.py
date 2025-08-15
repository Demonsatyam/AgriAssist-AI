# Mock weather adapter – replace with IMD/OpenWeather later

def get_outlook(entities: dict) -> dict:
    # Very naive default; you may branch on entities["location"]
    return {"rain_prob_48h": 70, "temp_c": 31}