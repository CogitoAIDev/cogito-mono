from typing import Optional

from app.config import logger

from app.auth.service import IAuthService

from app.users.exceptions import UserNotFound, UniqueDuplicated
from app.users.repository import IUserRepository
from app.users.schemas import (
    EmailRegisterDTO,
    TelegramRegisterDTO,
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

    async def find_users_by_ids(
            self,
            user_ids: Optional[list[int]]
    ) -> Optional[list[UserResponseDTO]]:
        if user_ids is None:
            user_ids = [1, 1, 1, 1, 1]
        return [UserResponseDTO(user_id=i) for i in user_ids]

    async def find_user_by_id(
        self,
        user_id: int
    ) -> Optional[UserResponseDTO]:
        try:
            return self.user_repository.get_user_by_id(user_id)
        except UserNotFound as e:
            logger.exception(f'User Service UserNotFound exeption: {e}')
            raise e

    async def find_user_by_filters(
        self,
        filters,
    ) -> Optional[UserResponseDTO]:
        return UserResponseDTO(user_id=13)

    async def register_user_by_email(
        self,
        user_data: EmailRegisterDTO
    ) -> Optional[UserResponseDTO]:
        logger.debug(user_data.model_dump(), type(user_data.model_dump()))
        return UserResponseDTO(
            user_id=19,
            **user_data.model_dump(
                exclude_none=True,
                exclude=['password']
            )
        )

    async def register_user_by_telegram_user_id(
            self,
            user_data: TelegramRegisterDTO
    ) -> UserResponseDTO | None:
        logger.debug(user_data.model_dump(), type(user_data.model_dump()))
        try:
            return self.user_repository.create_user(user_data)

        except Exception as e:
            logger.error(
                f'Error in user.repository.register_user_by_tg_user_id: {e}'
            )
            raise e

    async def update_user(
        self,
        user_id: int,
        user_data: UserUpdateDTO
    ) -> Optional[UserResponseDTO]:
        return UserResponseDTO(
            user_id=user_id,
            **user_data.model_dump(exclude_none=True),
        )
