from fastapi import APIRouter, Depends, Header, HTTPException
from app.clients.belvo_client.client import BelvoClient
from app.schemas.schemas import TransactionsResponse
from belvo.client import Client as BelvoClient
from app.services.transactions import TransactionService
from fastapi import Request

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("/")
async def list_transactions(link: str, request: Request):
    headers = request.headers
    
    if "Authorization" not in headers:
        raise HTTPException(status_code=400, detail="Access token is required")
    
    access_token = headers.get("Authorization")
    transaction_service = TransactionService(
        access_token=access_token,
        link_id=link
    )
    data = await transaction_service.list_transactions()
    
    return data

@router.get("/investments")
async def list_investments(link: str, request: Request):
    headers = request.headers
    
    if "Authorization" not in headers:
        raise HTTPException(status_code=400, detail="Access token is required")
    
    access_token = headers.get("Authorization")
    transaction_service = TransactionService(
        access_token=access_token,
        link_id=link
    )
    data = await transaction_service.list_investments()
    
    return data