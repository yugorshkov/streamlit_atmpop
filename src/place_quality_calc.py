import streamlit as st

col1, col2 = st.columns(2)
with col1:
    st.write("Укажите основные параметры точки:")
    city = st.selectbox("Выберите город", dg.get_cities_list())
    distance = st.slider('Расстояние до ближайшего банкомата', 0, 1500, 200, 100)
    banks = st.slider("Количество bankov", 0, 50, 0)
    cafe = st.slider("Количество food", 0, 50, 0)
    stores = st.slider("Количество магазинов", 0, 50, 0)
    pois = st.slider("Количество pois", 0, 50, 0)

with col2:
    st.write("Results")
    test_line = dg.generate_data(city, distance, banks, cafe, stores, pois)
    st.write(test_line)
    st.dataframe(aps.send_request(test_line))
    st.image(f"icons/{location.checker(aps.send_request(test_line))}.png")