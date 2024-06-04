# app/api/routes/login.py

from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import CurrentUser
from app.infra.security import security
from app.infra.config import settings
from app.domain.entities.user import Token, User
from app.api.controllers.user_controller import UserController

router = APIRouter()
controller = UserController()


@router.post("/login/access-token")
async def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
                             ) -> Token:
    user = controller.authenticate_user(email=form_data.username,
                                        password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=security.create_access_token(
            user.id, expires_delta=access_token_expires)
    )


@router.post("/login/test-token", response_model=User)
async def test_token(current_user: CurrentUser) -> Any:
    return current_user
