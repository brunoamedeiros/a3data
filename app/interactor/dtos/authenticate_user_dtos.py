from pydantic import BaseModel
from app.domain.entities.user import User


class AuthenticateUserInputDto(BaseModel):
    email: str
    password: str


class AuthenticateUserOutputDto(BaseModel):
    user: User
