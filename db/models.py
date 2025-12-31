from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from datetime import datetime
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    amount = Column(Float, nullable=False)
    merchant = Column(String, nullable=True)
    country = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    risk_score = Column(Float)
    is_anomaly = Column(Boolean, default=False)
