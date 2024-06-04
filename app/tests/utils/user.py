from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.infra.config import settings
from app.infra.repositories.user_repository import UserRepository
from app.interactor.dtos.create_user_dtos import CreateUserInputDto
from app.interactor.dtos.update_user_dtos import UpdateUserInputDto
from app.domain.entities.user import User
from app.tests.utils.utils import random_email, random_lower_string, random_username


def user_authentication_headers(
    *, client: TestClient, email: str, password: str
) -> dict[str, str]:
    data = {"username": email, "password": password}

    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_email(
    *, client: TestClient, email: str, db: Session
) -> dict[str, str]:
    """
    Return a valid token for the user with given email.

    If the user doesn't exist it is created first.
    """
    password = random_lower_string()
    user_repo = UserRepository(session=db)
    user = user_repo.get_by_email(email=email)
    if not user:
        user_in_create = CreateUserInputDto(email=email, password=password)
        user = user_repo.create(user_in_create)
    else:
        user_in_update = UpdateUserInputDto(password=password)
        if not user.id:
            raise Exception("User id not set")
        user = user_repo.update(user.id, user_in_update)

    return user_authentication_headers(client=client, email=email, password=password)
