from typing import Dict
from app.interactor.dtos.authenticate_user_dtos import AuthenticateUserOutputDto
from app.interactor.interfaces.presenters.authenticate_user_presenter import AuthenticateUserPresenterInterface


class AuthenticateUserPresenter(AuthenticateUserPresenterInterface):
    def present(self, output_dto: AuthenticateUserOutputDto) -> Dict:
        return output_dto.user
