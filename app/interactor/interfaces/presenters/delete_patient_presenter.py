""" Module for the DeletePatientPresenterInterface
"""


from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.delete_patient_dtos \
    import DeletePatientOutputDto


class DeletePatientPresenterInterface(ABC):
    """ Class for the Interface of the PatientPresenter
    """

    @abstractmethod
    def present(self, output_dto: DeletePatientOutputDto) -> Dict:
        """ Present the Patient 
        """
