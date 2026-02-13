import pathway as pw
import random
import time
from pathway.io.python import ConnectorSubject


# -------------------------------
# 1️⃣ Define Schema
# -------------------------------
class SensorSchema(pw.Schema):
    zone: str
    aqi: float
    temperature: float
    waste_index: float


# -------------------------------
# 2️⃣ Data Source
# -------------------------------
class SensorSource(ConnectorSubject):
    def run(self):
        zones = ["Zone A", "Zone B", "Zone C"]

        # Generate 100 records only (no infinite loop)
        for _ in range(100):
            self.next(
                zone=random.choice(zones),
                aqi=random.uniform(50, 300),
                temperature=random.uniform(15, 40),
                waste_index=random.uniform(20, 90),
            )
            time.sleep(0.2)


# -------------------------------
# 3️⃣ Read Stream
# -------------------------------
sensor_stream = pw.io.python.read(
    SensorSource(),
    schema=SensorSchema,
)


# -------------------------------
# 4️⃣ Risk Score Calculation
# -------------------------------
processed = sensor_stream.with_columns(
    risk_score=(
        0.5 * (sensor_stream.aqi / 300)
        + 0.3 * (sensor_stream.waste_index / 100)
        + 0.2 * (sensor_stream.temperature / 40)
    )
)


# -------------------------------
# 5️⃣ Risk Level Classification
# -------------------------------
processed = processed.with_columns(
    risk_level=pw.if_else(
        processed.risk_score > 0.7,
        "High",
        pw.if_else(processed.risk_score > 0.4, "Moderate", "Low"),
    )
)


# -------------------------------
# 6️⃣ Alert System
# -------------------------------
processed = processed.with_columns(
    alert=pw.if_else(
        (processed.aqi > 250) | (processed.waste_index > 85),
        "CRITICAL_ALERT",
        "NORMAL",
    )
)

processed = processed.with_columns(
    suggestion=pw.if_else(
        processed.alert == "CRITICAL_ALERT",
        pw.if_else(
            processed.aqi > 250,
            "Restrict industrial emissions immediately",
            "Deploy emergency waste collection teams",
        ),
        "Situation normal - monitoring",
    )
)


# -------------------------------
# 7️⃣ Write Output to CSV
# -------------------------------
pw.io.csv.write(processed, "output.csv")


# -------------------------------
# 8️⃣ Run Engine
# -------------------------------
pw.run()
