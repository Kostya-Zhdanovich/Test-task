import pytest
from fastapi.testclient import TestClient
from server.main import app 

client = TestClient(app)

# Тест для проверки статуса API
def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# Тест для проверки данных с городом (погода, курс доллара, новости)
@pytest.mark.parametrize("city", [
    "Minsk",  
    "London"  
])
def test_data_with_city(city):
    response = client.get(f"/data?city={city}")
    assert response.status_code == 200
    data = response.json()

    # Проверка наличия данных о курсе доллара
    assert "exchange_rate" in data  # Курс должен быть в ответе

    # Проверка наличия данных о погоде
    assert "weather" in data and data["weather"] is not None  # Погода должна быть в ответе
    weather_data = data["weather"]
    assert "temperature" in weather_data, "Температура должна быть в данных о погоде."
    assert isinstance(weather_data["temperature"], (int, float)), "Температура должна быть числом."
    assert -100 <= weather_data["temperature"] <= 100, f"Температура {weather_data['temperature']} выходит за пределы допустимого диапазона."

    assert "description" in weather_data, "Описание погоды должно быть в данных о погоде."
    assert isinstance(weather_data["description"], str), "Описание погоды должно быть строкой."

    # Проверка наличия данных о новостях
    assert "news" in data  # Новости должны быть в ответе
    assert isinstance(data["news"], list), "Новости должны быть в виде списка."
    assert len(data["news"]) > 0, "Список новостей не должен быть пустым."

# Тест для проверки получения данных о курсе доллара
def test_exchange_rate():
    response = client.get("/data?city=Minsk")
    assert response.status_code == 200
    data = response.json()
    assert "exchange_rate" in data  # Курс доллара должен быть в ответе
    assert isinstance(data["exchange_rate"], (int, float)), "Курс доллара должен быть числом."

# Тест для проверки получения данных о погоде
def test_weather():
    response = client.get("/data?city=Minsk")
    assert response.status_code == 200
    data = response.json()
    assert "weather" in data  # Погода должна быть в ответе
    weather_data = data["weather"]
    assert "temperature" in weather_data, "Температура должна быть в данных о погоде."
    assert isinstance(weather_data["temperature"], (int, float)), "Температура должна быть числом."
    assert -100 <= weather_data["temperature"] <= 100, f"Температура {weather_data['temperature']} выходит за пределы допустимого диапазона."
    assert "description" in weather_data, "Описание погоды должно быть в данных о погоде."

# Тест для проверки получения новостей
def test_news():
    response = client.get("/data?city=Minsk")
    assert response.status_code == 200
    data = response.json()
    assert "news" in data  # Новости должны быть в ответе
    assert isinstance(data["news"], list), "Новости должны быть в виде списка."
    assert len(data["news"]) > 0, "Список новостей не должен быть пустым."
    for news_item in data["news"]:
        assert "title" in news_item, "Каждая новость должна содержать заголовок."
        assert "url" in news_item, "Каждая новость должна содержать URL."
