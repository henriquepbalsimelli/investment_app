from app.clients.belvo_client.client import BelvoClient 
import os

class TransactionService:
    def __init__(self, access_token: str, link_id: str):
        self.client_id = os.getenv("BELVO_SECRET_KEY")
        self.client_secret = os.getenv("BELVO_SECRET_PASSWORD")
        self.access_token = access_token
        self.link_id = link_id
        self.belvo_client = BelvoClient(
            access_token=self.access_token
        )

    async def list_transactions(self):
        transactions = await self.belvo_client.get_transactions(self.link_id)
        return transactions
    
    async def list_investments(self):
        investments = await self.belvo_client.get_investments(self.link_id)
        return investments