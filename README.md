# ТЕСТОВОЕ ЗАДАНИЕ. MCP SERVER

## Установка и запуск

1. Клонируйте репозиторий и перейдите в папку проекта:
   ```
   git clone https://github.com/Kostya-Zhdanovich/Test-task.git
   cd Test-task
   ``` 
2. Создайте .env файл в корневой папке проекта. Сам проект будет работать и без явного объявлеия ключей, это необходимо для успешного проведения тестов  
   Необходимо зарегестрироваться и получить api ключи на данных сайтах:
   https://newsapi.org/
   https://openweathermap.org/api
   https://www.exchangerate-api.com/
   Ниже приведен скрипт, куда необходимо вставить полученные ключи
   ```
   EXCHANGE_RATE_API_KEY=your_api_key
   WEATHER_API_KEY=your_api_key
   NEWS_API_KEY=your_api_key
   ```
4. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
5. Запустите сервер:
   ```
   uvicorn server.main:app --reload
   ```
6. Запустите клиентскую часть, которая перенаправит на сайт, где можно ознакомиться с функционалом:
   ```
   streamlit run client/app.py
   ```

## Тестирование
1. установить переменную окружения `PYTHONPATH`, указывая Python искать модули и пакеты в директории. В кавычках необходимо указать путь, где лежить папка с проетом, ниже приведен пример. 
    ```
   $env:PYTHONPATH="C:\Users\user\Test-task"  
   ```
2. Запустите тесты с помощью pytest:
   ```
   pytest tests/
   ```
