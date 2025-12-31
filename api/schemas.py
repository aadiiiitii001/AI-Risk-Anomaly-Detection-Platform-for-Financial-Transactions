from pydantic import BaseModel

class Transaction(BaseModel):
    user_id: int
    amount: float
    merchant: str | None = None
    country: str | None = None
    timestamp: str
