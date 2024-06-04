from app.infra.db_models.patient_db_model import PatientsDBModel
from app.domain.entities.patient import Patient
from app.interactor.dtos.create_patient_dtos import CreatePatientInputDto
from app.interactor.dtos.update_patient_dtos import UpdatePatientInputDto
from app.interactor.dtos.delete_patient_dtos import DeletePatientOutputDto
from app.interactor.interfaces.repositories.patient_repository import PatientRepositoryInterface
from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy.exc import IntegrityError
from app.interactor.errors.error_classes import UniqueViolationError
from app.infra.db_models.db_base import engine
from elasticsearch import Elasticsearch, exceptions as es_exceptions
from tenacity import retry, wait_exponential, stop_after_attempt
from app.infra.config import settings


# @retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(5), reraise=True)
# def create_elasticsearch_client():
#     es = Elasticsearch(
#         settings.ELASTICSEARCH_URL,
#         ca_certs="/tmp/ca.crt",
#         basic_auth=("elastic", settings.ELASTIC_PASSWORD)
#     )

#     if not es.ping():
#         raise es_exceptions.ConnectionError("Elasticsearch is not reachable")
#     return es


# es = create_elasticsearch_client()


# def index_patient(patient: Patient):
#     es.index(index='patients', id=patient.id, body={
#         'name': f"{patient.first} {patient.last}",
#         'id': str(patient.id),
#         'address': patient.address,
#     })


class PatientRepository(PatientRepositoryInterface):
    def __init__(self, session: Optional[Session] = None) -> None:
        self.__session = session or Session(bind=engine)

    def __db_to_entity(self, db_row: PatientsDBModel) -> Optional[Patient]:
        return Patient(
            id=db_row.id,
            birthdate=db_row.birthdate,
            deathdate=db_row.deathdate,
            ssn=db_row.ssn,
            drivers=db_row.drivers,
            passport=db_row.passport,
            prefix=db_row.prefix,
            first=db_row.first,
            middle=db_row.middle,
            last=db_row.last,
            suffix=db_row.suffix,
            maiden=db_row.maiden,
            marital=db_row.marital,
            race=db_row.race,
            ethnicity=db_row.ethnicity,
            gender=db_row.gender,
            birthplace=db_row.birthplace,
            address=db_row.address,
            city=db_row.city,
            state=db_row.state,
            county=db_row.county,
            fips=db_row.fips,
            zip=db_row.zip,
            lat=db_row.lat,
            lon=db_row.lon,
            healthcare_expenses=db_row.healthcare_expenses,
            healthcare_coverage=db_row.healthcare_coverage,
            income=db_row.income
        )

    def create(self, patient_data: CreatePatientInputDto) -> Patient:
        patient_db_model = PatientsDBModel(**patient_data.model_dump())

        try:
            self.__session.add(patient_db_model)
            self.__session.commit()
            self.__session.refresh(patient_db_model)
        except IntegrityError as exception:
            self.__session.rollback()

            if "violates unique constraint" in str(exception.orig):
                raise UniqueViolationError(
                    "patient with the same SSN already exists"
                ) from exception
            raise
        except Exception as e:
            self.__session.rollback()
            raise e

        if patient_db_model is not None:
            patient_entity = self.__db_to_entity(patient_db_model)
            index_patient(patient_entity)

            return patient_entity
        return None

    def get_by_id(self, patient_id: str) -> Optional[Patient]:
        try:
            patient_db_model = self.__session.query(
                PatientsDBModel).filter_by(id=patient_id).first()

            if patient_db_model is not None:
                return self.__db_to_entity(patient_db_model)

            return None
        except Exception as e:
            self.__session.rollback()
            raise e

    def update(self, patient_id: str, patient_data: UpdatePatientInputDto) -> Optional[Patient]:
        try:
            patient_db_model = self.__session.query(
                PatientsDBModel).filter_by(id=patient_id).first()

            if patient_db_model is None:
                return None

            for key, value in patient_data.model_dump().items():
                if value is not None:
                    setattr(patient_db_model, key, value)

            self.__session.commit()
            self.__session.refresh(patient_db_model)

            patient_entity = self.__db_to_entity(patient_db_model)
            index_patient(patient_entity)

            return patient_entity
        except IntegrityError as exception:
            self.__session.rollback()

            if "violates unique constraint" in str(exception.orig):
                raise UniqueViolationError(
                    "patient with the same SSN already exists"
                ) from exception
            raise
        except Exception as e:
            self.__session.rollback()
            raise e

    def delete(self, patient_id: str) -> DeletePatientOutputDto:
        try:
            patient_db_model = self.__session.query(
                PatientsDBModel).filter_by(id=patient_id).first()

            if patient_db_model is not None:
                self.__session.delete(patient_db_model)
                self.__session.commit()

                return DeletePatientOutputDto(success=True, message="Patient deleted successfully")

            return DeletePatientOutputDto(success=False, message="Patient couldn't be deleted!")
        except Exception as e:
            self.__session.rollback()
            raise e
