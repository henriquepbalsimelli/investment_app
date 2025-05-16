from pydantic import BaseModel
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

class Settings(BaseModel):
    OF_BASE_URL: str = 'https://banking-openfinance.xpi.com.br'
    BELVO_SECRET_KEY: str = os.getenv("BELVO_SECRET_KEY")
    BELVO_SECRET_PASSWORD: str = os.getenv("BELVO_SECRET_PASSWORD")
    BELVO_API_URL: str = os.getenv("BELVO_API_URL")

    class Config:
        env_file = ".env"

class DatabaseSettings(BaseModel):
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")

    class Config:
        env_file = ".env"

def get_database_url():
    return f"postgresql+asyncpg://{settings_db.DB_USER}:{settings_db.DB_PASSWORD}@{settings_db.DB_HOST}:{settings_db.DB_PORT}/{settings_db.DB_NAME}"

settings = Settings()
settings_db = DatabaseSettings()
DATABASE_URL = get_database_url()

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

db = AsyncSession(autocommit=False, autoflush=False, bind=engine)



Base = declarative_base()