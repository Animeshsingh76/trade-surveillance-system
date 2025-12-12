from fastapi import FastAPI, UploadFile
import pandas as pd
from src.ml_detector import train_anomaly_detector, detect_anomalies

app = FastAPI()

@app.post("/detect")
async def detect(file: UploadFile):
    df = pd.read_csv(file.file)
    df["trade_value"] = df["volume"] * df["price"]
    model = train_anomaly_detector(df)
    df = detect_anomalies(model, df)
    anomalies = df[df["anomaly"] == "🚨"]
    return {"anomalies": anomalies.to_dict(orient="records")}
