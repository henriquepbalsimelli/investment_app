from fastapi import HTTPException
from app.repository.user_repository import UserRepository
from app.models.user import CreateUserInput

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_user(self, data: CreateUserInput):
        """
        Create a user in the Belvo system.
        """
        try:
            user = await self.user_repository.create_user(data)
            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def create_institution_user_link(self, user_id: str, institution_id: str, link: str):
        """
        Create a link for the user to connect their bank account.
        """
        try:
            link = await self.repo
            return link
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))