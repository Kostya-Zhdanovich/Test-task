import os
import requests
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

def get_exchange_rate():
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest/USD"
    response = requests.get(url).json()
    return response.get("conversion_rates", {}).get("BYN", "N/A")
