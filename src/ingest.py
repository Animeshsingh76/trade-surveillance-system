import pandas as pd

def load_trades(path="data/sample_trades.csv"):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    print(f"📂 Loaded {len(df)} trades from {path}")
    return df
