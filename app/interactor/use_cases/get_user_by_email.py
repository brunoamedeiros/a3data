from typing import Dict
from app.interactor.dtos.get_user_dtos \
    import GetUserOutputDto
from app.interactor.interfaces.presenters.get_user_presenter \
    import GetUserPresenterInterface
from app.interactor.interfaces.repositories.user_repository \
    import UserRepositoryInterface


class GetUserByEmailUseCase:
    def __init__(self, presenter: GetUserPresenterInterface, repository: UserRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, user_email: str) -> Dict:
        user = self.repository.get_by_email(user_email)
        output_dto = GetUserOutputDto(user=user)
        return self.presenter.present(output_dto)
