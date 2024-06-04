""" Module for the UpdatePatientPresenterInterface
"""


from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.update_patient_dtos \
    import UpdatePatientOutputDto


class UpdatePatientPresenterInterface(ABC):
    """ Class for the Interface of the PatientPresenter
    """

    @abstractmethod
    def present(self, output_dto: UpdatePatientOutputDto) -> Dict:
        """ Present the Patient 
        """
