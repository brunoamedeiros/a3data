""" Module for the CreateUserPresenterInterface
"""


from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.create_user_dtos \
    import CreateUserOutputDto


class CreateUserPresenterInterface(ABC):
    """ Class for the Interface of the UserPresenter
    """

    @abstractmethod
    def present(self, output_dto: CreateUserOutputDto) -> Dict:
        """ Present the User 
        """
