# app/main.py
from fastapi import FastAPI
from app.api import analyze, llms
from app.core.lifespan import lifespan

# from app.middleware.response_wrapper import ResponseWrapperMiddleware

app = FastAPI(
    title="AI Doctor Backend",
    version="0.1.0",
    lifespan=lifespan,
)


# app.add_middleware(ResponseWrapperMiddleware)


app.include_router(analyze.router)
app.include_router(llms.router)
