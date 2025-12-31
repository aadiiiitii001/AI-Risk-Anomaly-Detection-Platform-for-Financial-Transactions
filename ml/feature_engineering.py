import pandas as pd
import numpy as np

def create_features(df):
    df["transaction_hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    df["amount_log"] = np.log1p(df["amount"])

    df["velocity"] = df.groupby("user_id")["amount"].transform("count")

    return df
