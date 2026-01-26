# app/api/analyze.py
from fastapi import APIRouter
from app.schemas.analyze import AnalyzePayload
from app.services.analyze_service import AnalyzeService
from app.core.config import settings


router = APIRouter(prefix="/analyze", tags=["Analyze"])
analyze_service = AnalyzeService()


@router.post("")
async def analyze(payload: AnalyzePayload):
    result = await analyze_service.analyze(payload)
    return {"result": result}
