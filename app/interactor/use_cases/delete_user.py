from typing import Dict
from app.interactor.dtos.delete_user_dtos \
    import DeleteUserOutputDto
from app.interactor.interfaces.presenters.delete_user_presenter \
    import DeleteUserPresenterInterface
from app.interactor.interfaces.repositories.user_repository \
    import UserRepositoryInterface


class DeleteUserUseCase:
    def __init__(self, presenter: DeleteUserPresenterInterface, repository: UserRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, user_id: str) -> DeleteUserOutputDto:
        result = self.repository.delete(user_id)
        return self.presenter.present(result)
