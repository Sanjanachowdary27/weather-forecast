
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st # type: ignore
import pandas as pd
from search.search_feature import search_by_date, search_by_range
from ml.predictor import predict_next_30_days
from monsoon.monsoon_check import predict_monsoon

st.set_page_config(page_title="Weather Forecast Dashboard", layout="wide")

st.title("🌦️ Weather Forecast Dashboard")
st.markdown("This dashboard helps you predict and explore weather data with ML-powered insights.")

page = st.sidebar.selectbox("Go to", ["Forecast Next 30 Days", "Search Weather Data", "Monsoon Prediction"])

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/weather_data_2025.csv")
        return df
    except:
        return pd.DataFrame()

df = load_data()

if page == "Forecast Next 30 Days":
    st.subheader("📈 30-Day Weather Forecast")
    forecast = predict_next_30_days()
    st.dataframe(forecast)

elif page == "Search Weather Data":
    st.subheader("🔍 Search Weather Data")
    search_type = st.radio("Search by:", ["Single Date", "Date Range"])

    if search_type == "Single Date":
        date = st.date_input("Select date")
        if st.button("Search"):
            result = search_by_date(str(date))
            st.dataframe(result)

    else:
        start = st.date_input("Start date")
        end = st.date_input("End date")
        if st.button("Search Range"):
            result = search_by_range(str(start), str(end))
            st.dataframe(result)

elif page == "Monsoon Prediction":
    st.subheader("☔ Monsoon Forecast")

    col1, col2, col3 = st.columns(3)

    with col1:
        temp = st.number_input("Temperature (°C)", value=28.0)
    with col2:
        humidity = st.number_input("Humidity (%)", value=75.0)
    with col3:
        windspeed = st.number_input("Wind Speed (km/h)", value=10.0)

    if st.button("Predict Monsoon"):
        rainfall, percent, is_monsoon = predict_monsoon(temp, humidity, windspeed)

        st.metric("🌧️ Predicted Rainfall", f"{rainfall} mm")
        st.metric("💧 Rain Probability", f"{percent}%")
        st.metric("☔ Monsoon", "Yes" if is_monsoon else "No")
