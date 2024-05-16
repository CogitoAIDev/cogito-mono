
from fastapi import Depends

from app.auth.service import get_auth_service
from app.auth.service import IAuthService

from app.users.repository import get_user_repository
from app.users.repository import IUserRepository

from .service import UserService
from .interface import IUserService


def get_user_service(
        auth_service: IAuthService = Depends(get_auth_service),
        user_repository: IUserRepository = Depends(get_user_repository),
) -> IUserService:
    return UserService(
        user_repository=auth_service,
        auth_service=user_repository,
    )
