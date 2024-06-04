from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.get_user_dtos import GetUserOutputDto


class GetUserPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: GetUserOutputDto) -> Dict:
        """ Present the User 
        """
