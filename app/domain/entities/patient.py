""" This module has definition of the Patient entity
"""


from app.domain.value_objects import PatientId
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field


class Patient(BaseModel):
    """ Definition of the Patient entity
    """
    id: PatientId
    birthdate: date
    deathdate: Optional[date]
    ssn: str = Field(..., min_length=11, max_length=11)
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
    gender: str = Field(..., min_length=1, max_length=1)
    birthplace: str
    address: str
    city: str
    state: str
    county: str
    fips: Optional[str]
    zip: str = Field(..., min_length=5, max_length=10)
    lat: float
    lon: float
    healthcare_expenses: float
    healthcare_coverage: float
    income: float
