from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.get_patient_dtos import GetPatientOutputDto


class GetPatientPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: GetPatientOutputDto) -> Dict:
        """ Present the Patient 
        """
