from fastapi import HTTPException
from app.config import db
from app.models.user import UserModel, CreateUserInput


class UserRepository:
    def __init__(self):
        self.db = db

    def get_user_by_id(self, user_id):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    async def create_user(self, user_data: CreateUserInput):
        new_user = UserModel(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
        )
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user
