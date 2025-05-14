import httpx
from app.config import settings
import requests
import base64
from fastapi import HTTPException
import requests as r

class BelvoClient:
    def __init__(self, access_token: str = None):
        self.client_id = settings.BELVO_SECRET_KEY
        self.client_secret = settings.BELVO_SECRET_PASSWORD
        self.base_url = settings.BELVO_API_URL
        self.access_token = access_token


    async def get_transactions(self, link_id: str):
        url = self.base_url + "/transactions/"

        query = {
            "link": link_id
        }

        response = requests.get(url, params=query, auth=(self.client_id,self.client_secret))
        data = response.json()
        return data
    
    async def get_investments(self, link_id: str):
        url = self.base_url + "/br/investments/"

        query = {
            "link": link_id,
            "page_size": "100",
            "page": "1",
        }

        response = requests.get(url, params=query, auth=(self.client_id,self.client_secret))

        data = response.json()
        return data