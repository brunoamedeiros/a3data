""" Module for the CreatePatientPresenterInterface
"""


from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.create_patient_dtos \
    import CreatePatientOutputDto


class CreatePatientPresenterInterface(ABC):
    """ Class for the Interface of the PatientPresenter
    """

    @abstractmethod
    def present(self, output_dto: CreatePatientOutputDto) -> Dict:
        """ Present the Patient 
        """
