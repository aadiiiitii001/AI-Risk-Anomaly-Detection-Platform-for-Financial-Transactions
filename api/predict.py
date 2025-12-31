import pandas as pd
from ml.anomaly_model import AnomalyDetector
from ml.feature_engineering import create_features
from db.models import Transaction
from db.database import SessionLocal

model = AnomalyDetector()
model.load()

def predict_and_store(data):
    df = pd.DataFrame([data])
    df = create_features(df)

    features = ["amount_log", "transaction_hour", "velocity"]
    score, anomaly = model.predict(df[features])

    db = SessionLocal()
    tx = Transaction(
        user_id=data["user_id"],
        amount=data["amount"],
        merchant=data.get("merchant"),
        country=data.get("country"),
        risk_score=float(score[0]),
        is_anomaly=bool(anomaly[0] == -1)
    )

    db.add(tx)
    db.commit()
    db.refresh(tx)
    db.close()

    return {
        "transaction_id": tx.id,
        "risk_score": tx.risk_score,
        "anomaly": tx.is_anomaly
    }
