from app.domain.entities.user import User
from pydantic import EmailStr, BaseModel
from typing import Optional


class UpdateUserInputDto(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    full_name: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]


class UpdateUserOutputDto(BaseModel):
    """ Output Dto for update user 
    """
    user: User
