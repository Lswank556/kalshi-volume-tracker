import requests
import json
from datetime import datetime

def get_pro_football_volume():
    url = "https://api.elections.kalshi.com/trade-api/v2/markets"
    params = {"category": "sports", "sub_category": "pro_football"}

    response = requests.get(url, params=params, timeout=15)
    data = response.json()

    total_volume = sum(m.get("volume", 0) for m in data.get("markets", []))
    print(f"[{datetime.utcnow()}] Total Pro Football Volume:", total_volume)

if __name__ == "__main__":
    get_pro_football_volume()
