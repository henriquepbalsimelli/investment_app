from fastapi import APIRouter, Depends, Header, HTTPException
from app.clients.belvo_client.client import BelvoClient
from app.schemas.schemas import TransactionsResponse
from belvo.client import Client as BelvoClient
from app.services.transactions import TransactionService
from fastapi import Request
from app.services.user_service import UserService
from app.models.user import CreateUserInput

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create")
async def create_user(data: CreateUserInput):
    user_service = UserService()
    data = await user_service.create_user(data)
    return data


@router.post("/link")
async def create_user_link():
    user_service = UserService()
    data = await user_service.create_institution_user_link()
    return data