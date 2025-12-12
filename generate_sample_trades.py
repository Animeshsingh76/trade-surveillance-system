import pandas as pd
import numpy as np
import random

def generate_trades(n=500):
    np.random.seed(42)
    data = {
        "trade_id": range(1, n + 1),
        "trader_id": np.random.randint(100, 110, size=n),
        "instrument": np.random.choice(["AAPL", "GOOG", "TSLA", "MSFT", "AMZN"], size=n),
        "volume": np.random.randint(10, 1000, size=n),
        "price": np.round(np.random.uniform(100, 500, size=n), 2),
        "timestamp": pd.date_range(start="2024-01-01", periods=n, freq="H")
    }

    df = pd.DataFrame(data)

    # Inject anomalies
    anomalies = random.sample(range(1, n), 5)
    for idx in anomalies:
        df.loc[idx, "volume"] *= 10
        df.loc[idx, "price"] *= 5

    df.to_csv("data/sample_trades.csv", index=False)
    print(f"✅ Sample trade data generated with {n} records and saved to data/sample_trades.csv")

if __name__ == "__main__":
    generate_trades()
