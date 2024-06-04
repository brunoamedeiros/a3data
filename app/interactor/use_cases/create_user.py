""" This module is responsible for creating a new User
"""


from typing import Dict
from app.interactor.dtos.create_user_dtos \
    import CreateUserInputDto, CreateUserOutputDto
from app.interactor.interfaces.presenters.create_user_presenter \
    import CreateUserPresenterInterface
from app.interactor.interfaces.repositories.user_repository \
    import UserRepositoryInterface


class CreateUserUseCase():
    """ This class is responsible for creating a new User
    """

    def __init__(self, presenter: CreateUserPresenterInterface, repository: UserRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, input_dto: CreateUserInputDto) -> Dict:
        """ This method is responsible for creating a new user

        Args:
            input_dto (CreateUserInputDto): The input data transfer object

        Returns:
            Dict 
        """
        user = self.repository.create(input_dto)
        output_dto = CreateUserOutputDto(user=user)
        return self.presenter.present(output_dto)
