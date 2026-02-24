<div align="center">

<!-- Subtle hacker-green typing header (lightweight, judge-friendly) -->
<img
  src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=34&duration=2200&pause=700&color=22C55E&center=true&vCenter=true&width=980&lines=GreenPulse+%E2%80%94+Real-Time+Environmental+Intelligence;Pathway+Streaming+%7C+Anomaly+Detection+%7C+Stress+Scoring;Built+for+Hack+For+Green+Bharat"
  alt="Typing SVG"
/>

<br/>

<!-- Minimal info line (no fake badges/metrics) -->
<p align="center">
  <b>Hackathon:</b> Hack For Green Bharat &nbsp;•&nbsp;
  <b>Stream Processing:</b> Pathway &nbsp;•&nbsp;
  <b>Dashboard:</b> Streamlit (Cloud)
</p>

<!-- Thin neon divider -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=22c55e&height=2&section=header" width="88%"/>

</div>

# GreenPulse – Real-Time Environmental Intelligence Platform

GreenPulse is a streaming-first environmental intelligence platform that simulates live sensor signals (**AQI, temperature, humidity, waste index**), processes them continuously using **Pathway**, computes a live **Environmental Stress Score**, detects anomalies, and updates a **Streamlit dashboard** in real time with automatic recomputation.

---

## 🚀 Problem
Environmental conditions can shift within minutes (AQI spikes, heat waves, humidity swings, waste build-up). Many monitoring systems still rely on static dashboards or delayed batch processing—reducing response time and limiting actionable decision-making.

---

## 🧠 Solution Overview
GreenPulse delivers real-time environmental monitoring by:
- Simulating **continuous environmental telemetry**
- Running **continuous computation** using Pathway’s streaming engine
- Computing an **Environmental Stress Score** via weighted metrics
- Detecting anomalies and triggering alerts when **AQI** or **temperature** crosses defined thresholds
- **Automatically recomputing** results as new data arrives
- Visualizing outputs on a **live Streamlit dashboard**
- Deploying on **Streamlit Cloud**

---

## 🏗️ Architecture (Streaming Pipeline)

```text
+------------------------------------------------------+
|  Simulated Environmental Sensors                     |
|  AQI | Temperature | Humidity | Waste Index          |
+---------------------------+--------------------------+
                            |
                            v
+------------------------------------------------------+
|  Pathway Streaming Engine                             |
|  - Continuous ingestion                               |
|  - Weighted Stress Score computation                  |
|  - Threshold-based anomaly detection (AQI/Temp)       |
|  - Automatic recomputation on new events              |
+---------------------------+--------------------------+
                            |
                            v
+------------------------------------------------------+
|  Streamlit Live Dashboard                             |
|  - Live KPIs + charts                                 |
|  - Alerts / anomaly flags                              |
|  - Continuously updated views                          |
+------------------------------------------------------+
```

<!-- Small terminal vibe (subtle) -->
```text
[stream] ingest → compute(score) → detect(anomaly) → render(dashboard) → repeat
```

---

## ✨ Key Features
- **Real-time streaming ingestion** (simulated sensor feed)
- **Continuous processing** with automatic recomputation
- **Environmental Stress Score** computed via weighted metrics
- **Anomaly detection & alerts** for AQI/temperature spikes
- **Live dashboard updates** in Streamlit
- **Cloud deployment** on Streamlit Cloud

---

## 🛠 Technology Stack
- **Pathway** — real-time stream processing + recomputation
- **Streamlit** — live dashboard UI
- **Python** — implementation
- **Pandas** — data shaping / feature computation

---

## ⚙️ Installation & Local Setup

### Prerequisites
- Python 3.9+ recommended

### Run locally
```bash
git clone https://github.com/ridhi-png/greenpulse.git
cd greenpulse
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deployment
Deployed on **Streamlit Cloud**.

**Live Demo:** https://greenpulse-eckc9yfkxytdf4ugfahkye.streamlit.app/

To deploy your own instance:
1. Fork/push this repo to GitHub
2. Connect it in Streamlit Cloud
3. Set the entry point to `app.py`
4. Ensure dependencies are listed in `requirements.txt`

---

## 🌍 Real-World Impact & Scalability
- Supports **early warnings** for unhealthy air quality and extreme temperature events
- Useful for **smart cities, campuses, industrial zones, and municipalities**
- Streaming architecture supports **high-frequency, continuous signals**
- Easily extensible to real ingestion sources (MQTT/Kafka/HTTP)

---

## 🔮 Future Enhancements
- Real sensor ingestion (MQTT/Kafka/REST)
- Multi-location aggregation and geospatial views
- Adaptive thresholds (season/time/location-aware)
- Predictive forecasting for stress-score trends
- External notifications + incident logging

---

<div align="center">

<!-- Subtle green footer wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=22c55e&height=110&section=footer" width="100%"/>

<b>GreenPulse</b> — Track • Analyze • Act (streaming-first)

</div>
