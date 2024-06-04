""" Module for the UpdatePatientPresenter
"""

from typing import Dict
from app.interactor.dtos.update_patient_dtos \
    import UpdatePatientOutputDto
from app.interactor.interfaces.presenters.update_patient_presenter \
    import UpdatePatientPresenterInterface


class UpdatePatientPresenter(UpdatePatientPresenterInterface):
    """ Class for the UpdatePatientPresenter
    """

    def present(self, output_dto: UpdatePatientOutputDto) -> Dict:
        """ Present the UpdatePatient

        Args:
            output_dto (UpdatePatientOutputDto): The output data transfer object

        Returns:
            Dict 
        """

        return output_dto.patient
