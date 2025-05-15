
from app.config import Base
from sqlalchemy import BigInteger, Column, ForeignKey, Text, Boolean

class Institution(Base):
    __tablename__ = "institutions"

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    external_id: str = Column(Text, nullable=False, unique=True)
    name: str = Column(Text, nullable=False)
    logo: str = Column(Text, nullable=False)
    created_at: str = Column(Text, nullable=False)
    updated_at: str = Column(Text, nullable=False)
    deleted_at: str = Column(Text, nullable=True)
    is_active: bool = Column(Boolean, nullable=False)


