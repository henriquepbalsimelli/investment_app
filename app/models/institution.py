
from app.config import Base
from sqlalchemy import BigInteger, Column, ForeignKey, Text, Boolean, DateTime
from datetime import datetime

class Institution(Base):
    __tablename__ = "institutions"

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    external_id: str = Column(Text, nullable=False, unique=True)
    name: str = Column(Text, nullable=False)
    logo: str = Column(Text, nullable=False)
    is_active: bool = Column(Boolean, nullable=False)
    created_at: str = Column(DateTime, nullable=False, default=datetime.now)
    updated_at: str = Column(DateTime, nullable=False, onupdate=datetime.now)
    deleted_at: str = Column(DateTime, nullable=True)

