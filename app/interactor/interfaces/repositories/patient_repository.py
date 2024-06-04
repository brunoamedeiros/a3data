""" This module contains the interface for the PatientRepository
"""


from abc import ABC, abstractmethod
from app.domain.entities.patient import Patient
from app.interactor.dtos.create_patient_dtos import CreatePatientInputDto
from app.interactor.dtos.update_patient_dtos import UpdatePatientInputDto
from app.interactor.dtos.delete_patient_dtos import DeletePatientOutputDto
from typing import Optional


class PatientRepositoryInterface(ABC):
    """ This class is the interface for the PatientRepository
    """

    @abstractmethod
    def create(self, patient_data: CreatePatientInputDto) -> Optional[Patient]:
        """ Create a Patient

        Args:
            patient_data (CreatePatientInputDto): The input data transfer object

        Returns:
            Patient: A Patient object
        """
        raise NotImplementedError

    def get_by_id(self, patient_id: str) -> Optional[Patient]:
        """Get a Patient

        Args:
            patient_id (str): the uuid

        Returns:
            Optional[Patient]: A Patient object if exists
        """
        raise NotImplementedError

    def update(self, patient_id: str, patient_data: UpdatePatientInputDto) -> Optional[Patient]:
        """ Update a Patient

        Args:
            patient_id (str): the uuid
            patient_data (UpdatePatientInputDto): The input data transfer object

        Returns:
            Patient: A Patient object if exists
        """
        raise NotImplementedError

    def delete(self, patient_id: str) -> DeletePatientOutputDto:
        """ Delete a Patient

        Args:
            patient_id (str): the uuid

        Returns:
            Patient: A Patient object
        """
        raise NotImplementedError
