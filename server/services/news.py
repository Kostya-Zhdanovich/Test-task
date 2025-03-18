import os
import requests
from dotenv import load_dotenv

from datetime import datetime, timedelta

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news():
    today = datetime.today()
    seven_days_ago = today - timedelta(days=7)

    from_date = seven_days_ago.strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    url = f"https://newsapi.org/v2/everything?q=technology&from={from_date}&to={to_date}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"

    response = requests.get(url).json()

    return [{"title": article["title"], "url": article["url"]} for article in response.get("articles", [])]
