from typing import Dict
from app.interactor.dtos.update_user_dtos \
    import UpdateUserInputDto, UpdateUserOutputDto
from app.interactor.interfaces.presenters.update_user_presenter \
    import UpdateUserPresenterInterface
from app.interactor.interfaces.repositories.user_repository \
    import UserRepositoryInterface


class UpdateUserUseCase:
    def __init__(self, presenter: UpdateUserPresenterInterface, repository: UserRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, user_id: str, input_dto: UpdateUserInputDto) -> Dict:
        user = self.repository.update(user_id, input_dto)
        output_dto = UpdateUserOutputDto(user=user)
        return self.presenter.present(output_dto)
