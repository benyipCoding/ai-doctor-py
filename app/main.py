# app/main.py
from fastapi import FastAPI
from app.api import analyze
from app.core.lifespan import lifespan

app = FastAPI(
    title="AI Doctor Backend",
    version="0.1.0",
    lifespan=lifespan,
)


app.include_router(analyze.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
