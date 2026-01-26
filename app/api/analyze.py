# app/api/analyze.py
from fastapi import APIRouter
from app.schemas.analyze import AnalyzePayload
from app.services.analyze_service import AnalyzeService
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


router = APIRouter(prefix="/analyze", tags=["Analyze"])
analyze_service = AnalyzeService()


@router.post("")
async def analyze(payload: AnalyzePayload, db: AsyncSession = Depends(get_db)):
    result = await analyze_service.analyze(payload)
    return {"result": result}
