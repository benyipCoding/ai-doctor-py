from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.clients.gemini import init_gemini_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ===== startup =====
    init_gemini_client()
    print("✅ Gemini client initialized")

    yield

    # ===== shutdown =====
    print("👋 Application shutdown")
