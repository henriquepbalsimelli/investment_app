from app.config import Base
from sqlalchemy import BigInteger, Column, ForeignKey, Text, Boolean, DateTime
from datetime import datetime
from pydantic import BaseModel
import pytz

class UserModel(Base):
    __tablename__ = "users"

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    name: str = Column(Text, nullable=False)
    email: str = Column(Text, nullable=False, unique=True)
    password: str = Column(Text, nullable=False)
    created_at: str = Column(DateTime, nullable=False, default=datetime.date(datetime.now()))
    updated_at: str = Column(DateTime, nullable=False, onupdate=datetime.date(datetime.now()), default=datetime.date(datetime.now()))
    deleted_at: str = Column(DateTime, nullable=True)
    is_active: bool = Column(Boolean, nullable=False, default=True)


class CreateUserInput(BaseModel):
    name: str
    email: str
    password: str
