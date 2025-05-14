from pydantic import BaseModel
import os

class Settings(BaseModel):
    OF_BASE_URL: str = 'https://banking-openfinance.xpi.com.br'
    BELVO_SECRET_KEY: str = os.getenv("BELVO_SECRET_KEY")
    BELVO_SECRET_PASSWORD: str = os.getenv("BELVO_SECRET_PASSWORD")
    BELVO_API_URL: str = os.getenv("BELVO_API_URL")

    class Config:
        env_file = ".env"

settings = Settings()