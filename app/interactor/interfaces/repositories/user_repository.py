""" This module contains the interface for the UserRepository
"""


from abc import ABC, abstractmethod
from app.domain.entities.user import User
from app.interactor.dtos.create_user_dtos import CreateUserInputDto
from app.interactor.dtos.update_user_dtos import UpdateUserInputDto
from app.interactor.dtos.delete_user_dtos import DeleteUserOutputDto
from typing import Optional


class UserRepositoryInterface(ABC):
    """ This class is the interface for the UserRepository
    """

    @abstractmethod
    def create(self, user_data: CreateUserInputDto) -> Optional[User]:
        """ Create a User

        Args:
            user_data (CreateUserInputDto): The input data transfer object

        Returns:
            User: A User object
        """
        raise NotImplementedError

    def get_by_id(self, user_id: str) -> Optional[User]:
        """Get a User

        Args:
            user_id (str): the uuid

        Returns:
            Optional[User]: A User object if exists
        """
        raise NotImplementedError

    def get_by_email(self, user_email: str) -> Optional[User]:
        """Get a User

        Args:
            user_id (str): the uuid

        Returns:
            Optional[User]: A User object if exists
        """
        raise NotImplementedError

    def update(self, user_id: str, user_data: UpdateUserInputDto) -> Optional[User]:
        """ Update a User

        Args:
            user_id (str): the uuid
            user_data (UpdateUserInputDto): The input data transfer object

        Returns:
            User: A User object if exists
        """
        raise NotImplementedError

    def delete(self, user_id: str) -> DeleteUserOutputDto:
        """ Delete a User

        Args:
            user_id (str): the uuid

        Returns:
            User: A User object
        """
        raise NotImplementedError
