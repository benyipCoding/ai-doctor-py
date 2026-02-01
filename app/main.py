# app/main.py
from fastapi import FastAPI
from app.api import analyze, llms
from app.api import auth
from app.core.lifespan import lifespan


app = FastAPI(
    title="AI Doctor Backend",
    version="0.1.0",
    lifespan=lifespan,
)


app.include_router(analyze.router)
app.include_router(llms.router)
app.include_router(auth.router)
