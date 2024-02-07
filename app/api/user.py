from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import create_jwt_token

from app.core.database import get_db
from app.models.user import User
from app.serializers.user import UserCreate

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == form_data.username).first()
    if user is None or not user.verify_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = create_jwt_token(data={
        "id": user.id,
        "username": user.name,
        "email": user.email,
        "profile_image": user.profile_image
    })
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup")
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    user = User(**user.model_dump())
    user.set_password(user.password_hash)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
