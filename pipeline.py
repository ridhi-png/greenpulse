import pathway as pw
import random
import time
from datetime import datetime
import csv
import threading

# ---------------------------
# STEP 1: Create live sensor CSV generator
# ---------------------------

def generate_sensor_data():
    with open("sensor_stream.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "aqi", "temperature", "humidity", "waste_index"])

    while True:
        with open("sensor_stream.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                str(datetime.now()),
                random.randint(50, 250),
                random.uniform(20, 45),
                random.uniform(30, 80),
                random.uniform(10, 90)
            ])
        time.sleep(2)

# Run sensor generator in background thread
threading.Thread(target=generate_sensor_data, daemon=True).start()

# ---------------------------
# STEP 2: Define schema
# ---------------------------

class EnvSchema(pw.Schema):
    timestamp: str
    aqi: int
    temperature: float
    humidity: float
    waste_index: float

# ---------------------------
# STEP 3: Pathway live CSV ingestion
# ---------------------------

input_table = pw.io.csv.read(
    "sensor_stream.csv",
    schema=EnvSchema,
    mode="streaming"
)

# ---------------------------
# STEP 4: Real-time processing
# ---------------------------

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

# ---------------------------
# STEP 5: Output processed data
# ---------------------------

pw.io.csv.write(processed, "live_output.csv")

pw.run()
