""" Defines the patients database model.
"""

import uuid
from sqlalchemy import String, Date, Float
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.infra.db_models.db_base import Base


class PatientsDBModel(Base):
    """ Defines the patients database model.
    """

    __tablename__ = "patients"

    id: Mapped[uuid.UUID] = \
        mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    birthdate: Mapped[Date] = mapped_column(Date, nullable=False)
    deathdate: Mapped[Date] = mapped_column(Date, nullable=True)
    ssn: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    drivers: Mapped[str] = mapped_column(String(15), nullable=True)
    passport: Mapped[str] = mapped_column(
        String(20), unique=True, nullable=True)
    prefix: Mapped[str] = mapped_column(String(10), nullable=True)
    first: Mapped[str] = mapped_column(String(50), nullable=False)
    middle: Mapped[str] = mapped_column(String(50), nullable=True)
    last: Mapped[str] = mapped_column(String(50), nullable=False)
    suffix: Mapped[str] = mapped_column(String(10), nullable=True)
    maiden: Mapped[str] = mapped_column(String(50), nullable=True)
    marital: Mapped[str] = mapped_column(String(20), nullable=True)
    race: Mapped[str] = mapped_column(String(20), nullable=False)
    ethnicity: Mapped[str] = mapped_column(String(20), nullable=False)
    gender: Mapped[str] = mapped_column(String(1), nullable=False)
    birthplace: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    state: Mapped[str] = mapped_column(String(255), nullable=False)
    county: Mapped[str] = mapped_column(String(50), nullable=False)
    fips: Mapped[str] = mapped_column(String(5), nullable=True)
    zip: Mapped[str] = mapped_column(String(10), nullable=False)
    lat: Mapped[float] = mapped_column(Float, nullable=False)
    lon: Mapped[float] = mapped_column(Float, nullable=False)
    healthcare_expenses: Mapped[float] = mapped_column(Float, nullable=False)
    healthcare_coverage: Mapped[float] = mapped_column(Float, nullable=False)
    income: Mapped[float] = mapped_column(Float, nullable=False)
