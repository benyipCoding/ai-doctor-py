# from fastapi import Depends, HTTPException, status
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from jose import JWTError, jwt
# from app.core.config import settings

# security = HTTPBearer(auto_error=False)


# def ai_guard(
#     credentials: HTTPAuthorizationCredentials = Depends(security),
# ):
#     if credentials is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Missing Authorization token",
#         )

#     token = credentials.credentials

#     try:
#         payload = jwt.decode(
#             token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm]
#         )
#         user_id: str | None = payload.get("sub")
#         scope: str | None = payload.get("scope")

#         if user_id is None or scope != "ai":
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail="Invalid AI token",
#             )

#         return payload  # 👈 可以返回 user 信息给接口使用

#     except JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Token校验失败",
#         )
