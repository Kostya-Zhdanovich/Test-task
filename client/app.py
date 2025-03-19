import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/data"

st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main-container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stTextInput, .stButton {
            width: 100%;
        }
        .section-title {
            font-size: 22px;
            font-weight: bold;
            border-bottom: 2px solid #ddd;
            padding-bottom: 5px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.title("ТЕСТОВОЕ ЗАДАНИЕ")

    city = st.text_input("Введите город для получения данных о погоде:", "Minsk")

    if st.button("Получить данные о погоде"):
        with st.spinner(f"Загрузка погоды для {city}..."):
            response = requests.get(API_URL, params={"city": city})
            if response.status_code == 200:
                data = response.json()
                st.success(f"Данные о погоде для города {city} успешно загружены!")

                st.markdown('<div class="section-title">Погода</div>', unsafe_allow_html=True)
                st.write(f"**Температура:** {data['weather']['temperature']}°C")
                st.write(f"**Описание погоды:** {data['weather']['description']}")
            else:
                st.error(f"Ошибка при получении данных о погоде для города {city}. Проверьте работу сервера.")


    if st.button("Получить ифнормацию о курсе доллара"):
        with st.spinner(f"Загрузка курса доллара..."):
            response = requests.get(API_URL) 
            if response.status_code == 200:
                data = response.json()
                st.success(f"Данные о курсе доллара успешно загружены!")

                st.markdown('<div class="section-title">Курс доллара</div>', unsafe_allow_html=True)
                st.write(f"**Курс:** {data['exchange_rate']} BYN")
            else:
                st.error(f"Ошибка при получении данных о курсе доллара. Проверьте работу сервера.")

    if st.button("Получить новости"):
        with st.spinner(f"Загрузка новостей..."):
            response = requests.get(API_URL)  
            if response.status_code == 200:
                data = response.json()
                st.success(f"Новости за последние 7 дней успешно загружены!")

                st.markdown('<div class="section-title">Последние новости</div>', unsafe_allow_html=True)
                for news in data["news"]:
                    st.markdown(f"**[{news['title']}]({news['url']})**")
            else:
                st.error(f"Ошибка при получении новостей. Проверьте работу сервера.")
