from fastapi import APIRouter
from app.services.llms_service import llms_service
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


router = APIRouter(prefix="/llms", tags=["LLMs"])


# GET /llms
@router.get("")
async def list_llms(db: AsyncSession = Depends(get_db)):
    result = await llms_service.list_all(db)
    return {"result": result}


# GET /llms/{key}
@router.get("/{key}")
async def get_llm_by_key(key: str, db: AsyncSession = Depends(get_db)):
    llm = await llms_service.get_by_key(db, key)
    if llm is None:
        return {"error": "LLM not found"}
    return {"result": llm}
