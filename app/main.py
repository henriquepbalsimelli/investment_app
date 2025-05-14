from fastapi import FastAPI
from app.router.investments_router import router as investments_router
from app.router.auth_router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Open Finance - XP Transactions", version="0.1.0")
app.include_router(investments_router)
app.include_router(auth_router)

# Configure CORS middleware
origins = [
    "http://localhost",  # Permitir localhost
    "http://localhost:3000",  # Permitir localhost com porta 3000 (React, por exemplo)
    "*"  # Permitir todas as origens (use com cuidado em produção)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)