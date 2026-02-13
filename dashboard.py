import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

st.set_page_config(page_title="GreenPulse - Environmental Risk Monitor", layout="wide")

st.title("🌍 GreenPulse – Real-Time Environmental Risk Dashboard")
st.markdown("AI-powered real-time environmental stress monitoring system.")

# Create session state storage
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "timestamp", "aqi", "temperature", "waste_index", "risk_score", "risk_level"
    ])

def generate_data():
    aqi = random.randint(50, 300)
    temperature = random.randint(20, 45)
    waste_index = random.randint(10, 100)

    risk_score = (
        0.5 * (aqi / 300)
        + 0.3 * (waste_index / 100)
        + 0.2 * (temperature / 45)
    )

    if risk_score > 0.7:
        risk_level = "High"
    elif risk_score > 0.4:
        risk_level = "Moderate"
    else:
        risk_level = "Low"

    return {
        "timestamp": datetime.now(),
        "aqi": aqi,
        "temperature": temperature,
        "waste_index": waste_index,
        "risk_score": round(risk_score, 2),
        "risk_level": risk_level,
    }

# Generate new row every refresh
new_row = generate_data()
st.session_state.data = pd.concat(
    [st.session_state.data, pd.DataFrame([new_row])],
    ignore_index=True
)

# Keep only last 50 rows
st.session_state.data = st.session_state.data.tail(50)

df = st.session_state.data

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Latest AQI", df.iloc[-1]["aqi"])
col2.metric("Temperature (°C)", df.iloc[-1]["temperature"])
col3.metric("Waste Index", df.iloc[-1]["waste_index"])

st.subheader("Environmental Risk Trend")
st.line_chart(df.set_index("timestamp")["risk_score"])

st.subheader("Current Risk Level")

risk = df.iloc[-1]["risk_level"]

if risk == "High":
    st.error("🚨 HIGH RISK – Immediate intervention required")
elif risk == "Moderate":
    st.warning("⚠ MODERATE RISK – Monitor closely")
else:
    st.success("✅ LOW RISK – Stable environmental conditions")

st.subheader("Recent Data")
st.dataframe(df.tail(10), use_container_width=True)

# Auto-refresh
time.sleep(2)
st.rerun()
