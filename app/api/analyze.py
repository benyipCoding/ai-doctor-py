# app/api/analyze.py
from fastapi import APIRouter
from app.schemas.analyze import AnalyzePayload
from app.services.analyze_service import AnalyzeService
from app.schemas.response import APIResponse
from app.schemas.analyze import AnalyzeResponse

# from app.db import get_db
# from sqlalchemy.ext.asyncio import AsyncSession
# from fastapi import Depends


router = APIRouter(prefix="/analyze", tags=["Analyze"])
analyze_service = AnalyzeService()


@router.post("/image", response_model=APIResponse[AnalyzeResponse])
async def analyze(payload: AnalyzePayload):
    try:
        raise NotImplementedError("Analyze endpoint is not yet implemented.")
        result = await analyze_service.analyze(payload)
        return APIResponse(data=result)
    except Exception as e:
        return APIResponse(message=str(e), code=400)
