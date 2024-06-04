from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.authenticate_user_dtos import AuthenticateUserOutputDto


class AuthenticateUserPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: AuthenticateUserOutputDto) -> Dict:
        """ Present the User 
        """
