""" Module for the DeleteUserPresenterInterface
"""


from abc import ABC, abstractmethod
from typing import Dict
from app.interactor.dtos.delete_user_dtos \
    import DeleteUserOutputDto


class DeleteUserPresenterInterface(ABC):
    """ Class for the Interface of the UserPresenter
    """

    @abstractmethod
    def present(self, output_dto: DeleteUserOutputDto) -> Dict:
        """ Present the User 
        """
