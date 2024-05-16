from typing import Optional

from app.config import logger

from app.auth.service import IAuthService

from app.users.repository import IUserRepository
from app.users.schemas import (
    UserCreateDTO,
    UserResponseDTO,
    UserUpdateDTO
)

from .interface import IUserService


class UserService(IUserService):

    def __init__(
        self,
        user_repository: IUserRepository,
        auth_service: IAuthService,
    ) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.auth_service = auth_service

    async def find_users(
            self,
            user_ids: list[int],
            filters: dict | None
    ) -> Optional[list[UserResponseDTO]]:
        return [
            UserResponseDTO(
                user_id=1
            ),
            UserResponseDTO(
                user_id=9
            ),
        ]

    async def find_user_by_id(
        self,
        user_id: int
    ) -> Optional[UserResponseDTO]:
        return UserResponseDTO(user_id=13)

    async def find_user_by_filters(
        self,
        filters,
    ) -> Optional[UserResponseDTO]:
        return UserResponseDTO(user_id=13)

    async def register_user(
        self,
        user_data: UserCreateDTO
    ) -> Optional[UserResponseDTO]:
        logger.debug(user_data.model_dump(), type(user_data.model_dump()))
        return UserResponseDTO(
            user_id=19,
            **user_data.model_dump(exclude_none=True)
        )

    async def update_user(
        self,
        user_data: UserUpdateDTO
    ) -> Optional[UserResponseDTO]:
        return UserResponseDTO(user_id=111)
