# from fastapi import Depends, HTTPException, status, Request
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from jose import JWTError, jwt
# from app.models.users import Users as CurrentUser
# from datetime import datetime, timedelta

# from app.core.config import settings

# security = HTTPBearer(auto_error=False)


# async def get_current_user(request: Request) -> CurrentUser:
#     auth = request.headers.get("Authorization")
#     if not auth or not auth.startswith("Bearer "):
#         raise HTTPException(status_code=401, detail="Not authenticated")

#     token = auth.split(" ", 1)[1]

#     try:
#         payload = jwt.decode(
#             token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm]
#         )
#         user_id = payload.get("sub")
#         email = payload.get("email")
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

#     user = CurrentUser(id=int(user_id), email=email)
#     request.state.user = user
#     return user


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     expire = datetime.now() + (
#         expires_delta or timedelta(minutes=settings.jwt_access_token_expires_minutes)
#     )
#     to_encode.update({"exp": expire})
#     return jwt.encode(
#         to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm
#     )
