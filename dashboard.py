import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="GreenPulse Dashboard", layout="wide")

st.title("🌍 GreenPulse: Real-Time Environmental Risk Monitor")

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("output.csv")

        latest = df.tail(10)

        placeholder.dataframe(latest)

        st.bar_chart(latest[["aqi", "waste_index", "temperature"]])

        time.sleep(2)

    except:
        st.write("Waiting for data...")
        time.sleep(2)
