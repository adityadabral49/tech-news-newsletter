import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_top_headlines():
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "category": "technology",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print("Error:", data)
        return []

    return data.get("articles", [])

if __name__ == "__main__":
    news = fetch_top_headlines()

    for i, article in enumerate(news, start=1):
        print(f"{i}. {article['title']}")
        
