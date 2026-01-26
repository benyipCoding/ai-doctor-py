# app/middleware/response_wrapper.py
import json
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class ResponseWrapperMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # 只处理 JSON 响应
        if response.headers.get("content-type", "").startswith("application/json"):
            body = b""
            async for chunk in response.body_iterator:
                body += chunk

            raw_data = json.loads(body.decode())

            wrapped = {
                "code": 0,
                "message": "ok",
                "data": raw_data,
            }

            return JSONResponse(
                content=wrapped,
                status_code=response.status_code,
                headers=dict(response.headers),
            )

        return response
