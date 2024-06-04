from fastapi import APIRouter
from app.api.routes import patients, login, users

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(
    patients.router, prefix="/patients", tags=["patients"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
