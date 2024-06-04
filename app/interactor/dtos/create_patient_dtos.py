""" Module for CreatePatient Dtos
"""


from app.domain.entities.patient import Patient
from datetime import date
from typing import Optional
from pydantic import BaseModel


class CreatePatientInputDto(BaseModel):
    """ Input Dto for create patient 
    """
    birthdate: date
    deathdate: Optional[date]
    ssn: str
    drivers: Optional[str]
    passport: Optional[str]
    prefix: Optional[str]
    first: str
    middle: Optional[str]
    last: str
    suffix: Optional[str]
    maiden: Optional[str]
    marital: Optional[str]
    race: str
    ethnicity: str
    gender: str
    birthplace: str
    address: str
    city: str
    state: str
    county: str
    fips: Optional[str]
    zip: str
    lat: float
    lon: float
    healthcare_expenses: float
    healthcare_coverage: float
    income: float


class CreatePatientOutputDto(BaseModel):
    """ Output Dto for create patient 
    """
    patient: Patient
