""" Module for the CreatePatientPresenter
"""

from typing import Dict
from app.interactor.dtos.create_patient_dtos \
    import CreatePatientOutputDto
from app.interactor.interfaces.presenters.create_patient_presenter \
    import CreatePatientPresenterInterface


class CreatePatientPresenter(CreatePatientPresenterInterface):
    """ Class for the CreatePatientPresenter
    """

    def present(self, output_dto: CreatePatientOutputDto) -> Dict:
        """ Present the CreatePatient

        Args:
            output_dto (CreatePatientOutputDto): The output data transfer object

        Returns:
            Dict 
        """

        return output_dto.patient
