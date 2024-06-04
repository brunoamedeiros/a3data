from typing import Dict
from app.interactor.dtos.get_user_dtos import GetUserOutputDto
from app.interactor.interfaces.presenters.get_user_presenter import GetUserPresenterInterface


class GetUserPresenter(GetUserPresenterInterface):
    def present(self, output_dto: GetUserOutputDto) -> Dict:
        return output_dto.user
