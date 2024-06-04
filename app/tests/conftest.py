from collections.abc import Generator

import pytest
import uuid
from fastapi.testclient import TestClient
from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.infra.config import settings
from app.infra.db_models.db_base import engine
from app.infra.db_import import load_db

from app.main import app
from app.infra.db_models.user_db_model import UserDBModel as User
from app.infra.db_models.patient_db_model import PatientsDBModel as Patient
from app.tests.utils.user import authentication_token_from_email
from app.tests.utils.utils import get_superuser_token_headers


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        load_db(session)
        yield session
        statement = delete(Patient)
        session.execute(statement)
        statement = delete(User)
        session.execute(statement)
        session.commit()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> dict[str, str]:
    return get_superuser_token_headers(client)


@pytest.fixture(scope="module")
def normal_user_token_headers(client: TestClient, db: Session) -> dict[str, str]:
    return authentication_token_from_email(
        client=client, email=settings.EMAIL_TEST_USER, db=db
    )


@pytest.fixture
def session_mock(mocker):
    return mocker.patch('app.infra.repositories.patient_repository.Session')


@pytest.fixture
def patients_db_model_mock(mocker):
    return mocker.patch('app.infra.repositories.patient_repository.PatientsDBModel')


@pytest.fixture
def uuid_mock(mocker, fixture_patient_data):
    mocker.patch('uuid.uuid4', return_value=fixture_patient_data["id"])


@pytest.fixture
def fixture_patient_data():
    return {
        "id": str(uuid.uuid4()),
        "birthdate": "2024-06-03",
        "deathdate": None,
        "ssn": "123-45-6789",
        "drivers": "S99980558",
        "passport": "X70660767X",
        "prefix": "Mr.",
        "first": "John",
        "middle": "Doe",
        "last": "Smith",
        "suffix": "Jr.",
        "maiden": None,
        "marital": "Single",
        "race": "White",
        "ethnicity": "Non-Hispanic",
        "gender": "M",
        "birthplace": "New York",
        "address": "123 Main St",
        "city": "New York",
        "state": "NY",
        "county": "New York",
        "fips": "36061",
        "zip": "10001",
        "lat": 40.7128,
        "lon": -74.0060,
        "healthcare_expenses": 5000.0,
        "healthcare_coverage": 2000.0,
        "income": 75000.0
    }
