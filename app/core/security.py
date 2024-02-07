from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.core.database import get_db
from app.core.settings import SECRET_KEY, ALGORITHM
from app.models.user import User


def create_jwt_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt_token(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception


def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    payload = decode_jwt_token(token)
    user = next(get_db()).query(User).filter(User.name == payload['username']).first()
    return user


def authenticate_user(current_user: User = Depends(get_current_user)):
    # Perform any additional checks if needed
    # For example, check user roles or permissions
    # If authentication is not required for the endpoint, you can skip this check

    if current_user:
        return current_user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )
