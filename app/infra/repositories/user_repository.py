from app.infra.db_models.user_db_model import UserDBModel
from app.domain.entities.user import User
from app.interactor.dtos.create_user_dtos import CreateUserInputDto
from app.interactor.dtos.update_user_dtos import UpdateUserInputDto
from app.interactor.dtos.delete_user_dtos import DeleteUserOutputDto
from app.interactor.interfaces.repositories.user_repository import UserRepositoryInterface
from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy.exc import IntegrityError
from app.interactor.errors.error_classes import UniqueViolationError
from app.infra.db_models.db_base import engine
from app.infra.security import security


class UserRepository(UserRepositoryInterface):
    def __init__(self, session: Optional[Session] = None) -> None:
        self.__session = session or Session(bind=engine)

    def __db_to_entity(self, db_row: UserDBModel) -> Optional[User]:
        return User(
            id=db_row.id,
            email=db_row.email,
            password=db_row.password,
            is_active=db_row.is_active,
            is_superuser=db_row.is_superuser,
            full_name=db_row.full_name,
            created_at=db_row.created_at,
            updated_at=db_row.updated_at
        )

    def create(self, user_data: CreateUserInputDto) -> User:
        user_obj = user_data.model_dump()

        if "password" in user_obj:
            password = user_obj["password"]
            hashed_password = security.get_password_hash(password)
            user_obj["password"] = hashed_password

        user_db_model = UserDBModel(**user_obj)

        try:
            self.__session.add(user_db_model)
            self.__session.commit()
            self.__session.refresh(user_db_model)
        except IntegrityError as exception:
            self.__session.rollback()

            if "violates unique constraint" in str(exception.orig):
                raise UniqueViolationError(
                    "user with the same email already exists"
                ) from exception
            raise
        except Exception as e:
            self.__session.rollback()
            raise e

        if user_db_model is not None:
            return self.__db_to_entity(user_db_model)
        return None

    def get_by_id(self, user_id: str) -> Optional[User]:
        try:
            user_db_model = self.__session.query(
                UserDBModel).filter_by(id=user_id).first()

            if user_db_model is not None:
                return self.__db_to_entity(user_db_model)

            return None
        except Exception as e:
            self.__session.rollback()
            raise e

    def get_by_email(self, user_email: str) -> Optional[User]:
        try:
            user_db_model = self.__session.query(
                UserDBModel).filter_by(email=user_email).first()

            if user_db_model is not None:
                return self.__db_to_entity(user_db_model)

            return None
        except Exception as e:
            self.__session.rollback()
            raise e

    def update(self, user_id: str, user_data: UpdateUserInputDto) -> Optional[User]:
        try:
            user_db_model = self.__session.query(
                UserDBModel).filter_by(id=user_id).first()

            if user_db_model is None:
                return None

            user_obj = user_data.model_dump()

            if "password" in user_obj:
                password = user_obj["password"]
                hashed_password = security.get_password_hash(password)
                user_obj["password"] = hashed_password

            for key, value in user_obj.items():
                if value is not None:
                    setattr(user_db_model, key, value)

            self.__session.commit()
            self.__session.refresh(user_db_model)

            return self.__db_to_entity(user_db_model)
        except IntegrityError as exception:
            self.__session.rollback()

            if "violates unique constraint" in str(exception.orig):
                raise UniqueViolationError(
                    "user with the same email already exists"
                ) from exception
            raise
        except Exception as e:
            self.__session.rollback()
            raise e

    def delete(self, user_id: str) -> DeleteUserOutputDto:
        try:
            user_db_model = self.__session.query(
                UserDBModel).filter_by(id=user_id).first()

            if user_db_model is not None:
                self.__session.delete(user_db_model)
                self.__session.commit()

                return DeleteUserOutputDto(success=True, message="User deleted successfully")

            return DeleteUserOutputDto(success=False, message="User couldn't be deleted!")
        except Exception as e:
            self.__session.rollback()
            raise e
