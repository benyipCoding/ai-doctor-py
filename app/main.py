# app/main.py
from fastapi import FastAPI
from app.api import analyze

app = FastAPI(
    title="AI Doctor Backend",
    version="0.1.0",
)

app.include_router(analyze.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
