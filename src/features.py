import pandas as pd

def feature_engineering(df):
    df["trade_value"] = df["volume"] * df["price"]
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek
    return df
