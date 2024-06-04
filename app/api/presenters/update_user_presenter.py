""" Module for the UpdateUserPresenter
"""

from typing import Dict
from app.interactor.dtos.update_user_dtos \
    import UpdateUserOutputDto
from app.interactor.interfaces.presenters.update_user_presenter \
    import UpdateUserPresenterInterface


class UpdateUserPresenter(UpdateUserPresenterInterface):
    """ Class for the UpdateUserPresenter
    """

    def present(self, output_dto: UpdateUserOutputDto) -> Dict:
        """ Present the UpdateUser

        Args:
            output_dto (UpdateUserOutputDto): The output data transfer object

        Returns:
            Dict 
        """

        return output_dto.user
