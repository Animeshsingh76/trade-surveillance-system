from src.ingest import load_trades
from src.features import feature_engineering
from src.rules import apply_rules
from src.ml_detector import train_anomaly_detector, detect_anomalies
from src.alerts import log_alerts

def run_pipeline():
    df = load_trades()
    df = feature_engineering(df)
    alerts = apply_rules(df)

    model = train_anomaly_detector(df)
    df = detect_anomalies(model, df)

    anomaly_alerts = [(row.trade_id, "🚨 ML detected anomaly") for _, row in df[df["anomaly"] == "🚨"].iterrows()]
    all_alerts = alerts + anomaly_alerts

    log_alerts(all_alerts)

if __name__ == "__main__":
    run_pipeline()
