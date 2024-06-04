from app.domain.entities.patient import Patient
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class UpdatePatientInputDto(BaseModel):
    birthdate: Optional[date] = None
    deathdate: Optional[date] = None
    ssn: Optional[str] = Field(None, min_length=11, max_length=11)
    drivers: Optional[str] = None
    passport: Optional[str] = None
    prefix: Optional[str] = None
    first: Optional[str] = None
    middle: Optional[str] = None
    last: Optional[str] = None
    suffix: Optional[str] = None
    maiden: Optional[str] = None
    marital: Optional[str] = None
    race: Optional[str] = None
    ethnicity: Optional[str] = None
    gender: Optional[str] = Field(None, min_length=1, max_length=1)
    birthplace: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    county: Optional[str] = None
    fips: Optional[str] = None
    zip: Optional[str] = Field(None, min_length=5, max_length=10)
    lat: Optional[float] = None
    lon: Optional[float] = None
    healthcare_expenses: Optional[float] = None
    healthcare_coverage: Optional[float] = None
    income: Optional[float] = None


class UpdatePatientOutputDto(BaseModel):
    """ Output Dto for update patient 
    """
    patient: Patient
