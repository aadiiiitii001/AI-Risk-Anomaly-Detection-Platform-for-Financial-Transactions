import pandas as pd
import numpy as np

df = pd.read_csv("../raw/transactions.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["amount_log"] = np.log1p(df["amount"])

df.to_csv("transactions_processed.csv", index=False)

print("✅ Processed data saved")
