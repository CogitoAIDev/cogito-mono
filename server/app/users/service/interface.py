from typing import Optional
from abc import ABC, abstractmethod

from app.users.schemas import (
    EmailRegisterDTO,
    TelegramRegisterDTO,
    UserUpdateDTO,
    UserResponseDTO
)


class IUserService(ABC):
    @abstractmethod
    async def find_users_by_ids(
        self,
        user_ids: Optional[list[int]]
    ) -> Optional[list[UserResponseDTO]]: ...

    @abstractmethod
    async def find_user_by_id(
        self, user_id: int
    ) -> Optional[UserResponseDTO]: ...

    @abstractmethod
    async def find_user_by_filters(
        self,
        filters: Optional[dict]
    ) -> Optional[UserResponseDTO]: ...

    @abstractmethod
    async def register_user_by_email(
        self,
        user_data: EmailRegisterDTO
    ) -> Optional[UserResponseDTO]: ...

    @abstractmethod
    async def register_user_by_telegram_user_id(
        self,
        user_data: TelegramRegisterDTO
    ) -> Optional[UserResponseDTO]: ...

    @abstractmethod
    async def update_user(
        self,
        user_data: UserUpdateDTO
    ) -> Optional[UserResponseDTO]: ...
