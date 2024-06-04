""" Module for the UpdateUserPresenterInterface
"""


from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.update_user_dtos \
    import UpdateUserOutputDto


class UpdateUserPresenterInterface(ABC):
    """ Class for the Interface of the UserPresenter
    """

    @abstractmethod
    def present(self, output_dto: UpdateUserOutputDto) -> Dict:
        """ Present the User 
        """
