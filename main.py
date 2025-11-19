import requests
from datetime import datetime

# 🔑 INSERT YOUR REAL API KEY HERE
API_KEY = "71a8105f-9ef9-486a-9435-e168bd15f191"

# Base URL and headers
BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def get_total_pro_football_volume():
    """
    Fetches ALL Pro Football markets using the correct Kalshi endpoint,
    and returns the sum of their volume.
    """
    url = f"{BASE_URL}/search/markets?sport=PRO_FOOTBALL"
    response = requests.get(url, headers=HEADERS)

    # Raise if endpoint returns 4xx or 5xx
    response.raise_for_status()

    data = response.json()
    markets = data.get("markets", [])

    # Sum volume across all NFL markets
    total_volume = sum(m.get("volume", 0) for m in markets)
    return total_volume


def main():
    timestamp = datetime.utcnow().isoformat()

    try:
        total_volume = get_total_pro_football_volume()
        print(f"[{timestamp}] Total Pro Football Volume: {total_volume}")
    except Exception as e:
        print(f"[{timestamp}] ERROR: {e}")


if __name__ == "__main__":
    main()

