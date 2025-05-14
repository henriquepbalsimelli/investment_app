from fastapi import APIRouter, Depends, Header, HTTPException
from app.clients.belvo_client.client import BelvoClient
from app.schemas.schemas import TransactionsResponse
import httpx
from app.services.auth import AuthService

router = APIRouter(prefix="/authentication", tags=["authentication"])

@router.get("/belvo-token")
async def get_belvo_access_token():
    """
    Endpoint to retrieve an access token from Belvo.
    """
    try:
        auth_service = AuthService()
        response = auth_service.get_belvo_access_token()
        return response
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
