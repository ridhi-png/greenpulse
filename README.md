<div align="center">

# 🌱 GreenPulse

### *Real-Time Environmental Risk Monitoring System*

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=3000&pause=1000&color=00C7B7&center=true&vCenter=true&width=600&lines=Real-Time+Environmental+Monitoring;Stream+Processing+%7C+Risk+Analytics;Building+Sustainable+Tech+Solutions" alt="Typing SVG" />

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://greenpulse-vaeayzjywwfsurroozhdja.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/ridhi-png/greenpulse)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## 📝 Project Overview

GreenPulse is an intelligent environmental monitoring system that processes sensor data in real-time to identify environmental risks and provide actionable insights. Built for hackathons and real-world applications, it demonstrates the power of stream processing and interactive dashboards in creating sustainable solutions.

Urban areas face increasing environmental challenges from pollution, waste management, and climate change. GreenPulse tackles these challenges by providing instant visibility into environmental conditions, early detection of critical situations, and specific recommendations for intervention.

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔄 Real-Time Processing
- ⚡ **Stream Processing** with Pathway framework
- 🔄 **Live Data Updates** every 2 seconds
- 📡 **100+ sensor readings** per session
- ⏱️ **Sub-second** risk assessment latency

</td>
<td width="50%">

### 📊 Smart Analytics
- 🎯 **Multi-factor Risk Assessment** (AQI, temperature, waste)
- 🚨 **Smart Alert System** with automated recommendations
- 📈 **Visual Analytics** with trend monitoring
- 📊 **Interactive Dashboard** built with Streamlit

</td>
</tr>
</table>

### Core Capabilities

- 🌡️ **Temperature Monitoring** - Track real-time temperature variations across zones
- 💨 **Air Quality Index (AQI)** - Monitor air pollution levels and thresholds
- 🗑️ **Waste Management** - Track waste index and identify collection priorities
- 🎯 **3-Tier Risk Classification** - Low, Moderate, and High risk levels
- 🚨 **Critical Alert Generation** - Automated alerts for emergency situations
- 💡 **Actionable Recommendations** - Specific suggestions for each alert type

---

## 🏗️ Architecture & Data Flow

<div align="center">

```
┌─────────────────┐
│ Sensor Stream   │  Simulated environmental sensors
│  (Simulated)    │  Zone, AQI, Temperature, Waste Index
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Pathway Engine  │  Real-time stream processing
│  Real-Time      │  Risk calculation & classification
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Risk Analysis   │  Alert logic & recommendations
│  Alert System   │  CRITICAL_ALERT detection
└────────┬────────┘
         │
         ├──────────────┬──────────────┐
         ▼              ▼              ▼
  ┌──────────┐   ┌──────────┐   ┌──────────┐
  │   CSV    │   │ Streamlit│   │  Stream  │
  │  Output  │   │Dashboard │   │   Sink   │
  └──────────┘   └──────────┘   └──────────┘
```

</div>

**Data Flow:**
1. **Sensor Stream** → Collects data from simulated sensors (Zone, AQI, Temperature, Waste Index)
2. **Pathway Engine** → Processes incoming sensor data in real-time
3. **Risk Calculation** → Computes risk scores using weighted formula
4. **Alert Logic** → Generates alerts and recommendations based on thresholds
5. **Output** → Saves to CSV, displays on dashboard, streams to other services

---

## 💡 Technical Highlights

### Risk Score Calculation

```python
# Weighted risk score formula
Risk = (0.5 × AQI/300) + (0.3 × Waste/100) + (0.2 × Temp/40)

# Risk Classification
- High Risk:     risk_score > 0.7
- Moderate Risk: 0.4 < risk_score ≤ 0.7
- Low Risk:      risk_score ≤ 0.4
```

### Alert Thresholds

```python
# Critical alert conditions
CRITICAL_ALERT = AQI > 250 OR Waste_Index > 85

# Automated Recommendations:
- AQI > 250:         "Restrict industrial emissions immediately"
- Waste_Index > 85:  "Deploy emergency waste collection teams"
- Normal:            "Situation normal - monitoring"
```

### Stream Processing Pipeline

```python
# Pathway stream processing
sensor_stream → risk_calculation → classification → alerts → dashboard
```

---

## 💻 Technology Stack

<div align="center">

### Core Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pathway](https://img.shields.io/badge/Pathway-00C7B7?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### Development & Deployment

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

### Technology Details

| Technology | Purpose | Features |
|------------|---------|----------|
| **Python** | Core Language | Data processing, logic implementation |
| **Pathway** | Stream Processing | Real-time data pipeline, transformations |
| **Streamlit** | Dashboard UI | Interactive visualization, real-time updates |
| **Pandas** | Data Analysis | Data manipulation, analytics |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ridhi-png/greenpulse.git
   cd greenpulse
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the stream processing engine**
   ```bash
   python app.py
   ```

