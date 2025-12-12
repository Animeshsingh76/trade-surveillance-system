# src/alerts.py
def log_alerts(alerts, path="data/alerts.log"):
    """
    Write alerts to a log file using UTF-8 encoding so emoji / unicode works on Windows.
    """
    with open(path, "w", encoding="utf-8", errors="replace") as f:
        for trade_id, message in alerts:
            # message can contain emoji — open with utf-8 avoids UnicodeEncodeError
            f.write(f"Trade {trade_id}: {message}\n")
    print(f"✅ {len(alerts)} alerts logged to {path}")

