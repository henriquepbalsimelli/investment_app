import httpx
from fastapi import HTTPException
import os
import requests as r 
from belvo.client import Client as BelvoClient

class AuthService:
    def __init__(self):
        self.client_id = os.getenv("BELVO_SECRET_KEY")
        self.client_secret = os.getenv("BELVO_SECRET_PASSWORD")

    def get_belvo_access_token(self):
        """
        Retrieve an access token from Belvo using the provided client ID and secret.
        """
        try:
            response = r.post(
                url="https://sandbox.belvo.com/api/token/",
                data={
                    "id": self.client_id, 
                    "password": self.client_secret, 
                    "scopes": "read_institutions,write_links,read_consents,write_consents,write_consent_callback,delete_consents",
                    "fetch_resources": ["ACCOUNTS", "TRANSACTIONS", "OWNERS", "BILLS", "INCOMES", "RECURRING_EXPENSES", "RISK_INSIGHTS"],
                    "credentials_storage": "store",
                    "stale_in": "300d"
                    },
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        