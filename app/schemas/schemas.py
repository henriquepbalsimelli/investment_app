from typing import List
from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    symbol: str
    side: str
    quantity: int
    price: float
    transaction_date: str  # ISO format

class TransactionsResponse(BaseModel):
    count: int
    transactions: List[Transaction]