from typing import Dict, List
from app.api.presenters.authenticate_user_presenter import AuthenticateUserPresenter
from app.interactor.dtos.create_user_dtos import CreateUserInputDto
from app.interactor.dtos.update_user_dtos import UpdateUserInputDto
from app.interactor.dtos.delete_user_dtos import DeleteUserOutputDto
from app.interactor.use_cases.authenticate_user import AuthenticateUserUseCase
from app.interactor.use_cases.create_user import CreateUserUseCase
from app.interactor.use_cases.get_user_by_id import GetUserByIDUseCase
from app.interactor.use_cases.get_user_by_email import GetUserByEmailUseCase
from app.interactor.use_cases.update_user import UpdateUserUseCase
from app.interactor.use_cases.delete_user import DeleteUserUseCase
from app.infra.repositories.user_repository import UserRepository
from app.api.presenters.create_user_presenter import CreateUserPresenter
from app.api.presenters.get_user_presenter import GetUserPresenter
from app.api.presenters.update_user_presenter import UpdateUserPresenter
from app.api.presenters.delete_user_presenter import DeleteUserPresenter


class UserController:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, request_data) -> Dict:
        presenter = CreateUserPresenter()
        use_case = CreateUserUseCase(presenter, self.repository)
        input_dto = CreateUserInputDto(**request_data)
        return use_case.execute(input_dto)

    def get_user_by_id(self, user_id: str) -> Dict:
        presenter = GetUserPresenter()
        use_case = GetUserByIDUseCase(presenter, self.repository)
        return use_case.execute(user_id)

    def get_user_by_email(self, user_email: str) -> Dict:
        presenter = GetUserPresenter()
        use_case = GetUserByEmailUseCase(presenter, self.repository)
        return use_case.execute(user_email)

    def update_user(self, user_id: str, request_data) -> Dict:
        presenter = UpdateUserPresenter()
        use_case = UpdateUserUseCase(presenter, self.repository)
        input_dto = UpdateUserInputDto(**request_data)
        return use_case.execute(user_id, input_dto)

    def delete_user(self, user_id: str) -> DeleteUserOutputDto:
        presenter = DeleteUserPresenter()
        use_case = DeleteUserUseCase(presenter, self.repository)
        return use_case.execute(user_id)

    def authenticate_user(self, email: str, password: str):
        presenter = AuthenticateUserPresenter()
        use_case = AuthenticateUserUseCase(presenter, self.repository)
        return use_case.execute(email, password)
