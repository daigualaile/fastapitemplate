from typing import Any, Union
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.utils import verify_token

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None):
    to_encode = {"exp": datetime.utcnow() + expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    is_valid = verify_token(token)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
        )
    return True