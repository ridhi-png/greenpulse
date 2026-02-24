# GreenPulse – Real-Time Environmental Intelligence Platform

Built for **Hack For Green Bharat Hackathon** • Real-time streaming intelligence for environmental monitoring using **Pathway** + **Streamlit**.

## 🚀 Problem
Environmental conditions (air quality, heat, humidity, waste accumulation) change rapidly. Many monitoring systems still rely on delayed batch updates or static dashboards—making it hard to detect spikes early and respond in time.

## 🧠 Solution
GreenPulse is an **AI-assisted, real-time environmental monitoring platform** that:
- **Simulates live sensor streams** (AQI, temperature, humidity, waste index)
- Uses **Pathway streaming** to process events continuously
- Computes a continuously updated **Environmental Stress Score** (weighted metrics)
- **Detects anomalies** and triggers alerts when **AQI** or **temperature** crosses thresholds
- **Automatically recomputes** outputs as new data arrives
- Presents insights on a **live Streamlit dashboard**

## 🏗️ Architecture
GreenPulse is designed as a streaming pipeline: ingest → compute → detect → visualize.

```text
+-------------------------------+
|  Simulated Sensor Stream      |
|  (AQI, Temp, Humidity, Waste) |
+---------------+---------------+
                |
                v
+-------------------------------+
|   Pathway Streaming Engine    |
|  - Continuous ingestion       |
|  - Stress score computation   |
|  - Anomaly detection          |
+---------------+---------------+
                |
                v
+-------------------------------+
|     Streamlit Live Dashboard  |
|  - Real-time charts & KPIs    |
|  - Alerts / threshold flags   |
+-------------------------------+
```

## ✨ Key Features
- **Real-time streaming ingestion** (simulated sensor feed)
- **Continuous computation** with automatic recomputation
- **Environmental Stress Score** using weighted metrics
- **Anomaly detection & alerts** for AQI/temperature spikes
- **Live dashboard visualization** in Streamlit
- **Cloud deployment** via Streamlit Cloud

## 🧰 Technology Stack
- **Pathway** — real-time stream processing and recomputation
- **Streamlit** — interactive live dashboard
- **Python** — core implementation
- **Pandas** — data shaping/feature prep

## ⚙️ Installation & Local Setup

### 1) Clone the repository
```bash
git clone https://github.com/ridhi-png/greenpulse.git
cd greenpulse
```

### 2) Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the Streamlit app
```bash
streamlit run app.py
```

## ☁️ Deployment
GreenPulse is deployed on **Streamlit Cloud**.

Live demo: https://greenpulse-eckc9yfkxytdf4ugfahkye.streamlit.app/

To deploy your own version:
1. Push this repo to GitHub
2. Connect it in Streamlit Cloud
3. Set the entrypoint to `app.py`
4. Ensure `requirements.txt` is present and up to date

## 🌍 Real-World Impact & Scalability
- **Early warning system** for hazardous AQI and heat events
- Can support **schools, smart cities, industrial zones, and municipal bodies**
- Streaming-first design supports **continuous data** from distributed IoT sensors
- Pathway enables scalable incremental recomputation as data volume grows

## 🔮 Future Enhancements
- Integrate **real IoT feeds** (MQTT/Kafka/HTTP)
- Add **geospatial views** and multi-location aggregation
- Personalize thresholds by location, time-of-day, and season
- Add **predictive forecasting** for stress score trends
- Notifications via **SMS/WhatsApp/email**

---

### 📌 Hackathon Note
Built for **Hack For Green Bharat Hackathon** with a focus on real-time environmental intelligence and actionable alerts.