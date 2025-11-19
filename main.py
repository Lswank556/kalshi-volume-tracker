import requests
from datetime import datetime

BASE = "https://api.elections.kalshi.com/trade-api/v2"

def get_pro_football_event_ids():
    """Retrieve all event IDs for Pro Football using the official filters."""
    url = f"{BASE}/search/events"
    params = {"sport": "pro_football"}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()

    events = data.get("events", [])
    return [event["id"] for event in events]


def get_markets_for_event(event_id):
    """Retrieve all markets for a given event."""
    url = f"{BASE}/search/markets"
    params = {"event_id": event_id}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    return r.json().get("markets", [])


def get_total_pro_football_volume():
    """Sum volume across all Pro Football markets."""
    total_volume = 0

    event_ids = get_pro_football_event_ids()

    for event_id in event_ids:
        markets = get_markets_for_event(event_id)
        for m in markets:
            total_volume += m.get("volume", 0)

    return total_volume


def main():
    total = get_total_pro_football_volume()
    print(f"[{datetime.utcnow()}] Total Pro Football Market Volume: {total}")


if __name__ == "__main__":
    main()
