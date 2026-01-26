from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.clients.gemini import init_gemini_client
from app.core.config import settings
from app.db import init_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ===== startup =====
    init_gemini_client()
    print("✅ Gemini client initialized")
    # 初始化数据库（如果配置了 DATABASE_URL ）
    if settings.database_url:
        init_db(settings.database_url)
        print("✅ Database engine initialized")

    yield

    # ===== shutdown =====
    # 关闭数据库连接
    try:
        await close_db()
        print("🛑 Database engine disposed")
    except Exception:
        pass

    print("👋 Application shutdown")
