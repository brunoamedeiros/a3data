""" Module for the DeleteUserPresenter
"""

from typing import Dict
from app.interactor.dtos.delete_user_dtos \
    import DeleteUserOutputDto
from app.interactor.interfaces.presenters.delete_user_presenter \
    import DeleteUserPresenterInterface


class DeleteUserPresenter(DeleteUserPresenterInterface):
    """ Class for the DeleteUserPresenter
    """

    def present(self, result: DeleteUserOutputDto) -> DeleteUserOutputDto:
        """ Present the DeleteUser

        Args:
            output_dto (DeleteUserOutputDto): The output data transfer object

        Returns:
            Dict 
        """

        return result
