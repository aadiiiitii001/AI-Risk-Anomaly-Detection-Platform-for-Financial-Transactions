import pandas as pd
import numpy as np

FEATURES = ["amount_log", "transaction_hour", "velocity"]

def create_features(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["transaction_hour"] = df["timestamp"].dt.hour
    df["amount_log"] = np.log1p(df["amount"])
    df["velocity"] = df.groupby("user_id")["amount"].transform("count")
    return df
