# ТЕСТОВОЕ ЗАДАНИЕ. MCP SERVER

## Установка и запуск

1. Клонируйте репозиторий и перейдите в папку проекта:
   ```
   git clone https://github.com/Kostya-Zhdanovich/Test-task.git
   cd Test-task
   ``` 
2. Создайте и настройте файл .env
   ```
   EXCHANGE_RATE_API_KEY=your_api_key
   WEATHER_API_KEY=your_api_key
   NEWS_API_KEY=your_api_key
   ```
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Запустите сервер:
   ```
   uvicorn server.main:app --reload
   ```
5. Запустите клиентскую часть, которая перенаправит на сайт, где можно ознакомиться с функционалом:
   ```
   streamlit run client/app.py
   ```

## Тестирование
1. Запустите тесты с помощью pytest:
   ```
   pytest tests/
   ```
