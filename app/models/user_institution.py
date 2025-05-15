
from app.config import Base
from sqlalchemy import BigInteger, Column, ForeignKey, Text, Boolean

class UserInstitution(Base):
    __tablename__ = "users_institutions"

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id: int = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    institution_id: int = Column(BigInteger, ForeignKey("institutions.id"), nullable=False)
    link_id: str = Column(Text, nullable=False)
    created_at: str = Column(Text, nullable=False)
    updated_at: str = Column(Text, nullable=False)
    deleted_at: str = Column(Text, nullable=True)
    is_active: bool = Column(Boolean, nullable=False)

