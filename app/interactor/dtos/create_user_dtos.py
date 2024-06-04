from app.domain.entities.user import User
from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUserInputDto(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str]
    is_active: bool = True
    is_superuser: bool = False


class CreateUserOutputDto(BaseModel):
    """ Output Dto for create user 
    """
    user: User
