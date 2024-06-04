""" Module for the DeletePatientPresenter
"""

from app.interactor.dtos.delete_patient_dtos \
    import DeletePatientOutputDto
from app.interactor.interfaces.presenters.delete_patient_presenter \
    import DeletePatientPresenterInterface


class DeletePatientPresenter(DeletePatientPresenterInterface):
    """ Class for the DeletePatientPresenter
    """

    def present(self, result: DeletePatientOutputDto) -> DeletePatientOutputDto:
        """ Present the DeletePatient

        Args:
            output_dto (DeletePatientOutputDto): The output data transfer object

        Returns:
            Dict 
        """

        return result
