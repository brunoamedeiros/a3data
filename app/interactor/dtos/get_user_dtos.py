from pydantic import BaseModel
from app.domain.entities.user import User


class GetUserOutputDto(BaseModel):
    user: User
