import requests
from datetime import datetime

# 🔑 Insert your real Kalshi API key here
API_KEY = "71a8105f-9ef9-486a-9435-e168bd15f191"

# ✅ Correct base URL for sports endpoints
BASE_URL = "https://api.kalshi.com/trade-api/v2"

HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def get_total_pro_football_volume():
    """
    Fetch ALL markets tagged as PRO_FOOTBALL and sum their volume.
    """

    # Correct endpoint (sports are only supported on api.kalshi.com)
    url = f"{BASE_URL}/search/markets?sport=PRO_FOOTBALL"

    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()

    data = r.json()
    markets = data.get("markets", [])

    return sum(m.get("volume", 0) for m in markets)


def main():
    timestamp = datetime.utcnow().isoformat()

    try:
        total = get_total_pro_football_volume()
        print(f"[{timestamp}] Total Pro Football Volume: {total}")
    except Exception as e:
        print(f"[{timestamp}] ERROR: {e}")


if __name__ == "__main__":
    main()
