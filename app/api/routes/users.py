from fastapi import APIRouter, HTTPException, Depends
from app.api.controllers.user_controller import UserController
from app.interactor.dtos.create_user_dtos import CreateUserInputDto
from app.interactor.dtos.update_user_dtos import UpdateUserInputDto
from app.interactor.dtos.delete_user_dtos import DeleteUserOutputDto
from app.domain.entities.user import User
from app.api.deps import (
    get_current_active_superuser,
    CurrentUser
)

router = APIRouter()
controller = UserController()


@router.post("/", dependencies=[Depends(get_current_active_superuser)],
             response_model=User)
async def create_user(user_data: CreateUserInputDto):
    try:
        user = controller.get_user_by_email(email=user_data.email)

        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this email already exists in the system.",
            )

        result = controller.create_user(user_data.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{user_id}", response_model=User, dependencies=[Depends(get_current_active_superuser)])
async def get_user(user_id: str):
    try:
        result = controller.get_user_by_id(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{user_id}", response_model=User, dependencies=[Depends(get_current_active_superuser)])
async def update_user(user_id: str, user_data: UpdateUserInputDto):
    try:
        db_user = controller.get_user_by_id(user_id)

        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="The user with this id does not exist in the system",
            )
        if user_data.email:
            existing_user = controller.get_user_by_email(email=user_data.email)

            if existing_user and existing_user.id != user_id:
                raise HTTPException(
                    status_code=409, detail="User with this email already exists"
                )

        result = controller.update_user(user_id, user_data.model_dump())

        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{user_id}", response_model=DeleteUserOutputDto, dependencies=[Depends(get_current_active_superuser)])
async def delete_user(current_user: CurrentUser, user_id: str):
    try:
        db_user = controller.get_user_by_id(user_id)

        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        if db_user == current_user:
            raise HTTPException(
                status_code=403, detail="Users are not allowed to delete themselves"
            )

        result = controller.delete_user(user_id)

        if not result.success:
            raise HTTPException(status_code=404, detail=result.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
