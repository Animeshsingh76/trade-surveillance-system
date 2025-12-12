from sklearn.ensemble import IsolationForest
import pandas as pd

def train_anomaly_detector(df):
    model = IsolationForest(contamination=0.02, random_state=42)
    df["trade_value"] = df["volume"] * df["price"]
    model.fit(df[["volume", "price", "trade_value"]])
    return model

def detect_anomalies(model, df):
    df["anomaly"] = model.predict(df[["volume", "price", "trade_value"]])
    df["anomaly"] = df["anomaly"].apply(lambda x: "🚨" if x == -1 else "")
    return df
