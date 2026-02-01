# app/api/analyze.py
from fastapi import APIRouter
from app.schemas.analyze import AnalyzePayload
from app.services.analyze_service import AnalyzeService
from app.schemas.response import APIResponse
from app.schemas.analyze import AnalyzeResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.db import get_db
from fastapi_limiter.depends import RateLimiter
from fastapi import Request
from app.deps.auth import get_current_user


router = APIRouter(prefix="/analyze", tags=["Analyze"])
analyze_service = AnalyzeService()


async def ai_rate_limit_key(request: Request):
    user = getattr(request.state, "user", None)
    if user:
        return f"user:{user.id}"
    return f"ip:{request.client.host}"


@router.post(
    "/image",
    response_model=APIResponse[AnalyzeResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(RateLimiter(times=5, seconds=60, identifier=ai_rate_limit_key)),
        # Depends(ai_guard),
    ],
)
async def analyze(payload: AnalyzePayload, db: AsyncSession = Depends(get_db)):
    try:
        result = await analyze_service.analyze(payload, db)
        return APIResponse(data=result)
    except Exception as e:
        return APIResponse(message=str(e), code=400)
