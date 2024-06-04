from typing import Dict
from app.interactor.dtos.authenticate_user_dtos \
    import AuthenticateUserOutputDto
from app.interactor.interfaces.presenters.authenticate_user_presenter \
    import AuthenticateUserPresenterInterface
from app.interactor.interfaces.repositories.user_repository \
    import UserRepositoryInterface
from app.infra.security import security


class AuthenticateUserUseCase:
    def __init__(self, presenter: AuthenticateUserPresenterInterface, repository: UserRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, user_email: str, password: str) -> Dict:
        user = self.repository.get_by_email(user_email)

        if not security.verify_password(password, user.password):
            return None

        output_dto = AuthenticateUserOutputDto(user=user)

        return self.presenter.present(output_dto)
