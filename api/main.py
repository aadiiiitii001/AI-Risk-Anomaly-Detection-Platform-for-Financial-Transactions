from fastapi import FastAPI
from api.schemas import Transaction
from api.predict import predict_and_store
from db.database import engine
from db.models import Base

app = FastAPI(title="AI Risk & Anomaly Detection Platform")

# ✅ Ensure SQLite tables are created on startup
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.post("/predict")
def predict(tx: Transaction):
    return predict_and_store(tx.dict())
