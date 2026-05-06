from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.schemas import Transaction
from api.predict import predict_and_store
from db.database import engine
from db.models import Base

app = FastAPI(title="AI Risk & Anomaly Detection Platform")

# Ensure SQLite tables are created on startup
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# Serve static files (dashboard HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root route → serves the dashboard
@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/predict")
def predict(tx: Transaction):
    return predict_and_store(tx.dict())
