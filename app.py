import numpy as np
import pandas as pd
import streamlit as st
import src.atms_popularity_service as aps


st.set_page_config(page_title="Bankamatika", page_icon=":atm:")
st.markdown(
    """
## :bank: Оценка места размещения банкомата
"""
)

uploaded_file = st.file_uploader(
    "Загрузите окружение точек, чтобы рассчитать индекс популярности:", type=".csv"
)

st.info(
    """
*Текущая версия сервиса принимает только предварительно обработанные данные.*   
Загрузите .csv файл. Образцы для тестирования: [samples](samples)  
:point_down: Или используйте образец
"""
)

use_example_file = st.checkbox(
    "Использовать образец файла",
    False,
    help="Используйте встроенный файл пример для демонстрации",
)

if use_example_file:
    uploaded_file = f"samples/test{np.random.randint(1, 16)}.csv"
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.markdown("### Просмотр точек на карте")
    st.map(df)

    geo_data = df[["id", "address_rus", "lat", "lon"]]
    model_data = df[
        [
            "id",
            "atm",
            "attraction",
            "bank",
            "bar",
            "bureau_de_change",
            "bus_station",
            "bus_stop",
            "cafe",
            "clinic",
            "college",
            "dentist",
            "fast_food",
            "fuel",
            "hospital",
            "hotel",
            "ice_cream",
            "marketplace",
            "office",
            "parking",
            "payment_terminal",
            "pharmacy",
            "photostudio",
            "post_office",
            "pub",
            "public_building",
            "restaurant",
            "shop",
            "theatre",
            "townhall",
            "train_station",
            "university",
            "veterinary",
            "pois_cnt",
            "near_atm_dist",
            "geo_city",
        ]
    ]

    results = aps.send_request(model_data)
    results = results.merge(geo_data, how="left", on="id")
    results["id"] = results["id"].astype("int")
    st.markdown("### Результаты")
    st.dataframe(results.head())

    st.download_button(
        label="Download data as CSV",
        data=results.to_csv(),
        file_name="model_predictions.csv",
        mime="text/csv",
    )