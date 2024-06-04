""" This module has definition of the User entity
"""


from app.domain.value_objects import UserId
from datetime import datetime
from pydantic import EmailStr, BaseModel


class User(BaseModel):
    """ Definition of the User entity
    """
    id: UserId
    email: EmailStr
    password: str
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None
    created_at: datetime
    updated_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str | None = None


class NewPassword(BaseModel):
    token: str
    new_password: str
