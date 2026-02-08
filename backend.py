from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Fire Detection Backend")

class SensorData(BaseModel):
    temperature: float
    smoke: float
    gas: float

@app.post("/detect")
def detect_fire(data: SensorData):
    temperature = data.temperature
    smoke = data.smoke
    gas = data.gas

    severity = "LOW"
    fire_detected = False

    if temperature > 60 or smoke > 40 or gas > 500:
        fire_detected = True
        severity = "MEDIUM"

    if temperature > 90 or smoke > 70:
        severity = "HIGH"

    return {"fire_detected": fire_detected, "severity": severity}
