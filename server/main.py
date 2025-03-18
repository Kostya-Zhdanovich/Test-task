from fastapi import FastAPI
from server.services.exchange_rate import get_exchange_rate
from server.services.weather import get_weather
from server.services.news import get_news
from typing import Optional

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/data")
def get_data(city: Optional[str] = None):
    data = {
        "exchange_rate": get_exchange_rate(),  
        "weather": get_weather(city) if city else None,  
        "news": get_news() 
    }
    return data
