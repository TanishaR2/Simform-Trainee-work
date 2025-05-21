import requests
from typing import List, Dict

def real_hotel_search(destination: str, checkin: str, checkout: str, max_budget: int = 5000) -> List[Dict]:
    # Example using a fake endpoint (replace with real API endpoint + key)
    url = "https://api.example.com/hotels/search"
    headers = {"Authorization": f"Bearer {os.getenv('HOTEL_API_KEY')}"}
    params = {
        "location": destination,
        "checkin": checkin,
        "checkout": checkout,
        "max_price": max_budget,
        "currency": "INR"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    hotels = []
    for item in data.get("results", []):
        hotels.append({
            "name": item.get("name"),
            "price": item.get("price"),
            "rating": item.get("rating"),
            "amenities": item.get("amenities", [])
        })

    return hotels