4. **Launch the dashboard** (in a separate terminal)
   ```bash
   streamlit run dashboard.py
   ```

5. **Access the dashboard**
   - Open your browser to `http://localhost:8501`
   - Or visit the [live demo](https://greenpulse-vaeayzjywwfsurroozhdja.streamlit.app/)

---

## 🎯 Problem Solved

### Environmental Challenges

Urban areas worldwide struggle with:
- 🌫️ **Air Pollution** - Rising AQI levels affecting public health
- ♨️ **Climate Change** - Temperature extremes and heat waves
- 🗑️ **Waste Management** - Inefficient collection and overflow issues
- ⏰ **Delayed Response** - Lack of real-time monitoring systems

### GreenPulse Solution

1. **Real-time Monitoring** → Instant visibility into environmental conditions
2. **Risk Identification** → Early detection of critical situations
3. **Actionable Insights** → Specific recommendations for intervention
4. **Data-Driven Decisions** → Historical trends for better planning

---

## 🏆 Impact & Results

<div align="center">

| Metric | Achievement |
|--------|-------------|
| ⚡ **Processing Speed** | Sub-second risk assessment latency |
| 📊 **Data Volume** | 100+ sensor readings per session |
| 🎯 **Classification** | 3-tier risk level system |
| 🚨 **Alert System** | Automated critical alert generation |
| 🌐 **Deployment** | Fully functional live demo on Streamlit Cloud |
| 📈 **Update Frequency** | Real-time updates every 2 seconds |

</div>

---

## 📊 Features Breakdown

### 🔴 Critical Alert System
- Triggers when AQI > 250 or Waste Index > 85
- Provides specific emergency recommendations
- Real-time notification in dashboard

### 📈 Risk Assessment Engine
- Multi-factor weighted scoring system
- Considers AQI (50%), Waste (30%), Temperature (20%)
- Three-tier classification: High, Moderate, Low

### 📊 Interactive Dashboard
- Real-time data visualization
- Zone-wise monitoring
- Historical trend analysis
- Alert history and recommendations

### 🔄 Stream Processing
- Pathway framework for real-time processing
- Handles 100+ records with 0.2s intervals
- Automatic CSV output generation

---

## 🛠️ Project Structure

```
greenpulse/
├── app.py              # Main stream processing engine
├── dashboard.py        # Streamlit dashboard application
├── requirements.txt    # Python dependencies
├── output.csv         # Processed data output
├── README.md          # Project documentation
└── .gitignore         # Git ignore rules
```

---

## 🎬 Usage Example

### Running the System

```bash
# Terminal 1: Start stream processing
python app.py

# Terminal 2: Launch dashboard
streamlit run dashboard.py
```

### Sample Output

```
Zone: Zone A
AQI: 275.3
Temperature: 38.5°C
Waste Index: 82.3
Risk Score: 0.76
Risk Level: High
Alert: CRITICAL_ALERT
Suggestion: Restrict industrial emissions immediately
```

---

## 🌟 Key Differentiators

<table>
<tr>
<td width="25%" align="center">

### ⚡ Real-Time
Instant data processing with sub-second latency

</td>
<td width="25%" align="center">

### 🎯 Smart Alerts
Context-aware recommendations for each situation

</td>
<td width="25%" align="center">

### 📊 Visual
Beautiful, interactive dashboard with live updates

</td>
<td width="25%" align="center">

### 🔄 Scalable
Built on Pathway for production-grade streaming

</td>
</tr>
</table>

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **🚀 Live Demo**: [greenpulse-vaeayzjywwfsurroozhdja.streamlit.app](https://greenpulse-vaeayzjywwfsurroozhdja.streamlit.app/)
- **💻 GitHub Repository**: [github.com/ridhi-png/greenpulse](https://github.com/ridhi-png/greenpulse)
- **📚 Pathway Documentation**: [pathway.com/developers](https://pathway.com/developers)
- **🎨 Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)

---

## 🎓 Use Cases

- 🏙️ **Smart Cities** - Urban environmental monitoring
- 🏭 **Industrial Zones** - Emission and waste tracking
- 🏥 **Public Health** - Air quality health alerts
- 🎓 **Research** - Environmental data collection
- 📊 **Policy Making** - Data-driven environmental decisions

---

## 📅 Project Status

![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat-square)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![Maintained](https://img.shields.io/badge/Maintained-Yes-green?style=flat-square)

**Last Updated:** February 2026

---

<div align="center">

### 🌍 *Building Technology for a Sustainable Future*

**GreenPulse** - Real-time insights for a healthier planet

[![GitHub Stars](https://img.shields.io/github/stars/ridhi-png/greenpulse?style=social)](https://github.com/ridhi-png/greenpulse)
[![GitHub Forks](https://img.shields.io/github/forks/ridhi-png/greenpulse?style=social)](https://github.com/ridhi-png/greenpulse/fork)

Made with 💚 for the environment

</div>  
