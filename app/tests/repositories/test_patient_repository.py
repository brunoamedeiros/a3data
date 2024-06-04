import pytest
import uuid
from unittest import mock
from sqlalchemy.exc import IntegrityError
from app.domain.entities.patient import Patient
from app.interactor.dtos.create_patient_dtos import CreatePatientInputDto
from app.interactor.errors.error_classes import UniqueViolationError
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

with mock.patch("sqlalchemy.create_engine"):
    from app.infra.db_models.patient_db_model import PatientsDBModel
    from app.infra.repositories.patient_repository import PatientRepository


def test_patient_repository_create(
    session_mock,
    patients_db_model_mock,
    uuid_mock,
    fixture_patient_data
):
    patients_db_model = PatientsDBModel(**fixture_patient_data)
    patients_db_model_mock.return_value = patients_db_model
    repository = PatientRepository(session_mock)
    patient_dto = CreatePatientInputDto(**fixture_patient_data)

    # Test successful creation
    result = repository.create(patient_dto)
    patient = Patient(**fixture_patient_data)
    session_mock.add.assert_called_once_with(patients_db_model_mock())
    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(patients_db_model_mock())
    assert result == patient

    # Test creation returning None
    patients_db_model_mock.return_value = None
    result = repository.create(patient_dto)
    assert result is None

    # Test unique constraint violation
    session_mock.add.side_effect = IntegrityError(
        None, None, 'psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "patients_ssn_key"')
    with pytest.raises(UniqueViolationError, match="patient with the same SSN already exists"):
        repository.create(patient_dto)

    # Test other IntegrityError
    session_mock.add.side_effect = IntegrityError(None, None, "test error")
    with pytest.raises(IntegrityError, match="test error"):
        repository.create(patient_dto)


def test_patient_repository_update(
    session_mock,
    patients_db_model_mock,
    fixture_patient_data
):
    edited_fixture_patient_data = fixture_patient_data.copy()
    edited_fixture_patient_data["first"] = "Edited First Name"
    patients_edited_db_model = PatientsDBModel(**edited_fixture_patient_data)
    patients_db_model_mock.return_value = patients_edited_db_model
    edited_patient = Patient(**edited_fixture_patient_data)
    repository = PatientRepository(session_mock)

    # Test successful update
    session_mock.query.return_value.filter_by.return_value.update.return_value = 1
    result = repository.update(fixture_patient_data["id"], edited_patient)
    assert result == edited_patient

    # Test update with invalid patient_id
    session_mock.query.return_value.filter_by.return_value.update.return_value = 0
    result_invalid_id = repository.update(str(uuid.uuid4()), edited_patient)
    assert result_invalid_id is None


def test_patient_repository_get(
    session_mock,
    patients_db_model_mock,
    fixture_patient_data
):
    patient_mock = Patient(**fixture_patient_data)
    repository = PatientRepository(session_mock)

    # Test get by id returning a patient
    session_mock.query.return_value.get.return_value = patients_db_model_mock
    result = repository.get_by_id(fixture_patient_data["id"])
    assert result == patient_mock

    # Test get by id returning None
    session_mock.query.return_value.get.return_value = None
    result = repository.get_by_id(fixture_patient_data["id"])
    assert result is None


def test_search_patient():
    response = client.get("/api/v1/search?query=John")
    assert response.status_code == 200
    results = response.json()["results"]
    assert any(result["_source"]["name"] == "John Doe" for result in results)
