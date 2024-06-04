""" Module for the CreateUserPresenter
"""

from typing import Dict
from app.interactor.dtos.create_user_dtos \
    import CreateUserOutputDto
from app.interactor.interfaces.presenters.create_user_presenter \
    import CreateUserPresenterInterface


class CreateUserPresenter(CreateUserPresenterInterface):
    """ Class for the CreateUserPresenter
    """

    def present(self, output_dto: CreateUserOutputDto) -> Dict:
        """ Present the CreateUser

        Args:
            output_dto (CreateUserOutputDto): The output data transfer object

        Returns:
            Dict 
        """

        return output_dto.user
