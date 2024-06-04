from pydantic import BaseModel


class DeletePatientOutputDto(BaseModel):
    success: bool
    message: str
