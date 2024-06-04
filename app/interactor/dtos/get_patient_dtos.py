from pydantic import BaseModel
from app.domain.entities.patient import Patient


class GetPatientOutputDto(BaseModel):
    patient: Patient
