from pydantic import BaseModel


class DeleteUserOutputDto(BaseModel):
    success: bool
    message: str
