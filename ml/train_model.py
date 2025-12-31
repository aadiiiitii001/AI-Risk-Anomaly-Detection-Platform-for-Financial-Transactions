import pandas as pd
from anomaly_model import AnomalyDetector
from feature_engineering import create_features

df = pd.read_csv("data/processed/transactions.csv")
df = create_features(df)

features = ["amount_log", "transaction_hour", "velocity"]

model = AnomalyDetector()
model.train(df[features])
model.save()
