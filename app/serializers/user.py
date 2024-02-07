from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password_hash: str
    profile_image: str


class UserRead(BaseModel):
    id: int
    name: str
    email: str
    profile_image: str
