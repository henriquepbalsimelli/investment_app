from app.config import Base
from sqlalchemy import BigInteger, Column, ForeignKey, Text, Boolean

class UserModel(Base):
    __tablename__ = "users"

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    name: str = Column(Text, nullable=False)
    email: str = Column(Text, nullable=False, unique=True)
    password: str = Column(Text, nullable=False)
    created_at: str = Column(Text, nullable=False)
    updated_at: str = Column(Text, nullable=False)
    deleted_at: str = Column(Text, nullable=True)
    is_active: bool = Column(Boolean, nullable=False)

