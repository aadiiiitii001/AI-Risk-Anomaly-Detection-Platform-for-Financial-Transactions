import pandas as pd
from ml.anomaly_model import AnomalyDetector
from ml.feature_engineering import create_features, FEATURES

df = pd.read_csv("data/processed/transactions.csv")
df = create_features(df)

model = AnomalyDetector()
model.train(df[FEATURES])
model.save()
