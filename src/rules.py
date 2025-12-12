def apply_rules(df):
    alerts = []
    for _, row in df.iterrows():
        if row["volume"] > 5000:
            alerts.append((row["trade_id"], "⚠️ High Volume Alert"))
        elif row["price"] > 1000:
            alerts.append((row["trade_id"], "🚨 Unusual Price Alert"))
    return alerts
