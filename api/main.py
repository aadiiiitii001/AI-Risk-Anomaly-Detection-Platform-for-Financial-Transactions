from fastapi import FastAPI
from api.schemas import Transaction
from api.predict import predict_transaction

app = FastAPI(title="AI Risk & Anomaly Detection Platform")

@app.post("/predict")
def predict(tx: Transaction):
    return predict_transaction(tx.dict())
