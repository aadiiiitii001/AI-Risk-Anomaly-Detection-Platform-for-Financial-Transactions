import pandas as pd
import numpy as np

FEATURES = [
    "amount_log",
    "transaction_hour",
    "velocity"
]

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["amount_log"] = np.log1p(df["amount"])
    df["transaction_hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    df["velocity"] = df.groupby("user_id")["amount"].transform("count")

    return df
