import pandas as pd
from ml.anomaly_model import AnomalyDetector
from ml.feature_engineering import create_features

model = AnomalyDetector()
model.load()

def predict_transaction(data):
    df = pd.DataFrame([data])
    df = create_features(df)

    features = ["amount_log", "transaction_hour", "velocity"]
    score, anomaly = model.predict(df[features])

    return {
        "risk_score": float(score[0]),
        "anomaly": bool(anomaly[0] == -1)
    }
