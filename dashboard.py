from streamlit_autorefresh import st_autorefresh
import streamlit as st
import pandas as pd
import pathway as pw
import random
import time
from datetime import datetime
import os

st.set_page_config(layout="wide")
st.title("🌍 GreenPulse - Real-Time Environmental Intelligence")

# ---------------------------
# Create sensor file if not exists
# ---------------------------

if not os.path.exists("sensor_stream.csv"):
    with open("sensor_stream.csv", "w") as f:
        f.write("timestamp,aqi,temperature,humidity,waste_index\n")

# ---------------------------
# Append one new sensor reading
# ---------------------------

with open("sensor_stream.csv", "a") as f:
    f.write(
        f"{datetime.now()},"
        f"{random.randint(50,250)},"
        f"{random.uniform(20,45)},"
        f"{random.uniform(30,80)},"
        f"{random.uniform(10,90)}\n"
    )

# ---------------------------
# Define Pathway Schema
# ---------------------------

class EnvSchema(pw.Schema):
    timestamp: str
    aqi: int
    temperature: float
    humidity: float
    waste_index: float

# ---------------------------
# Read streaming file
# ---------------------------

input_table = pw.io.csv.read(
    "sensor_stream.csv",
    schema=EnvSchema,
    mode="static"  # static per rerun (stable)
)

processed = input_table.select(
    pw.this.timestamp,
    pw.this.aqi,
    pw.this.temperature,
    pw.this.humidity,
    pw.this.waste_index,
    stress_score=(
        0.4 * pw.this.aqi +
        0.3 * pw.this.temperature +
        0.2 * pw.this.waste_index +
        0.1 * pw.this.humidity
    ),
    alert=(
        (pw.this.aqi > 180) |
        (pw.this.temperature > 40)
    )
)

pw.io.csv.write(processed, "live_output.csv")

pw.run()

# ---------------------------
# Auto refresh every 3 sec
# ---------------------------

st_autorefresh(interval=3000, key="refresh")

# ---------------------------
# Display results
# ---------------------------

if os.path.exists("live_output.csv"):
    df = pd.read_csv("live_output.csv")
    latest = df.iloc[-1]

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("AQI", latest["aqi"])
    col2.metric("Temperature", round(latest["temperature"], 2))
    col3.metric("Humidity", round(latest["humidity"], 2))
    col4.metric("Waste Index", round(latest["waste_index"], 2))
    col5.metric("Stress Score", round(latest["stress_score"], 2))

    if latest["alert"]:
        st.error("⚠ Environmental Alert Triggered!")
    else:
        st.success("Environment Stable")

    st.line_chart(df["stress_score"])
else:
    st.warning("Initializing live data...")

